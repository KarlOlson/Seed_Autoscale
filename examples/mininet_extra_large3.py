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

ix86 = base.createInternetExchange(86)
ix87 = base.createInternetExchange(87)
ix88 = base.createInternetExchange(88)
ix89 = base.createInternetExchange(89)
ix90 = base.createInternetExchange(90)
ix91 = base.createInternetExchange(91)
ix92 = base.createInternetExchange(92)
ix93 = base.createInternetExchange(93)
ix94 = base.createInternetExchange(94)
ix95 = base.createInternetExchange(95)
ix96 = base.createInternetExchange(96)
ix97 = base.createInternetExchange(97)
ix98 = base.createInternetExchange(98)
ix99 = base.createInternetExchange(99)
ix100 = base.createInternetExchange(100)
#########################################
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
###################################################
ix132 = base.createInternetExchange(132)
ix133 = base.createInternetExchange(133)
ix134 = base.createInternetExchange(134)
ix135 = base.createInternetExchange(135)
ix136 = base.createInternetExchange(136)
ix137 = base.createInternetExchange(137)
ix138 = base.createInternetExchange(138)
ix139 = base.createInternetExchange(139)
ix140 = base.createInternetExchange(140)
ix141 = base.createInternetExchange(141)
ix142 = base.createInternetExchange(142)
ix143 = base.createInternetExchange(143)
ix144 = base.createInternetExchange(144)
ix145 = base.createInternetExchange(145)
ix146 = base.createInternetExchange(146)
ix147 = base.createInternetExchange(147)
ix148 = base.createInternetExchange(148)
ix149 = base.createInternetExchange(149)
ix150 = base.createInternetExchange(150)
ix151 = base.createInternetExchange(151)
ix152 = base.createInternetExchange(152)
ix153 = base.createInternetExchange(153)
ix154 = base.createInternetExchange(154)
ix155 = base.createInternetExchange(155)
ix156 = base.createInternetExchange(156)
ix157 = base.createInternetExchange(157)
ix158 = base.createInternetExchange(158)
ix159 = base.createInternetExchange(159)
ix160 = base.createInternetExchange(160)
ix161 = base.createInternetExchange(161)
ix162 = base.createInternetExchange(162)

###############################################################################
# 5 Transit ASes -> 100-105
# 12 Stub ASes -> 106-117
# Total num ASes of 17
total_ASes =  177
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

