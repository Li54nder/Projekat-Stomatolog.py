'''
@author: Aleksa
'''
def ucitajUsluge():
    for ln in open("usluge.txt","r").readlines():
        if len(ln)>1:
            usluga=fromStr(ln)
            usluge.append(usluga)
    return

def fromStr(ln):
    if ln[-1]=="\n":
        ln=ln[:-1]
    pregled, intervencija, cena = ln.split("|")
    cena = cena.strip()[3:]
    usluga={
     "vrstaPregleda": pregled.strip(),
     "nazivIntervencije": intervencija.strip(),
     "cena": float(cena.replace(',', '.'))  
    }
    return usluga

def pronadjiUslugu(naziv):
    for usluga in usluge:
        if usluga["nazivIntervencije"].lower() == naziv.lower():
            return usluga
    return -1

def pregledUFajl(usluga):
    tmp1 = usluga["intervencija"]
    tmp2 = usluga["cena"]
    return "Intervencija {} po ceni od {:6.2f}\u20ac".format(tmp1, tmp2)

def sortirajUsluge():
    sortiraj(0)
    
def sortiraj(pos):
    minPos = najjeftinijaUsluga(pos)
    if minPos != -1:
        usluge[pos], usluge[minPos] = usluge[minPos], usluge[pos]
        if pos < len(usluge) - 1:
            sortiraj(pos + 1)
    return

def najjeftinijaUsluga(pos):
    n = len(usluge)
    if n <= pos: return -1
    minPos = pos
    minC = usluge[minPos]
    for i in range(pos+1, n):
        if usluge[i]["cena"] < minC["cena"]:
            minC = usluge[i]
            minPos = i
    return minPos
  
     
print(__name__)
usluge=[]  
ucitajUsluge()
