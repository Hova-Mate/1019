def ketto():
    szam = int(input("Kérem adjon be egy 5-el osztható, háromjegyűjegyű számot: "))
    absSzam = abs(szam)
    if absSzam >= 100 and absSzam <= 999 and absSzam % 5 == 0 :
        negyzet = absSzam ** 2
        print(f"A {szam} négyzete: {negyzet}")
    else:
        print("HIBA: Nem megfelelő szám!")



    print("\n")