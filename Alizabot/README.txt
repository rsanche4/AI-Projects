   
   ######################
   AUTHOR: RAFAEL SANCHEZ
   
   PROJECT NAME: ALIZABOT
   ######################
   
   
1: WHAT IS ALIZA?
   **************
   ALIZA is a merge between the famous chatbots ALICE and ELIZA. Both bots use different algorithms to say things. For example, ELIZA tried to imitate a psychologist, and would ask the user questions related to what they said. ELIZA was written originally in 1966 and is considered a classic. ALICE, on the other hand, uses AIML which is a markup language for pattern matching. ALICE won awards in the early 2000s, and it's one of the best chatbots written. ALIZA borrows design concepts from both bots, making her able to sound like ELIZA and ALICE.
   
   
2: HOW ALIZA WORKS?
   ****************
   There are two files that contain all of ALIZA's brain. These are brain.py and brain.json. The .py communicates with the .json for certain answers. It also has the logic needed to access the data stored in the .json. When the user sends her a pattern (and it's not a command or a special query), ALIZA can do 1 of 2 things. She can either ask the user why they think that way, imitating the questions ELIZA would ask, or she can look up the pattern and match it with other patterns she knows the answer to. If she doesn't know how to answer, you can teach her by going to brain.json and writing the query in the "learned" core.
   
   
3: WHAT ARE THE ALIZA CORES?
   *************************
   ALIZA has different pattern cores that contain certain categories of replies. This was inspired by the fictional AI character GladOS from the Portal Video Games. Each core is activated after a pattern is matched. The cores are: 
   INSULTS: Insults are detected here.
   TIME: Allows her to tell the time.
   LEARNED: This core is special because it contains other replies the user or the world has taught her.
   SALUTE: Different ways to say hello to the user.
   ENDING: Different ways to say bye to the user.
   AGREE: If the user says phrases like "okay" or "great", she follows with something similar.
   EMOJI: Detects some emojis.
   JOKER: "Tell me a joke" functionality.
   SCARE: Makes her say strange and creepy things when prompted. She also sounds delusional.
   COMPLIMENTS: When the user says something nice, she will return the compliment.
   WORDS: This core contains a list of words. These words are nouns or adjectives, and each contains a specific reaction to that word.
   COMMANDS: The commands core is small, with only three basic functions: allows bot to repeat what user says, calculate numbers, check if the user sent nothing. This is a core that shows promise because if you want to integrate her with an OS, and make her do more advanced things, (like check the weather, open applications, make documents, etc), it would be faily simple to teach her this stuff using this core. This code is in her source code file (for python is brain.py, for c is aliza.c).
   
4: WHAT ELSE CAN SHE DO AND WHY IS SHE SO SIMPLE?
   **********************************************
   Apart from her pattern cores, ALIZA can learn things, calculate two numbers, and repeat after the user. To calculate two numbers, use this format: 4 + 8. To repeat after the user, simply say: repeat Hello!
   ALIZA is really simple because if programmers are unable to run python (say you are developing a game in Unreal Engine and want a chatbot like her but can't connect the python script), then they can take away from the concepts and algorithms and easily convert them to any language of their choice, given that her program is rather simple. All they would need to know is how to incorporate pattern matching with wildcards, and then some very simple string manipulation. The full source code contains all her answers, simple logic, and the brain.json is still a json file that can be accessed by any programming language! (keep in mind there is also a C version of ALIZA in this same directory)
   
   
5: HOW TO TEACH HER NEW THINGS?
   ****************************
   Go ahead and open the brain.json file. In the "learned" category, add your query, and after that a list of replies to that query. She will select a random reply from the list given. Note that you can use wildcards to match with 1 or more words in the middle of the sentence. For example: "I * tall" will match to "I am tall" or "I look tall", etc. Don't put the wildcards at the beginning or at the end of a pattern as this is done automatically when matching to different patterns. If you are confused on how to use JSON files, you can always look it up on the internet.
   
   
6: WHAT LIBRARIES DOES SHE USE?
   ****************************
   If you want to run her without the gui, you don't have to install any packages as all the essential ones she uses for parsing arguments and her brain are all pre-installed in python. You only need python installed.
   Here are the libraries she uses if you want to start the GUI:
   TKINTER (FOR THE GUI)
   PIL (DISPLAYING IMAGE FOR THE GUI)
   OS (OPENING THE CHAT LOGS FOLDER)
   PYGAME (PLAYING MUSIC)
   RANDOM (CREATING RANDOMNESS)
   DATETIME (TELLING THE TIME)
   JSON (READING THE JSON FILE)
   FNMATCH (FOR PATTERN MATCHING)
   There is also a C version of her with makefile included. You can type make, then ./aliza
   The C version of ALIZA uses: stdio.h string.h ctype.h string.h stdlib.h stdbool.h


7: HOW TO TALK TO HER?
   *******************
   If you have Python installed on your system, make sure you have the previous libraries installed (you can use the command "pip install" to install them. Look up "pip" in Google to learn to use it). You can simply open the terminal in this folder and type: python3 start_gui.py
   Also, I wrote a C version of her so it can run natively in any Operating System in UNIX. You can type make, then ./aliza
   It is best to send her complete, simple sentences with a clear subject and predicate. Avoid the apostrophe (Send "you are" instead of "you're") and avoid spelling and grammar mistakes as this might confuse her.
   
   
8: CAN I USE THIS IN A GAME OR IN MY PROJECT?
   ******************************************
   Of course! Just remember to credit me as the creator of her brain. You can even change the name to a specific character you have in mind since she never calls herself "ALIZA". This is great because you can simply give it its own unique name and this can be extended to NPCs, unique clones of her, a 3D humanoid clone etc.
   
   
9: DID YOU MAKE THE IMAGE AND MUSIC?
   *********************************
   If you are referring to the GUI version, then no. I got the music from the internet and the image was commissioned. All rights go to their respective owners.
   

10:IS THIS PROJECT FINISHED?
   *************************
   Everything is done. The only thing left to do is add replies! The WORD CORE specifically, it grows everyday as I find new words and different replies. Given there are already a lot of words, and I am doing this solo, it takes time. Eventually, there will be plenty of replies for all the words she knows.
   
   
11:HOW DOES THE DEVELOPER TEACH HER RESPONSES?
   *******************************************
   I use this random sentence & question generator website: https://randomwordgenerator.com/
   I use a random sentence, feed it to her, and see if she responds. If she doesn't have a response, I study the sentence and see what words are important and I then write a reply! I do this everytime and over time she accumulates more and more accurate responses to more sentences.

   
12:WHY DO THIS?
   ************
   Why not?

