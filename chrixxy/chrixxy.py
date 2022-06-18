import markovify
import discord
import random
import aiml
import os

# A discord bot that uses markov chains to generate new text.
# It is mainly a naughty bot! ;)
# In order to be triggered, the message should contain 'sex' in it.

BRAIN_FILE="brain.dump"

k = aiml.Kernel()

if os.path.exists(BRAIN_FILE):
    print("Loading from brain file: " + BRAIN_FILE)
    k.loadBrain(BRAIN_FILE)
else:
    print("Parsing aiml files")
    k.bootstrap(learnFiles="std-startup.aiml", commands="load aiml b")
    print("Saving brain file: " + BRAIN_FILE)
    k.saveBrain(BRAIN_FILE)

POST_RATE = 10 # frequency at which it should post messages, the larger the number the less likely to randomly post a message
TOKEN = 'OTg3NjA0MDM2ODQ3MDIyMTAw.G4dkhe.0HGnUKqQBo7dMKzSaImMwk4-SO708xgqUw1684'

ENDINGS = [":)", ":-)", "lol", ". . .", ";)", "(>.<)", ">_<", "hehehe", "hehe", "heeheehee", "heehee", "hahaha", "haha", "lmao", "lmaoo", "lmaooo", "yeah?", "also, ily", "omg"]
WITH_ENDING_FREQ = 1

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
    
    if message.guild and random.randint(0, POST_RATE)==0:
        text_model = markovify.Text(text)
        msg = text_model.make_short_sentence(random.randint(40, 50))
        msg = msg.replace(".", "")
        if random.randint(0, WITH_ENDING_FREQ)==0:
            msg = msg + " " + random.choice(ENDINGS)
        await message.channel.send(msg.lower())

    if not message.guild:
        input_text = message.content.replace("@chrixxy", "")
        input_text = message.content.replace("chrixxy", "")
        response = k.respond(input_text)
        if random.randint(0, WITH_ENDING_FREQ)==0:
            response = response + " " + random.choice(ENDINGS)
        await message.channel.send(response.lower())

client.run(TOKEN)