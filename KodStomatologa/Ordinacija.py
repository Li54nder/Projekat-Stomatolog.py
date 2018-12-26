'''
@author: Aleksa
'''

from KodStomatologa import Stomatolog, Usluge, Cekaonica
from KodStomatologa.Cekaonica import cekaonica

    
def login():
    print(">>> Ulogujte se kao stomatolog:")
    username = input("Korisnicko ime: ")
    password = input("Lozinka: ")
    return Stomatolog.login(username, password)

def main():
    print("\nxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print("x                          x")
    print("x  Ordinacija Denta Milic  x")
    print("x                          x")
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxx\n")
    if not login():
        print("\nNeispravno korisnicko ime ili lozinka!!! \nPonovo pokrenite program i pokusajte ponovo...")
        return
    naredba='0'
    while naredba != 'k':
        naredba = meni()
        if naredba =='1':
            brLjudiUCekaonici()
        elif naredba =='2':
            ljudiUCekaonici()
        elif naredba =='3':
            dodajOsobuURed()
        elif naredba =='4':
            pustiPrekoReda()
        elif naredba =='5':
            odradiPregled() 
        elif naredba =='6':
            zaradjenaSuma() 
        elif naredba =='7':
            stampajUsluge()  
        elif naredba =='k':
            obavljeniPregledi()
    print("\n\nProgram powered by Aleksa Novkovic")
def meni():
    stampajMeni()
    naredba = input(">>> ")
    while naredba.lower() not in ('1', '2', '3', '4', '5', '6', '7', 'k'):
        print( "Neispravna komanda.\n")
        naredba = input(">>> ")
    return naredba.lower()        
def stampajMeni():
    print("\n>>> Izaberite opciju: <<<") 
    print("1 - Koliko ljudi ceka u redu u cekaonici")
    print("2 - Ko sve ceka u redu")
    print("3 - Dodaj osobu u red")
    print("4 - Proveri da li ce drugu osobu pustiti preko reda")
    print("5 - ODRADI PREGLED...")
    print("6 - Pogledaj dosadasnju zaradjenu sumu")
    print("7 - INTERVENCIJE(usluge) NA RASPOLAGANJU")
    print("k - Kraj (zavrsi sa pregledima za danas)")   

def brLjudiUCekaonici():
    print( "\n1 - Koliko ljudi ceka u redu u cekaonici\n")
    print("U cekaonici ima jos ",len(Cekaonica.cekaonica),"osoba.")
                
def ljudiUCekaonici():
    print("\n2 - Ko sve ceka u redu\n")
    for osoba in Cekaonica.cekaonica:
        print(Cekaonica.toStr(osoba))
    return

def dodajOsobuURed():
    print("\n3 - Dodaj osobu u red\n\n>>>Podaci o osobi:")
    imeIPrezime = input("Ime i prezime\n>>> ")
    intervencija = input("Intervencija koju osoba zeli da izvrsi\n(ako niste sigurni unesite: \"odustajem\" i pogledajte koje intervencije imamo na raspolaganju)\n>>> ")
    if intervencija.lower() == "odustajem":
        return
    budzet = input("Novac koji osoba ima kod sebe\n(da bi mogli da vidimo ima li dovoljno novca za pregled)\n>>> ")
    zakazano = input("Da li osoba ima zakazano: (da/ne)\n>>> ")
    if zakazano == "da":
        mesto = eval(input("Koje mesto u redu je osoba rezervisala zakazivanjem\n>>> "))
    else: mesto = -1
    Cekaonica.dodajURed(imeIPrezime, intervencija, budzet, mesto) #intervencija se proverava...

def pustiPrekoReda():
    print("\n4 - Proveri da li ce drugu osobu pustiti preko reda\n")
    Cekaonica.propusiDrugog()

def odradiPregled():
    print("\n5 - ODRADI PREGLED...\n")
    global zarada
    if not cekaonica:
        print("Cekaonica je prazna!") 
        return
    nazivIntervencije = Cekaonica.cekaonica[0]["intervencije"]
    zaradaOdPregleda = Cekaonica.odradiPregled(nazivIntervencije)
    usluga = Usluge.pronadjiUslugu(nazivIntervencije)
    if(zarada != (zarada+zaradaOdPregleda)):
        zarada += zaradaOdPregleda
        pregledi.append({"intervencija": nazivIntervencije, "cena": usluga["cena"]})
    return

def stampajUsluge():
    print("\nUsluge koje imamo na raspolaganju sortirane po ceni rastuce su:\n")
    Usluge.sortirajUsluge()
    for usluga in Usluge.usluge:
        print(" -> {} = {:6.2f}\u20ac".format(usluga["nazivIntervencije"], usluga["cena"]))
    print()

def zaradjenaSuma():
    print("\n6 - Pogledaj dosadasnju zaradjenu sumu\n")
    print("Dosadasnja zaradjena suma novca je: {:6.2f}\u20ac".format(zarada))

def obavljeniPregledi():
    print('\nObavljeni pregledi ce se zavesti u knjigu pregleda...\nLjude koje niste pregledali poslali smo kucama...\n')
    with open('KnjigaObavljenihPregleda.txt', 'a') as f:
        f.write("Obavljeni pregldedi:\n")
        for pregled in pregledi:
            f.write("%s\n" % Usluge.pregledUFajl(pregled))
    return

print(__name__)
zarada = 0
pregledi = []
if __name__ == '__main__':
    main()