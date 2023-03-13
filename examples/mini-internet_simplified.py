#!/usr/bin/env python3
# encoding: utf-8

from seedemu.layers import Base, Routing, Ebgp, Ibgp, Ospf, PeerRelationship, Dnssec
from seedemu.services import WebService, DomainNameService, DomainNameCachingService
from seedemu.services import CymruIpOriginService, ReverseDomainNameService, BgpLookingGlassService
from seedemu.compiler import Docker, Graphviz
from seedemu.hooks import ResolvConfHook
from seedemu.core import Emulator, Service, Binding, Filter
from seedemu.layers import Router
from seedemu.raps import OpenVpnRemoteAccessProvider
from seedemu.utilities import Makers
from typing import List, Tuple, Dict
import argparse
import random

#Process command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('-d', type=int, required = False,
                    help="proxy deployment percentage")
FLAGS = parser.parse_args()
###############################################################################
emu     = Emulator()
base    = Base()
routing = Routing()
ebgp    = Ebgp()
ibgp    = Ibgp()
ospf    = Ospf()
web     = WebService()
ovpn    = OpenVpnRemoteAccessProvider()


###############################################################################


ix101 = base.createInternetExchange(101)
ix102 = base.createInternetExchange(102)
ix103 = base.createInternetExchange(103)
ix104 = base.createInternetExchange(104)
ix105 = base.createInternetExchange(105)
ix106 = base.createInternetExchange(106)
ix107 = base.createInternetExchange(107)
ix108 = base.createInternetExchange(108)
ix109 = base.createInternetExchange(109)
ix110 = base.createInternetExchange(110)


###############################################################################
# 5 Transit ASes -> 100-105
# 12 Stub ASes -> 106-117
# Total num ASes of 17
total_ASes =  72
if FLAGS.d:       
  dep_percentage = FLAGS.d/100
  true_count = int(total_ASes * dep_percentage)
  false_count = total_ASes - true_count
  proxy = [True] * true_count + [False] * false_count
  #random.seed(0) 
  random.shuffle(proxy)
else: # no percentage specified, do not deploy proxy
  proxy = [False] * total_ASes
  
###############################################################################
# Create Transit Autonomous Systems 

## Tier 1 ASes
Makers.makeTransitAs(base, 16, [101, 102], [(101, 102)], proxy[0])
Makers.makeTransitAs(base, 2, [101, 107], [(101, 107)], proxy[1])
Makers.makeTransitAs(base, 3, [101, 106], [(101, 106)], proxy[2])
Makers.makeTransitAs(base, 4, [102, 106], [(102, 106)], proxy[3])
Makers.makeTransitAs(base, 5, [105, 102], [(105, 102)], proxy[4])
Makers.makeTransitAs(base, 6, [103, 102], [(103, 102)], proxy[5])
Makers.makeTransitAs(base, 7, [103, 105], [(103, 105)], proxy[6])
Makers.makeTransitAs(base, 8, [103, 104], [(103, 104)], proxy[7])
Makers.makeTransitAs(base, 9, [105, 104], [(105, 104)], proxy[8])
Makers.makeTransitAs(base, 11, [109, 110], [(109, 110)], proxy[9])
Makers.makeTransitAs(base, 12, [105, 109], [(105, 109)], proxy[10])
Makers.makeTransitAs(base, 13, [108, 109], [(108, 109)], proxy[11])
Makers.makeTransitAs(base, 14, [108, 106], [(108, 106)], proxy[12])
Makers.makeTransitAs(base, 15, [108, 107], [(108, 107)], proxy[13])
Makers.makeTransitAs(base, 10, [104, 110], [(104, 110)], proxy[14])
###############################################################################
# Create single-homed stub ASes. "None" means create a host only 

Makers.makeStubAs(emu, base, 150, 101, [None], proxy[15])
Makers.makeStubAs(emu, base, 151, 102, [None], proxy[16])
Makers.makeStubAs(emu, base, 152, 103, [None], proxy[17])
Makers.makeStubAs(emu, base, 153, 104, [None], proxy[18])
Makers.makeStubAs(emu, base, 154, 105, [None], proxy[19])
Makers.makeStubAs(emu, base, 155, 106, [None], proxy[20])
Makers.makeStubAs(emu, base, 156, 107, [None], proxy[21])
Makers.makeStubAs(emu, base, 157, 108, [None], proxy[22])
Makers.makeStubAs(emu, base, 158, 109, [None], proxy[23])
Makers.makeStubAs(emu, base, 159, 110, [None], proxy[24])



# Add a host with customized IP address to AS-154 
#as154 = base.getAutonomousSystem(154)
#as154.createHost('host_2').joinNetwork('net0', address = '10.154.0.129')


# Create real-world AS.
# AS11872 is the Syracuse University's autonomous system

#as11872 = base.createAutonomousSystem(11872)
#as11872.createRealWorldRouter('rw').joinNetwork('ix102', '10.102.0.118')

# Allow outside computer to VPN into AS-152's network
#as152 = base.getAutonomousSystem(152)
#as152.getNetwork('net0').enableRemoteAccess(ovpn)


###############################################################################
#Simplification approach - Everything peers via IX. Will cause initial redirecting to appear,
#but that won't cause issues. Note that this is not route loop proof.


ebgp.addRsPeers(101, [16, 3, 2, 150])
ebgp.addRsPeers(102, [16, 4,5,6, 151])
ebgp.addRsPeers(103, [6, 7, 8, 152])
ebgp.addRsPeers(104, [8, 9, 10, 153])
ebgp.addRsPeers(105, [5, 7, 9,12, 154])
ebgp.addRsPeers(106, [4, 3, 14, 155])
ebgp.addRsPeers(107, [2, 15, 156])
ebgp.addRsPeers(108, [13, 14,15, 157])
ebgp.addRsPeers(109, [11, 12, 13, 158])
ebgp.addRsPeers(110, [10, 11, 159])



###############################################################################

# Add layers to the emulator
emu.addLayer(base)
emu.addLayer(routing)
emu.addLayer(ebgp)
emu.addLayer(ibgp)
emu.addLayer(ospf)
emu.addLayer(web)

# Save it to a component file, so it can be used by other emulators
emu.dump('base-component.bin')

# Uncomment the following if you want to generate the final emulation files
emu.render()
emu.compile(Docker(), './output_large1', override=True)