## Tier 2 ASes
Makers.makeTransitAs(base, 254, [101, 106], [(101, 106)], proxy[0])
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
##################################################################
Makers.makeTransitAs(base, 42, [132, 137], [(132, 137)], proxy[41])
Makers.makeTransitAs(base, 43, [137, 133], [(137, 133)], proxy[42])
Makers.makeTransitAs(base, 44, [133, 134], [(133, 134)], proxy[43])
Makers.makeTransitAs(base, 45, [134, 136], [(134, 136)], proxy[44])
Makers.makeTransitAs(base, 46, [136, 135], [(136, 135)], proxy[45])
Makers.makeTransitAs(base, 47, [135, 146], [(135, 146)], proxy[46])
Makers.makeTransitAs(base, 48, [146, 145], [(146, 145)], proxy[47])
Makers.makeTransitAs(base, 49, [136, 162], [(136, 162)], proxy[48])
Makers.makeTransitAs(base, 50, [137, 162], [(137, 162)], proxy[49])
Makers.makeTransitAs(base, 51, [162, 148], [(162, 148)], proxy[50])
Makers.makeTransitAs(base, 52, [148, 144], [(148, 144)], proxy[51])
Makers.makeTransitAs(base, 53, [148, 154], [(148, 154)], proxy[52])
Makers.makeTransitAs(base, 54, [148, 150], [(148, 150)], proxy[53])
Makers.makeTransitAs(base, 55, [148, 145], [(148, 145)], proxy[54])
Makers.makeTransitAs(base, 56, [145, 147], [(145, 147)], proxy[55])
Makers.makeTransitAs(base, 57, [147, 149], [(147, 149)], proxy[56])
Makers.makeTransitAs(base, 58, [149, 161], [(149, 161)], proxy[57])
Makers.makeTransitAs(base, 59, [151, 161], [(151, 161)], proxy[58])
Makers.makeTransitAs(base, 60, [151, 152], [(151, 152)], proxy[59])
Makers.makeTransitAs(base, 61, [152, 156], [(152, 156)], proxy[60])
Makers.makeTransitAs(base, 62, [156, 157], [(156, 157)], proxy[61])
Makers.makeTransitAs(base, 63, [157, 160], [(157, 160)], proxy[62])
Makers.makeTransitAs(base, 64, [160, 159], [(160, 159)], proxy[63])
Makers.makeTransitAs(base, 65, [159, 158], [(159, 158)], proxy[64])
Makers.makeTransitAs(base, 66, [157, 158], [(157, 158)], proxy[65])
Makers.makeTransitAs(base, 67, [157, 155], [(157, 155)], proxy[66])
Makers.makeTransitAs(base, 68, [155, 154], [(155, 154)], proxy[67])
Makers.makeTransitAs(base, 69, [153, 154], [(153, 154)], proxy[68])
Makers.makeTransitAs(base, 70, [153, 151], [(153, 151)], proxy[69])
Makers.makeTransitAs(base, 71, [151, 150], [(151, 150)], proxy[70])
Makers.makeTransitAs(base, 72, [138, 140], [(138, 140)], proxy[71])
Makers.makeTransitAs(base, 73, [139, 140], [(139, 140)], proxy[72])
Makers.makeTransitAs(base, 74, [139, 141], [(139, 141)], proxy[73])
Makers.makeTransitAs(base, 75, [142, 141], [(142, 141)], proxy[74])
Makers.makeTransitAs(base, 76, [142, 143], [(142, 143)], proxy[75])
Makers.makeTransitAs(base, 77, [143, 154], [(143, 154)], proxy[76])
Makers.makeTransitAs(base, 78, [143, 158], [(143, 158)], proxy[77])
Makers.makeTransitAs(base, 79, [140, 142], [(140, 142)], proxy[78])
Makers.makeTransitAs(base, 80, [132, 138], [(132, 138)], proxy[79])
Makers.makeTransitAs(base, 81, [138, 144], [(138, 144)], proxy[80])
Makers.makeTransitAs(base, 82, [140, 154], [(140, 154)], proxy[81])
###################################################################
Makers.makeTransitAs(base, 163, [86, 87], [(86, 87)], proxy[162])
Makers.makeTransitAs(base, 164, [86, 88], [(86, 88)], proxy[163])
Makers.makeTransitAs(base, 165, [86, 89], [(86, 89)], proxy[164])
Makers.makeTransitAs(base, 166, [87, 92], [(87, 92)], proxy[165])
Makers.makeTransitAs(base, 167, [92, 91], [(92, 91)], proxy[166])
Makers.makeTransitAs(base, 168, [90, 91], [(90, 91)], proxy[167])
Makers.makeTransitAs(base, 169, [88, 90], [(88, 90)], proxy[168])
Makers.makeTransitAs(base, 170, [91, 95], [(91, 95)], proxy[169])
Makers.makeTransitAs(base, 171, [92, 94], [(92, 94)], proxy[170])
Makers.makeTransitAs(base, 172, [92, 93], [(92, 93)], proxy[171])
Makers.makeTransitAs(base, 173, [90, 96], [(90, 96)], proxy[172])
Makers.makeTransitAs(base, 174, [90, 97], [(90, 97)], proxy[173])
Makers.makeTransitAs(base, 175, [96, 98, 132], [(96, 98),(98,132)], proxy[174])
Makers.makeTransitAs(base, 176, [95, 99, 138], [(95, 99),(99, 138)], proxy[175])
Makers.makeTransitAs(base, 177, [100, 94, 140], [(100, 94),(100, 140)], proxy[176])
#############
#interconnect topologies with linking transits ASes
Makers.makeTransitAs(base, 83, [140, 109], [(140, 109)], proxy[82])
Makers.makeTransitAs(base, 84, [138, 107], [(138, 107)], proxy[83])
Makers.makeTransitAs(base, 85, [132, 101], [(132, 101)], proxy[84])
###############################################################################
# Create single-homed stub ASes. "None" means create a host only 





