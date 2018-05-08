import requests
import json
# This is a program to gather a listing of albums by searching any musical artist that your heart desires.
# Using Discogs.com API

# Ask user for input, can search any musical artist
# Input can be upper or lower case and may contain spaces
artistID = input("Please enter an artist name to begin. ")

# Put user input in API search url
s = requests.get('https://api.discogs.com/database/search?q=%s&page=1&per_page=50&token=VvtqOZJpiKSGksrmMkAOaBAyobjzteweYygWpmNn' % artistID)

# Check status and convert to JSON
if int(s.status_code == 200):
    apiDict = json.loads(s.text)
    # From JSON, pull artist ID number to be used for album listing
    idnum = apiDict['results'][0]['id']
    # Put artist ID number in API artist release url
    a = requests.get('https://api.discogs.com/artists/%d/releases' % idnum)

    # Check status and convert to JSON
    if int(s.status_code == 200):
        albumDict = json.loads(a.text)
        # From JSON, parse releases dictionary
        albumInfo = albumDict['releases']
        # From albumDict, show first 50 results, title of album only
        for i in albumInfo[0:50]:
            print(i['title'])

