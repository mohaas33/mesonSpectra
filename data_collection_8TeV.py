#!/usr/bin/env python3

from ROOT import TTree, TFile, TObject

import csv
import numpy as np
from array import array

def get_rows(fileName, firstH=0, firstR=0, lastR=1, p=0):
    rows = []
    with open(fileName, mode='r') as infile:
        content = infile.readlines()
        header = content[firstH:firstR]
        rows = content[firstR:lastR]
    if p == 1:
        print(header)
    if p == 2:
        print(rows)

    return rows

def get_data(fileName, firstH=0, firstR=0, lastR=1, p=0):
    rows = get_rows(fileName, firstH, firstR, lastR, p)

    data = np.array([row.strip().split(',') for row in rows],dtype=float)

    p2e = []
    p2e .append(np.array([d[1] for d in data],dtype=float) )#0 low pT bin edge;  
    p2e .append(np.array([d[2] for d in data],dtype=float) )#1 high pT bin edge;  
    p2e .append(np.array([d[0] for d in data],dtype=float) )#2 is the mean pT <-- this order is different in the database, it starts with mean pT, but keep mine;  
    p2e .append(np.array([d[3] for d in data],dtype=float) )#3 is the cross-section or number;  
    p2e .append(np.array([d[4] for d in data],dtype=float) )#4 is the statistical error (positive);  
    p2e .append(np.array([d[6] for d in data],dtype=float) )#5 is a systematic error (positive);  
    p2e .append(np.array([d[5] for d in data],dtype=float) )#6 is a systematic error (negative) if it is different from positive 

    #y_0_7 = []
    #if data<8:
    #    p2e[3]/ y_0_7[data] / (pval[data][1][bin] - pval[data][0][bin])
    #    p2e[4]/ y_0_7[data] / (pval[data][1][bin] - pval[data][0][bin])
    #    p2e[5]/ y_0_7[data] / (pval[data][1][bin] - pval[data][0][bin])
    #    p2e[6]/ y_0_7[data] / (pval[data][1][bin] - pval[data][0][bin])

    return np.asarray(p2e)


nPlots = 8

# https://www.hepdata.net/record/ins1230344 J/Psi and Upsilon 1s/2s/3s double-differential cross sections 
data_points = [0 for i  in range(nPlots)]
experiment = [0 for i in range(nPlots)]
particle_type = [0 for i in range(nPlots)]
particle_mass = [0 for i in range(nPlots)]
rapidity_low = [0 for i in range(nPlots)]
rapidity_high = [0 for i in range(nPlots)]

#P P --> J/PSI X 2.5<y<3
data = 0
experiment[data] = 3
particle_type[data] = 100443
particle_mass[data] = 3.6861
rapidity_low[data]  = 2.5
rapidity_high[data] = 3.0

data_points[0] = get_data('./store/HEPData-ins1230344-v1-Table_3_JPsi.csv', 0, 14, 28, 0)    # 2.5<y<3

#P P --> J/PSI X 3<y<3.5
data = 1
experiment[data] = 3
particle_type[data] = 100443
particle_mass[data] = 3.6861
rapidity_low[data]  = 3.0
rapidity_high[data] = 3.5
data_points[data] = get_data('./store/HEPData-ins1230344-v1-Table_4_JPsi.csv', 28, 34, 34+14, 0)# 3<y<3.5

#P P --> UPSI(1/2/3S) < MU+ MU-> X 2.5<y<
data = 2
experiment[data] = 3
particle_type[data] = 553
particle_mass[data] = 9.4603
rapidity_low[data]  = 2.5
rapidity_high[data] = 3.0
data_points[data] = get_data('./store/HEPData-ins1230344-v1-Table_11_Y.csv', 0, 13, 28, 0)     # 1s 2.5<y<3

data = 3
experiment[data] = 3
particle_type[data] = 100553
particle_mass[data] = 10.02326
rapidity_low[data]  = 2.5
rapidity_high[data] = 3.0
data_points[data] = get_data('./store/HEPData-ins1230344-v1-Table_11_Y.csv', 28, 33, 48, 0) # 2s 2.5<y<3

data = 4
experiment[data] = 3
particle_type[data] = 200553
particle_mass[data] = 10.3552
rapidity_low[data]  = 2.5
rapidity_high[data] = 3.0
data_points[data] = get_data('./store/HEPData-ins1230344-v1-Table_11_Y.csv', 48, 53, 68, 0) # 3s 2.5<y<3