###########################################################
Makers.makeStubAs(emu, base, 192, 101, [None], proxy[85])
Makers.makeStubAs(emu, base, 193, 102, [None], proxy[86])
Makers.makeStubAs(emu, base, 194, 103, [None], proxy[87])
Makers.makeStubAs(emu, base, 195, 104, [None], proxy[88])
Makers.makeStubAs(emu, base, 196, 105, [None], proxy[89])
Makers.makeStubAs(emu, base, 197, 106, [None], proxy[90])
Makers.makeStubAs(emu, base, 198, 107, [None], proxy[91])
Makers.makeStubAs(emu, base, 199, 108, [None], proxy[92])
Makers.makeStubAs(emu, base, 200, 109, [None], proxy[93])
Makers.makeStubAs(emu, base, 201, 110, [None], proxy[94])
Makers.makeStubAs(emu, base, 202, 111, [None], proxy[95])
Makers.makeStubAs(emu, base, 203, 112, [None], proxy[96])
Makers.makeStubAs(emu, base, 204, 113, [None], proxy[97])
Makers.makeStubAs(emu, base, 205, 114, [None], proxy[98])
Makers.makeStubAs(emu, base, 206, 115, [None], proxy[99])
Makers.makeStubAs(emu, base, 207, 116, [None], proxy[100])
Makers.makeStubAs(emu, base, 208, 117, [None], proxy[101])
Makers.makeStubAs(emu, base, 209, 118, [None], proxy[102])
Makers.makeStubAs(emu, base, 210, 119, [None], proxy[103])
Makers.makeStubAs(emu, base, 211, 120, [None], proxy[104])
Makers.makeStubAs(emu, base, 212, 121, [None], proxy[105])
Makers.makeStubAs(emu, base, 213, 122, [None], proxy[106])
Makers.makeStubAs(emu, base, 214, 123, [None], proxy[107])
Makers.makeStubAs(emu, base, 215, 124, [None], proxy[108])
Makers.makeStubAs(emu, base, 216, 125, [None], proxy[109])
Makers.makeStubAs(emu, base, 217, 126, [None], proxy[110])
Makers.makeStubAs(emu, base, 218, 127, [None], proxy[111])
Makers.makeStubAs(emu, base, 219, 128, [None], proxy[112])
Makers.makeStubAs(emu, base, 220, 129, [None], proxy[113])
Makers.makeStubAs(emu, base, 221, 130, [None], proxy[114])
Makers.makeStubAs(emu, base, 222, 131, [None], proxy[115])
########################################################
Makers.makeStubAs(emu, base, 223, 132, [None], proxy[116])
Makers.makeStubAs(emu, base, 224, 133, [None], proxy[117])
Makers.makeStubAs(emu, base, 225, 134, [None], proxy[118])
Makers.makeStubAs(emu, base, 226, 135, [None], proxy[119])
Makers.makeStubAs(emu, base, 227, 136, [None], proxy[120])
Makers.makeStubAs(emu, base, 228, 137, [None], proxy[121])
Makers.makeStubAs(emu, base, 229, 138, [None], proxy[122])
Makers.makeStubAs(emu, base, 230, 139, [None], proxy[123])
Makers.makeStubAs(emu, base, 231, 140, [None], proxy[124])
Makers.makeStubAs(emu, base, 232, 141, [None], proxy[125])
Makers.makeStubAs(emu, base, 233, 142, [None], proxy[126])
Makers.makeStubAs(emu, base, 234, 143, [None], proxy[127])
Makers.makeStubAs(emu, base, 235, 144, [None], proxy[128])
Makers.makeStubAs(emu, base, 236, 145, [None], proxy[129])
Makers.makeStubAs(emu, base, 237, 146, [None], proxy[130])
Makers.makeStubAs(emu, base, 238, 147, [None], proxy[131])
Makers.makeStubAs(emu, base, 239, 148, [None], proxy[132])
Makers.makeStubAs(emu, base, 240, 149, [None], proxy[133])
Makers.makeStubAs(emu, base, 241, 150, [None], proxy[134])
Makers.makeStubAs(emu, base, 242, 151, [None], proxy[135])
Makers.makeStubAs(emu, base, 243, 152, [None], proxy[136])
Makers.makeStubAs(emu, base, 244, 153, [None], proxy[137])
Makers.makeStubAs(emu, base, 245, 154, [None], proxy[138])
Makers.makeStubAs(emu, base, 246, 155, [None], proxy[139])
Makers.makeStubAs(emu, base, 247, 156, [None], proxy[140])
Makers.makeStubAs(emu, base, 248, 157, [None], proxy[141])
Makers.makeStubAs(emu, base, 249, 158, [None], proxy[142])
Makers.makeStubAs(emu, base, 250, 159, [None], proxy[143])
Makers.makeStubAs(emu, base, 251, 160, [None], proxy[144])
Makers.makeStubAs(emu, base, 252, 161, [None], proxy[145])
Makers.makeStubAs(emu, base, 253, 162, [None], proxy[146])
########################################################

