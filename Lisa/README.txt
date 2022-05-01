   
   ######################
   AUTHOR: RAFAEL SANCHEZ
   PROJECT NAME:    ALIZA
   ######################
   
1: WHAT IS ALIZA?
   **************
   ALIZA is a merge between the famous chatbots ALICE and ELIZA. Both bots use different algorithms to say things. For example, ELIZA tried to imitate a psychologist, and would ask the user questions related to what they said. ELIZA was written originally in 1966 and is considered a classic. ALICE, on the other hand, uses AIML which is a markup language for pattern matching. ALICE won awards in the early 2000s, and it's one of the best chatbots written. ALIZA borrows design concepts from both bots, making her able to sound like ELIZA and ALICE. Eliza+Alice=Aliza. Though she will often refer to herself as Lisa, since it's easier to pronounce.
   
2: HOW ALIZA WORKS?
   ****************
   Refer to brain.txt for all her main replies.
   1-Aliza parses your input.
   2-Aliza first opens brain.txt, and checks your query with all the different queries there.
   3-Aliza will check if she should ask the user why they think so, and if she chooses not to task then she proceeds to pattern matching.
   4-It checks pattern in this order: insults, check the time commands, different greetings, goodbyes, agreements, emojis, tell me a joke queries, horror answers, compliments, extra queries she has learned, queries using the + sign (more on that later), and lastly specific keywords (most common 1500+ english words)
   5-If, after everything, she has no idea what to say, she will return the special response the empty string. (There are other responses that trigger special responses which are located also in brain.txt at the top.  

3: WHAT LIBRARIES DOES SHE USE?
   ****************************
   If you want to run her without the gui, you don't have to install any packages as all the essential ones she uses for parsing arguments and her brain are all pre-installed in python. You only need python installed.
   Here are the libraries she uses if you want to start the GUI in python:
   TKINTER (FOR THE GUI)
   PIL (DISPLAYING IMAGE FOR THE GUI)
   PYGAME (PLAYING MUSIC)
   RANDOM (CREATING RANDOMNESS)
   DATETIME (TELLING THE TIME)
   FNMATCH (FOR PATTERN MATCHING)

4: HOW TO TALK TO HER?
   *******************
   If you have Python installed on your system, make sure you have the previous libraries installed (you can use the command "pip install" to install them. Look up "pip" in Google to learn to use it). You can simply open the terminal in this folder and type: python3 start_gui.py, or python start_gui.py, or python start_raw.py, or python3 start_raw.py.
   
5: DID YOU MAKE THE IMAGE AND MUSIC?
   *********************************
   If you are referring to the GUI version, then no. I got the music from the internet and the image was commissioned. All rights go to their respective owners.
   
6: IS THIS PROJECT FINISHED?
   *************************
   The only thing left to do is add replies! Her brain grows everyday as I find new words and different replies. Given there are already a lot of words, and I am doing this solo, it takes time. Eventually, there will be plenty of replies for all the words she knows.