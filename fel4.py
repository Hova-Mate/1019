def negy():
    n = 1 # float(input("Kérem adjon meg a egy páratlan pozitív egész számot:"))
    k = 1 # float(input("Kérem adjon meg a egy pozitív egész számot:"))

    if (k % 2 == 1) and (n > 0) and (pow(2,n) > k):
        print("Proth-számok:  ", end=" ")
        for n in range(11):
            proth = k * pow(2, n)+1
            if n == 10:
                print(proth, end="")
            else:
                print(proth, end=", ")
    else:
        print("HIBA: Nem megfelelő számok!")

    print("\n")


def negyv():
    n = 1  # float(input("Kérem adjon meg a egy páratlan pozitív egész számot:"))
    k = 1  # float(input("Kérem adjon meg a egy pozitív egész számot:"))

    szamlalo = 10
    talalat = 0
    print("Proth-számok:  ", end=" ")

    if (k > 0) and (k % 2 == 1) and (n > 0) and (pow(2, n) > k):
        while talalat < szamlalo:
            if (k > 0) and (k % 2 == 1) and (n > 0) and (pow(2, n) > k):
                proth = k * pow(2, n) + 1
                if talalat == szamlalo - 1:
                    print(proth, end="")
                else:
                    print(proth, end=", ")
                talalat += 1
            k += 2
            if k > 2 * szamlalo:
                n += 1
    else:
        print("HIBA: Nem megfelelő számok!")

