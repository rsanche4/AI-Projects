import markovify
import discord
import random
import aiml
import os
from googlesearch import search
import wikipedia
from datetime import date, datetime

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

POST_RATE = 7 # frequency at which it should post messages, the larger the number the less likely to randomly post a message
tokenfile = open("C:\\Users\\rafas\\Documents\\chrixxytoken\\token.txt", "r")
TOKEN = tokenfile.read()

BEGINNINGS = ["yeah", "umm...", "i mean", "like", "uwu", "lol", "hey", "yeah so", ". . .", "uh", "yo", "bro", "idk"]
ENDINGS = [":)", ":-)", "lol", ". . .", ";)", "(>.<)", ">_<", "hehe", "hahaha", "haha", "lmao", "yeah?", "omg", "tho", "uwu", "yo", "bro"]
WEBSEARCH_MESSAGE = ["found this :-)", "looked it up", "here ya go", "yessir", "found all this", "well, here is what i got", "maybe this will help", "looking for this?", "there ya go"]
WITH_FREQ = 1
NUM_OF_SEARCHURLS = 5

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
        await message.channel.send('I am the egirl bot. You can chat with me privately to get a more personal chat, \nbut I can also comment randomly on group chats, \nsearch things on the internet using the "search" command (ex "search tiktok egirl") in which case I will provide urls to pages I found related to the search. Look into google advanced searches for better results! \nand finally I can also provide a definition of phrases and words using wikipedia (ex: define love) \nYou can also say "roll dice" to get a random number from 1 to 6, \nand you can ask for the time by including the word "time" in your message \nYou can choose to play a game called Blackjack Dice, in which I roll a 12 sided dice for you as often as possible until reaching a number higher than 16. Then I roll my dice and do the same, and if I get closer to 21 than you did, I win! Say, "blackjack dice" to start or just type "bd". \nlov u xoxo')

    # roll dice
    elif message.content.lower().startswith("roll dice"):
        await message.channel.send(str(message.author) + " got: " + str(random.randint(1, 6)))

    # tell the time
    elif "time" in message.content.lower():
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        await message.channel.send("The time is " + current_time)

    # the game blackjack dice
    elif "blackjack dice" in message.content.lower() or "bd"==message.content.lower():
        current_number = 0
        chrixxy_number = 0
        while current_number<16:
            current_number += random.randint(1, 12)
        if current_number>21:
            await message.channel.send("You went over 21 by scoring " + str(current_number) + ". You lost!")
        else:
            await message.channel.send("You scored: "+ str(current_number) + "\nThrowing my dice now...")
            while chrixxy_number<16:
                chrixxy_number += random.randint(1, 12)
            if chrixxy_number>21:
                await message.channel.send("I went over 21 by scoring " + str(chrixxy_number) + ". You won!")
            else:
                if chrixxy_number>current_number:
                    await message.channel.send("I am closer to 21 because I scored " + str(chrixxy_number) + ", I won!")
                elif chrixxy_number<current_number:
                    await message.channel.send("You are closer to 21, because I scored " + str(chrixxy_number) + ", you won!")
                else:
                    await message.channel.send("We have the same numer " + str(current_number) + "! Draw!!")



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