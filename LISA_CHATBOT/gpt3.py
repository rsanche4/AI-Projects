import openai as ai

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
    response = completion.create(prompt = prompt, engine =  "davinci", temperature = 0.7,top_p=1, frequency_penalty=0, 
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
  return str(chat(question,start_chat_log).split("Lisa:")[0]).strip()