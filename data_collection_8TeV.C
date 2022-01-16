#include <TH1.h>
#include <TH2.h>
#include <TFile.h>
#include <TF1.h>
#include <TTree.h>
#include <TStyle.h>
#include <TCanvas.h>
#include <TLine.h>
#include <TLatex.h>
#include <TGraph.h>
#include <TGraphErrors.h>
#include <TGraphAsymmErrors.h>
#include <TProfile.h>
#include <TLegend.h>
#include <TColor.h>
#include <stdlib.h>
#include <vector>


void data_collection_8TeV(){
    const int Nparts = 8;
    const int Nvals = 7;
    int data;
    //                           0  1  2  3  4  5  6  7    8  9  10 11 12 13 14 15 16   17 18 19 20 21 22 23   24 25 26 27   28 29 30 31 32 33 34   35 36 37 38   39 40 41 42   43 44 45 46        47 48 49
    int npoints[Nparts] = { 14, 14, 15, 15, 15, 15, 15, 15 };


    int   experiment[Nparts];    // ATLAS = 0, CMS = 1, ALICE = 2, LHCb = 3.
    int   particle_type[Nparts]; // accordingt to pythia
    float particle_mass[Nparts]; // in GeV
    float rapidity_low[Nparts];  // absolute value 0 = midrapidity
    float rapidity_high[Nparts]; // absolute value
    float pval[Nparts][Nvals][100];

    // https://www.hepdata.net/record/ins1230344 J/Psi and Upsilon 1s/2s/3s double-differential cross sections 
    //P P --> J/PSI X 2.5<y<3


    data = 0;
    experiment[data] = 3;
    particle_type[data] = 100443;
    particle_mass[data] = 3.6861;
    rapidity_low[data]  = 2.5;
    rapidity_high[data] = 3.0;
    float p200[]={ 0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0 };
    float p201[]={ 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0 };
    float p202[]={ 0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5 };
    float p203[]={ 727.45, 1463.31, 1237.49, 761.17, 432.67, 231.63, 126.5, 68.05, 39.23, 22.04, 13.6, 8.06, 5.26, 3.3 };
    float p204[]={ 13.14, 16.73, 12.28, 7.29, 4.33, 2.6, 1.65, 1.07, 0.74, 0.52, 0.39, 0.28, 0.22, 0.17 };
    float p205[]={ 25.66, 19.26, 22.39, 20.6, 20.79, 2.89, 2.29, 1.98, 1.88, 0.66, 0.45, 0.23, 0.2, 0.21 };
    float p206[]={ -13.14, -16.73, -12.28, -7.29, -4.33, -2.6, -1.65, -1.07, -0.74, -0.52, -0.39, -0.28, -0.22, -0.17 };

    for (int bin = 0; bin < npoints[data]; bin++){
        pval[data][0][bin] = p200[bin];
        pval[data][1][bin] = p201[bin];
        pval[data][2][bin] = p202[bin];
        pval[data][3][bin] = p203[bin];
        pval[data][4][bin] = p204[bin];
        pval[data][5][bin] = p205[bin];
        pval[data][6][bin] = p206[bin];
    }
    
    //P P --> J/PSI X 3<y<3.5


    data = 1;
    experiment[data] = 3;
    particle_type[data] = 100443;
    particle_mass[data] = 3.6861;
    rapidity_low[data]  = 3.0;
    rapidity_high[data] = 3.5;
    float p210[]={ 0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0 };
    float p211[]={ 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0 };
    float p212[]={ 0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5 };
    float p213[]={ 71.7, 157.59, 152.06, 106.89, 68.17, 41.94, 25.49, 15.36, 10.2, 6.26, 4.16, 2.82, 2.17, 1.39 };
    float p214[]={ 1.33, 1.84, 1.62, 1.16, 0.81, 0.57, 0.42, 0.31, 0.25, 0.19, 0.15, 0.13, 0.11, 0.09 };
    float p215[]={ 6.58, 3.88, 3.38, 1.79, 1.29, 1.07, 0.96, 0.31, 0.27, 0.17, 0.13, 0.14, 0.03, 0.04 };
    float p216[]={ -1.33, -1.84, -1.62, -1.16, -0.81, -0.57, -0.42, -0.31, -0.25, -0.19, -0.15, -0.13, -0.11, -0.09 };

    for (int bin = 0; bin < npoints[data]; bin++){
        pval[data][0][bin] = p210[bin];
        pval[data][1][bin] = p211[bin];
        pval[data][2][bin] = p212[bin];
        pval[data][3][bin] = p213[bin];
        pval[data][4][bin] = p214[bin];
        pval[data][5][bin] = p215[bin];
        pval[data][6][bin] = p216[bin];
    }
    
    
    
    //P P --> UPSI(1/2/3S) < MU+ MU-> X 2.5<y<3


    data = 2;
    experiment[data] = 3;
    particle_type[data] = 553;
    particle_mass[data] = 9.4603;
    rapidity_low[data]  = 2.5;
    rapidity_high[data] = 3.0;
    float p700[]={ 0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0 };
    float p701[]={ 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0 };
    float p702[]={ 0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5 };
    float p703[]={ 73.9, 197.7, 248.1, 237.9, 220.6, 181.2, 140.1, 106.2, 75.3, 60.9, 51.4, 34.7, 29.7, 22.3, 15.6 };
    float p704[]={ 4.2, 6.8, 7.5, 7.2, 6.9, 6.1, 5.3, 4.6, 3.8, 3.3, 3.0, 2.5, 2.2, 1.9, 1.6 };
    float p705[]={ 1.8, 2.7, 2.7, 4.1, 3.1, 4.2, 4.5, 1.6, 2.3, 1.5, 1.7, 1.4, 0.3, 0.5, 0.8 };
    float p706[]={ -4.2, -6.8, -7.5, -7.2, -6.9, -6.1, -5.3, -4.6, -3.8, -3.3, -3.0, -2.5, -2.2, -1.9, -1.6 };

    for (int bin = 0; bin < npoints[data]; bin++){
        pval[data][0][bin] = p700[bin];
        pval[data][1][bin] = p701[bin];
        pval[data][2][bin] = p702[bin];
        pval[data][3][bin] = p703[bin];
        pval[data][4][bin] = p704[bin];
        pval[data][5][bin] = p705[bin];
        pval[data][6][bin] = p706[bin];
    }
    
    data = 3;
    experiment[data] = 3;
    particle_type[data] = 100553;
    particle_mass[data] = 10.02326;
    rapidity_low[data]  = 2.5;
    rapidity_high[data] = 3.0;
    float p800[]={ 0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0 };
    float p801[]={ 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0 };
    float p802[]={ 0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5 };
    float p803[]={ 14.5, 33.2, 49.3, 56.8, 46.4, 51.1, 43.4, 28.6, 21.2, 20.9, 16.0, 14.9, 7.8, 5.6, 4.0 };
    float p804[]={ 1.8, 2.7, 3.3, 3.5, 3.1, 3.2, 2.9, 2.4, 2.0, 2.0, 1.7, 1.6, 1.2, 1.0, 0.8 };
    float p805[]={ 0.3, 1.3, 1.0, 0.6, 0.5, 0.8, 0.9, 0.6, 0.1, 0.2, 0.2, 0.2, 0.2, 0.2, 0.3 };
    float p806[]={ -1.8, -2.7, -3.3, -3.5, -3.1, -3.2, -2.9, -2.4, -2.0, -2.0, -1.7, -1.6, -1.2, -1.0, -0.8 };

    for (int bin = 0; bin < npoints[data]; bin++){
        pval[data][0][bin] = p800[bin];
        pval[data][1][bin] = p801[bin];
        pval[data][2][bin] = p802[bin];
        pval[data][3][bin] = p803[bin];
        pval[data][4][bin] = p804[bin];
        pval[data][5][bin] = p805[bin];
        pval[data][6][bin] = p806[bin];
    }
    
    data = 4;
    experiment[data] = 3;
    particle_type[data] = 200553;
    particle_mass[data] = 10.3552;
    rapidity_low[data]  = 2.5;
    rapidity_high[data] = 3.0;
    float p900[]={ 0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0 };
    float p901[]={ 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0 };
    float p902[]={ 0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5 };
    float p903[]={ 4.8, 17.9, 25.5, 22.9, 23.6, 19.6, 21.4, 13.7, 14.2, 8.7, 9.6, 8.1, 6.3, 10.0, 4.0 };
    float p904[]={ 1.0, 2.0, 2.3, 2.2, 2.2, 2.0, 2.1, 1.6, 1.6, 1.3, 1.3, 1.2, 1.0, 1.3, 0.8 };
    float p905[]={ 0.1, 0.3, 0.4, 0.3, 0.3, 0.3, 0.4, 0.3, 0.6, 0.3, 0.5, 0.1, 0.1, 0.2, 0.1 };
    float p906[]={ -1.0, -2.0, -2.3, -2.2, -2.2, -2.0, -2.1, -1.6, -1.6, -1.3, -1.3, -1.2, -1.0, -1.3, -0.8 };

    for (int bin = 0; bin < npoints[data]; bin++){
        pval[data][0][bin] = p900[bin];
        pval[data][1][bin] = p901[bin];
        pval[data][2][bin] = p902[bin];
        pval[data][3][bin] = p903[bin];
        pval[data][4][bin] = p904[bin];
        pval[data][5][bin] = p905[bin];
        pval[data][6][bin] = p906[bin];
    }
    
    
    //P P --> UPSI(1/2/3S) < MU+ MU-> X 3<y<3.5


    data = 5;
    experiment[data] = 3;
    particle_type[data] = 553;
    particle_mass[data] = 9.4603;
    rapidity_low[data]  = 3.0;
    rapidity_high[data] = 3.5;
    float p710[]={ 0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0 };
    float p711[]={ 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0 };
    float p712[]={ 0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5 };
    float p713[]={ 64.7, 185.6, 228.5, 243.5, 199.1, 177.4, 128.2, 106.3, 74.0, 56.7, 44.4, 31.1, 21.5, 16.8, 13.8 };
    float p714[]={ 2.6, 4.5, 5.0, 5.1, 4.7, 4.4, 3.7, 3.4, 2.8, 2.4, 2.1, 1.7, 1.4, 1.3, 1.1 };
    float p715[]={ 1.3, 1.9, 2.1, 1.5, 1.2, 1.8, 0.9, 1.5, 0.7, 0.7, 0.8, 0.6, 0.9, 0.1, 0.5 };
    float p716[]={ -2.6, -4.5, -5.0, -5.1, -4.7, -4.4, -3.7, -3.4, -2.8, -2.4, -2.1, -1.7, -1.4, -1.3, -1.1 };

    for (int bin = 0; bin < npoints[data]; bin++){
        pval[data][0][bin] = p710[bin];
        pval[data][1][bin] = p711[bin];
        pval[data][2][bin] = p712[bin];
        pval[data][3][bin] = p713[bin];
        pval[data][4][bin] = p714[bin];
        pval[data][5][bin] = p715[bin];
        pval[data][6][bin] = p716[bin];
    }
    
    data = 6;
    experiment[data] = 3;
    particle_type[data] = 100553;
    particle_mass[data] = 10.02326;
    rapidity_low[data]  = 3.0;
    rapidity_high[data] = 3.5;
    float p810[]={ 0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0 };
    float p811[]={ 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0 };
    float p812[]={ 0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5 };
    float p813[]={ 15.2, 42.6, 54.3, 61.0, 45.1, 48.9, 34.9, 29.3, 23.7, 16.1, 13.4, 10.2, 10.4, 7.0, 5.8 };
    float p814[]={ 1.3, 2.1, 2.4, 2.6, 2.2, 2.3, 1.9, 1.8, 1.6, 1.3, 1.2, 1.0, 1.0, 0.8, 0.8 };
    float p815[]={ 0.7, 0.3, 1.0, 0.4, 0.5, 0.3, 0.6, 0.7, 0.2, 0.2, 0.2, 0.2, 0.2, 0.1, 0.1 };
    float p816[]={ -1.3, -2.1, -2.4, -2.6, -2.2, -2.3, -1.9, -1.8, -1.6, -1.3, -1.2, -1.0, -1.0, -0.8, -0.8 };

    for (int bin = 0; bin < npoints[data]; bin++){
        pval[data][0][bin] = p810[bin];
        pval[data][1][bin] = p811[bin];
        pval[data][2][bin] = p812[bin];
        pval[data][3][bin] = p813[bin];
        pval[data][4][bin] = p814[bin];
        pval[data][5][bin] = p815[bin];
        pval[data][6][bin] = p816[bin];
    }
    

    data = 7;
    experiment[data] = 3;
    particle_type[data] = 200553;
    particle_mass[data] = 10.3552;
    rapidity_low[data]  = 3.0;
    rapidity_high[data] = 3.5;
    float p910[]={ 0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0 };
    float p911[]={ 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0 };
    float p912[]={ 0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5 };
    float p913[]={ 5.5, 18.2, 17.3, 26.2, 18.0, 21.8, 18.9, 16.1, 12.5, 10.4, 7.4, 5.9, 5.3, 4.6, 2.2 };
    float p914[]={ 0.8, 1.4, 1.3, 1.7, 1.4, 1.5, 1.4, 1.3, 1.1, 1.0, 0.9, 0.8, 0.7, 0.7, 0.5 };
    float p915[]={ 0.1, 0.2, 0.1, 0.2, 0.1, 0.2, 0.2, 0.2, 0.2, 0.2, 0.3, 0.2, 0.1, 0.2, 0.1 };
    float p916[]={ -0.8, -1.4, -1.3, -1.7, -1.4, -1.5, -1.4, -1.3, -1.1, -1.0, -0.9, -0.8, -0.7, -0.7, -0.5 };


    for (int bin = 0; bin < npoints[data]; bin++){
        pval[data][0][bin] = p910[bin];
        pval[data][1][bin] = p911[bin];
        pval[data][2][bin] = p912[bin];
        pval[data][3][bin] = p913[bin];
        pval[data][4][bin] = p914[bin];
        pval[data][5][bin] = p915[bin];
        pval[data][6][bin] = p916[bin];
    }
    

    //Write 
    int set,ndp,exp,ptype;
    float rl, rh, pmass;
    std::vector<float> *ptl = new std::vector<float>();
    std::vector<float> *ptu = new std::vector<float>();
    std::vector<float> *pt  = new std::vector<float>();
    std::vector<float> *mtl = new std::vector<float>();
    std::vector<float> *mtu = new std::vector<float>();
    std::vector<float> *mt  = new std::vector<float>();
    std::vector<float> *cross_s	         = new std::vector<float>();
    std::vector<float> *cross_s_stat       = new std::vector<float>();
    std::vector<float> *cross_s_syst_high  = new std::vector<float>();
    std::vector<float> *cross_s_syst_low   = new std::vector<float>();
  
    TTree *measure = new TTree("measure","particle measurements");
    measure -> Branch("set",  &set,   "set/I");
    measure -> Branch("exp",  &exp,   "exp/I");
    measure -> Branch("type", &ptype, "type/I");
    measure -> Branch("yu",   &rh,    "yu/F");
    measure -> Branch("yl",   &rl,    "yl/F");
    measure -> Branch("np",   &ndp,   "np/I");
    measure -> Branch("mass", &pmass, "mass/F");
    measure -> Branch("pT",   &pt);
    measure -> Branch("pTu",  &ptu);
    measure -> Branch("pTl",  &ptl);
    measure -> Branch("mT",   &mt);
    measure -> Branch("mTu",  &mtu);
    measure -> Branch("mTl",  &mtl);
    measure -> Branch("cs",   &cross_s);
    measure -> Branch("ecs",  &cross_s_stat);
    measure -> Branch("ecsu", &cross_s_syst_high);
    measure -> Branch("ecsl", &cross_s_syst_low);
  
    TGraphErrors *CS[Nparts];
    float x[200],ex[200],y[200],ey[200];
  
  
    for (int part = 0; part < Nparts; part++){
        pt->clear();
        ptu->clear();
        ptl->clear();
        mt->clear();
        mtu->clear();
        mtl->clear();
        cross_s->clear();
        cross_s_stat->clear();
        cross_s_syst_high->clear();
        cross_s_syst_low->clear();
        set = part;
        ndp = npoints[part];
        ptype = particle_type[part];
        exp = experiment[part];
        rl = rapidity_low[part];
        rh = rapidity_high[part];
        pmass = particle_mass[part];
        for (int bin = 0; bin < npoints[part]; bin++){
            ptl -> push_back(pval[part][0][bin]);
            ptu -> push_back(pval[part][1][bin]);
            pt  -> push_back(pval[part][2][bin]);

            mtl -> push_back(pow(pow(pval[part][0][bin],2) + pow(pmass,2),0.5));
            mtu -> push_back(pow(pow(pval[part][1][bin],2) + pow(pmass,2),0.5));
            mt  -> push_back(pow(pow(pval[part][2][bin],2) + pow(pmass,2),0.5));

            x[bin]  = (pval[part][1][bin] + pval[part][0][bin]) / 2.;
            y[bin]  = pval[part][3][bin] / x[bin];
            ey[bin] = pval[part][4][bin] / x[bin];

            cross_s           -> push_back(pval[part][3][bin] * (pval[part][1][bin]-pval[part][0][bin]));
            cross_s_stat      -> push_back(pval[part][4][bin] * (pval[part][1][bin]-pval[part][0][bin]));
            cross_s_syst_high -> push_back(pval[part][5][bin] * (pval[part][1][bin]-pval[part][0][bin]));
            cross_s_syst_low  -> push_back(pval[part][6][bin] * (pval[part][1][bin]-pval[part][0][bin]));          
	    }
        CS[part] = new TGraphErrors(npoints[part],x,y,ex,ey);
        CS[part] -> SetMarkerSize(1);
        CS[part] -> SetLineWidth(1);
 
        measure -> Fill();
    }
    for (int part = 0; part < Nparts; part++){
        for (int bin = 0; bin < npoints[part]; bin++)
	        printf("%4.1f - %4.1f  %4.1f | %6.4f +/- %6.4f: %6.4f %6.4f\n",pval[part][0][bin],pval[part][1][bin],pval[part][2][bin],pval[part][3][bin],pval[part][4][bin],pval[part][5][bin],pval[part][6][bin]);
        printf("\n");
    }

    printf("writting out\n");
    TFile *outf = new TFile("store/data_collection_8TeV.root","recreate");

    measure -> Write();
 
    outf -> Write();
    outf -> Close();
}