#P P --> UPSI(1/2/3S) < MU+ MU-> X 3<y<3.5
data = 5
experiment[data] = 3
particle_type[data] = 553
particle_mass[data] = 9.4603
rapidity_low[data]  = 3.0
rapidity_high[data] = 3.5
data_points[data] = get_data('./store/HEPData-ins1230344-v1-Table_12_Y.csv', 0, 13, 28, 0)     # 1s 3<y<3.5

data = 6
experiment[data] = 3
particle_type[data] = 100553
particle_mass[data] = 10.02326
rapidity_low[data]  = 3.0
rapidity_high[data] = 3.5
data_points[data] = get_data('./store/HEPData-ins1230344-v1-Table_12_Y.csv', 28, 33, 48, 0) # 2s 3<y<3.5

data = 7
experiment[data] = 3
particle_type[data] = 200553
particle_mass[data] = 10.3552
rapidity_low[data]  = 3.0
rapidity_high[data] = 3.5
data_points[data] = get_data('./store/HEPData-ins1230344-v1-Table_12_Y.csv', 48, 53, 68, 0) # 3s 3<y<3.5

# Writing the File

nPlots = data+1
set = array('f', [ 0 ])
ndp = array('f', [ 0 ])
exp = array('f', [ 0 ])
ptype = array('f', [ 0 ])
rl = array('f', [ 0 ])
rh = array('f', [ 0 ])
pmass = array('f', [ 0 ])

#arrays
nBinsMax=200
ptl = array('f',[np.nan]*nBinsMax) 
print(ptl)
ptu = array('f',[np.nan]*nBinsMax)
pt  = array('f',[np.nan]*nBinsMax)
mtl = array('f',[np.nan]*nBinsMax)
mtu = array('f',[np.nan]*nBinsMax)
mt  = array('f',[np.nan]*nBinsMax)
cross_s	         = array('f',[np.nan]*nBinsMax)
cross_s_stat       = array('f',[np.nan]*nBinsMax)
cross_s_syst_high  = array('f',[np.nan]*nBinsMax)
cross_s_syst_low   = array('f',[np.nan]*nBinsMax)

measure = TTree("measure","particle measurements")
measure.Branch("set",  set,   "set/F")
measure.Branch("exp",  exp,   "exp/F")
measure.Branch("type", ptype, "type/F")
measure.Branch("yu",   rh,    "yu/F")
measure.Branch("yl",   rl,    "yl/F")
measure.Branch("np",   ndp,   "np/F")
measure.Branch("mass", pmass, "mass/F")
measure.Branch("pT",   pt, "pT"+str(nBinsMax)+"F")
measure.Branch("pTu",  ptu, "pTu"+str(nBinsMax)+"F")
measure.Branch("pTl",  ptl, "pTl"+str(nBinsMax)+"F")
measure.Branch("mT",   mt, "mT"+str(nBinsMax)+"F")
measure.Branch("mTu",  mtu, "mTu"+str(nBinsMax)+"F")
measure.Branch("mTl",  mtl, "mTl"+str(nBinsMax)+"F")
measure.Branch("cs",   cross_s, "cs"+str(nBinsMax)+"F")
measure.Branch("ecs",  cross_s_stat, "ecs"+str(nBinsMax)+"F")
measure.Branch("ecsu", cross_s_syst_high, "ecsu"+str(nBinsMax)+"F")
measure.Branch("ecsl", cross_s_syst_low, "ecsl"+str(nBinsMax)+"F")



for i in range(len(data_points)):
    set[0] = i
    ptype[0] = particle_type[i]
    exp[0] = experiment[i]
    print(exp)

    rl[0] = rapidity_low[i]
    rh[0] = rapidity_high[i]
    pmass[0] = particle_mass[i]

    #arrays
    pval = data_points[i]
    ndp[0] = len(pval[0])
    print(pval[0])
    for p in range(int(ndp[0])):
        ptl[p] = pval[0][p]
        #print(ptl)
        ptu[p] = pval[1][p]
        pt[p]  = pval[2][p]
        mtl[p] = pow(pow(pval[0][p],2) + pow(pmass[0],2),0.5)
        mtu[p] = pow(pow(pval[1][p],2) + pow(pmass[0],2),0.5)
        mt[p]  = pow(pow(pval[2][p],2) + pow(pmass[0],2),0.5)
        cross_s[p]           = pval[3][p] * (pval[1][p]-pval[0][p])
        cross_s_stat[p]      = pval[4][p] * (pval[1][p]-pval[0][p])
        cross_s_syst_high[p] = pval[5][p] * (pval[1][p]-pval[0][p])
        cross_s_syst_low[p]  = pval[6][p] * (pval[1][p]-pval[0][p])
    measure.Fill()
    

outfile = TFile.Open("store/data_collection_8TeV.root", "RECREATE")

measure.Write()

outfile.Write()
outfile.Close()
