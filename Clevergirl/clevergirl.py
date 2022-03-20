# Author: Rafael Sanchez
# Desc: Part of Clevergirl Brain in python. Works together with brain.json.
import json

def girl_says(m):
    m=m.replace('?', '')
    m=m.replace('!', '')
    m=m.replace(',', '')
    m=m.replace('.', '')
    m=m.replace("'", '')
    m=m.strip() 
    m=m.upper()
    with open('brain.json', 'r+') as f:
        data = json.load(f)
        for pattern, reply in data.items():
            if m==pattern:
                return reply
        learn_str = input("Clevergirl: "+m+'\nUser: ')
        learn_str=learn_str.replace('?', '')
        learn_str=learn_str.replace('!', '')
        learn_str=learn_str.replace(',', '')
        learn_str=learn_str.replace('.', '')
        learn_str=learn_str.replace("'", '')
        learn_str=learn_str.strip() 
        learn_str=learn_str.upper()
        string = '{"'+m+'": "'+learn_str+'"}'
        new_stuff=json.loads(string)
        data.update(new_stuff)
        f.seek(0)
        json.dump(data, f, indent = 1)
        return learn_str

print("")
print("")
print("*************************** CLEVERGIRL CHATBOT ***************************")
print("*************************** TYPE BYE WHEN DONE ***************************")
print("-------------------- Conversation Started ---------------------------")
print("")
while True:
    m = input("User: ")
    print("Clevergirl: "+girl_says(m))
    if 'bye' in m.lower():
        break
print("")
print("-------------------- Conversation Ended -----------------------------")
print("")