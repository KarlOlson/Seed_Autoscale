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









###############################################################################
# 5 Transit ASes -> 100-105
# 12 Stub ASes -> 106-117
# Total num ASes of 17
total_ASes =  60
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
Makers.makeTransitAs(base, 69, [8, 19], [(8, 19)], proxy[7])
Makers.makeTransitAs(base, 70, [8, 18], [(8, 18)], proxy[8])
Makers.makeTransitAs(base, 71, [7, 18], [(7, 18)], proxy[9])
Makers.makeTransitAs(base, 72, [17, 18], [(17, 18)], proxy[10])
Makers.makeTransitAs(base, 73, [15, 16], [(15, 16)], proxy[11])
Makers.makeTransitAs(base, 74, [4, 16], [(4, 16)], proxy[12])
Makers.makeTransitAs(base, 80, [13, 4], [(13, 4)], proxy[13])
Makers.makeTransitAs(base, 81, [17, 7], [(17, 7)], proxy[14])
Makers.makeTransitAs(base, 82, [16, 17], [(16, 17)], proxy[15])
Makers.makeTransitAs(base, 83, [11, 12], [(11, 12)], proxy[16])
Makers.makeTransitAs(base, 87, [14, 13], [(14, 13)], proxy[17])
Makers.makeTransitAs(base, 90, [18, 19], [(18, 19)], proxy[18])
Makers.makeTransitAs(base, 92, [16, 6], [(16, 6)], proxy[19])
Makers.makeTransitAs(base, 93, [15, 6], [(15, 6)], proxy[20])
Makers.makeTransitAs(base, 94, [6, 5], [(6, 5)], proxy[21])
Makers.makeTransitAs(base, 95, [14, 5], [(14, 5)], proxy[22])
Makers.makeTransitAs(base, 96, [15, 14], [(15, 14)], proxy[23])
Makers.makeTransitAs(base, 99, [5, 13], [(5, 13)], proxy[24])
Makers.makeTransitAs(base, 100, [13, 12], [(13, 12)], proxy[25])
Makers.makeTransitAs(base, 111, [16, 7], [(16, 7)], proxy[26])
Makers.makeTransitAs(base, 112, [7, 8], [(7, 8)], proxy[27])
Makers.makeTransitAs(base, 113, [2, 3], [(2, 3)], proxy[28])
Makers.makeTransitAs(base, 123, [4, 12], [(4, 12)], proxy[29])
Makers.makeTransitAs(base, 124, [5, 4], [(5, 4)], proxy[30])
Makers.makeTransitAs(base, 125, [4, 11], [(4, 11)], proxy[31])
Makers.makeTransitAs(base, 126, [3, 4], [(3, 4)], proxy[32])
Makers.makeTransitAs(base, 127, [3, 10], [(3, 10)], proxy[33])
Makers.makeTransitAs(base, 128, [9, 10], [(9, 10)], proxy[34])
Makers.makeTransitAs(base, 129, [10, 11], [(10, 11)], proxy[35])
Makers.makeTransitAs(base, 132, [9, 20], [(9, 20)], proxy[36])
Makers.makeTransitAs(base, 133, [2, 9], [(2, 9)], proxy[37])
Makers.makeTransitAs(base, 134, [9, 19], [(9, 19)], proxy[38])
Makers.makeTransitAs(base, 84, [20, 10], [(20, 10)], proxy[39])








#Makers.makeTransitAs(base, 164, [187, 188], [(187, 188)], proxy[79])
#####################################################################
Makers.makeStubAs(emu, base, 249, 61, [None], proxy[40])
Makers.makeStubAs(emu, base, 190, 2, [None], proxy[41])
Makers.makeStubAs(emu, base, 191, 3, [None], proxy[42])
Makers.makeStubAs(emu, base, 192, 4, [None], proxy[43])
Makers.makeStubAs(emu, base, 193, 5, [None], proxy[44])
Makers.makeStubAs(emu, base, 194, 6, [None], proxy[45])
Makers.makeStubAs(emu, base, 195, 7, [None], proxy[46])
Makers.makeStubAs(emu, base, 196, 8, [None], proxy[47])
Makers.makeStubAs(emu, base, 197, 9, [None], proxy[48])
Makers.makeStubAs(emu, base, 198, 10, [None], proxy[49])
Makers.makeStubAs(emu, base, 199, 11, [None], proxy[50])
Makers.makeStubAs(emu, base, 200, 12, [None], proxy[51])
Makers.makeStubAs(emu, base, 201, 13, [None], proxy[52])
Makers.makeStubAs(emu, base, 202, 14, [None], proxy[53])
Makers.makeStubAs(emu, base, 203, 15, [None], proxy[54])
Makers.makeStubAs(emu, base, 204, 16, [None], proxy[55])
Makers.makeStubAs(emu, base, 205, 17, [None], proxy[56])
Makers.makeStubAs(emu, base, 206, 18, [None], proxy[57])
Makers.makeStubAs(emu, base, 207, 19, [None], proxy[58])
Makers.makeStubAs(emu, base, 208, 20, [None], proxy[59])










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
ebgp.addRsPeers(2, [190, 67, 68, 133, 11872, 113])
ebgp.addRsPeers(3, [191, 66, 126, 127, 113])
ebgp.addRsPeers(4, [192, 65, 123, 124, 125, 126, 74, 80])
ebgp.addRsPeers(5, [193, 64, 94, 95, 99, 124])
ebgp.addRsPeers(6, [194, 63, 92, 93, 94])
ebgp.addRsPeers(7, [195, 62, 81, 71, 112, 111])
ebgp.addRsPeers(8, [196, 68, 69, 70, 112])
ebgp.addRsPeers(9, [197, 128, 132, 133, 134])
ebgp.addRsPeers(10, [198, 127, 128, 129, 84])
ebgp.addRsPeers(11, [199, 125, 129, 83])
ebgp.addRsPeers(12, [200, 100,  123, 83])
ebgp.addRsPeers(13, [201,  99, 100, 87, 80])
ebgp.addRsPeers(14, [202, 95, 96 ,  87])
ebgp.addRsPeers(15, [203,  93, 96,  73])
ebgp.addRsPeers(16, [204, 82, 92, 111, 73, 74])
ebgp.addRsPeers(17, [205, 72, 81, 82])
ebgp.addRsPeers(18, [206, 70, 71, 72, 90])
ebgp.addRsPeers(19, [207, 69, 134, 90])
ebgp.addRsPeers(20, [208,  132, 84])


####AVG IX Connection = 101/20 = 5.03 ASes, 4 without Stubs.




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
emu.compile(Docker(), './output_2to1_40', override=True)
