import requests
import json


r = requests.get('https://api.discogs.com/artists/57916/releases')
if int(r.status_code == 200):
    apiDict = json.loads(r.text)
    artistList = apiDict
    for i in artistList['releases']:
        print(i['title'])

