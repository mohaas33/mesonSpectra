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

    #data = np.array([row.strip().split(',') for row in rows],dtype=float)
    data = []#np.array([row.strip().split(',') for row in rows])
    for row in rows:
        if '-,' in row:
            continue
        else:
            row_array = np.array(row.strip().split(','),dtype=float)
            data.append(row_array) 
    p2e = []
    p2e .append(np.array([d[1] for d in data],dtype=float) )#0 low pT bin edge;  
    p2e .append(np.array([d[2] for d in data],dtype=float) )#1 high pT bin edge;  
    p2e .append(np.array([d[0] for d in data],dtype=float) )#2 is the mean pT <-- this order is different in the database, it starts with mean pT, but keep mine;  
    p2e .append(np.array([d[3] for d in data],dtype=float) )#3 is the cross-section or number;  
    p2e .append(np.array([d[4] for d in data],dtype=float) )#4 is the statistical error (positive);  
    p2e .append(np.array([d[6] for d in data],dtype=float) )#5 is a systematic error (positive);  
    p2e .append(np.array([d[5] for d in data],dtype=float) )#6 is a systematic error (negative) if it is different from positive 
    #float p110[]={0,1,2,3,4,5,6,7};
    for i,p in enumerate(p2e):
        print('\tfloat p{0}[]={{ {1} }};'.format(i, ', '.join(str(x) for x in p) ) )

    #y_0_7 = []
    #if data<8:
    #    p2e[3]/ y_0_7[data] / (pval[data][1][bin] - pval[data][0][bin])
    #    p2e[4]/ y_0_7[data] / (pval[data][1][bin] - pval[data][0][bin])
    #    p2e[5]/ y_0_7[data] / (pval[data][1][bin] - pval[data][0][bin])
    #    p2e[6]/ y_0_7[data] / (pval[data][1][bin] - pval[data][0][bin])

    return np.asarray(p2e)

def print_first_lines(data , experiment, particle_type, particle_mass, rapidity_low, rapidity_high):
    print( '\n')
    print( '\tdata = {};'.format(data) )
    print( '\texperiment[data] = {};'.format(experiment) )
    print( '\tparticle_type[data] = {};'.format(particle_type) )
    print( '\tparticle_mass[data] = {};'.format(particle_mass) )
    print( '\trapidity_low[data]  = {};'.format(rapidity_low) )
    print( '\trapidity_high[data] = {};'.format(rapidity_high) )
    return 0


def print_last_lines():

    print('\tfor (int bin = 0; bin < npoints[data]; bin++){')
    print('\t\tpval[data][0][bin] = p0[bin];')
    print('\t\tpval[data][1][bin] = p1[bin];')
    print('\t\tpval[data][2][bin] = p2[bin];')
    print('\t\tpval[data][3][bin] = p3[bin];//*(p1[bin]-p0[bin]);')
    print('\t\tpval[data][4][bin] = p4[bin];//*(p1[bin]-p0[bin]);')
    print('\t\tpval[data][5][bin] = p5[bin];//*(p1[bin]-p0[bin]);')
    print('\t\tpval[data][6][bin] = p6[bin];//*(p1[bin]-p0[bin]);')
    print('\t}')

    return 0





nPlots = 27

data_points = [0 for i  in range(nPlots)]
experiment = [0 for i in range(nPlots)]
particle_type = [0 for i in range(nPlots)]
particle_mass = [0 for i in range(nPlots)]
rapidity_low = [0 for i in range(nPlots)]
rapidity_high = [0 for i in range(nPlots)]

# https://www.hepdata.net/record/ins1230344 J/Psi and Upsilon 1s/2s/3s double-differential cross sections 
#P P --> J/PSI X 2.5<y<3
print('\n \n \n//P P --> J/PSI X 2.5<y<3')
data = 0
experiment[data] = 3
particle_type[data] = 443
particle_mass[data] = 3.0969
rapidity_low[data]  = 2.5
rapidity_high[data] = 3.0

