import discord
import requests
import os


# Create an instance of the Intents class
intents = discord.Intents.default()

# Enable the specific intents that bot requires
intents.members = True

# Pass the intents to the Client constructor
client = discord.Client(intents=intents, token='PRO_DEVOPS_BOT_TOKEN')

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.content.startswith('!open-devops-roles'):
        response = requests.get('https://api.example.com/devops-roles')
        if response.status_code == 200:
            data = response.json()
            role_list = '\n'.join([f"{role['title']} - {role['location']}" for role in data['roles']])
            await message.channel.send(f"Here are some open DevOps roles:\n{role_list}")
        else:
            await message.channel.send("Sorry, there was an error fetching the roles.")

client.run(os.environ['PRO_DEVOPS_BOT_TOKEN'])
