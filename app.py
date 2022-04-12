#kabugo daniel 1900716476
#khalifan muwonge 1900700558
#Nuwagaba Raymond - 1900717708
#Kiberu Nuhu 1900700119



import os
from urllib import response
from flask import Flask, request
import urllib.request, json
import http.client
from flask_cors import CORS, cross_origin


app = Flask(__name__)
# for cross origin access
CORS(app)
NEWS_KEY = os.getenv("NEWS_API_KEY")
WEATHER_KEY = os.getenv("WEATHER_API_KEY")

@app.route('/')
def welcome_route():
    return 'This is the update app API by group 7'

@app.route('/local')
def local_route():
    return 'get local news'

@app.route('/global')
def global_route():
    conn = http.client.HTTPSConnection("bing-news-search1.p.rapidapi.com")
    headers = {
        "Accept-Language": "en",
	    "X-BingApis-SDK": "true",
	    "X-RapidAPI-Host": "bing-news-search1.p.rapidapi.com",
	    "X-RapidAPI-Key": NEWS_KEY
    }
    conn.request("GET", "/news?safeSearch=Off&textFormat=Raw", headers=headers)
    response = conn.getresponse()
    if not response.status == 200:
        return dict(status='failed', message='Api is down'), 501
    data = response.read()
    dict1 = json.loads(data)
    if not dict1:
        return dict(status='failed', message='No data'), 402
    return dict(status='sucess', data=dict1 ), 201

@app.route('/weather', methods=["POST"])
def testpost():
     input_json = request.get_json(force=True) 
     link ="https://api.openweathermap.org/data/2.5/onecall?lat="+str(input_json['lat'])+"&lon="+str(input_json['lon'])+"&appid="+WEATHER_KEY
    # dictToReturn = {'text':input_json['text']}
     response = urllib.request.urlopen(link)
     if not response.status == 200:
        return dict(status='failed', message='Api is down'), 501
     data = response.read()
     dict1 = json.loads(data)
     if not dict1:
        return dict(status='failed'), 402
     return dict(status='sucess', data=dict1 ), 200

if __name__ == '__main__':
	app.run(debug=True)