#Makers.makeStubAs(emu, base, 177, 86, [None], proxy[147])
Makers.makeStubAs(emu, base, 178, 87, [None], proxy[148])
Makers.makeStubAs(emu, base, 179, 88, [None], proxy[149])
Makers.makeStubAs(emu, base, 180, 89, [None], proxy[150])
Makers.makeStubAs(emu, base, 181, 90, [None], proxy[151])
Makers.makeStubAs(emu, base, 182, 91, [None], proxy[152])
Makers.makeStubAs(emu, base, 183, 92, [None], proxy[153])
Makers.makeStubAs(emu, base, 184, 93, [None], proxy[154])
Makers.makeStubAs(emu, base, 185, 94, [None], proxy[155])
Makers.makeStubAs(emu, base, 186, 95, [None], proxy[156])
Makers.makeStubAs(emu, base, 187, 96, [None], proxy[157])
Makers.makeStubAs(emu, base, 188, 97, [None], proxy[158])
Makers.makeStubAs(emu, base, 189, 98, [None], proxy[159])
Makers.makeStubAs(emu, base, 190, 99, [None], proxy[160])
Makers.makeStubAs(emu, base, 191, 100, [None], proxy[161])

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


#ebgp.addRsPeers(101, [51, 39])
ebgp.addRsPeers(101, [254, 39, 85, 192])
ebgp.addRsPeers(102, [2, 3, 193])
ebgp.addRsPeers(103, [3, 4, 194])
ebgp.addRsPeers(104, [5, 6,195])
ebgp.addRsPeers(105, [8, 4, 5,196])
ebgp.addRsPeers(106, [254, 2, 9,197])
#ebgp.addRsPeers(107, [39, 40, 31])
ebgp.addRsPeers(107, [39, 40, 31, 84,198])
ebgp.addRsPeers(108, [32, 33,199])
#ebgp.addRsPeers(109, [31, 32, 38, 41])
ebgp.addRsPeers(109, [31, 32, 38, 41, 83,200])
ebgp.addRsPeers(110, [33, 34,201])
ebgp.addRsPeers(111, [38, 34, 35,202])
ebgp.addRsPeers(112, [35, 36, 37,203])
ebgp.addRsPeers(113, [40, 11,204])
ebgp.addRsPeers(114, [7, 14, 15,205])
ebgp.addRsPeers(115, [6, 7,206])
ebgp.addRsPeers(116, [15, 16,207])
ebgp.addRsPeers(117, [10, 14, 11, 12, 13,208])
ebgp.addRsPeers(118, [16, 17,209])
ebgp.addRsPeers(119, [13, 30,210])
ebgp.addRsPeers(120, [18, 19, 29, 30,211])
ebgp.addRsPeers(121, [20, 19,212])
ebgp.addRsPeers(122, [28, 29,213])
ebgp.addRsPeers(123, [41, 12, 36, 27, 28,214])
ebgp.addRsPeers(124, [27, 26,215])
ebgp.addRsPeers(125, [21, 20,216])
ebgp.addRsPeers(126, [22, 25, 26, 21,217])
ebgp.addRsPeers(127, [24, 37, 25,218])
ebgp.addRsPeers(128, [23, 24,219])
ebgp.addRsPeers(129, [23, 22,220])
ebgp.addRsPeers(130, [17, 18,221])
ebgp.addRsPeers(131, [9, 8, 10,222])
######################################################
#ebgp.addRsPeers(132, [42, 80])
ebgp.addRsPeers(132, [42, 80, 85,223, 175])
ebgp.addRsPeers(133, [43, 44,224])
ebgp.addRsPeers(134, [44, 45,225])
ebgp.addRsPeers(135, [46, 47,226])
ebgp.addRsPeers(136, [49, 45, 46,227])
ebgp.addRsPeers(137, [42, 43, 50,228])
#ebgp.addRsPeers(138, [80, 81, 42])
ebgp.addRsPeers(138, [80, 81, 72, 84,229, 176])
ebgp.addRsPeers(139, [73, 74,230])
#ebgp.addRsPeers(140, [72, 73, 79, 82])
ebgp.addRsPeers(140, [72, 73, 79, 82, 83,231, 177])
ebgp.addRsPeers(141, [74, 75,232])
ebgp.addRsPeers(142, [79, 75, 76,233])
ebgp.addRsPeers(143, [76, 77, 78,234])
ebgp.addRsPeers(144, [81, 52,235])
ebgp.addRsPeers(145, [48, 55, 56,236])
ebgp.addRsPeers(146, [47, 48,237])
ebgp.addRsPeers(147, [56, 57,238])
ebgp.addRsPeers(148, [51, 55, 52, 53, 54,239])
ebgp.addRsPeers(149, [57, 58,240])
ebgp.addRsPeers(150, [54, 71,241])
ebgp.addRsPeers(151, [59, 60, 70, 71,242])
ebgp.addRsPeers(152, [61, 60,243])
ebgp.addRsPeers(153, [69, 70,244])
ebgp.addRsPeers(154, [82, 53, 77, 68, 69,245])
ebgp.addRsPeers(155, [68, 67,246])
ebgp.addRsPeers(156, [62, 61,247])
ebgp.addRsPeers(157, [63, 66, 67, 62,248])
ebgp.addRsPeers(158, [65, 78, 66,249])
ebgp.addRsPeers(159, [64, 65,250])
ebgp.addRsPeers(160, [64, 63,251])
ebgp.addRsPeers(161, [58, 59,252])
ebgp.addRsPeers(162, [50, 49, 51,253])
####################################################
ebgp.addRsPeers(86, [163,164])
ebgp.addRsPeers(87, [163,166,178])
ebgp.addRsPeers(88, [164,169,179])
ebgp.addRsPeers(89, [165,180])
ebgp.addRsPeers(90, [169,174,168,173,181])
ebgp.addRsPeers(91, [168,170,167,182])
ebgp.addRsPeers(92, [166,167,172,171,183])
ebgp.addRsPeers(93, [172,184])
ebgp.addRsPeers(94, [171,177,185])
ebgp.addRsPeers(95, [170,176,186])
ebgp.addRsPeers(96, [173,175,187])
ebgp.addRsPeers(97, [174,188])
ebgp.addRsPeers(98, [175,189])
ebgp.addRsPeers(99, [176,190])
ebgp.addRsPeers(100, [177,191])



