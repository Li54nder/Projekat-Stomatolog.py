'''
@author: Aleksa
'''
def loadDr():
    line = open("stomatolog.txt","r").readline()
    if len(line)>1:
        dr=fromStr(line)
        stomatolog.append(dr)
    return
       
def fromStr(line):
    if line[-1]=="\n":
        line=line[:-1]
    punoIme,username,password=line.split("|")  
    dr={
     "punoIme": punoIme.strip(),
     "username": username.strip(),
     "password": password.strip(),
     }
    return dr

def toStr(dr):
    s = " | "
    s = s.join([dr[0]["punoIme"], dr[0]["username"], dr[0]["password"]])
    return s

def login(username,password):
    if stomatolog[0]["username"]==username and stomatolog[0]["password"]==password:
        return True
    return False


print(__name__)
stomatolog=[]
loadDr()
# print(toStr(stomatolog))