# This works after dumping conversations from cleverbot, essentially also teaching Lisa stuff from cleverbot. It gets the stuff from clevertext and makes some changes to turn into rive
import json

def formal(str):
    return str[0].upper() + str[1:] + "."

def only_words(string):
    return string.replace("!", "").replace("@", "").replace("#", "").replace("$", "").replace("%", "").replace("^", "").replace("&", "").replace("*", "").replace("(", "").replace(")", "").replace("-", "").replace("_", "").replace("=", "").replace("+", "").replace("[", "").replace("{", "").replace("}", "").replace("]", "").replace(";", "").replace(":", "").replace("'", "").replace('"', "").replace("|", "").replace("\\", "").replace("?", "").replace("/", "").replace(".", "").replace(">", "").replace("<", "").replace(",", "").strip().upper()

def learn(m, query):
    new_m = only_words(m)
    new_q = only_words(query)
    with open('cleverbrain.json', 'r+') as f:
        data = json.load(f)
        string = '{"'+new_q+'": "'+new_m+'"}'
        new_stuff=json.loads(string)
        data.update(new_stuff)
        f.seek(0)
        json.dump(data, f, indent = 0)
        f.truncate()

# Parsing the raw data
def parseTrainData(filename):
    file = open(filename, 'r')
    file_content = file.readlines()
    for conversation in file_content:
        conversation = conversation.replace('#cleverbot', '')
        conversation = conversation.split('Clev:')
        learn(conversation[2], conversation[1])

def parseJson(file):
    
    with open('cleverbrain.json', 'r+') as f:
        data = json.load(f)
        for pattern, reply in data.items():
            reply = " "+reply.lower()+" "
            reply = reply.replace(" i ", " I ")
            reply = reply.replace(" im ", " I am ")
            reply = reply.replace(" dont ", " don't ")
            reply = reply.replace(" youre ", " you are ")
            reply = reply.replace(" whats ", " what's ")
            reply = reply.replace(" isnt ", " is not ")
            reply = reply.replace(" arent ", " are not ")
            reply = reply.replace(" hes ", " he's ")
            reply = reply.replace(" shes ", " she's ")
            reply = reply.replace(" weve ", " we've ")
            reply = reply.replace(" didnt ", " did not ")
            reply = reply.replace(" wouldve ", " would've ")
            reply = reply.replace(" wont ", " won't ")
            reply = reply.strip()
            file.write("+ " + pattern.lower() +"\n")
            file.write("- " + formal(reply)+"\n")
            file.write(""+"\n")
            file.write("+ * " + pattern.lower()+"\n")
            file.write("@ " + pattern.lower()+"\n")
            file.write(""+"\n")
            file.write("+ " + pattern.lower() + " *"+"\n")
            file.write("@ " + pattern.lower()+"\n")
            file.write(""+"\n")
            file.write("+ * " + pattern.lower() + " *"+"\n")
            file.write("@ " + pattern.lower()+"\n")
            file.write(""+"\n")


parseTrainData('clevertrain.txt')
rivefile = open("..\\LISA_CHATBOT\\lisa_rivescript_brain\\learned_phrases.rive", "a")
parseJson(rivefile)
rivefile.close()