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
ix31 = base.createInternetExchange(31)
ix32 = base.createInternetExchange(32)
ix33 = base.createInternetExchange(33)
ix34 = base.createInternetExchange(34)
ix35 = base.createInternetExchange(35)
ix36 = base.createInternetExchange(36)
ix37 = base.createInternetExchange(37)
ix38 = base.createInternetExchange(38)
ix39 = base.createInternetExchange(39)
ix40 = base.createInternetExchange(40)
ix41 = base.createInternetExchange(41)
ix42 = base.createInternetExchange(42)
ix43 = base.createInternetExchange(43)
ix44 = base.createInternetExchange(44)
ix45 = base.createInternetExchange(45)
ix46 = base.createInternetExchange(46)
ix47 = base.createInternetExchange(47)
ix48 = base.createInternetExchange(48)
ix49 = base.createInternetExchange(49)
ix50 = base.createInternetExchange(50)






###############################################################################
# 5 Transit ASes -> 100-105
# 12 Stub ASes -> 106-117
# Total num ASes of 17
total_ASes =  149
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
Makers.makeTransitAs(base, 76, [42, 30], [(42, 30)], proxy[14])
Makers.makeTransitAs(base, 77, [30, 43], [(30, 43)], proxy[15])
Makers.makeTransitAs(base, 78, [42, 43], [(42, 43)], proxy[16])
Makers.makeTransitAs(base, 79, [42, 29], [(42, 29)], proxy[17])
Makers.makeTransitAs(base, 80, [29, 17], [(29, 17)], proxy[18])
Makers.makeTransitAs(base, 81, [17, 7], [(17, 7)], proxy[19])
Makers.makeTransitAs(base, 82, [16, 17], [(16, 17)], proxy[20])
Makers.makeTransitAs(base, 83, [28, 17], [(28, 17)], proxy[21])
Makers.makeTransitAs(base, 84, [41, 29], [(41, 29)], proxy[22])
Makers.makeTransitAs(base, 85, [41, 42], [(41, 42)], proxy[23])
Makers.makeTransitAs(base, 86, [41, 28], [(41, 28)], proxy[24])
Makers.makeTransitAs(base, 87, [40, 28], [(40, 28)], proxy[25])
Makers.makeTransitAs(base, 88, [40, 41], [(40, 41)], proxy[26])
Makers.makeTransitAs(base, 89, [27, 28], [(27, 28)], proxy[27])
Makers.makeTransitAs(base, 90, [27, 16], [(27, 16)], proxy[28])
Makers.makeTransitAs(base, 91, [27, 15], [(27, 15)], proxy[29])
Makers.makeTransitAs(base, 92, [16, 6], [(16, 6)], proxy[30])
Makers.makeTransitAs(base, 93, [15, 6], [(15, 6)], proxy[31])
Makers.makeTransitAs(base, 94, [6, 5], [(6, 5)], proxy[32])
Makers.makeTransitAs(base, 95, [14, 5], [(14, 5)], proxy[33])
Makers.makeTransitAs(base, 96, [15, 14], [(15, 14)], proxy[34])
Makers.makeTransitAs(base, 97, [14, 25], [(14, 25)], proxy[35])
Makers.makeTransitAs(base, 98, [25, 13], [(25, 13)], proxy[36])
Makers.makeTransitAs(base, 99, [5, 13], [(5, 13)], proxy[37])
Makers.makeTransitAs(base, 100, [13, 12], [(13, 12)], proxy[38])
Makers.makeTransitAs(base, 101, [13, 24], [(13, 24)], proxy[39])
Makers.makeTransitAs(base, 102, [12, 24], [(12, 24)], proxy[40])
Makers.makeTransitAs(base, 103, [13, 37], [(13, 37)], proxy[41])
Makers.makeTransitAs(base, 104, [24, 48], [(24, 48)], proxy[42])
Makers.makeTransitAs(base, 105, [37, 48], [(37, 48)], proxy[43])
Makers.makeTransitAs(base, 106, [25, 37], [(25, 37)], proxy[44])
Makers.makeTransitAs(base, 107, [49, 25], [(49, 25)], proxy[45])
Makers.makeTransitAs(base, 108, [26, 25], [(26, 25)], proxy[46])
Makers.makeTransitAs(base, 109, [26, 15], [(26, 15)], proxy[47])
Makers.makeTransitAs(base, 110, [38, 26], [(38, 26)], proxy[48])
Makers.makeTransitAs(base, 111, [39, 26], [(39, 26)], proxy[49])
Makers.makeTransitAs(base, 112, [39, 27], [(39, 27)], proxy[50])
Makers.makeTransitAs(base, 113, [40, 27], [(40, 27)], proxy[51])
Makers.makeTransitAs(base, 114, [40, 39], [(40, 39)], proxy[52])
Makers.makeTransitAs(base, 115, [39, 38], [(39, 38)], proxy[53])
Makers.makeTransitAs(base, 116, [38, 49], [(38, 49)], proxy[54])
Makers.makeTransitAs(base, 117, [48, 49], [(48, 49)], proxy[55])
Makers.makeTransitAs(base, 118, [48, 36], [(48, 36)], proxy[56])
Makers.makeTransitAs(base, 119, [48, 50], [(48, 50)], proxy[57])
Makers.makeTransitAs(base, 120, [36, 50], [(36, 50)], proxy[58])
Makers.makeTransitAs(base, 121, [12, 36], [(12, 36)], proxy[59])
Makers.makeTransitAs(base, 122, [12, 23], [(12, 23)], proxy[60])
Makers.makeTransitAs(base, 123, [4, 12], [(4, 12)], proxy[61])
Makers.makeTransitAs(base, 124, [5, 4], [(5, 4)], proxy[62])
Makers.makeTransitAs(base, 125, [4, 11], [(4, 11)], proxy[63])
Makers.makeTransitAs(base, 126, [3, 4], [(3, 4)], proxy[64])
Makers.makeTransitAs(base, 127, [3, 10], [(3, 10)], proxy[65])
Makers.makeTransitAs(base, 128, [9, 10], [(9, 10)], proxy[66])
Makers.makeTransitAs(base, 129, [10, 11], [(10, 11)], proxy[67])
Makers.makeTransitAs(base, 130, [10, 21], [(10, 21)], proxy[68])
Makers.makeTransitAs(base, 131, [20, 21], [(20, 21)], proxy[69])
Makers.makeTransitAs(base, 132, [9, 20], [(9, 20)], proxy[70])
Makers.makeTransitAs(base, 133, [2, 9], [(2, 9)], proxy[71])
Makers.makeTransitAs(base, 134, [9, 19], [(9, 19)], proxy[72])
Makers.makeTransitAs(base, 135, [19, 31], [(19, 31)], proxy[73])
Makers.makeTransitAs(base, 136, [31, 43], [(31, 43)], proxy[74])
Makers.makeTransitAs(base, 137, [43, 44], [(43, 44)], proxy[75])
Makers.makeTransitAs(base, 138, [31, 44], [(31, 44)], proxy[76])
Makers.makeTransitAs(base, 139, [31, 20], [(31, 20)], proxy[77])
Makers.makeTransitAs(base, 140, [20, 32], [(20, 32)], proxy[78])
Makers.makeTransitAs(base, 141, [32, 44], [(32, 44)], proxy[79])
Makers.makeTransitAs(base, 142, [44, 45], [(44, 45)], proxy[80])
Makers.makeTransitAs(base, 143, [32, 45], [(32, 45)], proxy[81])
Makers.makeTransitAs(base, 144, [32, 33], [(32, 33)], proxy[82])
Makers.makeTransitAs(base, 145, [21, 33], [(21, 33)], proxy[83])
Makers.makeTransitAs(base, 146, [45, 33], [(45, 33)], proxy[84])
Makers.makeTransitAs(base, 147, [33, 34], [(33, 34)], proxy[85])
Makers.makeTransitAs(base, 148, [21, 22], [(21, 22)], proxy[86])
Makers.makeTransitAs(base, 149, [11, 22], [(11, 22)], proxy[87])
Makers.makeTransitAs(base, 150, [12, 22], [(12, 22)], proxy[88])
Makers.makeTransitAs(base, 151, [22, 23], [(22, 23)], proxy[89])
Makers.makeTransitAs(base, 152, [22, 35], [(22, 35)], proxy[90])
Makers.makeTransitAs(base, 153, [22, 34], [(22, 34)], proxy[91])
Makers.makeTransitAs(base, 154, [23, 35], [(23, 35)], proxy[92])
Makers.makeTransitAs(base, 155, [23, 46], [(23, 46)], proxy[93])
Makers.makeTransitAs(base, 156, [23, 50], [(23, 50)], proxy[94])
Makers.makeTransitAs(base, 157, [50, 46], [(50, 46)], proxy[95])
Makers.makeTransitAs(base, 158, [47, 46], [(47, 46)], proxy[96])
Makers.makeTransitAs(base, 159, [35, 47], [(35, 47)], proxy[97])
Makers.makeTransitAs(base, 160, [34, 47], [(34, 47)], proxy[98])













