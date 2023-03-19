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
ix21 = base.createInternetExchange(21)
ix22 = base.createInternetExchange(22)
ix23 = base.createInternetExchange(23)
ix24 = base.createInternetExchange(24)
ix25 = base.createInternetExchange(25)
ix26 = base.createInternetExchange(26)
ix27 = base.createInternetExchange(27)
ix28 = base.createInternetExchange(28)
ix29 = base.createInternetExchange(29)
ix30 = base.createInternetExchange(30)








###############################################################################
# 5 Transit ASes -> 100-105
# 12 Stub ASes -> 106-117
# Total num ASes of 17
total_ASes =  90
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
Makers.makeTransitAs(base, 73, [18, 30], [(18, 30)], proxy[11])
Makers.makeTransitAs(base, 74, [30, 19], [(30, 19)], proxy[12])
Makers.makeTransitAs(base, 75, [29, 30], [(29, 30)], proxy[13])
Makers.makeTransitAs(base, 80, [29, 17], [(29, 17)], proxy[14])
Makers.makeTransitAs(base, 81, [17, 7], [(17, 7)], proxy[15])
Makers.makeTransitAs(base, 82, [16, 17], [(16, 17)], proxy[16])
Makers.makeTransitAs(base, 83, [28, 17], [(28, 17)], proxy[17])
Makers.makeTransitAs(base, 87, [14, 13], [(14, 13)], proxy[18])
Makers.makeTransitAs(base, 89, [27, 28], [(27, 28)], proxy[19])
Makers.makeTransitAs(base, 90, [27, 16], [(27, 16)], proxy[20])
Makers.makeTransitAs(base, 91, [27, 15], [(27, 15)], proxy[21])
Makers.makeTransitAs(base, 92, [16, 6], [(16, 6)], proxy[22])
Makers.makeTransitAs(base, 93, [15, 6], [(15, 6)], proxy[23])
Makers.makeTransitAs(base, 94, [6, 5], [(6, 5)], proxy[24])
Makers.makeTransitAs(base, 95, [14, 5], [(14, 5)], proxy[25])
Makers.makeTransitAs(base, 96, [15, 14], [(15, 14)], proxy[26])
Makers.makeTransitAs(base, 97, [14, 25], [(14, 25)], proxy[27])
Makers.makeTransitAs(base, 98, [25, 13], [(25, 13)], proxy[28])
Makers.makeTransitAs(base, 99, [5, 13], [(5, 13)], proxy[29])
Makers.makeTransitAs(base, 100, [13, 12], [(13, 12)], proxy[30])
Makers.makeTransitAs(base, 101, [13, 24], [(13, 24)], proxy[31])
Makers.makeTransitAs(base, 102, [12, 24], [(12, 24)], proxy[32])
Makers.makeTransitAs(base, 103, [26, 14], [(26, 14)], proxy[33])
Makers.makeTransitAs(base, 106, [27, 26], [(27, 26)], proxy[34])
Makers.makeTransitAs(base, 108, [26, 25], [(26, 25)], proxy[35])
Makers.makeTransitAs(base, 109, [26, 15], [(26, 15)], proxy[36])
Makers.makeTransitAs(base, 110, [28, 16], [(28, 16)], proxy[37])
Makers.makeTransitAs(base, 111, [16, 7], [(16, 7)], proxy[38])
Makers.makeTransitAs(base, 112, [7, 8], [(7, 8)], proxy[39])
Makers.makeTransitAs(base, 113, [2, 3], [(2, 3)], proxy[40])
Makers.makeTransitAs(base, 122, [12, 23], [(12, 23)], proxy[41])
Makers.makeTransitAs(base, 123, [4, 12], [(4, 12)], proxy[42])
Makers.makeTransitAs(base, 124, [5, 4], [(5, 4)], proxy[43])
Makers.makeTransitAs(base, 125, [4, 11], [(4, 11)], proxy[44])
Makers.makeTransitAs(base, 126, [3, 4], [(3, 4)], proxy[45])
Makers.makeTransitAs(base, 127, [3, 10], [(3, 10)], proxy[46])
Makers.makeTransitAs(base, 128, [9, 10], [(9, 10)], proxy[47])
Makers.makeTransitAs(base, 129, [10, 11], [(10, 11)], proxy[48])
Makers.makeTransitAs(base, 130, [10, 21], [(10, 21)], proxy[49])
Makers.makeTransitAs(base, 131, [20, 21], [(20, 21)], proxy[50])
Makers.makeTransitAs(base, 132, [9, 20], [(9, 20)], proxy[51])
Makers.makeTransitAs(base, 133, [2, 9], [(2, 9)], proxy[52])
Makers.makeTransitAs(base, 134, [9, 19], [(9, 19)], proxy[53])
Makers.makeTransitAs(base, 148, [21, 22], [(21, 22)], proxy[54])
Makers.makeTransitAs(base, 149, [11, 22], [(11, 22)], proxy[55])
Makers.makeTransitAs(base, 150, [12, 22], [(12, 22)], proxy[56])
Makers.makeTransitAs(base, 151, [22, 23], [(22, 23)], proxy[57])
Makers.makeTransitAs(base, 76, [28, 29], [(28, 29)], proxy[58])
Makers.makeTransitAs(base, 84, [20, 10], [(20, 10)], proxy[59])








