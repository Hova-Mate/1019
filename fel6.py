def beolvas(szoveg):
    szam = float(input(szoveg))
    return szam
def hat():

    a = beolvas("Kérem adja meg a háromszög 'a' oldalát:")
    b = beolvas("Kérem adja meg a háromszög 'b' oldalát:")
    c = beolvas("Kérem adja meg a háromszög 'c' oldalát:")

    if a > 0 and b > 0 and c > 0:
        if a<b+c and b<a+c and c<a+b :
            print("Ez a Háromszög megszerkezthető!")
        else:
            print("Ez a Háromszög nem megszerkezthető!")
    else:
        print("HIBA: Nem megfelelő bemenő adatok!")