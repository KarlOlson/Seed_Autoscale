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
ix61 = base.createInternetExchange(61)
ix2 = base.createInternetExchange(2)
ix3 = base.createInternetExchange(3)
ix4 = base.createInternetExchange(4)
ix5 = base.createInternetExchange(5)
ix6 = base.createInternetExchange(6)
ix7 = base.createInternetExchange(7)
ix8 = base.createInternetExchange(8)
ix9 = base.createInternetExchange(9)
ix10 = base.createInternetExchange(10)










###############################################################################
# 5 Transit ASes -> 100-105
# 12 Stub ASes -> 106-117
# Total num ASes of 17
total_ASes =  30
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

##Tier 1 ASes
#None in this toplogy

## Tier 2 ASes: QTY - 8
Makers.makeTransitAs(base, 62, [7, 61], [(7, 61)], proxy[0])
Makers.makeTransitAs(base, 63, [6, 61], [(6, 61)], proxy[1])
Makers.makeTransitAs(base, 64, [5, 61], [(5, 61)], proxy[2])
Makers.makeTransitAs(base, 65, [4, 61], [(4, 61)], proxy[3])
Makers.makeTransitAs(base, 66, [3, 61], [(3, 61)], proxy[4])
Makers.makeTransitAs(base, 67, [2, 61], [(2, 61)], proxy[5])
Makers.makeTransitAs(base, 68, [2, 8], [(2, 8)], proxy[6])
Makers.makeTransitAs(base, 69, [6, 7], [(6, 7)], proxy[7])
Makers.makeTransitAs(base, 70, [7, 2], [(7, 2)], proxy[8])
Makers.makeTransitAs(base, 71, [8, 9], [(8, 9)], proxy[9])
Makers.makeTransitAs(base, 74, [2, 10], [(2, 10)], proxy[10])
Makers.makeTransitAs(base, 80, [4, 10], [(4, 10)], proxy[11])
Makers.makeTransitAs(base, 94, [6, 5], [(6, 5)], proxy[12])
Makers.makeTransitAs(base, 112, [7, 8], [(7, 8)], proxy[13])
Makers.makeTransitAs(base, 113, [2, 3], [(2, 3)], proxy[14])
Makers.makeTransitAs(base, 124, [5, 4], [(5, 4)], proxy[15])
Makers.makeTransitAs(base, 126, [3, 4], [(3, 4)], proxy[16])
Makers.makeTransitAs(base, 127, [3, 10], [(3, 10)], proxy[17])
Makers.makeTransitAs(base, 128, [9, 10], [(9, 10)], proxy[18])
Makers.makeTransitAs(base, 133, [2, 9], [(2, 9)], proxy[19])



#Makers.makeTransitAs(base, 164, [187, 188], [(187, 188)], proxy[79])
#####################################################################
Makers.makeStubAs(emu, base, 249, 61, [None], proxy[20])
Makers.makeStubAs(emu, base, 190, 2, [None], proxy[21])
Makers.makeStubAs(emu, base, 191, 3, [None], proxy[22])
Makers.makeStubAs(emu, base, 192, 4, [None], proxy[23])
Makers.makeStubAs(emu, base, 193, 5, [None], proxy[24])
Makers.makeStubAs(emu, base, 194, 6, [None], proxy[25])
Makers.makeStubAs(emu, base, 195, 7, [None], proxy[26])
Makers.makeStubAs(emu, base, 196, 8, [None], proxy[27])
Makers.makeStubAs(emu, base, 197, 9, [None], proxy[28])
Makers.makeStubAs(emu, base, 198, 10, [None], proxy[29])











# Create real-world AS.
# AS11872 is the Syracuse University's autonomous system

as11872 = base.createAutonomousSystem(11872)
as11872.createRealWorldRouter('rw').joinNetwork('ix2', '10.2.0.118')


###############################################################################
# Peering via RS (route server). The default peering mode for RS is PeerRelationship.Peer, 
# which means each AS will only export its customers and their own prefixes. 
# We will use this peering relationship to peer all the ASes in an IX.
# None of them will provide transit service for others. 


ebgp.addRsPeers(61, [249, 62, 63, 64, 65, 66, 67])
ebgp.addRsPeers(2, [190, 67, 68, 133, 11872, 113, 70, 74])
ebgp.addRsPeers(3, [191, 66, 126, 127, 113])
ebgp.addRsPeers(4, [192, 65, 124, 126, 80])
ebgp.addRsPeers(5, [193, 64, 94, 124])
ebgp.addRsPeers(6, [194, 63, 94, 69])
ebgp.addRsPeers(7, [195, 62, 112, 69, 70])
ebgp.addRsPeers(8, [196, 68, 112, 71])
ebgp.addRsPeers(9, [197, 128, 133, 71])
ebgp.addRsPeers(10, [198, 127, 128, 74, 80])



####AVG IX Connection = 51/10 = 5.01 ASes, 4 without Stubs.




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
emu.compile(Docker(), './output_2to1_20', override=True)
