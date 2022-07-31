   
   ######################
   AUTHOR: RAFAEL SANCHEZ
   PROJECT NAME:    LISA
   ######################
   
   WHAT IS LISA?
   **************
   LISA is a chatbot you can talk to about anything! Here you can find the source code for her. She is written in Python for the graphical user interface experience, as well as Perl for Rivescript (very similar to AIML but slightly different) as well as GPT-3 API for Open AI, which allows her to sound even more natural. Avoid complicated queries for best results.

   HOW TO TALK TO HER?
   *******************
   If you have Python installed on your system, make sure you have the libraries in chatbot_cmd.py (terminal version) installed and those in gui.py. Keep in mind that this is only the gui for Lisa, you still need to run her actual brain and consciousness, (not provided though you can find several rivescript files in the internet, especially Alice's) like a shell that needs a ghost. In the terminal you can type, python gui.py to start.
   To start up her brain: open up a unix environment (virtual machines will work) and then simply download rivescript with cpan. Then, move all her brain files to some folder (this is where she will load all her responses) and run the rivescript interpreter in TCP mode, like this:
   $ rivescript --listen localhost:2020 path/to/brain/directory
   After this, you are ready to run gui.py or chatbot_cmd.py. Here it will ask you for the IP address and Port number, which you provided when starting the server (in this case they are localhost and 2020)