# To buy transit services from another autonomous system, 
# we will use private peering  

#added 85
#ebgp.addPrivatePeerings(101, [90,39, 85],  [192], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(101, [90],  [39, 85], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(101, [39],  [85], PeerRelationship.Provider)

#ebgp.addPrivatePeerings(102, [2,3],  [193], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(102, [2],  [3], PeerRelationship.Provider)


#ebgp.addPrivatePeerings(103, [3,4],  [194], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(103, [3],  [4], PeerRelationship.Provider)

#ebgp.addPrivatePeerings(104, [5,6],  [195], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(104, [5],  [6], PeerRelationship.Provider)

#ebgp.addPrivatePeerings(105, [4,5,8],  [196], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(105, [4],  [5,8], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(105, [5],  [8], PeerRelationship.Provider)

#ebgp.addPrivatePeerings(106, [90,2,9],  [197], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(106, [2],  [90,9], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(106, [90],  [9], PeerRelationship.Provider)

#added 84
#ebgp.addPrivatePeerings(107, [31,39,40, 84],  [198], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(107, [39],  [31,40,84], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(107, [31],  [40,84], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(107, [40],  [84], PeerRelationship.Provider)

#ebgp.addPrivatePeerings(108, [33,32],  [199], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(108, [32],  [33], PeerRelationship.Provider)

#added 83
#ebgp.addPrivatePeerings(109, [31,32,38,41, 83],  [200], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(109, [32],  [31,38,41, 83], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(109, [31],  [38,41,83], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(109, [38],  [41,83], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(109, [41],  [83], PeerRelationship.Provider)

