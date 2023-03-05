This contains the complete BGPchain and test environment using the Mini-internet topology.

# To Run an Experiment
1. from `examples` find your experiment folder and run the chosen python file. Note: you can define a % of the topology to deploy BGPchain on by issuing the following `python3 mini-internet.py -d 50` will deply on 50% of the ASes. At the moment you must have a manual count and statically define the total.

2. [OLD - NEW Upates fix this. No longer needed] After topology deployed, run the `/bgp_smart_contracts/configs/b00-mini-internet/routerupdate.sh` script to reconfigure the topology to be fully routable. eg. `sudo bash routerupdate.sh`

3. Validate Topology operation and # devices with proxy running (identified by `_proxy` in name).

4. Validate control plane for target hijack prefix (none should have before attack). `/Hijacks/control_plane.sh`, e.g. `sudo ./control_plane.sh 10.199.0.0/24`

5. Conduct Hijack. `Hijacks/Random_Hijacks.sh`, e.g. `sudo ./Random_Hijack.sh 10.199.0.0/24'

6. Recheck control plan for effected routers. Verify that results make sense.


#Things to add
1. Automatically calculate the total ASes? 
2. Pull and aggregate proxy results (logs) showing attacks.
3. New Larger Toplogy
4. Per router? 

## Getting Started

To get started with the emulator:
1. Clone this repository into your environment (Windows or Linux or a VM).
2. Install docker, docker-compose, and python3 in your environment. 
3. If you require more than the 200 pre-defined blockchain accounts you should pre-establish them now and update the `bgp_smart_contracts/src/.env` file and the `accounts.txt` file with the additional accounts. You can create accounts by running `ganache -a <# of accounts> --deterministic` from any device with ganache installed. The deterministic flag will result in the same account info regardless of system. In the seed emulator, this can be run on the `ix100` system. Just copy and paste the generated data into the `.env` and `.txt` files following the same formatting (different for each file).

## Running a BGP and blockchain Scenario in SEED
1. Add `seedemu` to `PYTHONPATH`. This can be done by running `source development.env` under the project root directory or running `export PYTHONPATH="`pwd`:$PYTHONPATH" from the root seed directory.
1. Pre-built scenarios are located in the `/examples` folder. 
2. Pick an example, say `A00-simple-peering`. 
3. Build the emulation. For this example, cd to `examples/A00-simple-peering/`, and run `python3 ./simple-peering.py`. The container files will be created inside the newly generated `output/` folder in the same directory. For some examples, such as `B02-mini-internet-with-dns`, they depend on other examples, so you need to run those examples first. This is part of our component design.
4. Build and run the containers. First `cd output/`, then do `docker-compose build && docker-compose up`. The emulator will start running. Give it a minute or two (or longer if your emulator is large) to let the routers do their jobs. If this is a first build it can take about 40 minutes to build the containers.
5. Optionally, start the seedemu web client. Open a new terminal window, navigate to the project root directory, cd to `client/`, and run `docker-compose build && docker-compose up`. Then point your browser to `http://127.0.0.1:8080/map.html`, and you will see the entire emulator. Use the filter box if you want to see the packet flow.
6. [OPTIONAL] Ganache is set to load on the `ix100` device at startup and deploy the `IANA ACCOUNT0` account followed by the accounts and prefixes specified in the `account_script.py` script. You should see in your terminal after the containers deploy these accounts deploying on the chain successfully. If there is an issue or you want to reset the blockchain you can do so by going into the seed web client, click on the `ix100` device and then click `connect`. This will bring up the command prompt for that device. Deploy ganache by entering `$ ganache -a 200 -p 8545 -h 10.100.0.100 --deterministic`. Optionally, you can add `--database.dbPath /ganache` if you want to store and maintain the updates on the chain. I typically dont. 
7. [OPTIONAL] The startup scripts will establish the contract and the initial conditions by automatically running `$python3 compile.py` followed by `python3 deploy.py ACCOUNT0`. If you desire to add accounts separately later, this can be done from any device as they are all pre-loaded with these scripts. Once this is setup, you can run `account_script.py` to bulk deploy ASNs and Prefix's to the contract. Within here you can specify the ASNs you want authorized for the chain by defining line 16 values. So if you pick `asn_number=[151,152]` as the values, this will load the blockchain by assigning those ASNs to Account 151 and Account 152 along with their prefixes: 10.151.0.0/24 and 10.152.0.0/24. Those routers will then have to validate their actions on the chain when advertising.
8. [OPTIONAL] Again, the proxy will deploy automatically on each device. You can verify by running a `ps -aux` on your device and you should see a process for the python proxy script. Proxy should be running on each routing device by default. If not, you can manually deploy by running: `/bgp_smart_contracts/src/proxy.py` code to launch the proxy to begin intercepting packets and validating BGP packets with blockchain. 

