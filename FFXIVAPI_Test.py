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

#Retrieve a list of members from the FC, from the Lodestone
request = urllib2.Request("https://xivapi.com/freecompany/" + fcID + "?data=FCM")
request.add_header('User-Agent', '&lt;User-Agent&gt;')
FCMembers = json.loads(urllib2.urlopen(request).read())['FreeCompanyMembers']

#print(json.dumps(data, indent=2))

#Set up a Dataframe to hold players
playerList = pd.DataFrame(columns = ['ID', 'Name', 'Nameday', 'Diety', 'Race', 'Gender', 'FC', 'AvatarImg', 'Server'])

#For all FC Members...
for x in range(len(FCMembers)):
    #Get their character ID
    playerID = data['FreeCompanyMembers'][x]['ID']

    #Retrieve their Lodedstone Data
    request = urllib2.Request("https://xivapi.com/character/" + str(playerID))
    request.add_header('User-Agent', '&lt;User-Agent&gt;')
    playerData = json.loads(urllib2.urlopen(request).read())
    #print(json.dumps(playerData, indent=2))

    #Extract desired information
    playerName = playerData['Character']['Name']
    playerNameday = playerData['Character']['Nameday']
    playerDiety = playerData['Character']['GuardianDeity']
    playerRace = playerData['Character']['Race']
    playerGender = playerData['Character']['Gender']
    playerFC = playerData['Character']['FreeCompanyName']
    playerImg = playerData['Character']['Portrait']
    playerServer = playerData['Character']['Server']

    #Create a new row of data with that information
    newRow = pd.DataFrame({'ID':playerID, 'Name':playerName, 'Nameday':playerNameday, 'Diety':playerDiety, 'Race':playerRace, 'Gender':playerGender, 'FC':playerFC, 'AvatarImg':playerImg, 'Server':playerServer}, index = [0])

    #Add this row to the main player list
    playerList = pd.concat([playerList, newRow], ignore_index = True)
    
    print(playerName + ' added')

pd.options.display.max_colwidth = 200
print(playerList)