print_first_lines(data ,experiment[data] ,particle_type[data] ,particle_mass[data] ,rapidity_low[data]  ,rapidity_high[data] )
data_points[0] = get_data('./store/HEPData-ins1230344-v1-Table_3_JPsi.csv', 0, 14, 28, 0)    # 2.5<y<3
print_last_lines()

#P P --> J/PSI X 3<y<3.5
print('\n \n \n//P P --> J/PSI X 3<y<3.5')
data = 1
experiment[data] = 3
particle_type[data] = 443
particle_mass[data] = 3.0969
rapidity_low[data]  = 3.0
rapidity_high[data] = 3.5
print_first_lines(data ,experiment[data] ,particle_type[data] ,particle_mass[data] ,rapidity_low[data]  ,rapidity_high[data] )
data_points[data] = get_data('./store/HEPData-ins1230344-v1-Table_4_JPsi.csv', 0, 14, 28, 0)# 3<y<3.5
print_last_lines()

#P P --> UPSI(1/2/3S) < MU+ MU-> X 2.5<y<3
print('\n \n \n//P P --> UPSI(1/2/3S) < MU+ MU-> X 2.5<y<3')
data = 2
experiment[data] = 3
particle_type[data] = 553
particle_mass[data] = 9.4603
rapidity_low[data]  = 2.5
rapidity_high[data] = 3.0
print_first_lines(data ,experiment[data] ,particle_type[data] ,particle_mass[data] ,rapidity_low[data]  ,rapidity_high[data] )
data_points[data] = get_data('./store/HEPData-ins1230344-v1-Table_11_Y.csv', 0, 13, 28, 0)     # 1s 2.5<y<3
print_last_lines()

data = 3
experiment[data] = 3
particle_type[data] = 100553
particle_mass[data] = 10.02326
rapidity_low[data]  = 2.5
rapidity_high[data] = 3.0
print_first_lines(data ,experiment[data] ,particle_type[data] ,particle_mass[data] ,rapidity_low[data]  ,rapidity_high[data] )
data_points[data] = get_data('./store/HEPData-ins1230344-v1-Table_11_Y.csv', 28, 33, 48, 0) # 2s 2.5<y<3
print_last_lines()

data = 4
experiment[data] = 3
particle_type[data] = 200553
particle_mass[data] = 10.3552
rapidity_low[data]  = 2.5
rapidity_high[data] = 3.0
print_first_lines(data ,experiment[data] ,particle_type[data] ,particle_mass[data] ,rapidity_low[data]  ,rapidity_high[data] )
data_points[data] = get_data('./store/HEPData-ins1230344-v1-Table_11_Y.csv', 48, 53, 68, 0) # 3s 2.5<y<3
print_last_lines()

#P P --> UPSI(1/2/3S) < MU+ MU-> X 3<y<3.5
print('\n \n \n//P P --> UPSI(1/2/3S) < MU+ MU-> X 3<y<3.5')

data = 5
experiment[data] = 3
particle_type[data] = 553
particle_mass[data] = 9.4603
rapidity_low[data]  = 3.0
rapidity_high[data] = 3.5
print_first_lines(data ,experiment[data] ,particle_type[data] ,particle_mass[data] ,rapidity_low[data]  ,rapidity_high[data] )
data_points[data] = get_data('./store/HEPData-ins1230344-v1-Table_12_Y.csv', 0, 13, 28, 0)     # 1s 3<y<3.5
print_last_lines()

data = 6
experiment[data] = 3
particle_type[data] = 100553
particle_mass[data] = 10.02326
rapidity_low[data]  = 3.0
rapidity_high[data] = 3.5
print_first_lines(data ,experiment[data] ,particle_type[data] ,particle_mass[data] ,rapidity_low[data]  ,rapidity_high[data] )
data_points[data] = get_data('./store/HEPData-ins1230344-v1-Table_12_Y.csv', 28, 33, 48, 0) # 2s 3<y<3.5
print_last_lines()

data = 7
experiment[data] = 3
particle_type[data] = 200553
particle_mass[data] = 10.3552
rapidity_low[data]  = 3.0
rapidity_high[data] = 3.5
print_first_lines(data ,experiment[data] ,particle_type[data] ,particle_mass[data] ,rapidity_low[data]  ,rapidity_high[data] )
data_points[data] = get_data('./store/HEPData-ins1230344-v1-Table_12_Y.csv', 48, 53, 68, 0) # 3s 3<y<3.5
print_last_lines()

