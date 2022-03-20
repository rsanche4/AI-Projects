import markovify
import discord
import random

# A discord bot that uses markov chains to generate new text.

TOKEN = ''

with open("corpus.txt", encoding="utf-8") as f:
    text = f.read()

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if 'bot' in message.content:
        text_model = markovify.Text(text)
        msg = text_model.make_short_sentence(random.randint(100, 200))
        await message.channel.send(msg)

client.run(TOKEN)