# Author: Rafael Sanchez
# bot to help me learn japanese by providing me a random japanese character in a chat when prompted

import discord
import random

def files_to_list(file_loc):
    _list = []
    file1 = open(file_loc, encoding="utf8")
    Lines = file1.readlines()
    for line in Lines:
        _list.append(line.strip())
    file1.close()
    return _list

loc = 'C:\\Users\\rafas\\Documents\\The Japanese Temple of Loci (JATELO)\\Hiragana Wing\\'
names = ['Akasata\\あ.txt', 'Akasata\\か.txt', 'Akasata\\さ.txt', 'Akasata\\た.txt', 'Nihimi\\に.txt', 'Nihimi\\ひ.txt', 'Nihimi\\み.txt', 'Yorowo\\よ.txt', 'Yorowo\\ろ.txt', 'Yorowo\\を.txt']
all_hira = []
for name in names:
    all_hira = all_hira + files_to_list(loc+name)

loc = 'C:\\Users\\rafas\\Documents\\The Japanese Temple of Loci (JATELO)\\Katakana Wing\\'
names = ['Okosoto\\オ.txt', 'Okosoto\\コ.txt', 'Okosoto\\ソ.txt', 'Okosoto\\ト.txt', 'Nufumu\\ヌ.txt', 'Nufumu\\フ.txt', 'Nufumu\\ム.txt', 'Yarawa\\ヤ.txt', 'Yarawa\\ラ.txt', 'Yarawa\\ワ.txt']
all_kata = []
for name in names:
    all_kata = all_kata + files_to_list(loc+name)

loc = 'C:\\Users\\rafas\\Documents\\The Japanese Temple of Loci (JATELO)\\Radical Kanji Lobby\\'
names = ['1left_table.txt', '2desk.txt', '3left_board.txt', '4right_board.txt', '5right_table.txt']
all_rads = []
for name in names:
    all_rads = all_rads + files_to_list(loc+name)

# filetod = open("y.txt","w", encoding="utf-8")
# filetod.writelines(all_rads)
# filetod.close()

#real_rads = []
#for rad_dash_meaning in all_rads:
#    real_rads.append(rad_dash_meaning.split('--->')[0])

#print(real_rads)

# trans = open("transcript.txt", "a", encoding="utf-8")
# transcript = ''
# for i in range(5):
#     random.shuffle(all_hira)
#     random.shuffle(all_kata)
#     transcript = transcript + ''.join(all_hira) + ''.join(all_kata)
# trans.write(transcript)
# trans.close()

tokenfile = open("C:\\Users\\rafas\\Documents\\clevergirltoken\\token.txt", "r")
TOKENDISCORD = tokenfile.read()

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    
    if message.author == client.user:
        return

    if message.content.lower().startswith('ひ'):
        await message.channel.send(random.choice(all_hira))

    if message.content.lower().startswith('カ'):
        await message.channel.send(random.choice(all_kata))

    if message.content.lower().startswith('ら'):
        therad = random.choice(all_rads)
        await message.channel.send(therad[0] + " ||" + therad[1:] + "||")

    # if message.content.lower().startswith('.ヴぉ'):
    #     await message.channel.send()
   
    

client.run(TOKENDISCORD)