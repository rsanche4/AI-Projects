from lib2to3.pgen2 import token
import markovify
import discord
import random
import aiml
import os
from googlesearch import search
import wikipedia

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
tokenfile = open("C:\\Users\\rafas\\Documents\\chrixxytoken\\token.txt", "r")
TOKEN = tokenfile.read()

BEGINNINGS = ["yeah", "umm...", "i mean", "like", "uwu", "lol", "hey", "yeah so", ". . .", "uh", "yo", "bro", "idk"]
ENDINGS = [":)", ":-)", "lol", ". . .", ";)", "(>.<)", ">_<", "hehe", "hahaha", "haha", "lmao", "yeah?", "omg", "tho", "uwu", "yo", "bro"]
WEBSEARCH_MESSAGE = ["found this :-)", "looked it up", "here ya go", "yessir", "found all this", "well, here is what i got", "maybe this will help", "looking for this?", "there ya go"]
WITH_FREQ = 1
NUM_OF_SEARCHURLS = 10

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
    
    # Group Comments
    if message.guild and random.randint(0, POST_RATE)==0:
        text_model = markovify.Text(text)
        msg = text_model.make_short_sentence(random.randint(40, 50))
        msg = msg.replace(".", "")
        if random.randint(0, WITH_FREQ)==0:
            msg = msg + " " + random.choice(ENDINGS)
        if random.randint(0, WITH_FREQ)==0:
            msg = random.choice(BEGINNINGS) + " " + msg 
        await message.channel.send(msg.lower())

    # search on the web functionality.
    if message.content.lower().startswith("search "):
        await message.channel.send(random.choice(WEBSEARCH_MESSAGE))
        for url in search(message.content[7:], stop=NUM_OF_SEARCHURLS):
            await message.channel.send(url + "\n")

    # extract definitions
    elif message.content.lower().startswith("what is ") or message.content.lower().startswith("define "):
        await message.channel.send(wikipedia.summary(message.content[8:])[:1990])

    # help
    elif message.content.lower().startswith("plzhelp"):
        await message.channel.send('I am the egirl bot. You can chat with me privately to get a more personal chat, \nbut I can also comment randomly on group chats, \nsearch things on the internet using the "search" command (ex "search tiktok egirl") in which case I will provide urls to pages I found related to the search. Look into google advanced searches for better results! \n and finally I can also provide a definition of phrases and words using wikipedia (ex: define love) \n lov u xoxo')

    # Conversation Functionality
    elif not message.guild:
        input_text = message.content.replace("@chrixxy", "")
        input_text = message.content.replace("chrixxy", "")
        response = k.respond(input_text)
        if random.randint(0, WITH_FREQ)==0:
            response = response + " " + random.choice(ENDINGS)
        if random.randint(0, WITH_FREQ)==0:
            response = random.choice(BEGINNINGS) + " " + response
        await message.channel.send(response.lower())
        # conversation logs. Uncomment to save all conversations
        # file = open("logs.txt", "a")  # append mode
        # file.write(str(message.author) + ": " + str(message.content) + "\n")
        # file.write("chrixxy: " + str(response.lower()) + "\n")
        # file.close()    

    

    if message.content=="XXSHUTDOWNXX":
        exit()

client.run(TOKEN)