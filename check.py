all_drug = 0
good_drug = 0
all_o = 0
good_o =0
for type in dataset_dict:
    for sentence in dataset_dict[type]:
        (words,tag) = sentence
        res_tag = net.predict_for_token_batch([words])[0]
        if tag==['O']:
            all_o =all_o+1
            if res_tag==tag: good_o=good_o+1
        else:
            all_drug = all_drug+1
            if res_tag==tag: good_drug = good_drug +1


all_drug = 0
good_drug = 0
all_o = 0
good_o =0
for type in dataset_dict:
    for sentence in dataset_dict[type]:
        (words,tag) = sentence
        res_tag = net.predict_for_token_batch([words])[0]
        if tag==['O']:
            all_o =all_o+1
            if res_tag==tag: good_o=good_o+1
        else:
            all_drug = all_drug+1
            if res_tag==tag: good_drug = good_drug +1


all_drug = 0
good_drug = 0
all_o = 0
good_o =0
for sentence in dataset_dict['test']:
    (words,tag) = sentence
    res_tag = net.predict_for_token_batch([words])[0]
    if tag==['O']:
        all_o =all_o+1
        if res_tag==tag: good_o=good_o+1
    else:
        all_drug = all_drug+1
        if res_tag==tag: good_drug = good_drug +1

good_o/all_o
good_drug/all_drug


