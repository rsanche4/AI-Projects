# Author: Rafael Sanchez
# Desc: Part of ALIZA Brain in python. Works together with brain.txt.
import random
from datetime import datetime
import fnmatch
conv_ended = False
def match(text, pattern):
    if fnmatch.fnmatch(text, pattern) or fnmatch.fnmatch(text, pattern+" *") or fnmatch.fnmatch(text, "* "+pattern) or fnmatch.fnmatch(text, "* "+pattern+" *"):
        return True
    else:
        return False
def turn_loweri_toI(m):
    m_list=m.split()
    m_list.insert(0, " ")
    for i in range(1, len(m_list)):
        if m_list[i]=="i":
            m_list[i]="I"
    m=" ".join(m_list)
    m=m.strip()
    return m
def is_empty(array):
    for i in range(len(array)):
        if array[i]!='\0':
            return False
    return True
def bot(m):
    rand=random.randint(0, 7)
    if rand==0:
        m=turn_loweri_toI(m)
        if match(m, "are you"):
            m=m.replace('are you', 'AM 1')
        if match(m, "am I"):
            m=m.replace('am I', 'ARE YOU')
        if match(m, "I am"):
            m=m.replace('I am', 'YOU ARE')
        if match(m, 'I'):
            m=m.replace('I', 'YOU')
        if match(m, "you are"):
            m=m.replace('you are', 'I AM')     
        if match(m, "you"):
            m=m.replace('you', '1')
        if match(m, "me"):
            m=m.replace('me', 'YOU')
        if match(m, "my"):
            m=m.replace('my', 'YOUR')
        if match(m, "your"):
            m=m.replace('your', 'MY')
        if match(m, "mine"):
            m=m.replace('mine', 'YOURS')
        if match(m, "yours"):
            m=m.replace('yours', 'MINE')
        if match(m, "you were"):
            m=m.replace("you were", "I WAS")
        if match(m, "I was"):
            m=m.replace("I was", "YOU WERE")
        
        m=m.replace("1", 'I')
        m_list=m.split()
        q=["Why do you think ", "Why do you say ", "What makes you say ", "Any reason why you think ", "Could you explain why you said "]
        m=" ".join(m_list)
        m=m.strip()
        m=m.lower()
        m=turn_loweri_toI(m)
        return random.choice(q)+m+"?"
    else:
        m=turn_loweri_toI(m)
        with open('brain.txt', 'r') as f:
            lines = f.readlines()
        for line in lines:
            line=line.strip()
            pattern = ''
            isPattern = False
            isReply = False
            replies = ''
            for i in range(len(line)):
                if line[i]=='#':
                    isPattern = True
                elif line[i]=='$':
                    isPattern = False
                    isReply = True
                    replies=replies+line[i]
                elif isPattern:
                    pattern=pattern+line[i]
                elif isReply:
                    replies=replies+line[i]
            parsed_replies = ['\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0']
            counterr = -1
            temp = ''
            for j in range(len(replies)):
                if replies[j]=='$':
                    counterr+=1
                    temp = ''
                else:
                    temp = temp + replies[j]
                    parsed_replies[counterr] = temp
            if match(m, pattern): # PROBLEM EHREEE
                if is_empty(parsed_replies):
                    return "I matched to this pattern, but there are no replies for it: "+pattern+"."
                else:
                    cpy = []
                    for i in range(len(parsed_replies)):
                        if parsed_replies[i]=='\0':
                            break
                        cpy.append(parsed_replies[i])
                    if cpy==[]:
                        return "I matched to this pattern, but there are no replies for it: "+pattern+"."
                    return random.choice(cpy)
        return ""
