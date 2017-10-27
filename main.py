from flask import Flask
import NLTK_exp as nE
from flask import request
import urllib
import json
import createDict as cD

app = Flask(__name__)

@app.route('/getAllEvents',methods=['GET'])
def getAllEvents():
    url = " https://api.rss2json.com/v1/api.json?rss_url=http%3A%2F%2Fwww.gdacs.org%2FXML%2FRSS.xml"
    response = urllib.urlopen(url)
    text = json.loads(response.read())
    res =  nE.main(text)
    return res

@app.route('/getEvents',methods=['POST'])
def getEvents():
    res =  nE.main(request.json)
    return res

@app.route('/updatePlace',methods=['POST'])
def updatePlace():
    res = cD.updDict(request.json, 'Place')
    return res

@app.route('/updateHazard',methods=['POST'])
def updateHazard():
    res = cD.updDict(request.json, 'Hazard')
    return res

if __name__ == '__main__':
    app.run()