#Makers.makeTransitAs(base, 164, [187, 188], [(187, 188)], proxy[79])
#####################################################################
Makers.makeStubAs(emu, base, 249, 61, [None], proxy[60])
Makers.makeStubAs(emu, base, 190, 2, [None], proxy[61])
Makers.makeStubAs(emu, base, 191, 3, [None], proxy[62])
Makers.makeStubAs(emu, base, 192, 4, [None], proxy[63])
Makers.makeStubAs(emu, base, 193, 5, [None], proxy[64])
Makers.makeStubAs(emu, base, 194, 6, [None], proxy[65])
Makers.makeStubAs(emu, base, 195, 7, [None], proxy[66])
Makers.makeStubAs(emu, base, 196, 8, [None], proxy[67])
Makers.makeStubAs(emu, base, 197, 9, [None], proxy[68])
Makers.makeStubAs(emu, base, 198, 10, [None], proxy[69])
Makers.makeStubAs(emu, base, 199, 11, [None], proxy[70])
Makers.makeStubAs(emu, base, 200, 12, [None], proxy[71])
Makers.makeStubAs(emu, base, 201, 13, [None], proxy[72])
Makers.makeStubAs(emu, base, 202, 14, [None], proxy[73])
Makers.makeStubAs(emu, base, 203, 15, [None], proxy[74])
Makers.makeStubAs(emu, base, 204, 16, [None], proxy[75])
Makers.makeStubAs(emu, base, 205, 17, [None], proxy[76])
Makers.makeStubAs(emu, base, 206, 18, [None], proxy[77])
Makers.makeStubAs(emu, base, 207, 19, [None], proxy[78])
Makers.makeStubAs(emu, base, 208, 20, [None], proxy[79])
Makers.makeStubAs(emu, base, 209, 21, [None], proxy[80])
Makers.makeStubAs(emu, base, 210, 22, [None], proxy[81])
Makers.makeStubAs(emu, base, 211, 23, [None], proxy[82])
Makers.makeStubAs(emu, base, 212, 24, [None], proxy[83])
Makers.makeStubAs(emu, base, 213, 25, [None], proxy[84])
Makers.makeStubAs(emu, base, 214, 26, [None], proxy[85])
Makers.makeStubAs(emu, base, 215, 27, [None], proxy[86])
Makers.makeStubAs(emu, base, 216, 28, [None], proxy[87])
Makers.makeStubAs(emu, base, 217, 29, [None], proxy[88])
Makers.makeStubAs(emu, base, 218, 30, [None], proxy[89])









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
ebgp.addRsPeers(4, [192, 65, 123, 124, 125, 126])
ebgp.addRsPeers(5, [193, 64, 94, 95, 99, 124])
ebgp.addRsPeers(6, [194, 63, 92, 93, 94])
ebgp.addRsPeers(7, [195, 62, 81, 71, 112, 111])
ebgp.addRsPeers(8, [196, 68, 69, 70, 112])
ebgp.addRsPeers(9, [197, 128, 132, 133, 134])
ebgp.addRsPeers(10, [198, 127, 128, 129, 130, 84])
ebgp.addRsPeers(11, [199, 125, 129, 149])
ebgp.addRsPeers(12, [200, 100, 102,  122, 123])
ebgp.addRsPeers(13, [201, 98, 99, 100, 101, 87])
ebgp.addRsPeers(14, [202, 95, 96 ,97, 103, 87])
ebgp.addRsPeers(15, [203, 91, 93, 96, 109])
ebgp.addRsPeers(16, [204, 82, 90, 92, 111])
ebgp.addRsPeers(17, [205, 72, 80, 81, 82, 83])
ebgp.addRsPeers(18, [206, 70, 71, 72, 73])
ebgp.addRsPeers(19, [207, 69, 74, 134])
ebgp.addRsPeers(20, [208, 131, 132, 84])
ebgp.addRsPeers(21, [209, 130, 131, 148])
ebgp.addRsPeers(22, [210, 148, 149, 150, 151])
ebgp.addRsPeers(23, [211, 122, 151])
ebgp.addRsPeers(24, [212, 101, 102])
ebgp.addRsPeers(25, [213, 97, 98, 108])
ebgp.addRsPeers(26, [214, 108, 109, 106, 103])
ebgp.addRsPeers(27, [215, 89, 90, 91, 106])
ebgp.addRsPeers(28, [216, 83,  89, 76])
ebgp.addRsPeers(29, [217, 75, 80, 76])
ebgp.addRsPeers(30, [218, 73, 74, 75])


####AVG IX Connection = 148/30 = 4.93 ASes, 3.9 without Stubs.




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
emu.compile(Docker(), './output_2to1_60', override=True)
