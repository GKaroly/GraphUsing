#!/usr/bin/python


import facebook
import requests
import json

#Python 3.6.5 Source: https://www.python.org/downloads/
#Should install pip too
#add to environment (You can add automatically during install with a checkbox)

#After install python 3.6.5, install facebook-sdk
#pip install facebook-sdk


print("Hello")

#Based on this:
#https://stackoverflow.com/questions/11510850/python-facebook-api-need-a-working-example
token = 'Token value comes here'


#graph = facebook.GraphAPI(access_token=token, version="2.7")
#profile = graph.get_object("me")
#friends = graph.get_connections("me", "friends")
#friend_list = [friend['name'] for friend in friends['data']]


#Source:
#https://www.geeksforgeeks.org/get-post-requests-using-python/

BasicURL="https://graph.facebook.com/"
API_VERSION="v2.12/"
RequestParameters="me?fields=id,name,birthday,context"

URL=BasicURL+API_VERSION+RequestParameters
PARAMS={'access_token': token}
r = requests.get(url=URL, params=PARAMS)


print(r.json())
print(json.dumps(r.json(), indent=4, sort_keys=True))

#data = r.json()
#parsed_data = json.loads(data, indent=4, sort_keys=True)
#dumped_data=json.dumps(parsed_data, indent=4, sort_keys=True)
#print(dumped_data) 








