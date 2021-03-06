# Dictionary of reaction ids and names
# Found in Table 10.1.A.1 of the Scale documentation.
# Uses the shorthand when one was given. If a description
# does not make sense, longer descriptions are given in the table.
mt_ids = {1:'n,total', 2:'z,z0', 3:'z,nonelastic', 4:'z,n', 5:'z,anything', 10:'z,continuum', 11:'z,2nd', 16:'z,2n',
          17:'z,3n', 18:'z,fission', 19:'n,f', 20:'n,nf', 21:'n,2nf', 22:'z,n\u03b1', 23:'n,n3\u03b1', 24:'z,2n\u03b1',
          25:'z,3n\u03b1', 27:'n,abs', 28:'z,np', 29:'z,n2\u03b1', 30:'z,2n2\u03b1', 32:'z,nd', 33:'z,nt', 34:'z,n3He',
          35:'z,nd2\u03b1', 36:'z,nt2\u03b1', 37:'z,4n', 38:'n,3nf', 41:'z,2np', 42:'z,3np', 44:'z,n2p', 45:'z,np\u03b1', 50:'y,n0',
          51:'z,n1', 52:'z,n2', 90:'z,n40', 91:'z,nc', 101:'n,disap', 102:'z,\u03b3', 103:'z,p', 104:'z,d', 105:'z,t',
          106:'z,3He', 107:'z,\u03b1', 108:'z,2\u03b1', 109:'z,3\u03b1', 111:'z,2p', 112:'z,p\u03b1', 113:'z,t2\u03b1',
          114:'z,d2\u03b1', 115:'z,pd', 116:'z,pt', 117:'z,d\u03b1', 151:'n,RES', 201:'z,\u03a7n', 202:'z,\u03a7\u03b3',
          203:'z,\u03a7p', 204:'z,\u03a7d', 205:'z,\u03a7t', 206:'z,\u03a73He', 207:'z,\u03a7\u03b1', 208:'z,\u03a7\u03c0+',
          209:'z,\u03a7\u03c00', 210:'z,\u03a7\u03c0-', 211:'z,\u03a7\u03bc+', 212:'z,\u03a7\u03bc-', 213:'z,\u03a7\u03ba+',
          214:'z,\u03a7\u03ba0long', 215:'z,\u03a7\u03ba0short', 216:'z,\u03a7\u03ba-', 217:'z,\u03a7antip', 218:'z,\u03a7antin', 251:'n,\u03bcL',
          252:'n,\u03be', 253:'n,\u03b6', 301:'n,total kerma', 302:'z,z0 kerma', 303:'z,nonelastic kerma', 304:'z,n kerma',
          305:'z,anything kerma', 310:'z,continuum kerma', 311:'z,2nd kerma', 316:'z,2n kerma', 317:'z,3n kerma', 318:'z,fission kerma',
          319:'n,f kerma', 320:'n,nf kerma', 321:'n,2nf kerma', 322:'z,n\u03b1 kerma', 323:'n,n3\u03b1 kerma', 324:'z,2n\u03b1 kerma',
          325:'z,3n\u03b1 kerma', 327:'n,abs kerma', 328:'z,np kerma', 329:'z,n2\u03b1 kerma', 330:'z,2n2\u03b1 kerma', 332:'z,nd kerma',
          333:'z,nt kerma', 334:'z,n3He kerma', 335:'z,nd2\u03b1 kerma', 336:'z,nt2\u03b1 kerma', 337:'z,4n kerma', 338:'n,3nf kerma',
          341:'z,2np kerma', 342:'z,3np kerma', 344:'z,n2p kerma', 345:'z,np\u03b1 kerma', 350:'y,n0 kerma', 452:'z,\u03bdT',
          454:'z,Independent fission product yield data', 455:'z,\u03bdd', 456:'z,\u03bdp', 457:'z,Radioactive decay data',
          458:'n,Energy release in fission for incident neutrons', 459:'z,Cumulative fission product yield data', 500:'Total charged-particle stopping power',
          501:'Total photon interaction', 502:'Photon coherent scattering', 504:'Photon incoherent scattering', 505:'Imaginary scattering factor',
          506:'Real scattering factor', 515:'Pair production, electron field', 516:'Pair production; electron + nuclear field',
          517:'Pair production, nuclear field', 522:'Photoelectric absorption', 523:'Photo-excitation cross section', 526:'Electro-atomic scattering',
          527:'Electro-atomic bremsstrahlung', 528:'Electro-atomic excitation cross section', 533:'Atomic relaxation data', 534:'K', 535:'L1', 536:'L2',
          537:'L3', 538:'M1', 539:'M2', 540:'M3', 541:'M4', 542:'M5', 543:'N1', 544:'N2', 545:'N3', 546:'N4', 547:'N5',
          548:'N6', 549:'N7', 550:'O1', 551:'O2', 552:'O3', 553:'O4', 554:'O5', 555:'O6', 556:'O7', 557:'O8', 558:'O9',
          559:'P1', 560:'P2', 561:'P3', 562:'P4', 563:'P5', 564:'P6', 565:'P7', 566:'P8', 567:'P9', 568:'P10', 569:'P11',
          570:'Q1', 571:'Q2', 572:'Q3', 600:'z,p0', 601:'z,p1', 602:'z,p2', 603:'z,p3', 604:'z,p4', 649:'z,pc', 650:'z,d0',
          651:'z,d1', 652:'z,d2', 699:'z,dc', 700:'z,t0', 701:'z,t1', 702:'z,t2', 749:'z,tc', 750:'n,3He0', 751:'n,3He1',
          799:'n,3Hec', 800:'z,\u03b10', 801:'z,\u03b11', 849:'z,\u03b1c', 875:'z,2n0', 876:'z,2n1', 891:'z,2nc',
          1000:'Transport cross section based on the outscatter approximation', 1001:'Transport cross section based on the inscatter approximation', 1007:'Thermal scattering matrix',
          1008:'Elastic part of thermal scattering matrix', 1018:'Fission spectrum', 1019:'First chance fission spectrum', 1020:'Second chance fission spectrum',
          1021:'Third chance fission spectrum', 1038:'Fourth chance fission spectrum', 1099:'Group integral of the weight function',
          1111:'Flux moment (P1) weighted total cross section', 1112:'Flux moment (P2) weighted total cross section', 1113:'Flux moment (P3) weighted total cross section',
          1114:'Flux moment (P4) weighted total cross section', 1115:'Flux moment (P5) weighted total cross section', 1116:'Flux moment (P6) weighted total cross section',
          1117:'Flux moment (P7) weighted total cross section', 1118:'Flux moment (P8) weighted total cross section', 1119:'Flux amount (P9) weighted total cross section',
          1452:'Product of \u03bdT times the fission cross section', 1456:'Product of \u03bdp times the fission cross section',
          1455:'Product of \u03bdd times the fission cross section', 1500:'Transport cross section based on the outscatter approximation for gamma-ray cross sections',
          1501:'Transport cross section based on the inscatter approximation for gamma-ray cross sections', 1527:'Gamma-ray energy absorption coefficient factors',
          2006:'Non-absorption collision probability', 2016:'Probability of emitting two neutrons', 2017:'Probability of emitting three neutrons', 2018:'Fission probability',
          2022:'Within-group scattering cross section', 2027:'Absorption probability', 4561:'\u03bdp for first chance fissions',
          4562:'\u03bdp for second chance fissions', 4563:'\u03bdp for third chance fissions', 4564:'\u03bdp for fourth chance fissions'}

