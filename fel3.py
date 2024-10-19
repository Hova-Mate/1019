def harom():
    a1 = int(input("Kérem adjon be sorozat első elemét: "))
    n = int(input("Kérem adjon be sorozat elemszámát: "))
    d = int(input("Kérem adjon be sorozat differenciáját : "))

    an = a1 + (n - 1) * d
    sn = ((a1 + an) * n) / 2

    print(f"a1={a1}  n={n} d={d}   Sn={sn}")

    if d>0:
        print("A számtani sorozat monoton növekvő, és alulról korlátos!")
    elif d>0:
        print("A számtani sorozat monoton csökkenő, és felülről korlátos!")
    elif d==0:
        print("A számtani sorozat nemnövekvő, nemcsökkenő, azaz állandó!")

    print("\n")