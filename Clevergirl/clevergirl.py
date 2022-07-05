# Author: Rafael Sanchez
# Desc: Part of Clevergirl Brain in python. Works together with brain.json.
import json
from difflib import SequenceMatcher
import random
import discord

idk = ["I learned something new today...", "I am constantly improving.", "I just learned something new with our conversation.","Thank you for teaching me things just by chatting!","Let's talk about something else, because I just learned something new."]

def formal(str):
    return str[0] + str[1:].lower() + "."

def only_words(string):
    return string.replace("!", "").replace("@", "").replace("#", "").replace("$", "").replace("%", "").replace("^", "").replace("&", "").replace("*", "").replace("(", "").replace(")", "").replace("-", "").replace("_", "").replace("=", "").replace("+", "").replace("[", "").replace("{", "").replace("}", "").replace("]", "").replace(";", "").replace(":", "").replace("'", "").replace('"', "").replace("|", "").replace("\\", "").replace("?", "").replace("/", "").replace(".", "").replace(">", "").replace("<", "").replace(",", "").strip().upper()

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()*100.0

def girl_says(m):
    global idk
    new_m = only_words(m)
    with open('brain.json', 'r+') as f:
        data = json.load(f)
        for pattern, reply in data.items():
            sratio = similar(new_m, pattern)
            if sratio >= 75.00 and reply != "ERROR404":
                return (reply, "ANSWER")
            elif sratio >= 75.00 and reply == "ERROR404":
                items = list(data.items())
                if pattern==items[-1][0] and pattern!=new_m:
                    return (pattern, "LEARN")
                if pattern==items[-1][0] and pattern==new_m:
                    return (only_words(random.choice(idk)), "ANSWER")
                if pattern==new_m:
                    continue
        learn_pattern = new_m
        learn_reply = "ERROR404"
        string = '{"'+learn_pattern+'": "'+learn_reply+'"}'
        new_stuff=json.loads(string)
        data.update(new_stuff)
        f.seek(0)
        json.dump(data, f, indent = 0)
        f.truncate()
        for pattern, reply in data.items():
            if reply == "ERROR404":
                if pattern==learn_pattern:
                    continue
                return (pattern, "LEARN")
        return (only_words(random.choice(idk)), "ANSWER")

def learn(m, pattern_we_said_before):
    new_m = only_words(m)
    with open('brain.json', 'r+') as f:
        data = json.load(f)
        string = '{"'+pattern_we_said_before+'": "'+new_m+'"}'
        new_stuff=json.loads(string)
        data.update(new_stuff)
        f.seek(0)
        json.dump(data, f, indent = 0)
        f.truncate()

tokenfile = open("C:\\Users\\rafas\\Documents\\clevergirltoken\\token.txt", "r")
TOKEN = tokenfile.read()
isLearn = False

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    global isLearn
    if message.author == client.user:
        return
    
    if not message.guild:
        m = only_words(message.content)
        r = ()
        if isLearn:
            m_new_from_user = only_words(message.content)
            lastmes_file =  open("lastmes.txt", "r")
            lastmes = lastmes_file.read()
            learn(m_new_from_user, lastmes)
            await message.channel.send(formal(only_words(random.choice(idk))))
            isLearn = False
            return
        else:
            r = girl_says(m)
            with open("lastmes.txt", "w") as log:
                log.write(r[0])
            with open("state.txt", "w") as log:
                log.write(r[1])
        statef = open("state.txt", "r")
        state = statef.read()
        lastmes_file =  open("lastmes.txt", "r")
        lastmes = lastmes_file.read()
        if state=="LEARN":
            isLearn = True
            await message.channel.send(formal(lastmes))
        if state=="ANSWER":
            await message.channel.send(formal(lastmes))

client.run(TOKEN)

# while True:
#     m = input("User: ")
#     r = girl_says(m)
#     if r[1]=="LEARN":
#         print("Clevergirl: "+ r[0] + "    " + r[1])
#         m_new_from_user = input("User: ")
#         learn(m_new_from_user, r[0])
#         print("Clevergirl: " + only_words(random.choice(idk)))

#     if r[1]=="ANSWER":
#         print("Clevergirl: "+ r[0])
#     if 'bye' in m.lower():
#         break