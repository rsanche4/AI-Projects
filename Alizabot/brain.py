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
def swaps(m):
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
    if match(m, "myself"):
        m=m.replace("myself", "YOURSELF")
    if match(m, "yourself"):
        m=m.replace("yourself", "MYSELF")
    m=m.replace("1", 'I')
    m_list=m.split()
    m=" ".join(m_list)
    m=m.strip()
    m=m.lower()
    m=turn_loweri_toI(m)
    return m
def bot(m, brain_path):
    rand=random.randint(0, 16)
    if rand==0:
        q=["Why do you think ", "Why do you say ", "What makes you say ", "Any reason why you think ", "Could you explain why you said "]
        return random.choice(q)+swaps(m)+"?"
    else:
        m=turn_loweri_toI(m)
        with open(brain_path, 'r') as f:
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
            parsed_replies = ['\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0']
            counterr = -1
            temp = ''
            for j in range(len(replies)):
                if replies[j]=='$':
                    counterr+=1
                    temp = ''
                else:
                    temp = temp + replies[j]
                    parsed_replies[counterr] = temp
            old_pattern = pattern
            pattern = pattern.replace(' +', '')
            if match(m, pattern):
                if is_empty(parsed_replies):
                    return "I matched to this pattern, but there are no replies for it: "+old_pattern+"."
                else:
                    appending_words = ''
                    there_is_plus = False
                    if old_pattern[len(old_pattern)-1]=='+':
                        there_is_plus = True
                        k=len(old_pattern)-3
                        last_word = ''
                        while old_pattern[k]!=' ' and k>=0:
                            last_word = last_word + old_pattern[k]
                            k-=1
                        last_word = last_word[::-1]
                        curr_word = ''
                        last_word_index_in_m = 0
                        for l in range(len(m)):
                            if m[l]==' ':
                                if curr_word==last_word:
                                    last_word_index_in_m = l
                                    break
                                else:
                                    curr_word = ''
                            else:
                                curr_word = curr_word + m[l]
                        for n in range(last_word_index_in_m+1, len(m)):
                            appending_words = appending_words + m[n]
                    cpy = []
                    for i in range(len(parsed_replies)):
                        if parsed_replies[i]=='\0':
                            break
                        cpy.append(parsed_replies[i])
                    if cpy==[]:
                        return "I matched to this pattern, but there are no replies for it: "+old_pattern+"."
                    final = random.choice(cpy)
                    if there_is_plus:
                        if ('how ' in final.lower() or 'what ' in final.lower() or 'who ' in final.lower() or 'when ' in final.lower() or 'why ' in final.lower() or 'where ' in final.lower() or 'do you ' in final.lower()) and '?' not in final:
                            final = final +' '+swaps(appending_words)+'?'
                        else:
                            final = final +' '+swaps(appending_words)+'.'
                    return final
        return ""
def open_brain(m, brain_path):
    with open(brain_path, 'r') as f:
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
        parsed_replies = ['\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0']
        counterr = -1
        temp = ''
        for j in range(len(replies)):
            if replies[j]=='$':
                counterr+=1
                temp = ''
            else:
                temp = temp + replies[j]
                parsed_replies[counterr] = temp
        if match(m, pattern):
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
def aliza_says(m, brain_path="brain.txt"):
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
    m=m.replace('*', '')
    m=m.replace('+', '')
    m=m.strip() 
    m=m.lower()
    # COMMANDS SECTION
    if 'repeat' in m[0:7] or 'say' in m[0:3]:
        temp = temp.lower()
        temp = temp.replace('repeat', '').strip()
        temp = temp.replace('say', '').strip()
        return swaps(temp)
    elif m == "":
        return "Your message was blank."
    else:
        r=bot(m, brain_path)
        if r=="":
            return open_brain("NOTFOUND", brain_path)
        elif r=="INSULT DETECTED":
            return open_brain("INSULT", brain_path)
        elif r=="COMPLEMENT DETECTED":
            return open_brain("COMPLEMENT", brain_path)
        elif r=="JOKE MODE":
            return open_brain("JOKES", brain_path)
        elif r=="SALUTE MODE":
            return open_brain("SALUTE", brain_path)
        elif r=="END IT":
            conv_ended = True
            return open_brain("FIN", brain_path)
        elif r=="EMOJI MODE":
            return open_brain("EMOJI", brain_path)
        elif r=="HORROR MODE":
            return open_brain("HORROR", brain_path)
        elif r=="TELL TIME":
            da = datetime.now().strftime("Today is: %d/%m/%Y. The time is %H:%M:%S.")
            return da
        return r
def start(brain_path="brain.txt"):
    return open_brain("START", brain_path)