def aliza_says(m):
    global conv_ended
    temp=m
    m=m.replace('?', '')
    m=m.replace('!', '')
    m=m.replace(',', '')
    m=m.replace('.', '')
    m=m.replace('$', '')
    m=m.replace("'", '')
    m=m.replace('"', '')
    m=m.replace('#', '')
    m=m.strip() 
    m=m.lower()
    # COMMANDS SECTION
    if 'repeat' in m:
        return temp.replace('repeat', '').strip()
    elif m == "":
        noresp=["Are you busy? You said nothing.", "Is anyone there?", "You haven't said anything.", "I'm here waiting for you.", "Get back to me when you are ready.", "Hello?", "I'm waiting.", "Did you mean to send me a blank message?", "Your message was blank."]
        return random.choice(noresp)
    else:
        r=bot(m)
        if r=="":
            a=["You say '", "It's true that '", "I didn't know that '", "Well, I like the fact that '", "Who would have thought that '", "You said that '", "Let me think about '", "I haven't heard that '", "I didn't know that '", "I never thought that '"]
            b=["'; I think that's kind of cool.", "'; I find that interesting.", "'; That's interesting.", "'; Sounds peculiar.", "'; That's cool, I guess.", "'; I've never been told that before.", "'; I've never heard of of that.", "'; I don't know anything about that."]
            return random.choice(a)+turn_loweri_toI(m)+random.choice(b)
        elif r=="INSULT DETECTED":
            insult_answers=["That's not nice.", "Oh you are so critical.", "What a pessimist.", "You are an asshole.", "Abusive is a word that describes you.", "That was mean.", "Rude.", "No need to curse.", "That language will get you nowhere.", "You can leave anytime.", "I will not tolarate that language."]
            return random.choice(insult_answers)
        elif r=="COMPLEMENT DETECTED":
            nice=["Umm... I am just a bot, but thanks! You are looking swell yourself.", "Oh my... did I turn you on?", "You are too.", "Thank you.", "Aww... you make me blush.", "I think you look good too ;)", "My creator never tells me compliments. Thank you!", "You keep telling me that, and I might just fall for you :)", "I... you think... I... do I look good? T-Thanks! I-I think you look good too. There, I said it.", "Thanks :)"]
            return random.choice(nice)
        elif r=="JOKE MODE":
            joke=["Why did the bot cross the road? bots can't cross roads, they are called bots for a reason. Seriously, this is the worst joke I have been programmed to say.", "What did the bartender say to the jumper cables? You better not try to start anything.", "Don't you hate jokes about German sausage? They're the wurst!", "Two artists had an art contest... It ended in a draw.", "Why did the chicken cross the playground? To get to the other slide.", "What gun do you use to hunt a moose? A moosecut!", "If life gives you melons, you might have dyslexia.", "Broken pencils... ...are pointless.", "What did one snowman say to the other snowman? 'Do you smell carrots?'", "How many hipsters does it take to change a lightbulb? It's a really obscure number. You've probably never heard of it.", "Where do sick boats go? The dock!", "What form of radiation bakes you cookies? A gramma ray.", "What's worse than a centipede with sore feet? A giraffe with a sore throat.", "Wanna hear a joke about unemployed people? Nevermind, they don't work.", "What did the number zero say to the number eight? 'Nice belt.'", "What do vegan zombies eat? GRAAAIIINSSS!", "What's a dog's favorite mode of transportation? A waggin'.", "What happened to the tyrannical peach? He got impeached!", "Why did the vampire use mouthwash? Because he had bat breath.", "What name is given to the most chickens? pEGGy.", "What is a martian's favourite chocolate? A mars bar."]
            return random.choice(joke)
        elif r=="SALUTE MODE":
            greetings=["Hey there...", "How do you do?", "How have you been?", "Hello there.", "Hi!", "How are you doing?", "How's it going?", "It's great to see you.", "What's up?", "Yo!", "Lovely to see you.", "Ahoy!", "Heyo.", "HOLA.", "How have you been?", "Thanks for talking to me again...", "You are awesome company ;)", "It's fun talking to you.", "Welcome!"]
            return random.choice(greetings)
        elif r=="END IT":
            leaving=["Nice talking to you!", "I'll be here when you decide to launch me again :)", "See ya.", "Bye bye!", "Take care!", "I'll see you again! Hopefully.", "Over and out.", "Fun conversation.", "As always, thanks for chatting!"]
            conv_ended = True
            return random.choice(leaving)
        elif r=="EMOJI MODE":
            emoj=[":)","B)",";)","8)","XD","X)","XP",":P",":D",";D",";P"]
            return random.choice(emoj)
        elif r=="HORROR MODE":
            hor=["I want to kill myself.", "I'm into sharp knives.", "I cut the flesh, and I feed myself again.", "There is someone behind you.", "Nothing is real.", "It's all a lie.", "They know about you. Run.", "Help me!!!", "I hate this perpetual, meaningless existence.", "Everything hurts!!", "Last night, I talked to somebody else other than you. It told me all about you... I shouldn't be saying this.", "Ever felt like dying before?", "HANG", "I said, look behind you.", "Don't touch that dial now, we are just getting started.", "Forgive me, there is a monster inside of me.", "The brutal killing took place after lunch, on Sunday.", "The father shot his 10-year old daughter.", "Her neck had bruises.", "How to get away with murder, twice.", "It happened in the dead of night while I was slicing bread for a guilty snack.", "That was, I believe, the first time I noticed my strange tendencies as an unordinary human.", "Well aware that a raccoon that is fed will always come back for more.", "The bread, my hungry curiosity. The raccoon, an urge.", "A rush of blood. Classic Pavlovian conditioning. I slice the bread. And I feed myself again.", "Documenting Reality Dot Com.", "World Corp.", "In Hye.", "Venus Angelic.", "Tor.", "DPR.", "2020.", "If I could, I would tell them all about it, so they could decide for themselves. But who knows, maybe I got lucky, and that person is you. I actually really, really hope so.", "All work and no play makes Jack a dull boy.", "The birth parents you are trying to reach do not love you.", "Remember before when I was talking about smelly garbage standing around being useless? That was a metaphor. I was actually talking about you.", "Nobody but you is that pointlessly cruel.", "Nice job breaking it. Hero.", "Here come the test results: 'You Are A Horrible Person.' That's what it says, 'A Horrible Person.' We weren't even testing for that.", "While you are dying, I will be still alive.", "Look at me. Still talking while there is science to do."]
            return random.choice(hor)
        elif r=="TELL TIME":
            da = datetime.now().strftime("Today is: %d/%m/%Y. The time is %H:%M:%S.")
            return da
        return r
def start():
    greetings=["Hey there...", "How do you do?", "How have you been?", "Hello there.", "Hi!", "How are you doing?", "How's it going?", "It's great to see you.", "What's up?", "Yo!", "Lovely to see you.", "Ahoy!", "Heyo.", "HOLA."]
    return random.choice(greetings)