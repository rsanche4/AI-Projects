******************************************************
Programmer: Rafael Sanchez

An alicebot named zoey. Uses AIML, python,
tkinter, and pygame for several functionalities
like GUI, brain of the chatbot, pattern matching,
audio, etc.

It has all the original Alice AIML files, 
Standard AIML files, Mitsuku AIML files,
as well some extra files to expand on her 
personality.

Currently in development.

Things yet to implement:
-Notes for fixer.py:
   +The professor aiml files have some errors when being
   parsed by the python interpreter. Change the files
   to be 1.0 compliant by writing a 'fixer.py' that
   checks for it all and changes to the correct
   version by taking out 'learn' tags and unsopported
   wildcards (^ #). 
   +Also if finds misplaced tags delete
   the whole category, also if it finds text inside
   tags that shouldnt be there, delete that text
 
-If we find the <bot name=""/> tag, input the correct
 phrase. For example, name="name" should be zoey.

-Finish editting AIML files to fit her personality

-Games to play with her: game of pig, blackjack, 
 rock paper scissors, war(card game), Date Me Game 
 where you go on a virtual date with her ;)

-Keep a memory system where she knows about us 
 and what we like (in python). This is good because
 when we say 'bored' or something like that or she
 sends a 'im confused reply' we can tell the user
 i hread you like music. fun fact on  music: blah blah

-Cool quotes from different media about random things
 in life. (this will be her posts in twitter as well)

-Thoughts on different anime series she is watched (Top classic series)

-Song of This was a triumph im making a note
 whenever a user inputs a part of the lyric
 she sings the rest
 
-Translate to any language command
 
-Tell me a story functionality

-Calendar and date functionality

-Make it into an exe file include a How to Use guide and
 what she is capable of doing, recommandations on how
 she works best, and upload it to itch.io,
 indiedb, and other places, and perhaps STEAM but 
 under the Rafael Sanchez account. (create one)
 + On the github, create 2 folders, 1 where we have
 the src, and one with the finizaled version exe
 + Note that the final version doesnt have aiml files,
 it only has a .brn file because it's faster to load