## Known issues/To be worked.

1. I made new repositories on my account and set to public for easy update/changes. I can switch back, but one of Greg's was private and required entering my gpd key and programming that in to the compiler in order to pull. I am sure there is a way to automate without hard coding a password token in...but haven't got there. This was a quick test/fix.
2. The proxy stops/locks when using the graphical `disconnect` on the local router in seed. Not sure on cause.
3. Not an issue, but something to be aware of: The proxies are configured to only act on their own or neighbor updates. So changes occuring 2+ routers away do not trigger chain lookups.
4. The proxies deploy (even with docker depends-on trigger) before the blockchain is fully deployed. This prevents some necessary account info from being setup to validate requests. Am working a script to listen for blockchain setup completion before running proxy to avoid this issue. Otherwise to play right now you just need to reload the proxy on the device you are using and all is well.

## Key Files:
1. `/bgp_smart_contracts/src/.env` contains all the account info and location of system running the ganache chain. Used by all the blockchain setup scripts.
2. `/bgp_smart_contracts/src/solc_ver_install.py` script run by docker to pre-load solc version used by smart contracts. Currently set to 0.8.0 to support Greg's scripts.
3. `/bgp_smart_contracts/src/accounts.txt` contains same account info as .env but in a more python friendly parsable format.
4. `/bgp_smart_contracts/src/proxy.py` code to launch blockchain-integrated proxy for capturing and assessing BGP advertisements.
5. `/bgp_smart_contracts/src/compile.py` compiles smart contract
6. `/bgp_smart_contracts/src/deploy.py` deploys smart contract on ganache blockchain
7. `/bgp_smart_contracts/src/add_asn.py` establishes new ASNs within the smart contract
8. `/bgp_smart_contracts/src/add_prefix.py` assigns prefixes to ASNs within the smart contract
9. `Seed_scalable_complete/seedemu/compiler/docker.py` compiler script used to build containers for both local and distrubuted environments (the distributed_docker.py calls on this to build the containers first). Edit this file if you need to change any containers with pre-loaded requirements. Alternatively, if something necessary on all images, update the base image (see below).
10. `Seed_scalable_complete/Dockerfile` is the base build image. It is saved on docker repository as: `karlolson1/bgpchain:latest`. If you are going to add something to base image, then use this file and update compiler to point to your docker image, or update the `karlolson1/bgpchain:latest` image. This pre-build speeds up processing of images significantly.

## Base Image Customization
Currently the base image config used for all devices is found at `Seed_scalable_complete/Dockerfile` and on docker hub as `karlolson1/bgpchain:latest`. The compiler points to this image to help speed up processing on builds by using an image that has everything pre-loaded (everything in the `Seed_scalable_complete/Dockerfile`). If you plan to update the image, follow the below steps:
1. Modify the `Seed_scalable_complete/Dockerfile` to reflect your changes and save.
2. Run `docker image build .` from the directory of the Dockerfile. Alternatively, you can replace the `.` with the location of an alternate dockerfile. 
3. Tag the image by running `docker tag local-image:tagname new-repo:tagname`. You will have to figure out what your local image name is if you didn't specify a tag while building. Eg. `docker tag e34dca56 karlolson1/bgpchain:latest
4. Push the new image to your repository using `docker push new-repo:tagname` , eg. `docker push karlolson1/bgpchain:latest`. If you get an error you may not be logged in to your docker account. If so, run `docker login` and follow prompt to log in to your account first and retry the push.
5. You also may have an old image of the same name locally. If you see that nothing was pushed, check your list of images and see if there is a conflicting one. Remove it with `docker rmi <imagename>`.