print('===============================================================================================')
print('https://www.hepdata.net/record/ins1392456 Upsilon 1s/2s/3s double-differential cross sections')
# https://www.hepdata.net/record/ins1392456 Upsilon 1s/2s/3s double-differential cross sections 

#P P --> UPSI(1S) X | P P --> MU+ MU- X
data = 8
experiment[data] = 3
particle_type[data] = 553
particle_mass[data] = 9.4603
rapidity_low[data]  = 2.0
rapidity_high[data] = 2.5
print_first_lines(data ,experiment[data] ,particle_type[data] ,particle_mass[data] ,rapidity_low[data]  ,rapidity_high[data] )
data_points[data] = get_data('./store/HEPData-ins1392456-v1-Table_11.csv', 0, 13, 42, 0) # 1s 2.5<y<3
print_last_lines()

data = 9
experiment[data] = 3
particle_type[data] = 553
particle_mass[data] = 9.4603
rapidity_low[data]  = 2.5
rapidity_high[data] = 3.0
print_first_lines(data ,experiment[data] ,particle_type[data] ,particle_mass[data] ,rapidity_low[data]  ,rapidity_high[data] )
data_points[data] = get_data('./store/HEPData-ins1392456-v1-Table_11.csv', 44, 47, 76, 0) # 1s 3<y<3.5
print_last_lines()

#P P --> UPSI(2S) X | P P --> MU+ MU- X
data = 10
experiment[data] = 3
particle_type[data] = 100553
particle_mass[data] = 10.02326
rapidity_low[data]  = 2.0
rapidity_high[data] = 2.5
print_first_lines(data ,experiment[data] ,particle_type[data] ,particle_mass[data] ,rapidity_low[data]  ,rapidity_high[data] )
data_points[data] = get_data('./store/HEPData-ins1392456-v1-Table_12.csv', 0, 13, 42, 2) # 2s 2.5<y<3
print_last_lines()

data = 11
experiment[data] = 3
particle_type[data] = 100553
particle_mass[data] = 10.02326
rapidity_low[data]  = 2.5
rapidity_high[data] = 3.0
print_first_lines(data ,experiment[data] ,particle_type[data] ,particle_mass[data] ,rapidity_low[data]  ,rapidity_high[data] )
data_points[data] = get_data('./store/HEPData-ins1392456-v1-Table_12.csv', 44, 47, 76, 0) # 2s 3<y<3.5
print_last_lines()

#P P --> UPSI(3S) X | P P --> MU+ MU- X
data = 12
experiment[data] = 3
particle_type[data] = 200553
particle_mass[data] = 10.3552
rapidity_low[data]  = 2.0
rapidity_high[data] = 2.5
print_first_lines(data ,experiment[data] ,particle_type[data] ,particle_mass[data] ,rapidity_low[data]  ,rapidity_high[data] )
data_points[data] = get_data('./store/HEPData-ins1392456-v1-Table_12.csv', 0, 13, 42, 0) # 3s 2.5<y<3
print_last_lines()

data = 13
experiment[data] = 3
particle_type[data] = 200553
particle_mass[data] = 10.3552
rapidity_low[data]  = 2.5
rapidity_high[data] = 3.0
print_first_lines(data ,experiment[data] ,particle_type[data] ,particle_mass[data] ,rapidity_low[data]  ,rapidity_high[data] )
data_points[data] = get_data('./store/HEPData-ins1392456-v1-Table_12.csv', 44, 47, 76, 0) # 2.5<y<3.0
print_last_lines()



#==============
# ALICE
#==============

print('//==============')
print('// ALICE')
print('//==============')

