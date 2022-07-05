from tokenize import Double
import discord
from discord.ext import commands
import random
import aiml
import os
from googlesearch import search
import wikipedia
from datetime import date, datetime
import imdb

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

tokenfile = open(os.path.expanduser("~\\Documents\\evatoken\\token.txt"), "r")
TOKEN = tokenfile.read()

WEBSEARCH_MESSAGE = ["THIS IS WHAT I FOUND:", "MAYBE THIS WILL HELP:", "HERE ARE THE RESULTS:"]
NUM_OF_SEARCHURLS = 5

#client = discord.Client()
bot = commands.Bot(command_prefix='eva ')

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # search on the web functionality giving back top 5 urls.
    if message.content.lower().startswith("eva search "):
        await message.channel.send(random.choice(WEBSEARCH_MESSAGE))
        for url in search(message.content[10:], stop=NUM_OF_SEARCHURLS):
            await message.channel.send(url + "\n")

    # find people on imdb
    elif message.content.lower().startswith("eva who is "):
        await message.channel.send(wikipedia.summary(message.content[10:])[:1000].upper().upper())

    # send this and that to other people
    elif message.content.lower().startswith("eva send "):
        # turn message content into a list by spaces, then get the "eva send [dsa] a hug"
        cmd = message.content.split(' ')
        await message.channel.send(str(message.author).upper() + " SENDS " + str(cmd[2]).upper() + " " + str(' '.join(cmd[3:])).upper() + "!" )

    # extract definitions
    elif message.content.lower().startswith("eva define "):
        await message.channel.send(wikipedia.summary(message.content[10:])[:1000].upper())

    # help
    elif message.content.lower().startswith("eva help"):
        await message.channel.send('I AM EVA, THE DISCORD ASSISTANT BOT. \nUsage: \neva help => Shows this message. \neva search <query> => Returns top 5 urls on google that answer the query. \neva send <NAME> <THINGS TO SEND> => Displays a message from the bot sending NAME a THING TO SEND. For example: Send Lisa a hug returns User sends Lisa a hug! \neva define <QUERY> => Shows a summary from wikipedia about a specific show, song, etc. \neva random <min> <max> => Returns a random number from Min To Max. \neva calc <num1> <operator> <num2> => Calculates the numbers passed. Ex: eva calc 2 + 6 \neva <ANYTHING ELSE> => Turns Eva into a conversational agent to talk to responding to <ANYTHING ELSE>! \neva who is <NAME> => Finds famous people on wikipedia and returns a summary. \neva spam <INT> <Message to spam> => Posts a Message to spam int number of times.'.upper())

    # roll random number
    elif message.content.lower().startswith("eva random "):
        cmd = message.content.split(' ')
        num1 = int(cmd[2])
        num2 = int(cmd[3])
        if num1 > num2:
            await message.channel.send("FIRST NUMBER HAS TO BE LESS THAN THE SECOND NUMBER.")
        else:
            await message.channel.send(str(message.author) + " GOT: " + str(random.randint(num1, num2)))

    # calculator
    elif message.content.lower().startswith("eva calc "):
        cmd = message.content.split(' ')
        num1 = float(cmd[2])
        op = cmd[3]
        num2 = float(cmd[4])
        if op=='+':
            await message.channel.send(str(num1 + num2))
        elif op=='-':
            await message.channel.send(str(num1 - num2))
        elif op=='*':
            await message.channel.send(str(num1 * num2))
        elif op=='/':
            if num2==0:
                await message.channel.send("CANNOT DEVIDE BY ZERO.")
            else:
                await message.channel.send(str(num1 / num2))

    # spam messages on the server ;)
    elif message.content.lower().startswith("eva spam "):
        cmd = message.content.split(' ')
        spammess = ' '.join(cmd[3:]).upper()
        spamtime = int(cmd[2])
        while spamtime>0:
            await message.channel.send(spammess)
            spamtime -= 1

    # Conversation Functionality
    elif not message.guild or message.content.lower().startswith("eva "):
        input_text = message.content.replace("@eva", "")
        input_text = message.content.replace("eva", "")
        response = k.respond(input_text)
        await message.channel.send(response.upper())

bot.run(TOKEN)