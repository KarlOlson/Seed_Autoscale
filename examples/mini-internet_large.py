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
ix111 = base.createInternetExchange(111)
ix112 = base.createInternetExchange(112)
ix113 = base.createInternetExchange(113)
ix114 = base.createInternetExchange(114)
ix115 = base.createInternetExchange(115)
ix116 = base.createInternetExchange(116)
ix117 = base.createInternetExchange(117)
ix118 = base.createInternetExchange(118)
ix119 = base.createInternetExchange(119)
ix120 = base.createInternetExchange(120)
ix121 = base.createInternetExchange(121)
ix122 = base.createInternetExchange(122)
ix123 = base.createInternetExchange(123)
ix124 = base.createInternetExchange(124)
ix125 = base.createInternetExchange(125)
ix126 = base.createInternetExchange(126)
ix127 = base.createInternetExchange(127)
ix128 = base.createInternetExchange(128)
ix129 = base.createInternetExchange(129)
ix130 = base.createInternetExchange(130)
ix131 = base.createInternetExchange(131)

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
Makers.makeTransitAs(base, 51, [101, 106], [(101, 106)], proxy[0])
Makers.makeTransitAs(base, 2, [106, 102], [(106, 102)], proxy[1])
Makers.makeTransitAs(base, 3, [102, 103], [(102, 103)], proxy[2])
Makers.makeTransitAs(base, 4, [103, 105], [(103, 105)], proxy[3])
Makers.makeTransitAs(base, 5, [105, 104], [(105, 104)], proxy[4])
Makers.makeTransitAs(base, 6, [104, 115], [(104, 115)], proxy[5])
Makers.makeTransitAs(base, 7, [115, 114], [(115, 114)], proxy[6])
Makers.makeTransitAs(base, 8, [105, 131], [(105, 131)], proxy[7])
Makers.makeTransitAs(base, 9, [106, 131], [(106, 131)], proxy[8])
Makers.makeTransitAs(base, 10, [131, 117], [(131, 117)], proxy[9])
Makers.makeTransitAs(base, 11, [117, 113], [(117, 113)], proxy[10])
Makers.makeTransitAs(base, 12, [117, 123], [(117, 123)], proxy[11])
Makers.makeTransitAs(base, 13, [117, 119], [(117, 119)], proxy[12])
Makers.makeTransitAs(base, 14, [117, 114], [(117, 114)], proxy[13])
Makers.makeTransitAs(base, 15, [114, 116], [(114, 116)], proxy[14])
Makers.makeTransitAs(base, 16, [116, 118], [(116, 118)], proxy[15])
Makers.makeTransitAs(base, 17, [118, 130], [(118, 130)], proxy[16])
Makers.makeTransitAs(base, 18, [120, 130], [(120, 130)], proxy[17])
Makers.makeTransitAs(base, 19, [120, 121], [(120, 121)], proxy[18])
Makers.makeTransitAs(base, 20, [121, 125], [(121, 125)], proxy[19])
Makers.makeTransitAs(base, 21, [125, 126], [(125, 126)], proxy[20])
Makers.makeTransitAs(base, 22, [126, 129], [(126, 129)], proxy[21])
Makers.makeTransitAs(base, 23, [129, 128], [(129, 128)], proxy[22])
Makers.makeTransitAs(base, 24, [128, 127], [(128, 127)], proxy[23])
Makers.makeTransitAs(base, 25, [126, 127], [(126, 127)], proxy[24])
Makers.makeTransitAs(base, 26, [126, 124], [(126, 124)], proxy[25])
Makers.makeTransitAs(base, 27, [124, 123], [(124, 123)], proxy[26])
Makers.makeTransitAs(base, 28, [122, 123], [(122, 123)], proxy[27])
Makers.makeTransitAs(base, 29, [122, 120], [(122, 120)], proxy[28])
Makers.makeTransitAs(base, 30, [120, 119], [(120, 119)], proxy[29])
Makers.makeTransitAs(base, 31, [107, 109], [(107, 109)], proxy[30])
Makers.makeTransitAs(base, 32, [108, 109], [(108, 109)], proxy[31])
Makers.makeTransitAs(base, 33, [108, 110], [(108, 110)], proxy[32])
Makers.makeTransitAs(base, 34, [111, 110], [(111, 110)], proxy[33])
Makers.makeTransitAs(base, 35, [111, 112], [(111, 112)], proxy[34])
Makers.makeTransitAs(base, 36, [112, 123], [(112, 123)], proxy[35])
Makers.makeTransitAs(base, 37, [112, 127], [(112, 127)], proxy[36])
Makers.makeTransitAs(base, 38, [109, 111], [(109, 111)], proxy[37])
Makers.makeTransitAs(base, 39, [101, 107], [(101, 107)], proxy[38])
Makers.makeTransitAs(base, 40, [107, 113], [(107, 113)], proxy[39])
Makers.makeTransitAs(base, 41, [109, 123], [(109, 123)], proxy[40])