#ebgp.addPrivatePeerings(110, [33,34],  [201], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(110, [34],  [33], PeerRelationship.Provider)

#ebgp.addPrivatePeerings(111, [34,38,35],  [202], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(111, [38],  [34,35], PeerRelationship.Provider)

#ebgp.addPrivatePeerings(112, [35,36,37],  [203], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(112, [36],  [35,37], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(112, [35],  [37], PeerRelationship.Provider)

#ebgp.addPrivatePeerings(113, [40,11],  [204], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(113, [11],  [40], PeerRelationship.Provider)

#ebgp.addPrivatePeerings(114, [7,14,15],  [205], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(114, [14],  [7,15], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(114, [7],  [15], PeerRelationship.Provider)

#ebgp.addPrivatePeerings(115, [6,7],  [206], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(115, [7],  [6], PeerRelationship.Provider)

#ebgp.addPrivatePeerings(116, [15,16],  [207], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(116, [16],  [15], PeerRelationship.Provider)

#ebgp.addPrivatePeerings(117, [11,12,13,14,10],  [208], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(117, [12],  [11,13,14,10], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(117, [11],  [13,14,10], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(117, [13],  [14,10], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(117, [14],  [10], PeerRelationship.Provider)

#ebgp.addPrivatePeerings(118, [16,17],  [209], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(118, [17],  [16], PeerRelationship.Provider)

#ebgp.addPrivatePeerings(119, [13,30],  [210], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(119, [30],  [13], PeerRelationship.Provider)

#ebgp.addPrivatePeerings(120, [18,19,29,30],  [211], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(120, [19],  [18,29,30], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(120, [18],  [29,30], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(120, [29],  [30], PeerRelationship.Provider)

#ebgp.addPrivatePeerings(121, [19],  [212], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(121, [20],  [19], PeerRelationship.Provider)

#ebgp.addPrivatePeerings(122, [28,29],  [213], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(122, [29],  [28], PeerRelationship.Provider)

#ebgp.addPrivatePeerings(123, [41,36,12,27,28],  [214], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(123, [36],  [41,12,27,28], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(123, [41],  [12,27,28], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(123, [12],  [27,28], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(123, [27],  [28], PeerRelationship.Provider)

#ebgp.addPrivatePeerings(124, [26,27],  [215], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(124, [27],  [26], PeerRelationship.Provider)

#ebgp.addPrivatePeerings(125, [20,21],  [216], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(125, [21],  [20], PeerRelationship.Provider)

#ebgp.addPrivatePeerings(126, [21,22,25,26],  [217], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(126, [22],  [21,25,26], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(126, [21],  [25,26], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(126, [25],  [26], PeerRelationship.Provider)

#ebgp.addPrivatePeerings(127, [24,25,37],  [218], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(127, [25],  [24,37], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(127, [24],  [37], PeerRelationship.Provider)

#ebgp.addPrivatePeerings(128, [23,24],  [219], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(128, [24],  [23], PeerRelationship.Provider)

#ebgp.addPrivatePeerings(129, [22,23],  [220], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(129, [23],  [22], PeerRelationship.Provider)

#ebgp.addPrivatePeerings(130, [17,18],  [221], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(130, [18],  [17], PeerRelationship.Provider)

#ebgp.addPrivatePeerings(131, [8,9,10],  [222], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(131, [9],  [8,10], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(131, [8],  [10], PeerRelationship.Provider)

##############################################################################
#added 85
#ebgp.addPrivatePeerings(132, [42,80,85],  [223], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(132, [42],  [80,85], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(132, [80],  [85], PeerRelationship.Provider)

#ebgp.addPrivatePeerings(133, [43,44],  [224], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(133, [43],  [44], PeerRelationship.Provider)


#ebgp.addPrivatePeerings(134, [44,45],  [225], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(134, [44],  [45], PeerRelationship.Provider)

#ebgp.addPrivatePeerings(135, [46,47],  [226], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(135, [46],  [47], PeerRelationship.Provider)

#ebgp.addPrivatePeerings(136, [45,46,49],  [227], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(136, [45],  [46,49], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(136, [46],  [49], PeerRelationship.Provider)