print('//===============================================================================================')
print('//https://www.hepdata.net/record/ins1395099 Differential production cross sections of J/psi, psi, Y(1/2/3s)')
#P P --> JPSI < MU+ MU- > X
print('\n')
print('//P P --> JPSI < MU+ MU- > X')
data = 14
experiment[data] = 2
particle_type[data] = 443
particle_mass[data] = 3.0969
rapidity_low[data]  = 2.5
rapidity_high[data] = 4.0
print_first_lines(data ,experiment[data] ,particle_type[data] ,particle_mass[data] ,rapidity_low[data]  ,rapidity_high[data] )
data_points[data] = get_data('./store/HEPData-ins1395099-v1-Table_1.csv', 0, 13, 26, 0) 
print_last_lines()

#P P --> PSI(2S) < MU+ MU- > X
print('\n')
print('//P P --> PSI(2S) < MU+ MU- > X')
data = 15
experiment[data] = 2
particle_type[data] = 100443
particle_mass[data] = 3.6861
rapidity_low[data]  = 2.5
rapidity_high[data] = 4.0
print_first_lines(data ,experiment[data] ,particle_type[data] ,particle_mass[data] ,rapidity_low[data]  ,rapidity_high[data] )
data_points[data] = get_data('./store/HEPData-ins1395099-v1-Table_4.csv', 0, 13, 22, 0) 
print_last_lines()

#P P --> UPSI(1S) < MU+ MU- > X
print('\n')
print('//P P --> UPSI(1S) < MU+ MU- > X')
data = 16
experiment[data] = 2
particle_type[data] = 553
particle_mass[data] = 9.4603
rapidity_low[data]  = 2.5
rapidity_high[data] = 4.0
print_first_lines(data ,experiment[data] ,particle_type[data] ,particle_mass[data] ,rapidity_low[data]  ,rapidity_high[data] )
data_points[data] = get_data('./store/HEPData-ins1395099-v1-Table_7.csv', 0, 13, 18, 0) 
print_last_lines()

#P P --> UPSI(2S) < MU+ MU- > X
print('\n')
print('//P P --> UPSI(2S) < MU+ MU- > X')
data = 17
experiment[data] = 2
particle_type[data] = 100553
particle_mass[data] = 10.02326
rapidity_low[data]  = 2.5
rapidity_high[data] = 4.0
print_first_lines(data ,experiment[data] ,particle_type[data] ,particle_mass[data] ,rapidity_low[data]  ,rapidity_high[data] )
data_points[data] = get_data('./store/HEPData-ins1395099-v1-Table_10.csv', 0, 13, 15, 0) 
print_last_lines()

#P P --> UPSI(3S) < MU+ MU- > X
#Is not available as pt dependance
print('\n')
print('//P P --> UPSI(3S) < MU+ MU- > X')
print('//Is not available as pt dependance')
print('\n')



print('\n')
print('//===============================================================================================')
print('//https://www.hepdata.net/record/ins1620477 Invariant differential cross section of pi0, eta. Corrected by acceptance.')
#P P --> JPSI < MU+ MU- > X
print('P P --> pi0/eta X | D3SIG/DPT/DYRAP*1/BR*1/(2*pi*pt)')

data = 18
br_pi = 98.823
experiment[data] = 2
particle_type[data] = 111
particle_mass[data] = 0.1349768
rapidity_low[data]  = 0
rapidity_high[data] = 4.0
print_first_lines(data ,experiment[data] ,particle_type[data] ,particle_mass[data] ,rapidity_low[data]  ,rapidity_high[data] )
print('\tfloat br_pi = 98.823;')
data_points[data] = get_data('./store/HEPData-ins1620477-v2-Table_1.csv', 0, 13, 57, 0) 
print_last_lines()

data = 19
br_eta = 39.31
experiment[data] = 2
particle_type[data] = 111
particle_mass[data] = 0.1349768
rapidity_low[data]  = 0
rapidity_high[data] = 4.0
print_first_lines(data ,experiment[data] ,particle_type[data] ,particle_mass[data] ,rapidity_low[data]  ,rapidity_high[data] )
print('\tfloat br_eta = 39.31;')
data_points[data] = get_data('./store/HEPData-ins1620477-v2-Table_2.csv', 0, 13, 38, 0) 
print_last_lines()


