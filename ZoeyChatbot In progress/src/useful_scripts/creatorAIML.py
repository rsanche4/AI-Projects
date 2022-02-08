def simple_nouns():
    with open("english-nouns.txt", 'r') as f:
        lines1 = f.readlines()
        lines2 = lines1

    g = open("simple_sentences_nouns.aiml", 'w')
    g.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    g.write('<aiml>\n')

    for line in lines1:
        for lin in lines2:
            line = line.strip()
            lin = lin.strip()
            a=line.upper()+" * "+lin.upper()
            b=line.upper()+" * "+lin.upper()+" * "
            c=" * "+line.upper()+" * "+lin.upper()
            d=" * "+line.upper()+" * "+lin.upper()+" * "
            g.write('<category><pattern>'+ a +'</pattern><template><random><li><srai>'+ lin.upper() +'</srai></li><li><srai>'+ line.upper() +'</srai></li></random></template></category>\n')
            g.write('<category><pattern>'+ b +'</pattern><template><random><li><srai>'+ lin.upper() +'</srai></li><li><srai>'+ line.upper() +'</srai></li></random></template></category>\n')
            g.write('<category><pattern>'+ c +'</pattern><template><random><li><srai>'+ lin.upper() +'</srai></li><li><srai>'+ line.upper() +'</srai></li></random></template></category>\n')
            g.write('<category><pattern>'+ d +'</pattern><template><random><li><srai>'+ lin.upper() +'</srai></li><li><srai>'+ line.upper() +'</srai></li></random></template></category>\n')

    g.write('</aiml>\n')
    g.close()

# ---------------------------------------------------------------

def simple_adjectives():
    with open("english-nouns.txt", 'r') as p:
        l1 = p.readlines()

    with open("english-adjectives.txt", 'r') as m:
        l2 = m.readlines()

    k = open("simple_sentences_adjectives.aiml", 'w')
    k.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    k.write('<aiml>\n')

    for line in l1:
        for lin in l2:
            line = line.strip()
            lin = lin.strip()
            a=line.upper()+" * "+lin.upper()
            b=line.upper()+" * "+lin.upper()+" * "
            c=" * "+line.upper()+" * "+lin.upper()
            d=" * "+line.upper()+" * "+lin.upper()+" * "
            k.write('<category><pattern>'+ a +'</pattern><template><random><li><srai>'+ lin.upper() +'</srai></li><li><srai>'+ line.upper() +'</srai></li></random></template></category>\n')
            k.write('<category><pattern>'+ b +'</pattern><template><random><li><srai>'+ lin.upper() +'</srai></li><li><srai>'+ line.upper() +'</srai></li></random></template></category>\n')
            k.write('<category><pattern>'+ c +'</pattern><template><random><li><srai>'+ lin.upper() +'</srai></li><li><srai>'+ line.upper() +'</srai></li></random></template></category>\n')
            k.write('<category><pattern>'+ d +'</pattern><template><random><li><srai>'+ lin.upper() +'</srai></li><li><srai>'+ line.upper() +'</srai></li></random></template></category>\n')

    k.write('</aiml>\n')
    k.close()

# ---------------------------------------------------------------

def simple_verbs():
    with open("english-nouns.txt", 'r') as i:
        li1 = i.readlines()

    with open("english-verbs.txt", 'r') as o:
        li2 = o.readlines()

    fi = open("simple_sentences_verbs.aiml", 'w')
    fi.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    fi.write('<aiml>\n')

    for line in li1:
        for lin in li2:
            line = line.strip()
            lin = lin.strip()
            a=line.upper()+" * "+lin.upper()
            b=line.upper()+" * "+lin.upper()+" * "
            c=" * "+line.upper()+" * "+lin.upper()
            d=" * "+line.upper()+" * "+lin.upper()+" * "
            fi.write('<category><pattern>'+ a +'</pattern><template><random><li><srai>'+ lin.upper() +'</srai></li><li><srai>'+ line.upper() +'</srai></li></random></template></category>\n')
            fi.write('<category><pattern>'+ b +'</pattern><template><random><li><srai>'+ lin.upper() +'</srai></li><li><srai>'+ line.upper() +'</srai></li></random></template></category>\n')
            fi.write('<category><pattern>'+ c +'</pattern><template><random><li><srai>'+ lin.upper() +'</srai></li><li><srai>'+ line.upper() +'</srai></li></random></template></category>\n')
            fi.write('<category><pattern>'+ d +'</pattern><template><random><li><srai>'+ lin.upper() +'</srai></li><li><srai>'+ line.upper() +'</srai></li></random></template></category>\n')

    fi.write('</aiml>\n')
    fi.close()

# ---------------------------------------------------------------

