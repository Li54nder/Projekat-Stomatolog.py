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

# def proizvodtostr(rob):
#     return "|" .join([rob["sifra"],rob["ime"],rob["cena"],rob["kolicina"]])         
# 
# def formatHeader():
#     return \
#     "Sifra    |Ime          |Cena   |Kolicina \n"\
#     "--------|-------------|-------|--------"
#     
# def formatRoba(rob):
#     return u"{0:8}|{1:13}|{2:7}|{3:8}".format(
#         rob["sifra"],
#         rob["ime"],
#         rob["cena"],
#         rob["kolicina"])  
#     
# def formatRoba1(robaList):
#     r = ""
#     for rob in robaList:
#         r += formatRoba(rob) + '\n'
#     return r
# 
# def formatAllRoba():
#     return formatRoba1(roba)    
#  
# def sort(robaList,kljuc,start):
#     minPos=findMin(robaList,kljuc,start)
#     if minPos==-1:
#         return
#     robaList[start],robaList[minPos]=robaList[minPos],robaList[start]
#     if start < len(robaList)-1:
#         sort(robaList,kljuc,start+1)
#     return
# 
# def sortProizvodi(kljuc):
#     sort(roba,kljuc,0)        
#         
# def findMin(robaList,kljuc,start):
#     n=len(robaList)
#     if n==0:
#         return -1
#     if n<=start:
#         return -1
#     if n-start==1:
#         return start    
#     min=robaList[start]
#     minPos=start
#     for i in range(start+1,n):
#         if robaList[i][kljuc]<min[kljuc]:
#             min=robaList[i]
#             minPos=i
#     return minPos
# 
# def minusStanje(rob,kolicina):
#     
#     if eval(rob['kolicina']) >= kolicina:
#         rob['kolicina']=str(int(rob['kolicina'])-kolicina)
#         print("Roba", rob['sifra']," je smanjena na stanju")
#     else:
#         print("Ima manje robe na stanju nego sto ste uneli!")
#     
#     
#     
# def plusStanje(rob,kolicina):
#     rob["kolicina"]=str(int(rob["kolicina"])+kolicina)

    
     
print(__name__)
usluge=[]  
ucitajUsluge()
