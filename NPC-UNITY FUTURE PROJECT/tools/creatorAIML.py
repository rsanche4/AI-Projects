import fnmatch

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

def add_to_ing_to_verbs(filename_to_write):
    with open("english-verbs.txt", 'r') as o:
        li2 = o.readlines()
    
    fini = open(filename_to_write, 'w')

    for line in li2:
        fini.write(line)
        fini.write("to "+line)
        line=line.strip()
        if line[-1]=='e':
            line[-1]=''
            line=line+'ing'
        elif len(line)<=4 and (line[-2]=='a' or line[-2]=='e' or line[-2]=='i' or line[-2]=='o' or line[-2]=='u') and (line[-1]!='a' and line[-1]!='e' and line[-1]!='i' and line[-1]!='o' and line[-1]!='u'):
            line=line+line[-1]+'ing'
        else:
            line=line+'ing'
        fini.write(line+'\n')
    fini.close()

def turn_nouns_plural(filename_to_write):
    with open("english-nouns.txt", 'r') as o:
        li2 = o.readlines()
    
    fini = open(filename_to_write, 'w')

    for line in li2:
        fini.write(line)
        line=line.strip()
        line_list = list(line)
        if fnmatch.fnmatch(line, "*s") or fnmatch.fnmatch(line, "*ss") or fnmatch.fnmatch(line, "*sh") or fnmatch.fnmatch(line, "*ch") or fnmatch.fnmatch(line, "*x") or fnmatch.fnmatch(line, "*z") or fnmatch.fnmatch(line, "*o"):
            line_list=line_list+['es']
        
        elif fnmatch.fnmatch(line, "*f"):
            line_list[-1]='v'
            line_list=line_list+["es"]

        elif fnmatch.fnmatch(line, "*fe"):
            line_list[-2]='v'
            line_list = line_list+["s"]
        
        elif fnmatch.fnmatch(line, "*y") and line[-2]!='a' and line[-2]!='e' and line[-2]!='i' and line[-2]!='o' and line[-2]!='u':
            line_list[-1]=''
            line_list=line_list+['ies']
        
        elif fnmatch.fnmatch(line, "*y") and (line[-2]=='a' or line[-2]=='e' or line[-2]=='i' or line[-2]=='o' or line[-2]=='u'):
            line_list=line_list+['s']
        
        elif fnmatch.fnmatch(line, "*us"):
            line_list[-1]=''
            line_list[-2]='i'
        
        elif fnmatch.fnmatch(line, "*is"):
            line_list[-2]='e'

        elif fnmatch.fnmatch(line, "*on"):
            line_list[-1]=''
            line_list[-2]='a'
        
        else:
            line_list=line_list+["s"]
        
        fini.write("".join(line_list)+'\n')

    fini.close()