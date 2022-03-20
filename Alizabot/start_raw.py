# Sends message to ALIZA. No Gui.
# Author: Rafael Sanchez

import brain
print("")
print("")
print("*************************** ALIZA CHATBOT ***************************")
print("*********************** By Rafael Sanchez ***************************")
print("***************** To stop Aliza, type Bye ***************************")
print("")
print("-------------------- Conversation Started ---------------------------")
print("")
while True:
    m = input("User: ")
    print("Aliza: "+brain.aliza_says(m, 'C:\\Users\\rafas\\Documents\\Github\\AI-Projects\\Alizabot\\brain.txt', 'C:\\Users\\rafas\\Documents\\Github\\AI-Projects\\Alizabot\\brain0.txt'))
    if (brain.conv_ended):
        break

print("")
print("-------------------- Conversation Ended -----------------------------")