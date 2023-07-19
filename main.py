import math
#print("hello word")

#jedznie1=float(input("Ile kosztuje pierwszy produkt?"))
#jedznie2=float(input("Ile kosztuje drugi produkt?"))
#jedznie3=float(input("Ile kosztuje trzeci produkt?"))
#print(f"czy produkt 1 jest droższy od 2 ? {jedznie1>jedznie2} czy prukt 2 jest droższy od 3? {jedznie2>jedznie3}")
#lista_zakupow=input("wypisz liste zakupów ale prosze od przecinków bez spacji")
#odzielona=lista_zakupow.split(",")
#nie mogłem wytzymac i zrobiłem to ifem  choc nie miałem
#if len(odzielona)>5:
 #   print("długa lista")
#else:
#    print("Krótka lista")


#if elsy elsy
#if warunek1:
 #   instrukcja1
#elif warunek2:
#    instrukcja2
#else:
#    instrukcja3

#print("obliczymy czy zdałes do kolejnej klasy!")
#ocena1=float(input("podaj 1 ocene"))
#ocena2=float(input("podaj 2 ocene"))
#ocena3=float(input("podaj 3 ocene"))
#ocena4=float(input("podaj 4 ocene"))
#ocena5=float(input("podaj 5 ocene"))
#ocena6=float(input("podaj 6 ocene"))
#oceny=[ocena6,ocena5,ocena4,ocena3,ocena2,ocena1]
#srednia=(ocena6+ocena5+ocena4+ocena3+ocena2+ocena1)/float(len(oceny))
#if srednia>2:
#    print("zdałes!")
#else:
#    print("nie dałes nie robie!")
#name=input("what is your name?")
#len_name=len(name)
#ostatnia_litera=name[len_name-1:]
#if ostatnia_litera=="a":
#    print("twoje imie konczy sie na a")
#else:
#    print("twoje imie nie nkonczy sie na a")

#and or not

#prosty kalkulaotr kredytowy

#celem jest sprawdzenie czy użtkownika stać na kredyt hipoteczny o podanych parametrach

#kwota_kredytu=float(input("Podaj kwote kredytu"))
#wartosc_wlasna=float(input("podaj wartosc wkladu wlasnego "))
#czas=float(input("czas kredytu w latach "))
#przyhod=float(input("podaj przychod miesieczny "))
#oprocentowanie=float(input("podaj  oproecentowanie "))
#wydatki=float(input("podaj sume miesieczna wydatkow "))

#rata=(kwota_kredytu*oprocentowanie/100)/12+(kwota_kredytu/(czas*12))

#dostepne_srodki=przyhod-wydatki
#wartosc_nieruchomosci=wartosc_wlasna+kwota_kredytu

#if wartosc_wlasna>wartosc_nieruchomosci/5:
#    warunek1=dostepne_srodki-1000>rata
#elif wartosc_wlasna<=wartosc_nieruchomosci/5>= wartosc_nieruchomosci/10:
#    warunek1=dostepne_srodki-2000>rata
#else:
#    warunek1=False

#if   warunek1:
#    print("możesz wzaisc kredyt")
#else:
#    print(" nie mozesz")

#elif

#test coopera ale do 20 lat bo dalej mi sie nie chce/ ogólnie to zadanie niedbale zrobiłęm troche i NIe działa


plec=input(" Jestes Kobietaą czy mężczyzną ? (K/M) ")
wiek=int(input("podaj swój wiek"))
wynik=int(input("podaj swój wynik w biegu 12 mintowym"))

if plec=="M":
    if  13<=wiek<20:
        if wynik>2700:
            print("Bardzo Dobrze!")
        elif 2700>wynik>2400:
            print("dobrze")
        elif 2400 > wynik >= 2200:
            print("sredniak")
        elif 2100 > wynik > 2000:
            print("zle")
        else:
            print("bardoz zel")
    else:
        print("haha kobieta")

print("Bardzo Dobrze!")
print("dobrze")
print("średnio")
print("źle")
print("Bardzo źle!")




