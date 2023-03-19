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






###############################################################################
# 5 Transit ASes -> 100-105
# 12 Stub ASes -> 106-117
# Total num ASes of 17
total_ASes =  81
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
Makers.makeTransitAs(base, 87, [11, 27], [(11, 27)], proxy[2])
Makers.makeTransitAs(base, 91, [12, 20], [(12, 20)], proxy[3])
Makers.makeTransitAs(base, 92, [6, 12], [(6, 12)], proxy[4])
Makers.makeTransitAs(base, 93, [12, 28], [(12, 28)], proxy[5])
Makers.makeTransitAs(base, 94, [12, 3], [(12, 3)], proxy[6])
Makers.makeTransitAs(base, 95, [35, 81], [(35, 81)], proxy[7])
Makers.makeTransitAs(base, 96, [12, 16], [(12, 16)], proxy[8])
Makers.makeTransitAs(base, 97, [8, 13], [(8, 13)], proxy[9])
Makers.makeTransitAs(base, 101, [40, 26], [(40, 26)], proxy[11])
Makers.makeTransitAs(base, 108, [39, 25], [(39, 25)], proxy[12])
Makers.makeTransitAs(base, 109, [18, 25], [(18, 25)], proxy[13])
Makers.makeTransitAs(base, 110, [10, 25], [(10, 25)], proxy[14])
Makers.makeTransitAs(base, 111, [10, 26], [(10, 26)], proxy[15])
Makers.makeTransitAs(base, 112, [18, 9], [(18, 9)], proxy[16])
Makers.makeTransitAs(base, 113, [9, 17], [(9, 17)], proxy[17])
Makers.makeTransitAs(base, 114, [8, 5], [(8, 5)], proxy[18])
Makers.makeTransitAs(base, 115, [17, 16], [(17, 16)], proxy[19])
Makers.makeTransitAs(base, 116, [16, 8], [(16, 8)], proxy[20])
Makers.makeTransitAs(base, 117, [16, 22], [(16, 22)], proxy[21])
Makers.makeTransitAs(base, 118, [22, 23], [(22, 23)], proxy[22])
Makers.makeTransitAs(base, 119, [23, 36], [(23, 36)], proxy[23])
Makers.makeTransitAs(base, 120, [24, 37], [(24, 37)], proxy[24])
Makers.makeTransitAs(base, 122, [24, 38], [(24, 38)], proxy[25])
Makers.makeTransitAs(base, 129, [22, 35], [(22, 35)], proxy[26])
Makers.makeTransitAs(base, 133, [21, 34], [(21, 34)], proxy[27])
Makers.makeTransitAs(base, 134, [15, 21], [(15, 21)], proxy[28])
Makers.makeTransitAs(base, 135, [8, 15], [(8, 15)], proxy[29])
Makers.makeTransitAs(base, 136, [81, 4], [(81, 4)], proxy[30])
Makers.makeTransitAs(base, 137, [7, 14], [(7, 14)], proxy[31])
Makers.makeTransitAs(base, 138, [4, 14], [(4, 14)], proxy[32])
Makers.makeTransitAs(base, 139, [14, 32], [(14, 32)], proxy[33])
Makers.makeTransitAs(base, 140, [32, 33], [(32, 33)], proxy[34])
Makers.makeTransitAs(base, 152, [19, 31], [(19, 31)], proxy[35])
Makers.makeTransitAs(base, 153, [7, 19], [(7, 19)], proxy[36])
Makers.makeTransitAs(base, 154, [13, 30], [(13, 30)], proxy[37])
Makers.makeTransitAs(base, 155, [29, 13], [(29, 13)], proxy[38])
Makers.makeTransitAs(base, 157, [18, 24], [(18, 24)], proxy[39])

