'''
@author: Aleksa
'''
from random import randint
from KodStomatologa import Usluge

def ucitajPacijente():
    for linija in open("pacijenti.txt","r").readlines():
        if len(linija)>1:
            pacijent=fromStr(linija)
            cekaonica.append(pacijent)
    return

def fromStr(ln):
    if ln[-1]=="\n":
        ln=ln[:-1]
    imeIPrezime, intervencija, budzet = ln.split("|")
    budzet = budzet.strip()[3:] #karakter EURA predstavljen sa 3 karaktera
    pacijent={
     "imeIPrezime": imeIPrezime.strip(),
     "intervencije": intervencija.strip(),
     "budzet": float(budzet)  
    }
    return pacijent

def toStr(osoba):
    return "Osoba {} ceka za {} i ima budzet od {:6.2f}\u20ac".format(osoba["imeIPrezime"], osoba["intervencije"], osoba["budzet"])

def propusiDrugog(): #Propustanje sa verovatnocom od 20%
    randomBr = randint(0, 100)
    if(randomBr < 20):
        cekaonica[0], cekaonica[1] = cekaonica[1], cekaonica[0]
        print("Druga osoba uspesno propustena na prvo mesto!")
    else: print("Osoba na prvom mestu u redu nije htela da pusti drugu ispred sebe...")
    return

def dodajURed(imeIPrezime, intervencija, budzet, mesto):
    pacijent = {"imeIPrezime": imeIPrezime, "intervencije": intervencija, "budzet": float(budzet)}
    if mesto == -1:
        cekaonica.append(pacijent)
    else:
        cekaonica.insert(mesto-1, pacijent)
    return

def odradiPregled(naziv):
    cena = 0
    usluga = Usluge.pronadjiUslugu(naziv)
    if usluga != -1:
        if cekaonica[0]["budzet"] >= usluga["cena"]:
            cena += usluga["cena"]
            del cekaonica[0]
            print("Pregled uspesno obavljen...")
        else:
            del cekaonica[0]
            print("Pacijent nema dovoljno novca za uslugu...Sledeci!")
    else:
        del cekaonica[0]
        print("Trazenu uslugu nemamo u ponudi...Sledeci!")
    return cena

def toStrZaFajl(pacijent):
    return " | " .join([pacijent["imeIPrezime"], pacijent["intervencije"], pacijent["budzet"]])         

print(__name__)
cekaonica=[]  
ucitajPacijente()
