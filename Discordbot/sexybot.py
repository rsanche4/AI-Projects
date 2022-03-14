import markovify
import discord
import random

# A discord bot that uses markov chains to generate new text.
# It is mainly a naughty bot! ;)
# In order to be triggered, the message should contain 'sex' in it.

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

    if 'sex' in message.content or 'Sex' in message.content or 'SEx' in message.content or 'SEX' in message.content or 'SeX' in message.content or 'seX' in message.content or 'sEx' in message.content or 'sEX' in message.content:
        text_model = markovify.Text(text)
        msg = text_model.make_short_sentence(random.randint(100, 300))
        await message.channel.send(msg)

client.run(TOKEN)