#Makers.makeTransitAs(base, 164, [187, 188], [(187, 188)], proxy[79])
#####################################################################
Makers.makeStubAs(emu, base, 249, 81, [None], proxy[40])
Makers.makeStubAs(emu, base, 170, 2, [None], proxy[41])
Makers.makeStubAs(emu, base, 171, 3, [None], proxy[42])
Makers.makeStubAs(emu, base, 172, 4, [None], proxy[43])
Makers.makeStubAs(emu, base, 173, 5, [None], proxy[44])
Makers.makeStubAs(emu, base, 174, 6, [None], proxy[45])
Makers.makeStubAs(emu, base, 175, 7, [None], proxy[46])
Makers.makeStubAs(emu, base, 176, 8, [None], proxy[47])
Makers.makeStubAs(emu, base, 177, 9, [None], proxy[48])
Makers.makeStubAs(emu, base, 178, 10, [None], proxy[49])
Makers.makeStubAs(emu, base, 179, 11, [None], proxy[50])
Makers.makeStubAs(emu, base, 180, 12, [None], proxy[51])
Makers.makeStubAs(emu, base, 181, 13, [None], proxy[52])
Makers.makeStubAs(emu, base, 182, 14, [None], proxy[53])
Makers.makeStubAs(emu, base, 183, 15, [None], proxy[54])
Makers.makeStubAs(emu, base, 184, 16, [None], proxy[55])
Makers.makeStubAs(emu, base, 185, 17, [None], proxy[56])
Makers.makeStubAs(emu, base, 186, 18, [None], proxy[57])
Makers.makeStubAs(emu, base, 187, 19, [None], proxy[58])
Makers.makeStubAs(emu, base, 188, 20, [None], proxy[59])
Makers.makeStubAs(emu, base, 189, 21, [None], proxy[60])
Makers.makeStubAs(emu, base, 190, 22, [None], proxy[61])
Makers.makeStubAs(emu, base, 191, 23, [None], proxy[62])
Makers.makeStubAs(emu, base, 192, 24, [None], proxy[63])
Makers.makeStubAs(emu, base, 193, 25, [None], proxy[64])
Makers.makeStubAs(emu, base, 194, 26, [None], proxy[65])
Makers.makeStubAs(emu, base, 195, 27, [None], proxy[66])
Makers.makeStubAs(emu, base, 196, 28, [None], proxy[67])
Makers.makeStubAs(emu, base, 197, 29, [None], proxy[68])
Makers.makeStubAs(emu, base, 198, 30, [None], proxy[69])
Makers.makeStubAs(emu, base, 199, 31, [None], proxy[70])
Makers.makeStubAs(emu, base, 200, 32, [None], proxy[71])
Makers.makeStubAs(emu, base, 201, 33, [None], proxy[72])
Makers.makeStubAs(emu, base, 202, 34, [None], proxy[73])
Makers.makeStubAs(emu, base, 203, 35, [None], proxy[74])
Makers.makeStubAs(emu, base, 204, 36, [None], proxy[75])
Makers.makeStubAs(emu, base, 205, 37, [None], proxy[76])
Makers.makeStubAs(emu, base, 206, 38, [None], proxy[77])
Makers.makeStubAs(emu, base, 207, 39, [None], proxy[78])
Makers.makeStubAs(emu, base, 208, 40, [None], proxy[79])







# Create real-world AS.
# AS11872 is the Syracuse University's autonomous system

as11872 = base.createAutonomousSystem(11872)
as11872.createRealWorldRouter('rw').joinNetwork('ix2', '10.2.0.118')


###############################################################################
# Peering via RS (route server). The default peering mode for RS is PeerRelationship.Peer, 
# which means each AS will only export its customers and their own prefixes. 
# We will use this peering relationship to peer all the ASes in an IX.
# None of them will provide transit service for others. 


ebgp.addRsPeers(81, [249, 85, 136, 95])
ebgp.addRsPeers(2, [170, 85, 86, 11872])
ebgp.addRsPeers(3, [171, 94])
ebgp.addRsPeers(4, [172, 136,138])
ebgp.addRsPeers(5, [173, 114])
ebgp.addRsPeers(6, [174, 92])
ebgp.addRsPeers(7, [175, 153, 137])
ebgp.addRsPeers(8, [176, 114,116,135, 97])
ebgp.addRsPeers(9, [177, 112, 113])
ebgp.addRsPeers(10, [178, 110, 111])
ebgp.addRsPeers(11, [179, 86, 87])
ebgp.addRsPeers(12, [180, 91, 92, 93, 94, 96])
ebgp.addRsPeers(13, [181, 154, 155, 97])
ebgp.addRsPeers(14, [182, 137, 138, 139])
ebgp.addRsPeers(15, [183, 135, 134])
ebgp.addRsPeers(16, [184, 115, 116, 117, 96])
ebgp.addRsPeers(17, [185, 113, 115])
ebgp.addRsPeers(18, [186, 109, 112, 157])
ebgp.addRsPeers(19, [187, 152, 153])
ebgp.addRsPeers(20, [188, 91])
ebgp.addRsPeers(21, [189, 134])
ebgp.addRsPeers(22, [190, 117, 118, 129])
ebgp.addRsPeers(23, [191, 119, 118])
ebgp.addRsPeers(24, [192, 157, 120, 122])
ebgp.addRsPeers(25, [193, 108, 109, 110])
ebgp.addRsPeers(26, [194, 101, 111])
ebgp.addRsPeers(27, [195, 87])
ebgp.addRsPeers(28, [196, 93])
ebgp.addRsPeers(29, [197, 155])
ebgp.addRsPeers(30, [198, 154])
ebgp.addRsPeers(31, [199, 152])
ebgp.addRsPeers(32, [200, 139, 140])
ebgp.addRsPeers(33, [201, 140])
ebgp.addRsPeers(34, [202, 133])
ebgp.addRsPeers(35, [203, 129, 95])
ebgp.addRsPeers(36, [204, 119])
ebgp.addRsPeers(37, [205, 120])
ebgp.addRsPeers(38, [206, 122])
ebgp.addRsPeers(39, [207, 108])
ebgp.addRsPeers(40, [208, 101])

#118/40 = 2.95 connections/ix, removing stubs = 1.925



####AVG IX Connection = 168/32 = 5.25 ASes




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
emu.compile(Docker(), './output_1to1_40', override=True)