###############################################################################
# Create single-homed stub ASes. "None" means create a host only 

Makers.makeStubAs(emu, base, 150, 101, [None], proxy[41])
Makers.makeStubAs(emu, base, 151, 102, [None], proxy[42])
Makers.makeStubAs(emu, base, 152, 103, [None], proxy[43])
Makers.makeStubAs(emu, base, 153, 104, [None], proxy[44])
Makers.makeStubAs(emu, base, 154, 105, [None], proxy[45])
Makers.makeStubAs(emu, base, 155, 106, [None], proxy[46])
Makers.makeStubAs(emu, base, 156, 107, [None], proxy[47])
Makers.makeStubAs(emu, base, 157, 108, [None], proxy[48])
Makers.makeStubAs(emu, base, 158, 109, [None], proxy[49])
Makers.makeStubAs(emu, base, 159, 110, [None], proxy[50])
Makers.makeStubAs(emu, base, 160, 111, [None], proxy[51])
Makers.makeStubAs(emu, base, 161, 112, [None], proxy[52])
Makers.makeStubAs(emu, base, 162, 113, [None], proxy[53])
Makers.makeStubAs(emu, base, 163, 114, [None], proxy[54])
Makers.makeStubAs(emu, base, 164, 115, [None], proxy[55])
Makers.makeStubAs(emu, base, 165, 116, [None], proxy[56])
Makers.makeStubAs(emu, base, 166, 117, [None], proxy[57])
Makers.makeStubAs(emu, base, 167, 118, [None], proxy[58])
Makers.makeStubAs(emu, base, 168, 119, [None], proxy[59])
Makers.makeStubAs(emu, base, 169, 120, [None], proxy[60])
Makers.makeStubAs(emu, base, 170, 121, [None], proxy[61])
Makers.makeStubAs(emu, base, 171, 122, [None], proxy[62])
Makers.makeStubAs(emu, base, 172, 123, [None], proxy[63])
Makers.makeStubAs(emu, base, 173, 124, [None], proxy[64])
Makers.makeStubAs(emu, base, 174, 125, [None], proxy[65])
Makers.makeStubAs(emu, base, 175, 126, [None], proxy[66])
Makers.makeStubAs(emu, base, 176, 127, [None], proxy[67])
Makers.makeStubAs(emu, base, 177, 128, [None], proxy[68])
Makers.makeStubAs(emu, base, 178, 129, [None], proxy[69])
Makers.makeStubAs(emu, base, 179, 130, [None], proxy[70])
Makers.makeStubAs(emu, base, 180, 131, [None], proxy[71])


# Add a host with customized IP address to AS-154 
#as154 = base.getAutonomousSystem(154)
#as154.createHost('host_2').joinNetwork('net0', address = '10.154.0.129')


# Create real-world AS.
# AS11872 is the Syracuse University's autonomous system

as11872 = base.createAutonomousSystem(11872)
as11872.createRealWorldRouter('rw').joinNetwork('ix102', '10.102.0.118')

# Allow outside computer to VPN into AS-152's network
#as152 = base.getAutonomousSystem(152)
#as152.getNetwork('net0').enableRemoteAccess(ovpn)


###############################################################################
# Peering via RS (route server). The default peering mode for RS is PeerRelationship.Peer, 
# which means each AS will only export its customers and their own prefixes. 
# We will use this peering relationship to peer all the ASes in an IX.
# None of them will provide transit service for others. 


ebgp.addRsPeers(101, [51, 39])
ebgp.addRsPeers(102, [2, 3])
ebgp.addRsPeers(103, [3, 4])
ebgp.addRsPeers(104, [5, 6])
ebgp.addRsPeers(105, [8, 4, 5])
ebgp.addRsPeers(106, [51, 2, 9])
ebgp.addRsPeers(107, [39, 40, 31])
ebgp.addRsPeers(108, [32, 33])
ebgp.addRsPeers(109, [31, 32, 38, 41])
ebgp.addRsPeers(110, [33, 34])
ebgp.addRsPeers(111, [38, 34, 35])
ebgp.addRsPeers(112, [35, 36, 37])
ebgp.addRsPeers(113, [40, 11])
ebgp.addRsPeers(114, [7, 14, 15])
ebgp.addRsPeers(115, [6, 7])
ebgp.addRsPeers(116, [15, 16])
ebgp.addRsPeers(117, [10, 14, 11, 12, 13])
ebgp.addRsPeers(118, [16, 17])
ebgp.addRsPeers(119, [13, 30])
ebgp.addRsPeers(120, [18, 19, 29, 30])
ebgp.addRsPeers(121, [20, 19])
ebgp.addRsPeers(122, [28, 29])
ebgp.addRsPeers(123, [41, 12, 36, 27, 28])
ebgp.addRsPeers(124, [27, 26])
ebgp.addRsPeers(125, [21, 20])
ebgp.addRsPeers(126, [22, 25, 26, 21])
ebgp.addRsPeers(127, [24, 37, 25])
ebgp.addRsPeers(128, [23, 24])
ebgp.addRsPeers(129, [23, 22])
ebgp.addRsPeers(130, [17, 18])
ebgp.addRsPeers(131, [9, 8, 10])

