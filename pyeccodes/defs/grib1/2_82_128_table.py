def load(h):
    return ({'abbr': 'so2', 'code': 1, 'title': 'SO2 SO2/SO2 -'},
            {'abbr': 'so4_2-', 'code': 2, 'title': 'SO4_2- SO4(2-)/SO4(2-) (sulphate) -'},
            {'abbr': 'dms', 'code': 3, 'title': 'DMS DMS/DMS -'},
            {'abbr': 'msa', 'code': 4, 'title': 'MSA MSA/MSA -'},
            {'abbr': 'h2s', 'code': 5, 'title': 'H2S H2S/H2S -'},
            {'abbr': 'nh4so4', 'code': 6, 'title': 'NH4SO4 NH4SO4/(NH4)1.5H0.5SO4 -'},
            {'abbr': 'nh4hso4', 'code': 7, 'title': 'NH4HSO4 NH4HSO4/NH4HSO4 -'},
            {'abbr': 'nh42so4', 'code': 8, 'title': 'NH42SO4 NH42SO4/(NH4)2SO4 -'},
            {'abbr': 'sft', 'code': 9, 'title': 'SFT SULFATE/SULFATE -'},
            {'abbr': 'so2_aq',
             'code': 10,
             'title': 'SO2_AQ SO2_AQ/SO2 in aqueous phase -'},
            {'abbr': 'so4_aq',
             'code': 11,
             'title': 'SO4_AQ SO4_AQ/sulfate in aqueous phase -'},
            {'abbr': 'lrt_so2_s',
             'code': 23,
             'title': 'LRT_SO2_S LRT_SO2_S/long-range SO2_S -'},
            {'abbr': 'lrt_so4_s',
             'code': 24,
             'title': 'LRT_SO4_S LRT_SO4_S/LRT-contriubtion to SO4_S -'},
            {'abbr': 'lrt_sox_s',
             'code': 25,
             'title': 'LRT_SOX_S LRT_SOX_S/LRT-contriubtion to SO4_S -'},
            {'abbr': 'xsox_s',
             'code': 26,
             'title': 'XSOX_S XSOX_S/excess SOX (corrected for sea salt as sulfur) -'},
            {'abbr': 'so2_s', 'code': 27, 'title': 'SO2_S SO2_S/SO2 (as sulphur) -'},
            {'abbr': 'so4_s', 'code': 28, 'title': 'SO4_S SO4_S/SO4 (as sulphur) -'},
            {'abbr': 'sox_s',
             'code': 29,
             'title': 'SOX_S SOX_S/All oxidised sulphur compounds (as sulphur) -'},
            {'abbr': 'no', 'code': 30, 'title': 'NO NO -'},
            {'abbr': 'no2', 'code': 31, 'title': 'NO2 NO2/NO2 -'},
            {'abbr': 'hno3', 'code': 32, 'title': 'HNO3 HNO3/HNO3 -'},
            {'abbr': 'no3-', 'code': 33, 'title': 'NO3- NO3(-1)/NO3(-1) (nitrate) -'},
            {'abbr': 'nh4no3', 'code': 34, 'title': 'NH4NO3 NH4NO3/NH4NO3 -'},
            {'abbr': 'nitrate', 'code': 35, 'title': 'NITRATE NITRATE/NITRATE -'},
            {'abbr': 'pno3', 'code': 36, 'title': 'PNO3 PNO3/(COARSE) NITRATE -'},
            {'abbr': 'lrt_noy_n',
             'code': 37,
             'title': 'LRT_NOY_N LRT_NOY_N/long-range NOY_N -'},
            {'abbr': 'no3_n', 'code': 38, 'title': 'NO3_N NO3_N/NO3 as N -'},
            {'abbr': 'hno3_n', 'code': 39, 'title': 'HNO3_N HNO3_N/HNO3 as N -'},
            {'abbr': 'lrt_no3_n',
             'code': 40,
             'title': 'LRT_NO3_N LRT_NO3_N/long-range NO3_N -'},
            {'abbr': 'lrt_hno3_n',
             'code': 41,
             'title': 'LRT_HNO3_N LRT_HNO3_N/long-range HNO3_N -'},
            {'abbr': 'lrt_no2_n',
             'code': 42,
             'title': 'LRT_NO2_N LRT_NO2_N/long-range NO2_N -'},
            {'abbr': 'lrt_noz_n',
             'code': 43,
             'title': 'LRT_NOZ_N LRT_NOZ_N/long-range NOZ_N -'},
            {'abbr': 'nox', 'code': 44, 'title': 'NOX NOX/NOX as NO2 -'},
            {'abbr': 'no_n', 'code': 45, 'title': 'NO_N NO_N/NO as N -'},
            {'abbr': 'no2_n', 'code': 46, 'title': 'NO2_N NO2_N/NO2 as N -'},
            {'abbr': 'nox_n',
             'code': 47,
             'title': 'NOX_N NOX_N/NO2+NO (NOx) as nitrogen -'},
            {'abbr': 'noy_n',
             'code': 48,
             'title': 'NOY_N NOY_N/All oxidised N-compounds (as nitrogen) -'},
            {'abbr': 'noz_n', 'code': 49, 'title': 'NOZ_N NOZ_N/NOy-NOx (as nitrogen) -'},
            {'abbr': 'nh3', 'code': 50, 'title': 'NH3 NH3/NH3 -'},
            {'abbr': 'nh4_plus', 'code': 51, 'title': 'NH4_PLUS NH4(+1)/NH4 -'},
            {'abbr': 'ammonium', 'code': 52, 'title': 'AMMONIUM AMMONIUM/AMMONIUM -'},
            {'abbr': 'nh3_n', 'code': 54, 'title': 'NH3_N NH3_N/NH3 (as nitrogen) -'},
            {'abbr': 'nh4_n', 'code': 55, 'title': 'NH4_N NH4_N/NH4 (as nitrogen) -'},
            {'abbr': 'lrt_nh3_n',
             'code': 56,
             'title': 'LRT_NH3_N LRT_NH3_N/long-range NH3_N -'},
            {'abbr': 'lrt_nh4_n',
             'code': 57,
             'title': 'LRT_NH4_N LRT_NH4_N/long-range NH4_N -'},
            {'abbr': 'lrt_nhx_n',
             'code': 58,
             'title': 'LRT_NHX_N LRT_NHX_N/long-range NHX_N -'},
            {'abbr': 'nhx_n',
             'code': 59,
             'title': 'NHX_N NHX_N/All reduced nitrogen (as nitrogen) -'},
            {'abbr': 'o3', 'code': 60, 'title': 'O3 O3 -'},
            {'abbr': 'h2o2', 'code': 61, 'title': 'H2O2 H2O2/H2O2 -'},
            {'abbr': 'oh', 'code': 62, 'title': 'OH OH/OH -'},
            {'abbr': 'o3_aq', 'code': 63, 'title': 'O3_AQ O3_AQ/O3 in aqueous phase -'},
            {'abbr': 'h2o2_aq',
             'code': 64,
             'title': 'H2O2_AQ H2O2_AQ/H2O2 in aqueous phase -'},
            {'abbr': 'ox', 'code': 65, 'title': 'OX OX/Ox=O3+NO2 -'},
            {'abbr': 'c', 'code': 70, 'title': 'C C -'},
            {'abbr': 'co', 'code': 71, 'title': 'CO CO/CO -'},
            {'abbr': 'co2', 'code': 72, 'title': 'CO2 CO2/CO2 -'},
            {'abbr': 'ch4', 'code': 73, 'title': 'CH4 CH4/CH4 -'},
            {'abbr': 'oc', 'code': 74, 'title': 'OC OC/Organic carbon (particles) -'},
            {'abbr': 'ec', 'code': 75, 'title': 'EC EC/Elementary carbon (particles) -'},
            {'abbr': 'cf6', 'code': 80, 'title': 'CF6 CF6 -'},
            {'abbr': 'pmch', 'code': 81, 'title': 'PMCH PMCH/PMCH -'},
            {'abbr': 'pmcp', 'code': 82, 'title': 'PMCP PMCP/PMCP -'},
            {'abbr': 'tracer', 'code': 83, 'title': 'TRACER TRACER/Tracer -'},
            {'abbr': 'inert', 'code': 84, 'title': 'INERT Inert/Inert -'},
            {'abbr': 'h3', 'code': 85, 'title': 'H3 H3 -'},
            {'abbr': 'ar41', 'code': 86, 'title': 'AR41 Ar41/Ar41 -'},
            {'abbr': 'kr85', 'code': 87, 'title': 'KR85 Kr85/Kr85 -'},
            {'abbr': 'kr88', 'code': 88, 'title': 'KR88 Kr88/Kr88 -'},
            {'abbr': 'xe131', 'code': 91, 'title': 'XE131 Xe131/Xe131 -'},
            {'abbr': 'xe133', 'code': 92, 'title': 'XE133 Xe133/Xe133 -'},
            {'abbr': 'rn222', 'code': 93, 'title': 'RN222 Rn222/Rn222 -'},
            {'abbr': 'i131', 'code': 95, 'title': 'I131 I131/I131 -'},
            {'abbr': 'i132', 'code': 96, 'title': 'I132 I132/I132 -'},
            {'abbr': 'i133', 'code': 97, 'title': 'I133 I133/I133 -'},
            {'abbr': 'i135', 'code': 98, 'title': 'I135 I135/I135 -'},
            {'abbr': 'sr90', 'code': 100, 'title': 'SR90 Sr90 -'},
            {'abbr': 'co60', 'code': 101, 'title': 'CO60 Co60/Co60 -'},
            {'abbr': 'ru103', 'code': 102, 'title': 'RU103 Ru103/Ru103 -'},
            {'abbr': 'ru106', 'code': 103, 'title': 'RU106 Ru106/Ru106 -'},
            {'abbr': 'cs134', 'code': 104, 'title': 'CS134 Cs134/Cs134 -'},
            {'abbr': 'cs137', 'code': 105, 'title': 'CS137 Cs137/Cs137 -'},
            {'abbr': 'ra223', 'code': 106, 'title': 'RA223 Ra223/Ra123 -'},
            {'abbr': 'ra228', 'code': 108, 'title': 'RA228 Ra228/Ra228 -'},
            {'abbr': 'zr95', 'code': 110, 'title': 'ZR95 Zr95 -'},
            {'abbr': 'nb95', 'code': 111, 'title': 'NB95 Nb95/Nb95 -'},
            {'abbr': 'ce144', 'code': 112, 'title': 'CE144 Ce144/Ce144 -'},
            {'abbr': 'np238', 'code': 113, 'title': 'NP238 Np238/Np238 -'},
            {'abbr': 'np239', 'code': 114, 'title': 'NP239 Np239/Np239 -'},
            {'abbr': 'pu241', 'code': 115, 'title': 'PU241 Pu241/Pu241 -'},
            {'abbr': 'pb210', 'code': 116, 'title': 'PB210 Pb210/Pb210 -'},
            {'abbr': 'all', 'code': 119, 'title': 'ALL ALL -'},
            {'abbr': 'nacl', 'code': 120, 'title': 'NACL NACL -'},
            {'abbr': 'na_plus', 'code': 121, 'title': 'NA_PLUS SODIUM/Na+ -'},
            {'abbr': 'mg_2plus', 'code': 122, 'title': 'MG_2PLUS MAGNESIUM/Mg++ -'},
            {'abbr': 'k_plus', 'code': 123, 'title': 'K_PLUS POTASSIUM/K+ -'},
            {'abbr': 'ca_2plus', 'code': 124, 'title': 'CA_2PLUS CALCIUM/Ca++ -'},
            {'abbr': 'xmg',
             'code': 125,
             'title': 'XMG XMG/excess Mg++ (corrected for sea salt) -'},
            {'abbr': 'xk',
             'code': 126,
             'title': 'XK XK/excess K+ (corrected for sea salt) -'},
            {'abbr': 'xca',
             'code': 128,
             'title': 'XCA XCA/excess Ca++ (corrected for sea salt) -'},
            {'abbr': 'cl2', 'code': 140, 'title': 'CL2 Cl2/Cloride -'},
            {'abbr': 'pmfine', 'code': 160, 'title': 'PMFINE PMFINE -'},
            {'abbr': 'pmcoarse',
             'code': 161,
             'title': 'PMCOARSE PMCOARSE/Coarse particles -'},
            {'abbr': 'dust', 'code': 162, 'title': 'DUST DUST/Dust (particles) -'},
            {'abbr': 'pnumber',
             'code': 163,
             'title': 'PNUMBER PNUMBER/Number concentration -'},
            {'abbr': 'pradius', 'code': 164, 'title': 'PRADIUS PRADIUS/Particle radius -'},
            {'abbr': 'psurface',
             'code': 165,
             'title': 'PSURFACE PSURFACE/Particle surface conc -'},
            {'abbr': 'pmass', 'code': 166, 'title': 'PMASS PMASS/Particle mass conc -'},
            {'abbr': 'pm10', 'code': 167, 'title': 'PM10 PM10/PM10 particles -'},
            {'abbr': 'psox', 'code': 168, 'title': 'PSOX PSOX/Particulate sulfate -'},
            {'abbr': 'pnox', 'code': 169, 'title': 'PNOX PNOX/Particulate nitrate -'},
            {'abbr': 'pnhx', 'code': 170, 'title': 'PNHX PNHX/Particulate ammonium -'},
            {'abbr': 'ppmfine',
             'code': 171,
             'title': 'PPMFINE PPMFINE/Primary emitted fine particles -'},
            {'abbr': 'ppm10',
             'code': 172,
             'title': 'PPM10 PPM10/Primary emitted particles -'},
            {'abbr': 'soa', 'code': 173, 'title': 'SOA SOA/Secondary Organic Aerosol -'},
            {'abbr': 'pm2.5', 'code': 174, 'title': 'PM2.5 PM2.5/PM2.5 particles -'},
            {'abbr': 'pm', 'code': 175, 'title': 'PM PM/Total particulate matter -'},
            {'abbr': 'birch_pollen',
             'code': 180,
             'title': 'BIRCH_POLLEN BIRCH_POLLEN/Birch pollen -'},
            {'abbr': 'kz', 'code': 200, 'title': 'KZ KZ m2/s'},
            {'abbr': 'l', 'code': 201, 'title': 'L L/Monin-Obukhovs length [m] m'},
            {'abbr': 'u_star',
             'code': 202,
             'title': 'U_STAR U*/Friction velocity [m/s] m/s'},
            {'abbr': 'w_star',
             'code': 203,
             'title': 'W_STAR W*/Convective velocity scale [m/s] m/s'},
            {'abbr': 'z-d',
             'code': 204,
             'title': 'Z-D Z-D/Z0 minus displacement length [m] m'},
            {'abbr': 'surftype',
             'code': 210,
             'title': 'SURFTYPE SURFTYPE/Surface type (see \\link{OCTET45}) -'},
            {'abbr': 'lai', 'code': 211, 'title': 'LAI LAI/Leaf area index -'},
            {'abbr': 'soiltype', 'code': 212, 'title': 'SOILTYPE SOILTYPE/Soil type -'},
            {'abbr': 'ssalb',
             'code': 213,
             'title': 'SSALB SSALB/Single scattering albodo [1] 1'},
            {'abbr': 'asympar',
             'code': 214,
             'title': 'ASYMPAR ASYMPAR/Asymmetry parameter -'},
            {'abbr': 'vis', 'code': 215, 'title': 'VIS VIS/Visibility [m] m'},
            {'abbr': 'ext', 'code': 216, 'title': 'EXT EXT/Extinction [1/m] 1/m'},
            {'abbr': 'bsca',
             'code': 217,
             'title': 'BSCA BSCA/Backscattering coeff [1/m/sr] 1/m/sr'},
            {'abbr': 'aod', 'code': 218, 'title': 'AOD AOD/Aerosol opt depth [1] 1'},
            {'abbr': 'daod', 'code': 219, 'title': 'DAOD DAOD/AOD per layer [1] 1'},
            {'abbr': 'conv_tied', 'code': 220, 'title': 'CONV_TIED CONV_TIED -'},
            {'abbr': 'conv_bot',
             'code': 221,
             'title': 'CONV_BOT CONV_BOT/Convective cloud bottom (unit?) -'},
            {'abbr': 'conv_top',
             'code': 222,
             'title': 'CONV_TOP CONV_TOP/Convective cloud top (unit?) -'},
            {'abbr': 'dxdy', 'code': 223, 'title': 'DXDY DXDY/Gridsize [m2] m2'},
            {'abbr': 'emis', 'code': 240, 'title': 'EMIS EMIS/Sectoral emissions -'},
            {'abbr': 'long', 'code': 241, 'title': 'LONG LONG/Longitude -'},
            {'abbr': 'lat', 'code': 242, 'title': 'LAT LAT/Latitude -'})
