import json
#import re
from nltk.corpus import stopwords
import pickle
import nltk
#import AzureStore as aSt


with open("NPlaceCorpus.db", "rb") as myFile:
    placeDict = (pickle.load(myFile))
  
with open("NHazardCorpus.db", "rb") as myFile:
    hazardDict = (pickle.load(myFile))
    
#regex_str = [
    #r'<[^>]+>', # HTML tags
    #r'(?:@[\w_]+)', # @-mentions
    #r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)", # hash-tags
    #r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', # URLs
    #r'\d{1,2}[-/]\d{1,2}[-/]\d{4}', #Dates
    #r'(?:(?:\d+,?)+(?:\.?\d+)?)', # numbers
    #r"(?:[a-z][a-z'\-_]+[a-z])", # words with - and '
    #r'(?:[\w_]+)', # other words
    #r'(?:\S)',
    #'\\//'# anything else
#]
    
#tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE)

#def tokenize(s):
    #return tokens_re.findall(s)

def getHazard(s):
    tokens = [];
    for hValue in hazardDict:
        if(s.__contains__(hValue['dictVal'].lower())):
            tokens.append(hValue['dictVal'].lower())
        else:
            synList = hValue['synsets']
            for i in synList:
                if(s.__contains__(i)):
                    tokens.append(hValue['dictVal'].lower())
                    break
    return set(tokens)

def getPlace(s):
    tokens = [];
    for hValue in placeDict:
        if(s.__contains__(hValue['dictVal'].lower())):
            tokens.append(hValue['dictVal'].lower())
        else:
            synList = hValue['synsets']
            for i in synList:
                if(s.__contains__(i)):
                    tokens.append(i.lower())
                    break
    return set(tokens)
    
def preprocess(s, lowercase=True):
    #tokens = tokenize(s)
    tokens = nltk.word_tokenize(s)
    stop_words = set(stopwords.words('english'))
    stop_words.update(['.', ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{', '}', '\'' , '\"' , '\'\'' , '\\\\', '\\']) # remove it if you need punctuation 
    tokens = [w for w in tokens if not w in stop_words]
    #newS = " ".join(tokens)
    return tokens

def set_default(obj):
    if isinstance(obj, set):
        return list(obj)
    raise TypeError

def createEvent(newsTokenizedData, fLink):
        j = []
        hazardSet = getHazard(" ".join(newsTokenizedData).lower())
        locationSet = getPlace(" ".join(newsTokenizedData).lower())
        
        for h in hazardSet:
            newsTokenizedData.append(h)
        
        for p in locationSet:
            newsTokenizedData.append(p)
        
        for hVal in hazardSet:
            ndat = {
                'place':json.dumps(locationSet, default=set_default),
                'hazard':hVal,
                'feedLink':fLink,
                'feedSummary':json.dumps(newsTokenizedData)
                }
            j.append(ndat)
            print ndat["hazard"]
            #aSt.sendToQueue(json.dumps(ndat, default=set_default),ndat["hazard"].lower())
        
        return json.dumps(j)
    
def main(text):
    token = preprocess(text["FeedSummary"].lower())
    return createEvent(token, text["FeedLink"])