print('\n')
print('//===============================================================================================')
print('//https://www.hepdata.net/record/ins1762364 pT spectra of K*0 and phi.')
#p p --> K*(892)^{0} + X
print('//p p --> K*(892)^{0} + X | 1/Nev d^2N/(dp_Tdy) (GeV/c)^{-1}')

data = 20
experiment[data] = 2
particle_type[data] = 313
particle_mass[data] = 0.890
rapidity_low[data]  = 0.0
rapidity_high[data] = 0.5
print_first_lines(data ,experiment[data] ,particle_type[data] ,particle_mass[data] ,rapidity_low[data]  ,rapidity_high[data] )
data_points[data] = get_data('./store/HEPData-ins1762364-v1-Table_1.csv', 0, 11, 39, 0) 
print_last_lines()


#p p --> phi + X
print('//p p --> phi + X | 1/Nev d^2N/(dp_Tdy) (GeV/c)^{-1}')

data = 21
experiment[data] = 2
particle_type[data] = 333
particle_mass[data] = 1.019461
rapidity_low[data]  = 0.0
rapidity_high[data] = 0.5
print_first_lines(data ,experiment[data] ,particle_type[data] ,particle_mass[data] ,rapidity_low[data]  ,rapidity_high[data] )
data_points[data] = get_data('./store/HEPData-ins1762364-v1-Table_2.csv', 0, 11, 34, 0) 
print_last_lines()


print('\n')
print('//===============================================================================================')
print('//https://www.hepdata.net/record/ins1861688 pT spectra of phi.')
#p p --> phi + X
print('//p p --> phi + X |  d^2sigma/(dp_Tdy) (GeV/c)^{-1}')

data = 22
experiment[data] = 2
particle_type[data] = 333
particle_mass[data] = 1.019461
rapidity_low[data]  = 2.5
rapidity_high[data] = 4.0
print_first_lines(data ,experiment[data] ,particle_type[data] ,particle_mass[data] ,rapidity_low[data]  ,rapidity_high[data] )
data_points[data] = get_data('./store/HEPData-ins1861688-v1-Table_2.csv', 0, 11, 23, 0) 
print_last_lines()
print('1e6')



#==============
# CMS
#==============
print('\t//==============')
print('\t// CMS - Did not find any 8 TeV results')
print('\t//==============')

#==============
# ATLAS
#==============
print('\t//==============')
print('\t// ATLAS')
print('\t//==============')



print('\t//===============================================================================================')
print('\t//https://www.hepdata.net/record/ins1409298 ATLAS P P --> J/PSI(2S) ')
#P P --> JPSI < MU+ MU- > X
print('\n')
print('//P P --> J/PSI < MU+ MU- > X  | D2SIG/DPT/DYRAP*BR [NB/GEV]')
data = 23
experiment[data] = 0
particle_type[data] = 443
particle_mass[data] = 3.0969
rapidity_low[data]  = 0.
rapidity_high[data] = 2
print_first_lines(data ,experiment[data] ,particle_type[data] ,particle_mass[data] ,rapidity_low[data]  ,rapidity_high[data] )
data_points[data] = get_data('./store/HEPData-ins1409298-v1-Table_2.csv', 0, 13, 37, 0) 
get_data('./store/HEPData-ins1409298-v1-Table_2.csv', 38, 42, 66, 0) 
print('\n')
get_data('./store/HEPData-ins1409298-v1-Table_2.csv', 67, 71, 95, 0) 
print('\n')
get_data('./store/HEPData-ins1409298-v1-Table_2.csv', 96, 100, 124, 0) 
print('\n')
get_data('./store/HEPData-ins1409298-v1-Table_2.csv', 125, 129, 153, 0) 
print('\n')
get_data('./store/HEPData-ins1409298-v1-Table_2.csv', 154, 158, 182, 0) 
print('\n')
get_data('./store/HEPData-ins1409298-v1-Table_2.csv', 183, 187, 211, 0) 
print('\n')
get_data('./store/HEPData-ins1409298-v1-Table_2.csv', 212, 216, 240, 0) 
print_last_lines()


