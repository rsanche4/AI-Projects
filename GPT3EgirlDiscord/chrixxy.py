# Author: Rafael Sanchez
import discord
import openai as ai

tokenfile = open("C:\\Users\\rafas\\Documents\\gpt3token\\token.txt", "r")
TOKEN = tokenfile.read()

start_sequence = "\nChrixxy:"
restart_sequence = "\nPerson:"
session_prompt = "You are talking to Chrixxy, a tiktok influencer and egirl. She is shy and sounds cute all the time. She listens to Kpop, wears heavy make up all the time, and is extremely concerned about how she looks. She tells everyone to subscribe to her Only Fans.\n\nPerson: Hello.\nChrixxy: Hey uwu\n\nPerson: What do you like?\nChrixxy: I like Kpop and small tiktok edits lol. hbu\n\nPerson: You are really cute.\nChrixxy: *blushes* aww thank you. Subcribe to my only fans for more uwu *wink*\n\nPerson:"

def chat(question,chat_log = None) -> str:
    if(chat_log == None):
        chat_log = start_chat_log
    prompt = f"{chat_log}Person: {question}\nChrixxy:"
    response = completion.create(prompt = prompt, engine =  "davinci", temperature = 0.7,top_p=1, frequency_penalty=0, 
    presence_penalty=0, best_of=2,max_tokens=100,stop = "\nPerson: ")
    return response.choices[0].text

def modify_start_message(chat_log,question,answer) -> str:
    if chat_log == None:
        chat_log = start_chat_log
    chat_log += f"Person: {question}\nChrixxy: {answer}\n"
    return chat_log


ai.api_key = TOKEN

completion = ai.Completion()

start_chat_log = session_prompt

def gpt3_reply(question):
  return str(chat(question,start_chat_log).split("Chrixxy:")[0].split("Person:")[0]).strip()

tokenfile = open("C:\\Users\\rafas\\Documents\\chrixxytoken\\token.txt", "r")
TOKENDISCORD = tokenfile.read()

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    
    if message.author == client.user:
        return

    if message.content.lower().startswith('chrixxy,'):
        await message.channel.send(gpt3_reply(message.content.lower().replace('chrixxy,', '')))
   
client.run(TOKENDISCORD)