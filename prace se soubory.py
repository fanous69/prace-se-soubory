from random import randint, choice



def pocitadlo(soubor):
    try:
        f = open(soubor, "r")
    except FileNotFoundError as e:
        print(f"Soubor se nepovedlo otevřít. {e.filename}")
        exit(1)
    pocet = {}

    while True:
        pismeno = f.read(1).lower()
        if pismeno == "":
            break
        if pismeno.isalpha():
            try:
                pocet[pismeno] += 1
            except:
                pocet[pismeno] = 1

    for key in sorted(pocet.keys()):
        mapovany = 50 * pocet[key] / max(pocet.values()) #maximum * tvoje hodnota co chceš namapovat / maximum co dosahl tvoje hodnoty
        bar = int(mapovany) * "#" 
        print(f"{key} -----> {pocet[key]:7} | {bar}")

    f.close()

def slovo(maxpismen = 7):
    samohlasky = "aeiyou"
    souhlasky = "qwrtpsdfghjklzxcvbnm"
    slovo = ""
    for i in range(randint(1, maxpismen)):
        if i % 2 == randint(0, 1):
            slovo = slovo + choice(souhlasky)
        else:    
            slovo = slovo + choice(samohlasky)
    return slovo 

def veta(minslovo = 3, maxslovo = 12):
    veta = ""
    for i in range(randint(minslovo, maxslovo)):
        veta = veta + slovo() + " "
    veta = (veta[:-1] + ".").capitalize()
    return veta

def text(minvet = 3, maxvet = 10):
    text = ""
    for i in range(randint(minvet, maxvet)):
        text = text + veta()
        if randint(1, 5) == 5:
            text = text + "\n"
    return text

def generator(soubor, minvet = 3, maxvet = 10):
    f = open(soubor, "w")
    f.write(text(minvet, maxvet))
    f.close()

def menic(soubor, znakA, znakB):
    try:
        f = open(soubor, "r")
    except FileNotFoundError as e:
        print(f"Soubor se nepovedlo otevřít. {e.filename}")
        exit(1)

    soubor2 = soubor.split(".")[0]
    fB = open(f"{soubor2}_meneno.txt", "w")

    while True:
        pismeno = f.read(1)
        if pismeno == znakA:
            pismeno = znakB
        if pismeno == "":
            break
        fB.write(pismeno)
        
    f.close()
    fB.close()

def zmensovac(soubor):
    try:
        f = open(soubor, "r")
    except FileNotFoundError as e:
        print(f"Soubor se nepovedlo otevřít. {e.filename}")
        exit(1)
    soubor2 = soubor.split(".")[0]
    fB = open(f"{soubor2}_zmenseno.txt","w")

    while True:
        pismeno = f.read(1).lower()
        if pismeno == "":
            break
        fB.write(pismeno)
        

    f.close()
    fB.close()

def zvetsovac(soubor):
    try:
        f = open(soubor, "r")
    except FileNotFoundError as e:
        print(f"Soubor se nepovedlo otevřít. {e.filename}")
        exit(1)
    
    soubor2 = soubor.split(".")[0]
    fB = open(f"{soubor2}_zvetseno.txt","w")

    while True:
        pismeno = f.read(1).upper()
        if pismeno == "":
            break
        fB.write(pismeno)
        

    f.close()
    fB.close()

def menu():
    soubor = input("Zadejte prosím název souboru: ")
    print("""
    1) převede na malá písmena
    2) převede na velká písmena
    3) změna znaku
    4) generátor náhodného textu
    5) počitadlo písmen
    ENTER - Konec
    """)
    
    try:
        cinnost = int(input("Zadejte co chcete provést: "))
    except:
        print("Neplatná volba!")
        exit(1)
    
    if cinnost == 1:
        zmensovac(soubor)
    elif cinnost == 2:
        zvetsovac(soubor)
    elif cinnost == 3:
        znakA = input("Zadejte znak který bude změněn: ")
        znakB = input(f"Zadejte znak na který se bude {znakA} měnit: ")
        if znakA == "" or znakB == "":
            menic(soubor)
        else:
            menic(soubor, znakA , znakB)
    elif cinnost == 4:
        try:
            minvet = int(input("Minimální počet vět: "))
            maxvet = int(input("Zadejte Maximální počet vět: "))
        except:
            print("Musíte zadat celé číslo")
            exit(1)
        generator(soubor, minvet, maxvet)
    elif cinnost == 5:
        pocitadlo(soubor)
    else:
        exit(0)

while True:
    menu()
    try:
        pokracovat = int(input("Chcete pokračovat dál?(1/0): "))
    except:
        break
    if pokracovat == 1:
        menu()
    else:
        break 
    