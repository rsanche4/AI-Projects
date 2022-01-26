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

******************************************************
STUFF TO IMPLEMENT
-Notes for fixer.py:
   + The professor aiml files have some errors when being
   parsed by the python interpreter. Change the files
   to be 1.0 compliant by writing a 'fixer.py' that
   checks for it all and changes to the correct
   version by taking out 'learn' tags and unsopported
   wildcards (^ #). 
   + Also if finds misplaced tags delete
   the whole category, also if it finds text inside
   tags that shouldnt be there, delete that text
   + If we find the <bot name=""/> tag, input the correct
   phrase. For example, name="name" should be zoey.
   + If we find the <br> tag just remove it. and Put a
   space instead.
   + Also, fixer should remind me of all the patterns that
   are the same (if any two patterns are matched, please
   let us know)

-Finish editting AIML files to fit her personality
 cool_quotes.aiml add to her

-Keep a memory system where she knows about us 
 and what we like (in python). If user ever says
 what do you know about me? She will show us. How
 will this information be used? When the bored
 command in issued, she might say something that
 she knows we like, ask us about that (and hopefully
 this should steer the conversation back to her AIML
 where she can respond based on that)

-Games to play with her: Date Me Game 
 where you go on a virtual date with her ;)

******************************************************
DEPLOYMENT:
-Make it into an exe file 
-include a How to Use guide and
 what she is capable of doing, recommandations on how
 she works best
-upload it to itch.io, STEAM but 
 under the Rafael Sanchez account.