#ebgp.addPrivatePeerings(137, [42,43,50],  [228], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(137, [43],  [42,50], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(137, [42],  [50], PeerRelationship.Provider)

#added 84
#ebgp.addPrivatePeerings(138, [72,80,81,84],  [229], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(138, [80],  [72,81,84], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(138, [72],  [81,84], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(138, [81],  [84], PeerRelationship.Provider)

#ebgp.addPrivatePeerings(139, [74,73],  [230], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(139, [73],  [74], PeerRelationship.Provider)

#added 83
#ebgp.addPrivatePeerings(140, [72,73,79,82,83],  [231], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(140, [73],  [72,79,82,83], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(140, [72],  [79,82,83], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(140, [79],  [82,83], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(140, [82],  [83], PeerRelationship.Provider)

#ebgp.addPrivatePeerings(141, [74,75],  [232], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(141, [75],  [74], PeerRelationship.Provider)

#ebgp.addPrivatePeerings(142, [75,79,76],  [233], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(142, [79],  [75,76], PeerRelationship.Provider)

#ebgp.addPrivatePeerings(143, [76,77,78],  [234], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(143, [77],  [76,78], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(143, [76],  [78], PeerRelationship.Provider)

#ebgp.addPrivatePeerings(144, [81,52],  [235], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(144, [52],  [81], PeerRelationship.Provider)

#ebgp.addPrivatePeerings(145, [48,55,56],  [236], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(145, [55],  [48,56], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(145, [48],  [56], PeerRelationship.Provider)

#ebgp.addPrivatePeerings(146, [47,48],  [237], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(146, [48],  [47], PeerRelationship.Provider)

#ebgp.addPrivatePeerings(147, [56,57],  [238], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(147, [57],  [56], PeerRelationship.Provider)

#ebgp.addPrivatePeerings(148, [52,53,54,55,51],  [239], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(148, [53],  [52,54,55,51], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(148, [52],  [54,55,51], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(148, [54],  [55,51], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(148, [55],  [51], PeerRelationship.Provider)

#ebgp.addPrivatePeerings(149, [57,58],  [240], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(149, [58],  [57], PeerRelationship.Provider)

#ebgp.addPrivatePeerings(150, [54,71],  [241], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(150, [71],  [54], PeerRelationship.Provider)

#ebgp.addPrivatePeerings(151, [59,60,70,71],  [242], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(151, [60],  [59,70,71], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(151, [59],  [70,71], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(151, [70],  [71], PeerRelationship.Provider)

#ebgp.addPrivatePeerings(152, [60],  [243], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(152, [61],  [60], PeerRelationship.Provider)

#ebgp.addPrivatePeerings(153, [69,70],  [244], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(153, [70],  [69], PeerRelationship.Provider)

#ebgp.addPrivatePeerings(154, [82,77,53,68,69],  [245], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(154, [77],  [82,53,68,69], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(154, [82],  [53,68,69], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(154, [53],  [68,69], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(154, [68],  [69], PeerRelationship.Provider)

#ebgp.addPrivatePeerings(155, [67,68],  [246], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(155, [68],  [67], PeerRelationship.Provider)

#ebgp.addPrivatePeerings(156, [61,62],  [247], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(156, [62],  [61], PeerRelationship.Provider)

#ebgp.addPrivatePeerings(157, [62,63,66,67],  [248], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(157, [63],  [62,66,67], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(157, [62],  [66,67], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(157, [66],  [67], PeerRelationship.Provider)

#ebgp.addPrivatePeerings(158, [65,66,78],  [249], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(158, [66],  [65,78], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(158, [65],  [78], PeerRelationship.Provider)

#ebgp.addPrivatePeerings(159, [64,65],  [250], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(159, [65],  [64], PeerRelationship.Provider)

#ebgp.addPrivatePeerings(160, [63,64],  [251], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(160, [64],  [63], PeerRelationship.Provider)

#ebgp.addPrivatePeerings(161, [58,59],  [252], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(161, [59],  [58], PeerRelationship.Provider)

#ebgp.addPrivatePeerings(162, [49,50,51],  [253], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(162, [50],  [49,51], PeerRelationship.Provider)
#ebgp.addPrivatePeerings(162, [49],  [51], PeerRelationship.Provider)
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
emu.compile(Docker(), './output_xlarge', override=True)

