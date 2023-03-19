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
ix81 = base.createInternetExchange(81)
ix2 = base.createInternetExchange(2)
ix3 = base.createInternetExchange(3)
ix4 = base.createInternetExchange(4)
ix5 = base.createInternetExchange(5)
ix6 = base.createInternetExchange(6)
ix7 = base.createInternetExchange(7)
ix8 = base.createInternetExchange(8)
ix9 = base.createInternetExchange(9)
ix10 = base.createInternetExchange(10)
ix11 = base.createInternetExchange(11)
ix12 = base.createInternetExchange(12)
ix13 = base.createInternetExchange(13)
ix14 = base.createInternetExchange(14)
ix15 = base.createInternetExchange(15)
ix16 = base.createInternetExchange(16)
ix17 = base.createInternetExchange(17)
ix18 = base.createInternetExchange(18)
ix19 = base.createInternetExchange(19)
ix20 = base.createInternetExchange(20)
ix21 = base.createInternetExchange(21)







###############################################################################
# 5 Transit ASes -> 100-105
# 12 Stub ASes -> 106-117
# Total num ASes of 17
total_ASes =  41
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
Makers.makeTransitAs(base, 85, [2, 81], [(2, 81)], proxy[0])
Makers.makeTransitAs(base, 86, [2, 11], [(2, 11)], proxy[1])
Makers.makeTransitAs(base, 91, [12, 20], [(12, 20)], proxy[2])
Makers.makeTransitAs(base, 92, [6, 12], [(6, 12)], proxy[3])
Makers.makeTransitAs(base, 93, [12, 81], [(12, 81)], proxy[4])
Makers.makeTransitAs(base, 94, [12, 3], [(12, 3)], proxy[5])
Makers.makeTransitAs(base, 95, [17, 10], [(17, 10)], proxy[6])
Makers.makeTransitAs(base, 110, [10, 2], [(10, 2)], proxy[7])
Makers.makeTransitAs(base, 112, [18, 9], [(18, 9)], proxy[8])
Makers.makeTransitAs(base, 113, [9, 17], [(9, 17)], proxy[9])
Makers.makeTransitAs(base, 114, [8, 5], [(8, 5)], proxy[10])
Makers.makeTransitAs(base, 115, [17, 16], [(17, 16)], proxy[11])
Makers.makeTransitAs(base, 116, [16, 8], [(16, 8)], proxy[12])
Makers.makeTransitAs(base, 135, [8, 15], [(8, 15)], proxy[14])
Makers.makeTransitAs(base, 136, [81, 4], [(81, 4)], proxy[15])
Makers.makeTransitAs(base, 137, [7, 14], [(7, 14)], proxy[16])
Makers.makeTransitAs(base, 138, [4, 14], [(4, 14)], proxy[17])
Makers.makeTransitAs(base, 153, [7, 19], [(7, 19)], proxy[18])
Makers.makeTransitAs(base, 154, [13, 3], [(13, 3)], proxy[19])


#Makers.makeTransitAs(base, 164, [187, 188], [(187, 188)], proxy[79])
#####################################################################
Makers.makeStubAs(emu, base, 249, 81, [None], proxy[20])
Makers.makeStubAs(emu, base, 170, 2, [None], proxy[21])
Makers.makeStubAs(emu, base, 171, 3, [None], proxy[22])
Makers.makeStubAs(emu, base, 172, 4, [None], proxy[23])
Makers.makeStubAs(emu, base, 173, 5, [None], proxy[24])
Makers.makeStubAs(emu, base, 174, 6, [None], proxy[25])
Makers.makeStubAs(emu, base, 175, 7, [None], proxy[26])
Makers.makeStubAs(emu, base, 176, 8, [None], proxy[27])
Makers.makeStubAs(emu, base, 177, 9, [None], proxy[28])
Makers.makeStubAs(emu, base, 178, 10, [None], proxy[29])
Makers.makeStubAs(emu, base, 179, 11, [None], proxy[30])
Makers.makeStubAs(emu, base, 180, 12, [None], proxy[31])
Makers.makeStubAs(emu, base, 181, 13, [None], proxy[32])
Makers.makeStubAs(emu, base, 182, 14, [None], proxy[33])
Makers.makeStubAs(emu, base, 183, 15, [None], proxy[34])
Makers.makeStubAs(emu, base, 184, 16, [None], proxy[35])
Makers.makeStubAs(emu, base, 185, 17, [None], proxy[36])
Makers.makeStubAs(emu, base, 186, 18, [None], proxy[37])
Makers.makeStubAs(emu, base, 187, 19, [None], proxy[38])
Makers.makeStubAs(emu, base, 188, 20, [None], proxy[39])








# Create real-world AS.
# AS11872 is the Syracuse University's autonomous system

as11872 = base.createAutonomousSystem(11872)
as11872.createRealWorldRouter('rw').joinNetwork('ix2', '10.2.0.118')


###############################################################################
# Peering via RS (route server). The default peering mode for RS is PeerRelationship.Peer, 
# which means each AS will only export its customers and their own prefixes. 
# We will use this peering relationship to peer all the ASes in an IX.
# None of them will provide transit service for others. 


ebgp.addRsPeers(81, [249, 85, 136, 93])
ebgp.addRsPeers(2, [170, 85, 86, 11872])
ebgp.addRsPeers(3, [171, 94])
ebgp.addRsPeers(4, [172, 136,138])
ebgp.addRsPeers(5, [173, 114])
ebgp.addRsPeers(6, [174, 92])
ebgp.addRsPeers(7, [175, 153, 137])
ebgp.addRsPeers(8, [176, 114,116,135])
ebgp.addRsPeers(9, [177, 112, 113])
ebgp.addRsPeers(10, [178, 110, 95])
ebgp.addRsPeers(11, [179, 86])
ebgp.addRsPeers(12, [180, 91, 92, 94, 93])
ebgp.addRsPeers(13, [181, 154])
ebgp.addRsPeers(14, [182, 137, 138])
ebgp.addRsPeers(15, [183, 135, 134])
ebgp.addRsPeers(16, [184, 115, 116])
ebgp.addRsPeers(17, [185, 113, 115, 95])
ebgp.addRsPeers(18, [186, 112])
ebgp.addRsPeers(19, [187, 153])
ebgp.addRsPeers(20, [188, 91])

######58/20 = 2.9 connection density/IX or 1.85 removing stubs









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
emu.compile(Docker(), './output_1to1_20', override=True)

