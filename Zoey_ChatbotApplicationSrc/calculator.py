def calcut(m):
    if "+" in m:
        l=m.split('+')
        s1=l[0].strip()
        if s1.isnumeric():
            n1=float(s1)
            s2=l[1].strip()
            if s2.isnumeric():
                n2=float(s2)
                return str(n1+n2)
            else:
                return "If you are trying to calculate something, just type in this format: number operator number (Ex: 1 + 3)"
        else:
            return "If you are trying to calculate something, just type in this format: number operator number (Ex: 1 + 3)"
    elif "*" in m:
        l=m.split('*')
        s1=l[0].strip()
        if s1.isnumeric():
            n1=float(s1)
            s2=l[1].strip()
            if s2.isnumeric():
                n2=float(s2)
                return str(n1*n2)
            else:
                return "If you are trying to calculate something, just type in this format: number operator number (Ex: 1 + 3)"
        else:
            return "If you are trying to calculate something, just type in this format: number operator number (Ex: 1 + 3)"
    elif "-" in m:
        l=m.split('-')
        s1=l[0].strip()
        if s1.isnumeric():
            n1=float(s1)
            s2=l[1].strip()
            if s2.isnumeric():
                n2=float(s2)
                return str(n1-n2)
            else:
                return "If you are trying to calculate something, just type in this format: number operator number (Ex: 1 + 3)"
        else:
            return "If you are trying to calculate something, just type in this format: number operator number (Ex: 1 + 3)"
    elif "/" in m:
        l=m.split('/')
        s1=l[0].strip()
        if s1.isnumeric():
            n1=float(s1)
            s2=l[1].strip()
            if s2.isnumeric():
                n2=float(s2)
                if n2==0.0:
                    return "Can't divide by zero... I think."  
                else:
                    return str(n1/n2)
            else:
                return "If you are trying to calculate something, just type in this format: number operator number (Ex: 1 + 3)"
        else:
            return "If you are trying to calculate something, just type in this format: number operator number (Ex: 1 + 3)"