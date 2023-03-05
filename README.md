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
