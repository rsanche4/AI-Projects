   
   ######################
   AUTHOR: RAFAEL SANCHEZ
   PROJECT NAME: ALIZABOT
   ######################
   
   
1: WHAT IS ALIZA?
   **************
   ALIZA is a merge between the famous chatbots ALICE and ELIZA. Both bots use different algorithms to say things. For example, ELIZA tried to imitate a psychologist, and would ask the user questions related to what they said. ELIZA was written originally in 1966 and is considered a classic. ALICE, on the other hand, uses AIML which is a markup language for pattern matching. ALICE won awards in the early 2000s, and it's one of the best chatbots written. ALIZA borrows design concepts from both bots, making her able to sound like ELIZA and ALICE.
   
   
2: HOW ALIZA WORKS?
   ****************
   The most important file for ALZIA are brain.txt and either aliza.c or brain.py. The .py or .c communicate with the .txt for extracting the correct answer. brain.txt contain all of aliza's answers and their replies. When the user sends her a pattern (and it's not a command or a special query), ALIZA can do 1 of 2 things. She can either ask the user why they think that way, imitating the questions ELIZA would ask, or she can look up the pattern and match it with other patterns she knows the answer to.
   
   
3: WHAT ELSE CAN SHE DO AND WHY IS SHE SO SIMPLE?
   **********************************************
   ALIZA can repeat after the user, and also check if the user sent anything at all. This part of her code is known as the "commands section" and can be enhanced depending on your own project. For example, it would be fairly simple to teach her to open a browser, check the weather, etc. All you need is to write code that would do this in this section. She should always return a string in this section, and in the .c file, she should always copy her answer to the reply array. To repeat after the user, simply say: repeat Hello!
   ALIZA is really simple because if programmers are unable to run python (say you are developing a game in Unreal Engine and want a chatbot like her but can't connect the python script), then they can take away from the concepts and algorithms and easily convert them to any language of their choice, given that her program is rather simple. All they would need to know is how to incorporate pattern matching with wildcards, and then some very simple string manipulation. The full source code contains all her answers, simple logic, and the brain.txt is still a txt file that can be accessed by any programming language! (keep in mind there is also a C version of ALIZA in this same directory)
   
   
4: HOW TO TEACH HER NEW THINGS?
   ****************************
   Go ahead and open the brain.txt file. Search for the query "#person", right above this, you can start writing whatever queries you want to teach her in this format: #PATTERN$ANSWER1$ANSWER2... where PATTERN is what she will match the queries to and the replies what she will say. There is a limit to how many answers she can learn per pattern (20). She will select a random reply from all the replies she was taught. Note that you can use wildcards to match with 1 or more words in the middle of the sentence. For example: "I * tall" will match to "I am tall" or "I look tall", etc. Don't put the wildcards at the beginning or at the end of a pattern as this is done automatically when matching to different patterns.
   
   
5: WHAT LIBRARIES DOES SHE USE?
   ****************************
   If you want to run her without the gui, you don't have to install any packages as all the essential ones she uses for parsing arguments and her brain are all pre-installed in python. You only need python installed.
   Here are the libraries she uses if you want to start the GUI:
   TKINTER (FOR THE GUI)
   PIL (DISPLAYING IMAGE FOR THE GUI)
   PYGAME (PLAYING MUSIC)
   RANDOM (CREATING RANDOMNESS)
   DATETIME (TELLING THE TIME)
   FNMATCH (FOR PATTERN MATCHING)
   There is also a C version of her with makefile included. You can type "make", then ./aliza
   The C version of ALIZA has these headers:
   #include <stdio.h>
   #include <string.h>
   #include <ctype.h>
   #include <string.h>
   #include <stdlib.h>
   #include <stdbool.h>
   #include <sys/types.h>
   #include <sys/stat.h>
   #include <unistd.h>


6: HOW TO TALK TO HER?
   *******************
   If you have Python installed on your system, make sure you have the previous libraries installed (you can use the command "pip install" to install them. Look up "pip" in Google to learn to use it). You can simply open the terminal in this folder and type: python3 start_gui.py, or python start_gui.py, or python start_raw.py, or python3 start_raw.py.
   Also, I wrote a C version of her so it can run natively in any Operating System in UNIX. You can type make, then ./aliza
   It is best to send her complete, simple sentences with a clear subject and predicate. Avoid the apostrophe (Send "you are" instead of "you're") and avoid spelling and grammar mistakes as this might confuse her.
   There is also a version of her running on discord in this server (feel free to drop by, I am always there developing and improving her answers): https://discord.gg/h7vqR2YD
   
   
7: CAN I USE THIS IN A GAME OR IN MY PROJECT?
   ******************************************
   Of course! Just remember to credit me as the creator of her design. You can even change the name to a specific character you have in mind since she never calls herself "ALIZA". This is great because you can simply give it its own unique name and this can be extended to NPCs, unique clones of her, a 3D humanoid clone etc.
   
   
8: DID YOU MAKE THE IMAGE AND MUSIC?
   *********************************
   If you are referring to the GUI version, then no. I got the music from the internet and the image was commissioned. All rights go to their respective owners.
   

9: IS THIS PROJECT FINISHED?
   *************************
   Everything is done. The only thing left to do is add replies! Her brain grows everyday as I find new words and different replies. Given there are already a lot of words, and I am doing this solo, it takes time. Eventually, there will be plenty of replies for all the words she knows.
   
   
10:HOW DOES THE DEVELOPER TEACH HER RESPONSES?
   *******************************************
   I use this random sentence & question generator website: https://randomwordgenerator.com/
   I use a random sentence, feed it to her, and see if she responds. If she doesn't have a response, I study the sentence and see what words are important and I then write a reply! I do this everytime and over time she accumulates more and more accurate responses to more sentences.