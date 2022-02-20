   
   ###########################
      AUTHOR RAFAEL SANCHEZ
   
   PROJECT NAME: ALIZA CHATBOT
   ###########################
   
   
1: WHAT IS ALIZA?
   **************
   ALIZA is a merge between the famous chatbots ALICE and ELIZA. Both bots use different algorithms to say things. For example, ELIZA tried to imitate a psychologist, and would ask the user questions related to what they said. ELIZA was written originally in 1966 and is considered a classic. ALICE, on the other hand, uses AIML which is mark up language for pattern matching. ALICE won awards in the early 2000s, and it's one of the best chatbots written. ALIZA borrows design concepts from both bots, making her able to sound like ELIZA and ALICE.
   
   
2: HOW ALIZA WORKS?
   ****************
   There are two files that contain all of ALIZA's brain. These are brain.py and brain.json. The .py communicates with the .json for certain answers. It also has the logic needed to access the data stored in the .json. When the user sends her a pattern (and it's not a command or a special query), ALIZA can do 1 of 2 things. She can either ask the user why they think that way, imitating the questions ELIZA would ask, or she can look up the pattern and match it with other patterns she knows the answer to. If she doesn't know how to answer, she will show the user how they can 'teach' her different patterns with replies.
   
   
3: WHAT ARE THE ALIZA CORES?
   *************************
   ALIZA has different pattern cores that contain certain categories of replies. This was inspired by the fictional AI character GladOS from the Portal Videogames. Each core is activated after a pattern is matched. The cores are: 
   INSULTS: Insults are detected here.
   TIME: Allows her to tell the time.
   LEARNED: This core is special because it contains the patterns and replies that the user has taught her.
   SALUTE: Different ways to say hello to the user.
   ENDING: Different ways to say bye to the user.
   AGREE: If the user says phrases like "okay" or "great", she follows with something similar.
   EMOJI: Detects some emojis.
   JOKER: "Tell me a joke" functionality.
   SCARE: Makes her say strange and creepy things when prompted. She also sounds delusional.
   COMPLIMENTS: When the user says something nice, she will return the compliment.
   WORDS: The last core that is checked contains a list of words. These words are nouns or adjectives, and each contains a specific reaction that word.
   
   
4: WHAT ELSE CAN SHE DO AND WHY IS SHE SO SIMPLE?
   **********************************************
   Apart from her pattern cores, ALIZA can learn things, calculate two numbers, and repeat after the user. To calculate two numbers, use this format: 4 + 8. To repeat after the user, simply say: repeat Hello!
   ALIZA is really simple because if programmers are unable to run python (say you are developing a game in Unreal Engine and want a chatbot like her but can't connect the python script), then they can take away from the concepts and algorithms and easily convert them to any language of their choice, given that her program is rather simple. All they would need to know is how to incorporate pattern matching with wildcards, and then some very simple string manipulation. The full source code contains all her answers, simple logic, and the brain.json is still a json file that can be accessed by any programming language! 
   
   
5: HOW TO TEACH HER NEW THINGS?
   ****************************
   Learning things is perhaps the most interesting functionality of ALIZA that sets her apart from ALICE and ELIZA. The process for learning new queries is really simple. 
   Simply say: My NamE > You are Brian! > Your name is Brian.
   What ALIZA will do is turn the first pattern to lowercase, add the pattern "my name" to the LEARNED CORE and next time you say any variation of that pattern, for exaple "What is my name, girl?", "Do you know My NaME?", ALIZA will return one of the choices you taught her. In this example, she can return "You are Brian!" or "Your name is Brian." You can teach her any number of replies. 
   Keep in mind you can use the * wildcard for matching any 1 or more words in that part of the pattern. For example: "you * artificial" will match to anything that has you [any word or words in the middle] artificial. Don't put the wildcards at the beginning or at the end of a pattern as this is done automatically by the brain.py.
   It is important to note that ALIZA will not relearn patterns she already learned. In which case, she will say she already learned that fact. If you want to erase a certain pattern, you can open her brain.json file and search your desired pattern and delete that along with the replies. If you are confused on how to use JSON files, you can always look it up in the internet.
   
   
6: WHAT LIBRARIES DOES SHE USE?
   ****************************
   ALIZA uses a number of python libraries for functionality:
   TKINTER (FOR THE GUI)
   PIL (DISPLAYING IMAGE FOR THE GUI)
   OS (OPENING THE CHATLOGS FOLDER)
   PYGAME (PLAYING MUSIC)
   RANDOM (CREATING RANDOMNESS)
   DATETIME (TELLING THE TIME)
   JSON (READING THE JSON FILE)
   FNMATCH (FOR PATTERN MATCHING)


7: HOW TO TALK TO HER?
   *******************
   If you are on Windows, simply double click on the start_gui.exe file. This will open up her graphical user interface.
   If you have Python installed on your system, make sure you have the previous libraries installed (you can use the command "pip install" to install them. Look up "pip" in Google to learn to use it). You can simply open the terminal in this folder and type: python start_gui.py
   
   
8: CAN I USE THIS IN A GAME OR IN MY PROJECT?
   ******************************************
   Of course! Just remember to credit me as the creator of her brain. You can even change the name to a specific character you have in mind since she never calls herself "ALIZA". This is great because you can simply give it its own unique name and this can be extended to NPCs, unique clones of her, a 3D humanoid clone etc. She can learn things, so you can teach her to say whatever you want!
   
   
9: DID YOU MAKE THE IMAGE AND MUSIC?
   *********************************
   No. I got the music from the internet and the image was commisioned. All rights go to their respective owners.
   

10:IS THIS PROJECT FINISHED?
   *************************
   Everything is done. The only thing left to do is add replies! The WORD CORE specifically, it grows everyday as I find new words and different replies. Given there are already a lot of words, and I am doing this solo, it takes time. Eventually, there will plenty of replies for all the words she knows.
   
   
11:WHY DID YOU DO THIS?
   ********************
   Why not?