print('\t//===============================================================================================')
print('\t//https://www.hepdata.net/record/ins1409298 ATLAS P P --> PSI(2S) ')
#P P --> PSI < MU+ MU- > X
print('\n')
print('//P P --> PSI(2S) < MU+ MU- > X  | D2SIG/DPT/DYRAP*BR [NB/GEV]')
data = 24
experiment[data] = 0
particle_type[data] = 100443
particle_mass[data] = 3.6861
rapidity_low[data]  = 0.
rapidity_high[data] = 2
print_first_lines(data ,experiment[data] ,particle_type[data] ,particle_mass[data] ,rapidity_low[data]  ,rapidity_high[data] )
data_points[data] = get_data('./store/HEPData-ins1409298-v1-Table_6.csv', 0, 13, 37, 0) 
get_data('./store/HEPData-ins1409298-v1-Table_6.csv', 38, 42, 66, 0) 
print('\n')
get_data('./store/HEPData-ins1409298-v1-Table_6.csv', 67, 71, 95, 0) 
print('\n')
get_data('./store/HEPData-ins1409298-v1-Table_6.csv', 96, 100, 124, 0) 
print('\n')
get_data('./store/HEPData-ins1409298-v1-Table_6.csv', 125, 129, 153, 0) 
print('\n')
get_data('./store/HEPData-ins1409298-v1-Table_6.csv', 154, 158, 182, 0) 
print('\n')
get_data('./store/HEPData-ins1409298-v1-Table_6.csv', 183, 187, 211, 0) 
print('\n')
get_data('./store/HEPData-ins1409298-v1-Table_6.csv', 212, 216, 240, 0) 
print_last_lines()




print('\t//===============================================================================================')
print('\t//https://www.hepdata.net/record/ins1495026 Measured cross section times branching fractions as a function of pT for prompt psi(2S) and X(3872) production.')
#P P --> PSI(2s) < MU+ MU- > X
print('\n')
print('//P P --> PSI(2S) < MU+ MU- PI+ PI- > X  | pb / GeV')
data = 25
experiment[data] = 0
particle_type[data] = 100443
particle_mass[data] = 3.6861
rapidity_low[data]  = 0.0
rapidity_high[data] = 0.75
print_first_lines(data ,experiment[data] ,particle_type[data] ,particle_mass[data] ,rapidity_low[data]  ,rapidity_high[data] )
print('\tfloat pico_nano = 1e-3;')
print('\tfloat br_psi_2s_2mu2pi = 0.3446;')
data_points[data] = get_data('./store/HEPData-ins1495026-v1-Table_8.csv', 0, 11, 16, 0)
print_last_lines()

#P P --> X(3872) X
print('\n')
print('//P P --> X(3872) X  | pb / GeV')
data = 26
experiment[data] = 0
particle_type[data] = 20445
particle_mass[data] = 3.872
rapidity_low[data]  = 0.0
rapidity_high[data] = 0.75
print_first_lines(data ,experiment[data] ,particle_type[data] ,particle_mass[data] ,rapidity_low[data]  ,rapidity_high[data] )
print('\tfloat br_X_JPsi2pi = 0.038;')
data_points[data] = get_data('./store/HEPData-ins1495026-v1-Table_10.csv', 0, 11, 16, 0)
print_last_lines()

#print(len(data_points))



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
#print(ptl)
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

ndp_all = np.empty(nPlots )

for i in range(len(data_points)):
    set[0] = i
    ptype[0] = particle_type[i]
    exp[0] = experiment[i]
    #print(exp)

    rl[0] = rapidity_low[i]
    rh[0] = rapidity_high[i]
    pmass[0] = particle_mass[i]

    #arrays
    pval = data_points[i]
    #print(pval[0])
    ndp[0] = len(pval[0])
    if i==23 or i==24:
        ndp_all[i] = ndp[0]-4
    else:
        ndp_all[i] = ndp[0]
    #print(pval[0])
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
print("number of points")    
print(ndp_all.astype(int))
print('int npoints[Nparts] = {{ {0} }};'.format( ', '.join(str(int(x)) for x in ndp_all) ) )

outfile = TFile.Open("store/data_collection_8TeV.root", "RECREATE")

measure.Write()

outfile.Write()
outfile.Close()