# Elements and their atomic numbers
elements = {'H': 1, 'He': 2, 'Li': 3, 'Be': 4, 'B': 5, 'C': 6, 'N': 7, 'O': 8, 'F': 9, 'Ne': 10,
            'Na': 11, 'Mg': 12, 'Al': 13, 'Si': 14, 'P': 15, 'S': 16, 'Cl': 17, 'Ar': 18, 'K': 19, 'Ca': 20,
            'Sc': 21, 'Ti': 22, 'V': 23, 'Cr': 24, 'Mn': 25, 'Fe': 26, 'Co': 27, 'Ni': 28, 'Cu': 29, 'Zn': 30,
            'Ga': 31, 'Ge': 32, 'As': 33, 'Se': 34, 'Br': 35, 'Kr': 36, 'Rb': 37, 'Sr': 38, 'Y': 39, 'Zr': 40,
            'Nb': 41, 'Mo': 42, 'Tc': 43, 'Ru': 44, 'Rh': 45, 'Pd': 46, 'Ag': 47, 'Cd': 48, 'In': 49, 'Sn': 50,
            'Sb': 51, 'Te': 52, 'I': 53, 'Xe': 54, 'Cs': 55, 'Ba': 56, 'La': 57, 'Ce': 58, 'Pr': 59, 'Nd': 60,
            'Pm': 61, 'Sm': 62, 'Eu': 63, 'Gd': 64, 'Tb': 65, 'Dy': 66, 'Ho': 67, 'Er': 68, 'Tm': 69, 'Yb': 70,
            'Lu': 71, 'Hf': 72, 'Ta': 73, 'W': 74, 'Re': 75, 'Os': 76, 'Ir': 77, 'Pt': 78, 'Au': 79, 'Hg': 80,
            'Tl': 81, 'Pb': 82, 'Bi': 83, 'Po': 84, 'At': 85, 'Rn': 86, 'Fr': 87, 'Ra': 88, 'Ac': 89, 'Th': 90,
            'Pa': 91, 'U': 92, 'Np': 93, 'Pu': 94, 'Am': 95, 'Cm': 96, 'Bk': 97, 'Cf': 98, 'Es': 99, 'Fm': 100,
            'Md': 101, 'No': 102, 'Lr': 103, 'Rf': 104, 'Db': 105, 'Sg': 106, 'Bh': 107, 'Hs': 108, 'Mt': 109,
            'Ds': 110, 'Rg': 111, 'Cn': 112, 'Nh': 113, 'Fl': 114, 'Mc': 115, 'Lv': 116, 'Ts': 117, 'Og': 118}

