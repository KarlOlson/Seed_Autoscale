This contains the complete BGPchain and test environment using the Mini-internet topology.

# To Run an Experiment
1. from `examples` find your experiment folder and run the chosen python file. Note: you can define a % of the topology to deploy BGPchain on by issuing the following `python3 mini-internet.py -d 50` will deply on 50% of the ASes. At the moment you must have a manual count and statically define the total.

2. After topology deployed, run the `/bgp_smart_contracts/configs/b00-mini-internet/routerupdate.sh` script to reconfigure the topology to be fully routable. eg. `sudo bash routerupdate.sh`

3. Validate Topology operation and # devices with proxy running (identified by `_proxy` in name).

4. Validate control plane for target hijack prefix (none should have before attack). `/Hijacks/control_plane.sh`, e.g. `sudo ./control_plane.sh 10.199.0.0/24`

5. Conduct Hijack. `Hijacks/Random_Hijacks.sh`, e.g. `sudo ./Random_Hijack.sh 10.199.0.0/24'

6. Recheck control plan for effected routers. Verify that results make sense.


#Things to add
1. Automatically calculate the total ASes? 
2. Pull and aggregate proxy results (logs) showing attacks.
3. New Larger Toplogy
4. Per router? 
5. 

# Code Changes
### EBGP.py
1. `Line 19` added `table t_bgp;` and removed `rsclient;`
2. `Line 127`, `141`, `152`, and `174` removed the export filter and changed to `all`. This fixes the peer depth problem where routes do not get shared with neighbor peers after 2x peer depth. Seed expected to reach a tier1 ISP by this point, but if needing to transit multiple ASes to get to T1, this would not work.

### Routing.py
1. `Lines 7-46` added a new template for ix that uses route server peering setup to instead directly peer and add IX as a routing participant. Also adds local peering OSPF network into BGP to ensure all routers can now ping across full topology.
2. `Line 134` added format variables to align with new IX template.

### Docker.py
1. `Line 13` changed client image to custom image with software pre-loaded to prevent long build times.
2. `Line 26` added a `specialCommands` template for inclusion of additional parameters such as blockchain and proxy for startup.
3. `Lines 44-62` added a Ganache blockchain start script template. Only deployed on IX100.
4. `Lines 63 - 148` added a `WaitForIt.sh` script to delay proxy deployment until blockchain is fully deployed. Based on fixed delay after blockchain launches. need to develop better trigger. Without delay, proxies will launch and fail to validate accepting bad routes on startup and ruining experiment data.
5. `Lines 249-264` added proxy.sh deployment script for routers deploying proxy.
6. `Line 428` added a listening port for blockchain interaction for container.
7. `Line 500` set default image as the pre-compiled image. Should set this back to be earlier reference (fix).
8. `Line 502` added list for `network_devices` that will track all devices in toplogy and use info to deploy blockchain accounts later.
9. `Line 540` defined ethClientPort.
10. `Line 729` use pre-build reference image instead of blank ubuntu. For build time improvement.
11. `Line 1044-1045` and `1050-1051` removed soft_install_tiers and included in pre-built image. Added `pass` to prevent multiple other edits to bypass. 
12. `Line 1053` removed zshrc install. website has a request limit that will make large toplogies fail due to reaching request limit. added to base image to avoid.
13. `Lines 1068-1069` added ganache and proxy scripts to each container build.
14. `Line 1060` added `special_commands` string to add proxy and blockchain commands to startup script.
15. `Line 1081-1083` added commands to start Ganache blockchain if node is `IX100`. 
16. `Lines 1089-1098` hack job code to add IXes to nodes array. Need to fix. Was for a test.
17. `Lines 1102-1103` deploys proxy accounts for all nodes in toplogy as part of startup script for blockchain.
18. `Lines 1110-1115` using the random selector for deployment, any router that is picked to deploy a proxy will inlude all necessary configuration/setup into the startup of that router node.
19. `Lines 1126-1146` old commands to customize deployment. Moved all to pre-built image config to speed up deployment.
20. `Line 345` added privileged statement for each container. Can't remember what I needed for, but definitely needed.
21. `Line 360` removed `:` after `line 358` to fix error when deploying B00 example (random : causes build to fail)

### Node.py
1. `Lines 299-318` Not sure what greg was doing here, but there are some changes.
2. `Lines 963-967` Bashayer added default route statement to get routers to use 'rw' router correctly.
3. `Lines 972-973` Bashayer added default routing to host NAT to allow real-world use correctly. 

### Mini-internet_large.py
1. `Lines 68-83` Bashayer added random selector code for experiment deployments for a given % of topology.
2. `Line 87` added `proxy[#]` as identifier for random selection. Selected ASes will deploy proxy using setup scripts as appropriate.
3. `Line 378` added `override=True` to overwrite experiments automatically to avoid extra steps.

### Dockerfile (root directory)
1. Base image build file. If needing to adjust anything on base image, use this Dockerfile.

### `_exp` (root directory)
1. bash script to auto-deploy most of the experiment setup. -d flag specifies percentage of ASes deploying security solution.

### `Hijack/<files>`
1. `control_plane.sh` shell script to check router control plane for inclusion of malicious routes.
2. `Random_Hijack.sh` shell script to randomly inject bad advertisement into toplogy.
