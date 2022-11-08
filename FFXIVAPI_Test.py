import urllib.request as urllib2
import urllib.error
import urllib.parse
import json
import pandas as pd

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

#Set up a Dataframe to hold players
playerList = pd.DataFrame(columns = ['Name', 'Server', 'ID'])

#Access all members of the FC
for x in range(len(data['FreeCompanyMembers'])):

    playerName = data['FreeCompanyMembers'][x]['Name']
    playerServer = data['FreeCompanyMembers'][x]['Server']
    playerID = data['FreeCompanyMembers'][x]['ID']

    newRow = pd.DataFrame({'Name': playerName, 'Server': playerServer, 'ID': playerID}, index = [0])

    playerList = pd.concat([playerList, newRow], ignore_index = True)
    print(playerName + ' added')

    #Retrieve information for the member
    request = urllib2.Request("https://xivapi.com/character/" + str(playerID))
    request.add_header('User-Agent', '&lt;User-Agent&gt;')
    playerData = json.loads(urllib2.urlopen(request).read())
    print(json.dumps(playerData, indent=2))

print(playerList)