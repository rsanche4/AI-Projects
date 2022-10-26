#!/usr/bin/python3
from datetime import datetime
import socket
import json

host_port = input("Let's connect to the server. Input the IP Address and port (Ex: 192.168.163.128:2020): ")
hp_list = host_port.split(':')
HOST, PORT = hp_list[0], int(hp_list[1])
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
name = input("What should the bot call you? ")
print("")
print("***************************")
print("LISA CHATBOT")
print("By Rafael Sanchez")
print("To quit program, type shutdown")
da = datetime.now().strftime("%d/%m/%Y %H:%M:%S.")
print("Conversation start: "+da)
print("")
try:
    sock.connect((HOST, PORT))
    while True:
        input_text = input(">>> ")
        if 'shutdown' in input_text.lower():
            quit()

        dataJson = {"username":"localuser","message": input_text, "vars": {"name": name}}
        data = json.dumps(dataJson)
        data = str(data)+"\n"+"__END__"        
        sock.sendall(bytes(data,encoding="utf-8"))
        received = sock.recv(4096)
        received = received.decode("utf-8")
        received = received.replace("__END__", "")
        parsed_data = json.loads(received)
        answer = parsed_data["reply"].upper()
        if answer.strip()=="}" or answer.strip()=="":
            print("I don't know!".upper())
        else:
            print(parsed_data["reply"].upper())

finally:
    sock.close()