## Terraform and Google Cloud Deployment
You can use SEED to build a terraform project and then deploy that to google cloud programmatically. This will walk you thorugh steps necessary to deploy in GCP.

### Google Cloud Setup
1. Go to https://cloud.google.com/ and establish an account. You will get $300 in compute time credit (you will need a credit card to verify yourself, but it is never charged, even after use of credits). 
2. Once you have an account, the first thing you will need to define is a new project. If first time, this should be your landing page. If not, in top left of screen is a drop down (next to the three line menu), select that and do `New Project`. 
3. Now you need to creat a service account that will be used by the Terraform environment to deploy everything to the cloud. A service account is just like any other account, but you can control permissions and such separately to control settings as you see fit. To create a service account that will be used by Terraform, click the 3 line menu in the top left of the screen, select `IAM & Admin ->Service Accounts`. Then select `Create new account`. Give it a name like `terraform` and then click next. On role, assign it `compute admin` and then click `continue`. Click done. Update: for later/larger configurations with firewalls, etc. you will need additional permissions: `Compute Instance Admin v1`, `Compute network admin`, `Compute security admin`, `compute.firewalls.create` (create a new role and assign this separately, then add new role to permissions selection for service account).
4. Add keys to your service account. You should see your account created, but no keys assigned. On the far right, click the three dots to bring up a menu. Then click `manage keys`. Select `add key->create new key` and then select .json as your output. A new public key will be added to your account. The private key is automatically downloaded so check your downloads. You will need to move this key to the directory that contains your terraform files. 

### SEED VM Setup
1. For the most part everything should be set up with seed. There are two changes that you need to make in order to compile to a terraform output and then deploy the terraform environment. 
2. The first thing you need to change is compilation script to select your chosen output method. In this script change your compiler to GcpDistributedDocker() prior to compilation. 
3. Run the compilation script for your project to generate the output files and directory which should include all the terraform scripts.
4. Prior to deploying in terraform, you will likely need to install `jq` on your host. This is used for key generation for terraform containers. The errors don't really clue you in to the fact that this package is likely missing, so if you get a warning that 'ssh-keygen' failed, this is likely the issue. Just run a `sudo apt-get install -y jq` and you should have everything needed to run terraform.

### Terraform Deployment
1. To run execute `terraform init` from your root project directory (the one with main.tf file). Make sure you have your Google cloud .json key in this directory form the earlier steps. Running init will ask a few questions about your targeted google cloud environment. For `Path to credential JSON file` enter the path to where you placed your private key (should be the same location as the main.tf file). For `Project ID`, this can be found under `IAM & Admin - > Settings` and then grab the number under `Project Number` (alternatively the project ID name also should work). For `Region` and `Zone` you can pick any of the options from google. If no idea, pick `us-west4` for Region and `us-west4-b` for zone. 
2. Everything should now deploy. Give it about 5 minutes and you should see everything deployed in your Google cloud project under the `compute` resource (under the menu). Each IX will deploy on a docker swarm `master` node and each AS will deploy on its own `worker` node. All items associated with an AS will deploy on the same worker node. 
3. To prevent long term charges, you need to completely wipe the effort when done. Otherwise maintining the VMs occur charges by the minute. To wipe, go to 'IAM->Resources' and then select and delete the resources. You can also delete the project by going to the 'Dashboard->project settins-> select and delete'. 

### Terraform Issues:
1. If you deploy the terraform to the same project more than once, there is an error about some conflicting network information already existing for swarm deployment. I cannot figure out what this is (after deleting everything within the project). I have to start a new project (and create a new credential) each time I deploy. Not a big issue as you will likely clear out a project anyway to prevent recurring billing charges....but can be annoying if doing quick tests. Have yet to ID/solve conflict.

### Good Commands To Know:
1. scapy: pkt.show() - Shows packet information in pretty print format, does not recalculate packet info (chksum, length). use show2() to recalc.
2. scapy: pkt.command() - Shows packet information in order of what commands you would use to get to specific data
3. docker: docker cp {containerId}:/file/path/within/container /host/path/target - copies file form container to local host
4. docker: docker container exec -it [containerId] /bin/zsh - connects to a container from a host.


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