#Makers.makeTransitAs(base, 164, [187, 188], [(187, 188)], proxy[79])
#####################################################################
Makers.makeStubAs(emu, base, 249, 61, [None], proxy[99])
Makers.makeStubAs(emu, base, 190, 2, [None], proxy[100])
Makers.makeStubAs(emu, base, 191, 3, [None], proxy[101])
Makers.makeStubAs(emu, base, 192, 4, [None], proxy[102])
Makers.makeStubAs(emu, base, 193, 5, [None], proxy[103])
Makers.makeStubAs(emu, base, 194, 6, [None], proxy[104])
Makers.makeStubAs(emu, base, 195, 7, [None], proxy[105])
Makers.makeStubAs(emu, base, 196, 8, [None], proxy[106])
Makers.makeStubAs(emu, base, 197, 9, [None], proxy[107])
Makers.makeStubAs(emu, base, 198, 10, [None], proxy[108])
Makers.makeStubAs(emu, base, 199, 11, [None], proxy[109])
Makers.makeStubAs(emu, base, 200, 12, [None], proxy[110])
Makers.makeStubAs(emu, base, 201, 13, [None], proxy[111])
Makers.makeStubAs(emu, base, 202, 14, [None], proxy[112])
Makers.makeStubAs(emu, base, 203, 15, [None], proxy[113])
Makers.makeStubAs(emu, base, 204, 16, [None], proxy[114])
Makers.makeStubAs(emu, base, 205, 17, [None], proxy[115])
Makers.makeStubAs(emu, base, 206, 18, [None], proxy[116])
Makers.makeStubAs(emu, base, 207, 19, [None], proxy[117])
Makers.makeStubAs(emu, base, 208, 20, [None], proxy[118])
Makers.makeStubAs(emu, base, 209, 21, [None], proxy[119])
Makers.makeStubAs(emu, base, 210, 22, [None], proxy[120])
Makers.makeStubAs(emu, base, 211, 23, [None], proxy[121])
Makers.makeStubAs(emu, base, 212, 24, [None], proxy[122])
Makers.makeStubAs(emu, base, 213, 25, [None], proxy[123])
Makers.makeStubAs(emu, base, 214, 26, [None], proxy[124])
Makers.makeStubAs(emu, base, 215, 27, [None], proxy[125])
Makers.makeStubAs(emu, base, 216, 28, [None], proxy[126])
Makers.makeStubAs(emu, base, 217, 29, [None], proxy[127])
Makers.makeStubAs(emu, base, 218, 30, [None], proxy[128])
Makers.makeStubAs(emu, base, 219, 31, [None], proxy[129])
Makers.makeStubAs(emu, base, 220, 32, [None], proxy[130])
Makers.makeStubAs(emu, base, 221, 33, [None], proxy[131])
Makers.makeStubAs(emu, base, 222, 34, [None], proxy[132])
Makers.makeStubAs(emu, base, 223, 35, [None], proxy[133])
Makers.makeStubAs(emu, base, 224, 36, [None], proxy[134])
Makers.makeStubAs(emu, base, 225, 37, [None], proxy[135])
Makers.makeStubAs(emu, base, 226, 38, [None], proxy[136])
Makers.makeStubAs(emu, base, 227, 39, [None], proxy[137])
Makers.makeStubAs(emu, base, 228, 40, [None], proxy[138])
Makers.makeStubAs(emu, base, 229, 41, [None], proxy[139])
Makers.makeStubAs(emu, base, 230, 42, [None], proxy[140])
Makers.makeStubAs(emu, base, 231, 43, [None], proxy[141])
Makers.makeStubAs(emu, base, 232, 44, [None], proxy[142])
Makers.makeStubAs(emu, base, 233, 45, [None], proxy[143])
Makers.makeStubAs(emu, base, 234, 46, [None], proxy[144])
Makers.makeStubAs(emu, base, 235, 47, [None], proxy[145])
Makers.makeStubAs(emu, base, 236, 48, [None], proxy[146])
Makers.makeStubAs(emu, base, 237, 49, [None], proxy[147])
Makers.makeStubAs(emu, base, 238, 50, [None], proxy[148])







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
ebgp.addRsPeers(2, [190, 67, 68, 133, 11872])
ebgp.addRsPeers(3, [191, 66, 126, 127])
ebgp.addRsPeers(4, [192, 65, 123, 124, 125, 126])
ebgp.addRsPeers(5, [193, 64, 94, 95, 99, 124])
ebgp.addRsPeers(6, [194, 63, 92, 93, 94])
ebgp.addRsPeers(7, [195, 62, 81, 71])
ebgp.addRsPeers(8, [196, 68, 69, 70])
ebgp.addRsPeers(9, [197, 128, 132, 133, 134])
ebgp.addRsPeers(10, [198, 127, 128, 129, 130])
ebgp.addRsPeers(11, [199, 125, 129, 149])
ebgp.addRsPeers(12, [200, 100, 102, 121, 122, 123])
ebgp.addRsPeers(13, [201, 98, 99, 100, 101, 103])
ebgp.addRsPeers(14, [202, 95, 96 ,97])
ebgp.addRsPeers(15, [203, 91, 93, 96, 109])
ebgp.addRsPeers(16, [204, 82, 90, 92])
ebgp.addRsPeers(17, [205, 72, 80, 81, 82, 83])
ebgp.addRsPeers(18, [206, 70, 71, 72, 73])
ebgp.addRsPeers(19, [207, 69, 74, 134, 135])
ebgp.addRsPeers(20, [208, 131, 132, 139, 140])
ebgp.addRsPeers(21, [209, 130, 131, 145, 148])
ebgp.addRsPeers(22, [210, 148, 149, 150, 151, 152, 153])
ebgp.addRsPeers(23, [211, 122, 151, 154, 155, 156])
ebgp.addRsPeers(24, [212, 101, 102, 104])
ebgp.addRsPeers(25, [213, 97, 98, 106, 107, 108])
ebgp.addRsPeers(26, [214, 108, 109, 110, 111])
ebgp.addRsPeers(27, [215, 89, 90, 91, 112, 113])
ebgp.addRsPeers(28, [216, 83, 86, 87, 89])
ebgp.addRsPeers(29, [217, 75, 79, 80, 84])
ebgp.addRsPeers(30, [218, 73, 74, 75, 76, 77])
ebgp.addRsPeers(31, [219, 135, 136, 138, 139])
ebgp.addRsPeers(32, [220, 140, 141, 143, 144])
ebgp.addRsPeers(33, [221, 144, 145, 146, 147])
ebgp.addRsPeers(34, [222, 147, 153, 160])
ebgp.addRsPeers(35, [223, 152, 154, 159])
ebgp.addRsPeers(36, [224, 118, 120, 121])
ebgp.addRsPeers(37, [225, 103, 105, 106])
ebgp.addRsPeers(38, [226, 110, 115, 116])
ebgp.addRsPeers(39, [227, 111, 112, 114, 115])
ebgp.addRsPeers(40, [228, 87, 88, 113, 114])
ebgp.addRsPeers(41, [229, 84, 85, 86, 88])
ebgp.addRsPeers(42, [230, 76, 78, 79, 85])
ebgp.addRsPeers(43, [231, 77, 78, 136, 137])
ebgp.addRsPeers(44, [232, 137, 138, 141, 142])
ebgp.addRsPeers(45, [233, 142, 143, 146,])
ebgp.addRsPeers(46, [234, 155, 157, 158])
ebgp.addRsPeers(47, [235, 158, 159, 160])
ebgp.addRsPeers(48, [236, 104, 105, 118, 119, 117])
ebgp.addRsPeers(49, [237, 116, 117, 107])
ebgp.addRsPeers(50, [238, 119, 120, 156, 157])





####AVG IX Connection = 264/50 = 5.36 ASes, 4.34 without Stubs.




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
emu.compile(Docker(), './output_2to1_100', override=True)
