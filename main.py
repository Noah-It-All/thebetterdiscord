import discord
import os
from os import environ
import requests

token = environ['THETOKEN']
covidapi = environ['THETOKEN2']

url = "https://covid-19-data.p.rapidapi.com/totals"

headers = {
    'x-rapidapi-key': covidapi,
    'x-rapidapi-host': "covid-19-data.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers)

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('bruh'):
        await message.channel.send('bruh urself ugly fatty')

async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$covid'):
        await message.channel.send(response.text[3:-3])

client.run(token)