# Special cases for nuclides
# I have tried to get all of them, but some may have slipped
# through the cracks.
specials = {1002: 'D', 1001001: 'H-liquid_CH4', 1013027: 'Al27bound', 1040090: 'Zr90-Zr5H8', 1040091: 'Zr91-Zr5H8',
            1040092: 'Zr92-Zr5H8', 1040093: 'Zr93-Zr5H8', 1040094: 'Zr94-Zr5H8', 1040095: 'Zr95-Zr5H8',
            1040096: 'Zr96-Zr5H8', 2001001: 'H-solid_CH4', 3004009: 'Bebound', 4001001: 'H-cryo_ortho',
            4001002: 'D-cryo_ortho', 5001001: 'H-cryo_para', 5001002: 'D-cryo_para', 5004009: 'Be-BeO',
            5008016: 'O-BeO', 6001001: 'H-benzene h', 7001001: 'H-ZrH2', 8001001: 'Hfreegas', 8001002: 'Dfreegas',
            9001001: 'H-poly', 3006000: 'graphite', 5006000: 'H-benzene c', 1014028: 'Si28bound', 1014029: 'Si29bound',
            1014030: 'Si30bound',  1026000: 'febound', 1027058: 'Co-58m', 1047110: 'Ag-110m', 1048115: 'Cd-115m',
            1052127: 'Te-127m', 1052129: 'Te-129m', 1061148: 'Pm-148m', 1067166: 'Ho-166m', 1095242: 'Am-242m',
            1095244: 'Am-244m', 1099254: 'Es-254m', 1008016: 'O-UO2', 1092235: 'U-UO2'}
