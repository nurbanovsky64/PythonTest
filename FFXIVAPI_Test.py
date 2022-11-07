import urllib.request as urllib2
import urllib.error
import urllib.parse
import json

#Search for an FC by name/server
request = urllib2.Request("https://xivapi.com/freecompany/search?name=Frog+Squad&server=Goblin")
request.add_header('User-Agent', '&lt;User-Agent&gt;')
data = json.loads(urllib2.urlopen(request).read())
fcID = data['Results'][0]['ID']

#print(data)
print("Free Company ID: " + fcID + "\n")

#Retrieve FC Information
request = urllib2.Request("https://xivapi.com/freecompany/" + fcID + "?data=FCM")
request.add_header('User-Agent', '&lt;User-Agent&gt;')
data = json.loads(urllib2.urlopen(request).read())

#print(json.dumps(data, indent=2))

playerName = data['FreeCompanyMembers'][0]['Name']
playerServer = data['FreeCompanyMembers'][0]['Server']
playerID = data['FreeCompanyMembers'][0]['ID']

print("First Member is " + playerName + " from " + playerServer)

#Retrieve information for the first member on the list
request = urllib2.Request("https://xivapi.com/character/" + str(playerID))
request.add_header('User-Agent', '&lt;User-Agent&gt;')
data = json.loads(urllib2.urlopen(request).read())

print(json.dumps(data, indent=2))