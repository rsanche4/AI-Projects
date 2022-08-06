import openai as ai
import socket
import json
import random

tokenfile = open("C:\\Users\\rafas\\Documents\\gpt3token\\token.txt", "r")
TOKEN = tokenfile.read()

start_sequence = "\nLisa:"
restart_sequence = "\nPerson:"
session_prompt_file = open("C:\\Users\\rafas\\Documents\\Github\\AI-Projects\LISA_CHATBOT\\gpt3-preset.txt", "r")
session_prompt = session_prompt_file.read()

def chat(question,chat_log = None) -> str:
    if(chat_log == None):
        chat_log = start_chat_log
    prompt = f"{chat_log}Person: {question}\nLisa:"
    response = completion.create(prompt = prompt, engine =  "curie", temperature = 0.7,top_p=1, frequency_penalty=0, 
    presence_penalty=0, best_of=2,max_tokens=100,stop = "\nPerson: ")
    return response.choices[0].text

def modify_start_message(chat_log,question,answer) -> str:
    if chat_log == None:
        chat_log = start_chat_log
    chat_log += f"Person: {question}\nLisa: {answer}\n"
    return chat_log


ai.api_key = TOKEN

completion = ai.Completion()

start_chat_log = session_prompt

def gpt3_reply(question):
    return str(chat(question,start_chat_log).split("Lisa:")[0].split("Person:")[0]).strip()

# Pass the socket when doing main_open as well as message to reply to and the name the bot should call you
# Right here, compare polarity and the higher the better so output that
def reply(sock, input_text, name):
    if random.randint(0, 2)==0:
        dataJson = {"username":"localuser","message": input_text, "vars": {"name": name}}
        data = json.dumps(dataJson)
        data = str(data)+"\n"+"__END__"        
        sock.sendall(bytes(data,encoding="utf-8"))
        received = sock.recv(4096)
        received = received.decode("utf-8")
        received = received.replace("__END__", "")
        parsed_data = json.loads(received)
        answer = parsed_data["reply"]
        if answer.strip()=="}" or answer.strip()=="":
            return gpt3_reply(input_text)
        else:
            return parsed_data["reply"]
    else:
        return gpt3_reply(input_text)

# Returns the socket to the server running her brain script in Rivescript -> See Lisa Chatbot directory for more information
def open(host_port="192.168.163.128:2020"):
    hp_list = host_port.split(':')
    HOST, PORT = hp_list[0], int(hp_list[1])
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))
    return sock

# Pass the socket from above to close
def close(sock):
    sock.close()