# To buy transit services from another autonomous system, 
# we will use private peering  


ebgp.addPrivatePeerings(101, [51,39],  [150], PeerRelationship.Provider)
ebgp.addPrivatePeerings(101, [51],  [39], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(101, [39],  [150], PeerRelationship.Provider)

ebgp.addPrivatePeerings(102, [2,3],  [151], PeerRelationship.Provider)
ebgp.addPrivatePeerings(102, [2],  [3], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(102, [3],  [151], PeerRelationship.Provider)

ebgp.addPrivatePeerings(103, [3,4],  [152], PeerRelationship.Provider)
ebgp.addPrivatePeerings(103, [3],  [4], PeerRelationship.Provider)

ebgp.addPrivatePeerings(104, [5,6],  [153], PeerRelationship.Provider)
ebgp.addPrivatePeerings(104, [5],  [6], PeerRelationship.Provider)

ebgp.addPrivatePeerings(105, [4,5,8],  [154], PeerRelationship.Provider)
ebgp.addPrivatePeerings(105, [4],  [5,8], PeerRelationship.Provider)
ebgp.addPrivatePeerings(105, [5],  [8], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(105, [8],  [154], PeerRelationship.Provider)

ebgp.addPrivatePeerings(106, [51,2,9],  [155], PeerRelationship.Provider)
ebgp.addPrivatePeerings(106, [2],  [51,9], PeerRelationship.Provider)
ebgp.addPrivatePeerings(106, [51],  [9], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(106, [9],  [155], PeerRelationship.Provider)

ebgp.addPrivatePeerings(107, [31,39,40],  [156], PeerRelationship.Provider)
ebgp.addPrivatePeerings(107, [39],  [31,40], PeerRelationship.Provider)
ebgp.addPrivatePeerings(107, [31],  [40], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(107, [40],  [156], PeerRelationship.Provider)

ebgp.addPrivatePeerings(108, [33,32],  [157], PeerRelationship.Provider)
ebgp.addPrivatePeerings(108, [32],  [33], PeerRelationship.Provider)

ebgp.addPrivatePeerings(109, [31,32,38,41],  [158], PeerRelationship.Provider)
ebgp.addPrivatePeerings(109, [32],  [31,38,41], PeerRelationship.Provider)
ebgp.addPrivatePeerings(109, [31],  [38,41], PeerRelationship.Provider)
ebgp.addPrivatePeerings(109, [38],  [41], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(109, [38],  [158], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(109, [41],  [158], PeerRelationship.Provider)

ebgp.addPrivatePeerings(110, [33,34],  [159], PeerRelationship.Provider)
ebgp.addPrivatePeerings(110, [34],  [33], PeerRelationship.Provider)

ebgp.addPrivatePeerings(111, [34,38,35],  [160], PeerRelationship.Provider)
ebgp.addPrivatePeerings(111, [38],  [34,35], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(111, [35],  [160], PeerRelationship.Provider)

ebgp.addPrivatePeerings(112, [35,36,37],  [161], PeerRelationship.Provider)
ebgp.addPrivatePeerings(112, [36],  [35,37], PeerRelationship.Provider)
ebgp.addPrivatePeerings(112, [35],  [37], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(112, [37],  [161], PeerRelationship.Provider)

ebgp.addPrivatePeerings(113, [40,11],  [162], PeerRelationship.Provider)
ebgp.addPrivatePeerings(113, [11],  [40], PeerRelationship.Provider)

ebgp.addPrivatePeerings(114, [7,14,15],  [163], PeerRelationship.Provider)
ebgp.addPrivatePeerings(114, [14],  [7,15], PeerRelationship.Provider)
ebgp.addPrivatePeerings(114, [7],  [15], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(114, [15],  [163], PeerRelationship.Provider)

ebgp.addPrivatePeerings(115, [6,7],  [164], PeerRelationship.Provider)
ebgp.addPrivatePeerings(115, [7],  [6], PeerRelationship.Provider)

ebgp.addPrivatePeerings(116, [15,16],  [165], PeerRelationship.Provider)
ebgp.addPrivatePeerings(116, [16],  [15], PeerRelationship.Provider)

ebgp.addPrivatePeerings(117, [11,12,13,14,10],  [166], PeerRelationship.Provider)
ebgp.addPrivatePeerings(117, [12],  [11,13,14,10], PeerRelationship.Provider)
ebgp.addPrivatePeerings(117, [11],  [13,14,10], PeerRelationship.Provider)
ebgp.addPrivatePeerings(117, [13],  [14,10], PeerRelationship.Provider)
ebgp.addPrivatePeerings(117, [14],  [10], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(117, [13],  [166], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(117, [14],  [166], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(117, [10],  [166], PeerRelationship.Provider)

ebgp.addPrivatePeerings(118, [16,17],  [167], PeerRelationship.Provider)
ebgp.addPrivatePeerings(118, [17],  [16], PeerRelationship.Provider)

ebgp.addPrivatePeerings(119, [13,30],  [168], PeerRelationship.Provider)
ebgp.addPrivatePeerings(119, [30],  [13], PeerRelationship.Provider)

ebgp.addPrivatePeerings(120, [18,19,29,30],  [169], PeerRelationship.Provider)
ebgp.addPrivatePeerings(120, [19],  [18,29,30], PeerRelationship.Provider)
ebgp.addPrivatePeerings(120, [18],  [29,30], PeerRelationship.Provider)
ebgp.addPrivatePeerings(120, [29],  [30], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(120, [29],  [169], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(120, [30],  [169], PeerRelationship.Provider)

ebgp.addPrivatePeerings(121, [19],  [170], PeerRelationship.Provider)
ebgp.addPrivatePeerings(121, [20],  [19], PeerRelationship.Provider)

ebgp.addPrivatePeerings(122, [28,29],  [171], PeerRelationship.Provider)
ebgp.addPrivatePeerings(122, [29],  [28], PeerRelationship.Provider)

ebgp.addPrivatePeerings(123, [41,36,12,27,28],  [172], PeerRelationship.Provider)
ebgp.addPrivatePeerings(123, [36],  [41,12,27,28], PeerRelationship.Provider)
ebgp.addPrivatePeerings(123, [41],  [12,27,28], PeerRelationship.Provider)
ebgp.addPrivatePeerings(123, [12],  [27,28], PeerRelationship.Provider)
ebgp.addPrivatePeerings(123, [27],  [28], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(123, [12],  [172], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(123, [27],  [172], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(123, [28],  [172], PeerRelationship.Provider)

ebgp.addPrivatePeerings(124, [26,27],  [173], PeerRelationship.Provider)
ebgp.addPrivatePeerings(124, [27],  [26], PeerRelationship.Provider)

ebgp.addPrivatePeerings(125, [20,21],  [174], PeerRelationship.Provider)
ebgp.addPrivatePeerings(125, [21],  [20], PeerRelationship.Provider)

ebgp.addPrivatePeerings(126, [21,22,25,26],  [175], PeerRelationship.Provider)
ebgp.addPrivatePeerings(126, [22],  [21,25,26], PeerRelationship.Provider)
ebgp.addPrivatePeerings(126, [21],  [25,26], PeerRelationship.Provider)
ebgp.addPrivatePeerings(126, [25],  [26], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(126, [25],  [175], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(126, [26],  [175], PeerRelationship.Provider)

ebgp.addPrivatePeerings(127, [24,25,37],  [176], PeerRelationship.Provider)
ebgp.addPrivatePeerings(127, [25],  [24,37], PeerRelationship.Provider)
ebgp.addPrivatePeerings(127, [24],  [37], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(127, [37],  [176], PeerRelationship.Provider)

ebgp.addPrivatePeerings(128, [23,24],  [177], PeerRelationship.Provider)
ebgp.addPrivatePeerings(128, [24],  [23], PeerRelationship.Provider)


ebgp.addPrivatePeerings(129, [22,23],  [178], PeerRelationship.Provider)
ebgp.addPrivatePeerings(129, [23],  [22], PeerRelationship.Provider)


ebgp.addPrivatePeerings(130, [17,18],  [179], PeerRelationship.Provider)
ebgp.addPrivatePeerings(130, [18],  [17], PeerRelationship.Provider)

ebgp.addPrivatePeerings(131, [8,9,10],  [180], PeerRelationship.Provider)
ebgp.addPrivatePeerings(131, [9],  [8,10], PeerRelationship.Provider)
ebgp.addPrivatePeerings(131, [8],  [10], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(131, [10],  [180], PeerRelationship.Provider)


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
emu.compile(Docker(), './output_large', override=True)