def react(filename_to_read, filename_to_write, count=1):
    print('Input EXIT as an answer to the input if you want to quit. Keep in mind, after going through everything, you need to go back to the document and add <aiml> </aiml> tag as well as <?xml version="1.0" encoding="UTF-8"?>')
    with open(filename_to_read, 'r') as u1:
        lin1 = u1.readlines()

    fini = open(filename_to_write, 'a')

    init_count = 0
    count-=1
    for line in lin1:
        if init_count!=count:
            init_count+=1
            continue
        init_count+=1
        count+=1
        line = line.strip()
        text1 = input("What answer 1 would you like to input for " + line + ": ")
        text2 = input("What answer 2 would you like to input for " + line + ": ")
        if text1 == "EXIT" or text2 == "EXIT":
            print("Left at line " + str(count) + ".")
            break
        fini.write('<category><pattern>'+ line.upper() +'</pattern><template><random><li>'+ text1 +'</li><li>'+ text2 +'</li></random></template></category>\n')
        fini.write('<category><pattern>* '+ line.upper() +'</pattern><template><random><li>'+ text1 +'</li><li>'+ text2 +'</li></random></template></category>\n')
        fini.write('<category><pattern>'+ line.upper() +' *</pattern><template><random><li>'+ text1 +'</li><li>'+ text2 +'</li></random></template></category>\n')
        fini.write('<category><pattern>* '+ line.upper() +' *</pattern><template><random><li>'+ text1 +'</li><li>'+ text2 +'</li></random></template></category>\n')
        print("Wrote texts to " + filename_to_write +".")
        
    fini.close()

# ---------------------------------------------------------------

# first do combinations on all the nouns and then use the wildcard for You or I. Also don't forget to turn to plural.
# noun + noun
# Fly * cheek
# Fly * cheeks
# Flies * cheek
# Flies * cheeks
# Fly * cheek *
# Fly * cheeks *
# Flies * cheek *
# Flies * cheeks *
# * Fly * cheek
# * Fly * cheeks
# * Flies * cheek
# * Flies * cheeks
# * Fly * cheek *
# * Fly * cheeks *
# * Flies * cheek *
# * Flies * cheeks *

# noun + verb
# Cake * to think
# Cakes * to think
# Cake * to think *
# Cakes * to think *
# * Cake * to think
# * Cakes * to think
# * Cake * to think *
# * Cakes * to think *
# Cake * thinking
# Cakes * thinking
# Cake * thinking *
# Cakes * thinking *
# * Cake * thinking
# * Cakes * thinking
# * Cake * thinking *
# * Cakes * thinking *

# noun + adj
# Moon * white
# Moons * white
# Moon * white *
# Moons * white *
# * Moon * white
# * Moons * white
# * Moon * white *
# * Moons * white *

# ------------------------------------------------------------------------------------------
# Ex: Pronoun and anything else that is not recognizable
# noun
# cheek *
# * cheek 
# * cheek *
# cheeks *
# * cheeks 
# * cheeks *

# verb
# to think *
# * to think 
# * to think *
# thinking *
# * thinking 
# * thinking *

# adj
# white *
# * white
# * white *

# ------------------------------------------------------------------------------------------

# Now there is another set of statements that should be looked at: Compliments and Insults (if user insults her, she should be sarcastic, rude, as well) (You are dumb, You look cute, thank you for being here, I like you)
# You * dumb
# You * dumb *
# * You * dumb
# * You * dumb *
# Same thing with compliments (in above case she reacts to dumb)

# Also user might say things like: That's tragic, or that's funny, or that's sad. (So we need to incorparate phrases the user says that are reactions to something Zoey said. Oh wow. I'm suprised. That's crazy. That's wild. That's sad, among others you can think of)

# Also user might ask certain questions to her. This shall be handled by the questions.aiml. Any questions not handled by the logical or what's google functionality (is that true? Is that so?)

# ----------------------------

# Sample program run:
# Z: Hey there! (zoey just says hi)
# u: Hi
# Z: hello (zoey responds to a hi statement from user)
# u: I feel good
# Z: That's good to hear. (zoey reacts to the word "good")
# u: I am bored.
# Z: I get bored when you don't launch me often. (reacting to 'bored')
# u: I really like you.
# Z: That's nice to hear. I like you too! (this is handled by the Compliments and Insults handler)
# u: I love you.
# Z: You sure you want to love a robot? Loving a human might be better for you. (again, C and I)
# u: Is that true?
# Z: That is certaintly true. (this is reacting from the questions.aiml)
# u: I dont know what to say.
# Z: I can't really say much, but I'd say you said something cool. (reacting to "to say")
# u: What did I say that was cool? 
# Z: I'm looking that up in google. (finds the 'what' and looks the rest of the sentence up)
# u: Cool.
# Z: Yessir! (Again, the compliments and insults document)
# u: this was a cool conversation
# Z: I like talking! (reacts to 'conversation')

# -------------------------------------------------

# add the still alive functionality
# also add games we can play with her (black jack)
# Tell me a joke functionality
# Tell me a story functionality

# ----------------