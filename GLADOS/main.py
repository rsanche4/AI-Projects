
import datetime
import os
import aiml
import glados
from playsound import playsound

print("Initializing GLADOS")
#dictionary=PyDictionary()
BRAIN_FILE="brain.dump"

k = aiml.Kernel()

# To increase the startup speed of the bot it is
# possible to save the parsed aiml files as a
# dump. This code checks if a dump exists and
# otherwise loads the aiml from the xml files
# and saves the brain dump.
if os.path.exists(BRAIN_FILE):
    print("Loading from brain file: " + BRAIN_FILE)
    k.loadBrain(BRAIN_FILE)
else:
    print("Parsing aiml files")
    k.bootstrap(learnFiles="std-startup.aiml", commands="load aiml b")
    print("Saving brain file: " + BRAIN_FILE)
    k.saveBrain(BRAIN_FILE)

MASTER = "MASTER"

def speak(text):
    glados.glados_voice(text)
    playsound('output.wav')

#This funtion will wish you as per the current time
def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour <12:
        print("GOOD MORNING " + MASTER.upper())
        speak("good morning " + MASTER)

    elif hour>=12 and hour<18:
        print("GOOD AFTERNOON " + MASTER.upper())
        speak("good afternoon " + MASTER)

    else:
        print("GOOD EVENING " + MASTER.upper())
        speak("good evening " + MASTER)

    print("Hello and, again, welcome to the Aperture Science computer-aided enrichment center.".upper())
    speak("Hello and, again, welcome to the Aperture Science computer-aided enrichment center.")

#main program starting
def main():
    print("")
    query = input("> ")
    query = query.lower()

    if 'time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"{MASTER} THE TIME IS {strTime}")
        speak(f"{MASTER} THE TIME IS {strTime}")

    elif 'see your brain' in query:
        codePath = __file__
        os.startfile(codePath)

    elif 'shutdown' in query:
        print("GOODBYE")
        speak("Goodbye")
        exit()

    else:
        answer = k.respond(query)
        print(answer.upper())
        speak(answer)

print("""

             .,-:;//;:=,
         . :H@@@MM@M#H/.,+%;,
      ,/X+ +M@@M@MM%=,-%HMMM@X/,
     -+@MM; $M@@MH+-,;XMMMM@MMMM@+-
    ;@M@@M- XM@X;. -+XXXXXHHH@M@M#@/.
  ,%MM@@MH ,@%=            .---=-=:=,.
  -@#@@@MX .,              -%HX$$++%+;
 =-./@M@M$                  .;@MMMM@MM:
 X@/ -$MM/                    .+MM@@@M$
,@M@H: :@:                    . -X#@@@@-
,@@@MMX, .                    /H- ;@M@M=
.H@@@@M@+,                    %MM+..%#$.
 /MMMM@MMH/.                  XM@MH; -;
  /%++$XHH@$=              , .H@@@@MX,
   .=--------.           -%H.,@@@@@MX,
   .%MM@@@HHHXX$$$%+- .:$MMX -M@@MM%.
     =XMMM@MM@MM#H;,-+HMM@M+ /MMMX=
       =%@M@M#@$-.=$@MM@@@M; %M%=
         ,:+$+-,/H#MMMMMMM@- -,
               =++%&%&+/:-.

                    """)
print("")
print("************************************************************")
print("            GLADOS HUMAN INTERFACE CONSOLE")
print("By Rafael Sanchez")
print("Type SHUTDOWN to end the chat.")
print("")
wishMe()
while True:
    main()