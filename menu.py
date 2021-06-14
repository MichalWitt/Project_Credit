from obliczenia import *
import time
def kwota():
    total = ""
    total += str(podsumuj(zamowienie))
    file = open("kwota_total", 'a')
    print(total, file=file)
    file.close()

    """with open(the_filename, 'w') as f:
    for s in my_list:
        f.write(s + '\n')
    """    
    with open("kwota_total", 'r') as f:
        my_list = [line.rstrip('\n') for line in f]
    my_list = list(map(int, my_list))
    return sum(my_list)
               
    
twoje = {}
skladniki = {
    "feta" : 4,
    "szczypiorek" : 3,
    "cebula" : 3,
    "kapary" : 5,
    "oliwki" : 4,
    "burak" : 3,
    "tuńczyk" : 6,
    "łosoś" : 6,
    "parmezan" : 5,
    "pomidory" : 4
}
zamowienie = {}
gotowe = {
    "hawajska" : 18,
    "polska" : 15,
    "americano" : 24,
    "grecka" : 19,
    "tuna" : 25,
    "bogatta" : 30,
    "letnia" : 17
} 

def menu():
    print(' ___________________________________________')
    print('|Wybierz jedną z poniższych opcji:          |')
    print('|                                           |')
    print('|1 - Wybierz salatke                        |')
    print('|2 - Skomponuj wlasna salatke               |')
    print('|3 - Podsumuj Twoje zamówienie              |')
    print('|4 - Przeglądaj logi                        |')
    print('|5 - Wyjdź z programu                       |')
    print('|___________________________________________|')
    wybor = input(":")
    if wybor == "1":
        wybierz_salatke()
    elif wybor == "2":
        skomponuj()
    elif wybor == "3":
        if zamowienie:
            final()
        else:
            print("Brak zamówienia.")
            menu()         
    elif wybor == "4":
        text = open('logi.txt').read()
        print(text)
        wybor = input("Nacisnij 1 aby wyjść z programu, 2 aby wrócić do menu.")
        if wybor == "1":
            exit()
        elif wybor == "2":
            menu()
        
    elif wybor == "5":
        exit()

def skomponuj():
    n=0
    print("*********************************************")
    for skladnik in skladniki:
        n+=1        
        print(n,".", skladnik+",",skladniki[skladnik],"zł")
    print("*********************************************")
    nazwa = input("Podaj nazwę składnika: ")
    if nazwa in skladniki:
        if nazwa in twoje:
            print("")
            powtorka = input("Składnik został już dodany.\n\nPotwierdzasz wybór? T/N: ")
            if powtorka == "T":
                for i in twoje:
                    if i == nazwa: 
                        twoje[i]=twoje[i]+skladniki[i]
                print("****************************")
                print("Składnik został dodany.")
                print("*****************************")
                print("Twoja sałatka (własna kompozycja):")
                print("")
                for element in twoje:
                    print("-", element+",", twoje[element], "zł")
                print("")
                print("Wartość zamówienia: ",podsumuj(twoje),"zł")
                print("*****************************")
                suma = podsumuj(twoje)
                zamowienie['własna kompozycja'] = suma
            elif powtorka == "N":
                menu()
            else:
                print("Błędny wybór.")
                menu()
        else:        
            for i in skladniki:
                if i == nazwa:
                    twoje[i]=skladniki[i]
            print("*****************************")
            print("Składnik został dodany.")
            print("*****************************")
            print("Twoja sałatka (własna kompozycja):")
            print("")
            for element in twoje:
                print("-", element+",", twoje[element], "zł")
            print("")
            print("Wartość zamówienia: ",podsumuj(twoje),"zł")
            print("*****************************")
            suma = podsumuj(twoje)
            zamowienie['własna kompozycja'] = suma
    else:
        print("Wybrany składnik jest niedostępny.")
    dalej1()
def wybierz_salatke():
    n=0
    print("*********************************************")
    for salatka in gotowe:
        n+=1        
        print(n,".", salatka+",",gotowe[salatka],"zł")
    print("*********************************************")
    nazwa = input("Podaj nazwę sałatki: ")
    if nazwa in gotowe:
        if nazwa in zamowienie:
            print("")
            powtorka = input("Sałatka jest już w zamówieniu.\n\nPotwierdzasz wybór? T/N: ")
            if powtorka == "T":
                for i in zamowienie:
                    if i == nazwa: 
                        zamowienie[i]=zamowienie[i]+gotowe[i]
                print("****************************")
                print("Sałatka dodana do zamówienia.")
                print("*****************************")
                print("Twoje zamówienie:")
                print("")
                for element in zamowienie:
                    print("-", element+",", zamowienie[element], "zł")
                print("")
                print("Wartość zamówienia: ",podsumuj(zamowienie),"zł")
                print("*****************************")
            elif powtorka == "N":
                menu()
            else:
                print("Błędny wybór.")
                menu()
        else:        
            for i in gotowe:
                if i == nazwa:
                    zamowienie[i]=gotowe[i]
            print("*****************************")
            print("Sałatka dodana do zamówienia.")
            print("*****************************")
            print("Twoje zamówienie:")
            print("")
            for element in zamowienie:
                print("-", element+",", zamowienie[element], "zł")
            print("")
            print("Wartość zamówienia: ",podsumuj(zamowienie),"zł")
            print("*****************************")
    else:
        print("Nie ma takiej sałatki w menu.")

    
    dalej()
def dalej1():
    wybor = input("Kontynuować zamówienie? T/N: ")
    if wybor == "T":
        skomponuj()
    elif wybor == "N":
        menu()
    else:
        print("Błędny wybór")
        menu()
def dalej():
    wybor = input("Kontynuować zamówienie? T/N: ")
    if wybor == "T":
        wybierz_salatke()
    elif wybor == "N":
        menu()
    else:
        print("Błędny wybór")
        menu()
def final(): 
    
    file = open("logi.txt", "a")
    print("*****************************", file=file)
    czas = time.localtime()
    time_string = time.strftime("%m/%d/%Y, %H:%M:%S", czas)
    print(time_string, file=file)

    print("Twoje zamówienie:", file=file)
    print("", file=file)
    for element in zamowienie:
        print("-", element+",", zamowienie[element], "zł", file=file)
    print("", file=file)
    print("Wartość zamówienia: ", podsumuj(zamowienie),"zł", file=file)
    print("*****************************", file=file)
    print("", file=file)
    print("***ZAMÓWIENIA TOTAL***", file=file)
    print(kwota(),"zł", file=file)
    print("**********************", file=file)
    file.close()

    print("*****************************")
    print("Twoje zamówienie:")
    print("")
    for element in zamowienie:
        print("-", element+",", zamowienie[element], "zł")
    print("")
    print("Wartość zamówienia: ", podsumuj(zamowienie),"zł")
    print("*****************************")    
    twoje.clear()
    zamowienie.clear()
    
    wybor = input("Nacisnij 1 aby wyjść z programu, 2 aby wrócić do menu.")
    if wybor == "1":
        exit()
    elif wybor == "2":
        menu()                

    
