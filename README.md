The best way to look for this data is via experimental public result pages:

ALICE: https://twiki.cern.ch/twiki/bin/view/ALICEpublic/ALICEPublicResults?sortcol=0;table=2;up=0#sorted_table 

ATLAS: https://twiki.cern.ch/twiki/bin/view/AtlasPublic/BPhysPublicResults

CMS: https://cms-results.web.cern.ch/cms-results/public-results/publications/

LHCb: https://lhcbproject.web.cern.ch/Publications/LHCbProjectPublic/Summary_all.html

then you click on a paper and find a link to the text and to the database. i used excel format to download files and copy-pasted it into my file, this takes time, but you can use any format that you prefer.

-- I need spectra of ALL mesons (no baryons, no bosons, no leptons) measured in pp collisions at 8 TeV and 13 TeV from all LHC experiments, w/o exceptions.
-- if the meson is measured as prompt and non-prompt, take the prompt one, if not take inclusive. do not take non-prompt.
-- if the meson correction involves polarization, take zero polarization assumption
-- take fully corrected spectrum, but if it is measured only in fiducial, take in fiducial and put a note

attached you find a macro called 'data_collection' where i keep the raw data at 7 TeV. This file contains all relevant LHC experimental data at 7 TeV. i need the same at 8 TeV and 13 TeV as two separate files with the same structure. 

the structure of each data set is the following:

header, always keep it; mention link, experiment, decay mode, rapidity and units.

//================

//https://www.hepdata.net/record/ins1511870 ALICE P P --> D+ (Q=PROMPT) X |y|<0.5

//PT [GEV] PT [GEV] LOW PT [GEV] HIGH D2(SIG)/DPT/DYRAP [MUB/GEV] stat + stat - sys + sys - sys,luminosity uncertainty + sys,luminosity uncertainty - sys,branching ratio uncertainty + sys,branching ratio uncertainty -


below are data points, pXYZ stands for

X particle specie type, 0 are pions, 2 are kaons, but this is not so important here.

Y is the measurement number. if the same experiment measured pions in 4 rapidity slices then make them Y, Y+1, Y+2, Y+3 and start the next measurement at Y+4, etc...

if an experiment measured the same particle twice or more (probably with different years, pT, y and integrated lumi) it would be good if you put them one after another. 

- Z is "0/1" low/high pT bin edge; 
- 2 is the mean pT <-- this order is different in the database, it starts with mean pT, but keep mine; 
- 3 is the cross-section or number; 
- 4 is the statistical error (positive); 
- 5 is a systematic error (positive); 
- 6 is a systematic error (negative) if it is different from positive

if there is a scaling error, do not write it, just throw it away

```
  float p140[]={1,2,3,4,5,6,7,8,10,12,16};
  float p141[]={  2,3,4,5,6,7,8,10,12,16,24};
  float p142[]={1.5,2.5,3.5,4.5,5.5,6.5,7.5,9,11,14,20};
  float p143[]={92.2,43.9,23,10.9,4.82,2.67,1.6,0.761,0.258,0.0996,0.0242};
  float p144[]={13.8,3.07,1.08,0.487,0.249,0.163,0.109,0.0467,0.0264,0.0104,0.00325};
  float p145[]={12,5.59,1.86,0.877,0.406,0.232,0.141,0.0672,0.023,0.00971,0.0024};
  float p146[]={-12.1,-5.62,-1.89,-0.898,-0.421,-0.239,-0.145,-0.0688,-0.0237,-0.0099,-0.0024};
  // 4.3,4.3,4.3,4.3,4.3,4.3,4.3,4.3,4.3,4.3,4.3 // %%
 
  data = 11;  <-- increment by 1 for each new measurement set
  experiment[data] = 2;  // ATLAS = 0, CMS = 1, ALICE = 2, LHCb = 3.
  particle_type[data] = 411; // by PDG
  particle_mass[data] = 1.86966;
  rapidity_low[data]  = 0.;
  rapidity_high[data] = 0.5;
[data][Z][bin] --> [data] is data, Z is the same Z as above, 'bin' is the point order number. counter npoints[data] shall be entered in the array at the header of the macro file by hands.
  for (int bin = 0; bin < npoints[data]; bin++)
    {
      pval[data][0][bin] = p140[bin];
      pval[data][1][bin] = p141[bin];
      pval[data][2][bin] = p142[bin];
      pval[data][3][bin] = p143[bin] * 1e3; <-- in the file you find other options. the idea is that the output is the cross section in nb the pT bin, do not divide by bin width.
      pval[data][4][bin] = p144[bin] * 1e3;
      pval[data][5][bin] = p145[bin] * 1e3;
      pval[data][6][bin] = p146[bin] * 1e3;
    }
```
