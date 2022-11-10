import discord
import requests
import json
import random

#Client setup
intents = discord.Intents.all()
client = discord.Client(intents = intents)

#Word bank setup
sad_words = ["sad", "depressed", "unhappy", "angry", "miserable"]
encouragements = ["Cheer up!","Hang in there.","You are a great person / bot!"]
encouraging = [True]


#Retrieves an inspirational message from zenquotes and formats it for further use
def get_quote():
    response = json.loads(requests.get("https://zenquotes.io/api/random").text)
    quote = response[0]['q'] + " - " + response[0]['a']
    return quote

#Add a message to the list of encouragements
def update_encouragements(msg):
    encouragements.append(msg)

#Remove a message from the list of encouragements
def delete_encouragement(index):
    if len(encouragements) > index:
        del encouragements[index]

#Bot logon
@client.event
async def on_ready():
    print("Logged in as a bot {0.user}".format(client))

#When a message is sent in the channel
@client.event
async def on_message(message):
    #Avoid recursion by ignoring self-written messages
    if message.author == client.user:
        return

    msg = message.content

    #Send a quick hello message to the channel
    if msg.startswith('$hello'):
        await message.channel.send("Howdy!")

    #Send an inspiring quote (zenquotes) to the channel
    if msg.startswith('$inspire'):
        await message.channel.send(get_quote())

    #If any message found has a sad word, send an encouragement to the channel
    if any(word in msg for word in sad_words):
        if encouraging[0]:
            await message.channel.send(random.choice(encouragements))

    #Add an encouraging message to the list
    if msg.startswith('$new'):
        encouraging_msg = msg.split("$new ", 1)[1]
        update_encouragements(encouraging_msg)
        await message.channel.send("New Encouragement Added!")

    #Remove an encouraging message from the list
    if msg.startswith('$del'):
        index = int(msg.split("$del ", 1)[1])
        delete_encouragement(index)
        await message.channel.send(encouragements)

    #Send the current list to the chat
    if msg.startswith('$list'):
        await message.channel.send(encouragements)
    
    #Configure if the bot should be sending encouraging messages or not
    if msg.startswith('$responding'):
        value = msg.split("$responding ", 1)[1]
        if value.lower() == 'true':
            encouraging[0] = True
            await message.channel.send("Encouragement is on!")
        else:
            encouraging[0] = False
            await message.channel.send("Encouragement is off!")

token = ''
client.run(token)
