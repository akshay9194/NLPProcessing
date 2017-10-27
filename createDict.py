import pickle
from nltk.corpus import wordnet as wn
import os.path as FPath

def set_default(obj):
    if isinstance(obj, set):
        return list(obj)
    raise TypeError
    
def updDict(myMadeUpDictionary, DictTy):
    listData = []
    placeDict = set()
    hazardDict = set()
    
    for rSt in myMadeUpDictionary:
        ruleSet = set()
        for synset in wn.synsets(rSt['dictVal'].lower()):
            for lemma in synset.lemmas():
                ruleSet.add(lemma.name().replace('_',' ').lower())
        ndata = {
                    'dictVal':rSt['dictVal'].lower(),
                    'synsets':list(ruleSet)
                }
        listData.append(ndata)
               
    if DictTy == 'Place':
        
        if (FPath.isfile("NPlaceCorpus.db")):
            with open("NPlaceCorpus.db", "rb") as myFile:
                placeDict = (pickle.load(myFile))
                
        for hValue in placeDict:
             ndata =   {
                         'dictVal':hValue['dictVal'].lower(),
                         'synsets':hValue['synsets']
                        }
             listData.append(ndata)
        
        with open("NPlaceCorpus.db", "wb") as myFile:
            pickle.dump(listData, myFile) 
        
    if DictTy == 'Hazard':
        
        if (FPath.isfile("NHazardCorpus.db")):
            with open("NHazardCorpus.db", "rb") as myFile:
                hazardDict = (pickle.load(myFile))
                
        for hValue in hazardDict:
             ndata =   {
                         'dictVal':hValue['dictVal'].lower(),
                         'synsets':hValue['synsets']
                        }
             listData.append(ndata)
           
        with open("NHazardCorpus.db", "wb") as myFile:
            pickle.dump(listData, myFile) 
                        
    return 'Created'
