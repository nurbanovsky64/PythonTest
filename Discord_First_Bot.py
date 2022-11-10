import discord
import requests
import json
import random

#Client setup
intents = discord.Intents.all()
client = discord.Client(intents = intents)

#Word bank setup
sad_words = ["sad", "depressed", "unhappy", "angry", "miserable"]
starter_encouragements = ["Cheer up!","Hang in there.","You are a great person / bot!"]

#Retrieves an inspirational message from zenquotes and formats it for further use
def get_quote():
    response = json.loads(requests.get("https://zenquotes.io/api/random").text)
    quote = response[0]['q'] + " - " + response[0]['a']
    return quote

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
        await message.channel.send(random.choice(starter_encouragements))


token = ''
client.run(token)
