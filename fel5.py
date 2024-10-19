import math


def ot():
    pass
    szam = int(input("Kérem adjon be egy [40, 95] intervallumban lévő egész számot:"))
    if szam >= 40 and szam <= 90:
        szam = str(szam)
        print(szam[0])

        szam=int(szam)
        print(str(int(szam/10)))

        szam = int(szam)
        print(str(math.floor(szam/10)))
    else:
        print("Hiba! a megadott szám nem az intervallumban helyezkedik el!")