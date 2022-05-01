# Sends message to ALIZA. No Gui.
# Author: Rafael Sanchez
from datetime import datetime
import brain
print("")
print("***************************")
print("LISA CHATBOT")
print("By Rafael Sanchez")
print("To stop talking to Lisa, say goodbye!")
da = datetime.now().strftime("%d/%m/%Y %H:%M:%S.")
print("Conversation start: "+da)
print("")
print(brain.start())
while True:
    m = input("> ")
    print(brain.aliza_says(m))
    if (brain.conv_ended):
        break

print("")
db = datetime.now().strftime("%d/%m/%Y %H:%M:%S.")
print("Conversation end: "+db)
