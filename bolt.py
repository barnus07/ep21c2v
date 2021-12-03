
def feladat_1(filepath: str)->list:
    try:
        with open(filepath,"r",encoding="UTF-8") as fajl:
            lista = [sor.strip() for sor in fajl]
            return lista
    except FileNotFoundError:
            print("hiba")

def termekek(lista)->list:
    termekek = []
    for i in range(len(lista)):
        if lista[i] not in termekek:
            termekek.append(lista[i])
    termekek.remove("F")
    return termekek

def feladat_2(lista: list)->None:
    f = 0
    for i in range(len(lista)):
        if lista[i] == "F":
            f += 1
    print(f'2. Feladat : {f} alkalommal fizettek a pénztárnál.')
def feladat_3(lista:list)->None:
    try:
        vasarlas_szama = int(input("Adja meg a vásárlás sorozat számát:"))
        f_indexek = [0]
        aru = []
        for i in range(len(lista)):
            if lista[i] == "F":
                f_indexek.append(i)
        if vasarlas_szama == 0:
            aru.append(lista[0])
        else:
            i = f_indexek[vasarlas_szama]+1
            while i < len(lista):
                aru.append(lista[i])
                i += 1
                if lista[i] == "F":
                    break
        osszeg = 0
        aru = sorted(aru)
        ismetles = 0
        for i in range(len(aru)):
            if aru[i] in aru:
                osszeg += 1000

        print("3. Feladat. A kosár tartalma:\n",aru)
        print("Összege:",osszeg)
        print(ismetles)
    except ValueError:
        print("nem megfelelő értéket adott meg.")

def feladat_4(lista:list)->None:
    print(termekek(lista))
    f_indexek = [0]
    for i in range(len(lista)):
        if lista[i] == "F":
            f_indexek.append(i)
    termek = str(input("Adja meg a termék nevét: "))



