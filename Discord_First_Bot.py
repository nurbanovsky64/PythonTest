import discord

intents = discord.Intents.all()
client = discord.Client(intents = intents)

@client.event
async def on_ready():
    print("Logged in as a bot {0.user}".format(client))

@client.event
async def on_message(message):
    #print("Message from " + str(message.author) + " caught -- " + message.content)
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        print("Message sent!")
        await message.channel.send('Hello!')

token = ''
client.run(token)