gold = ["N-pyrrolyl",
"8-(n-Decyl)protopalmatine",
"isoquinoline-1, 3-(2H, 4H)-diones",
"4-(2,5-Dimethylpyrrol-1-yl)piperidine",
"4-aminopiperidine",
"tert-Butyl 4-(2,5-dimethyl-1H-pyrrol-1-yl)piperidine-1-carboxylate",
"tricyclic phthalimide",
"8-(n-Decyl)pseudoprotoberberine chloride",
"gallate",
"pyrrolones",
"8-(p-Methyl)phenylprotopalmatine choride",
"amide",
"DMF",
"carbonyl",
"Difluorophosgene",
"acetone",
"1-benzylpiperidine",
"Perfluoroheptanoyl fluoride",
"8-(p-Methoxy)phenylprotopalmatine choride",
"acetonitrile",
"8-(n-Decyl)protopalmatine chloride",
"(E)-5-Benzyl-2-((2,5-dimethyl-1-(2-(trifluoromethyl)phenyl)-1H-pyrrol-3-yl)methylene)-1H-pyrrolo[3,2-c]pyridine-3,4(2H, 5H)dione",
"hydroxyl",
"4-[(3-hydroxybenzylamino)-methylene]-4H-isoquinoline-1,3-diones",
"5H)dione",
"3,4-dichlorophenyl",
"glycerol monolaurate",
"pyrrolo [3,2-c] pyridine-3, 4-dione",
"dihydropseudoberberine",
"dihydroberberine",
"(E)-Ethyl 5-((1-(1-benzylpiperidin-4-yl)-2,5-dimethyl-1H-pyrrol-3-yl)methylene)-2-methyl-4-oxo-4,5-dihydro-1H-pyrrole-3-carboxylate",
"Sepharose",
"Fcontrol",
"N,N-dimethylformamide",
"4-fluorobenzyl",
"aminomethyl",
"8-(1-Naphthyl)protoberberine choride",
"8-(p-Methyl)phenylpseudoprotoberberine choride",
"indinavir",
"piperidinyl",
"3-furyl",
"pyrrolo[3,2-c]",
"-NHAc",
"amine",
"amino",
"prodelphinidin A2-3′-O-gallate",
"diethyl acetal",
"pyrazine",
"protomol",
"pyrrolone",
"phthalimide",
"methanol",
"1-benzyl-4-(2,5-dimethyl-1H-pyrrol-1-yl)piperidine",
"1-Benzyl-4-(2,5-dimethyl-1H-pyrrol-1-yl)piperidine",
"ester",
"4-(2,5-dimethyl-1H-pyrrol-1-yl)piperidine",
"1-piperidinylmethyl",
"1-naphthyl",
"8-(m-Chloro)phenylpseudoprotoberberine",
"elvitegravir",
"isoquinoline-1,3-diones",
"iso-propanol",
"2-furyl",
"acetic acid",
"4-oxo-4,5-dihydro-1H-pyrrole-3-carboxylate",
"bromate",
"phenyl",
"4-methylumbelliferyl (4-MU) oleate",
"difluorophosgene",
"imino",
"GML",
"Sephacryl S-300",
")-4-oxo-4,5-dihydro-1H-pyrrole-3-carboxylate",
"3-furyl, N-pyrrolyl",
"PFCAs",
"tetrazolium 3-(4,5-dimethylthiazol-2-yl)-2,5-diphenyltetrazolium bromide",
"8-(n-Dodecyl)pseudoprotoberberine chloride",
"8-(1-Naphthyl)protopalmatine choride",
"perfluorohexyl",
"pyrimethamine",
"perfluorooctanoic acid",
"cyclohexane",
"methoxyl",
"Trifluoroacetic Acid",
"piperazinyl",
"pseudoberberine",
"kcals",
"polyphenolic compounds",
"(2R,3R,2′R,3′R)-desgalloyloolongtheanin-3,3′-O-digallate",
"palmatine",
"acetal",
"isoxazole",
"2,5-dimethyl-1-(1-substituted-piperidine)-1H-pyrrole",
"sulfonamide",
"Phenyl Sepharose",
"Perfluorooctanoic Acid",
"Perfluorinated carboxylic acids (PFCAs)",
"RIF",
"8-(n-Dodecyl)pseudoprotoberberine",
"dihydropalmatine",
"polyphenols",
"8-(p-Chloro)phenylpseudoprotoberberine chloride",
"carboxylic acids",
"ethanol",
"1-(1-Benzylpiperidin-4-yl)-2,5-dimethyl-1H-pyrrole-3-carbaldehyde",
"carboxylic acid",
"aa–aj)",
"tert-butyloxycarbonyl",
"surfactants",
"Pyrrolone",
"morpholinyl",
"carbonyl-hydroxy-aromatic nitrogen",
"PFCA",
"propyl-2-",
"4-methylumbelliferone",
"galloyl",
"3-formylpyrrole 4-aminopiperidine (7, 16 a–z, 16 aa–aj)",
"8-n-decylberberines",
"2,5-hexandione",
"benzoyl",
"2,5-Hexandione",
"trifluoroacetic acid",
"4-pyridyl",
"perfluorinated carboxylic acids",
"perfluorinated",
"N,N-dimethylformamido-",
"8-(m-Methoxy)phenylprotopalmatine choride",
"8-(p-Methoxy)phenylprotoberberine choride",
"8-(1-Naphthyl)pseudoprotoberberine choride",
"piperidine",
"berberine",
"8-(p-Methoxy)phenylpseudoprotoberberine choride",
"perfluorinated acid",
"PFOA",
"(E)-Ethyl 5-((2,5-dimethyl-1-(2-(trifluoromethyl)phenyl)-1H-pyrrol-3-yl)methylene)-2-((E)-2-(dimethylamino)vinyl)-4-oxo-4,5-dihydro-1H-pyrrole-3-carboxylate",
"8-(n-Decyl)pseudoprotoberberine",
"8-(p-Chloro)phenylpseudoprotoberberine",
"polyphenol",
"pyrogallol",
"tetramethylsilane",
"tetrazolium 3-(4,5-dimethylthiazol-2-yl)-2,5-diphenyltetrazolium",
"/dichloromethane",
"isoquinoline-1,3-(2H,4H)-dione",
"4-quinazolinone",
"dimethylamine",
"5H-pyrido[4,3-b]indol-4-carboxamide",
"isoniazid",
"dichloromethane",
"phthalimides",
"4-methylpiperazinyl, -CH2-(1-piperidinyl)",
"8-(n-Decyl)protoberberine chloride",
"DOTD",
"3-Formylpyrrole",
"isoquinoline-1, 3-(2H, 4H)-dione",
"8-(m-Methoxy)phenylprotoberberine choride",
"polyphenol oxidase",
"para-toluenesulfonic acid",
"m-methoxyphenyl",
"5-O-gallate",
"4-carboxamide",
"3-thienyl",
"Isoquinolin-1,3-Dione",
"p-methoxyphenyl",
"pseudoprotoberberine",
"oleate",
"-NH",
"4-dione",
"(E)-ethyl 5-((1-substituted-piperidin-4-yl)-2,5-dimethyl-1H-pyrrol-3-yl)methylene)-2-methyl-4-oxo-4,5-dihydro-1H-pyrrole-3-carboxylates",
"isoquinoline- 1, 3-(2H,4H)-dione",
"pyridone",
"rifampin",
"p-methylphenyl",
"efavirenz",
"perfluoroheptyl",
"chloroquine",
"phenol",
"n-decyl",
"3-pyridyl",
"3” hydroxyl",
"ethyl piperidine-1-",
"PFHA",
"raltegravir",
"perfluoroheptanoic acid",
"4-amino-1-benzylpiperidine",
"2,5-dimethyl-1-(1-substituted-piperidine)-3-formylpyrroles",
"2,5-dimethyl-1-(1-substituted-piperidine)-3-formylpyrrole",
"monoglycerides",
"5H-Pyrido[4,3-b]indol-4-carboxamide",
"isoquinolinedione",
"carboxyl",
"Bedaquiline",
"diethyl aceta",
"8-(n-Decyl)protoberberine",
"8-(m-Methoxy)phenylpseudoprotoberberine choride",
"benzyl",
"8-(m-Chloro)phenylpseudoprotoberberine chloride",
"benzopyrone",
"4H)-diones",
"HOAc",
"methylpyrazole",
"2,5-dimethyl-1-aryl/substituted-aryl-3-formylpyrrole",
"protoberberine",
"10,11-dimethoxy",
"prodelphinidin",
"pesudoberberine",
"8-(p-Methyl)phenylprotoberberine choride"]

for e in gold:
    tokens = tokenize(e.lower())
    tags = net.predict_for_token_batch([tokens])[0]
    for token, tag in zip(tokens, tags):
        print(token, tag)