def horner(a, b, c, x):
    wynik = a * x + b
    wynik = wynik * x + c
    return wynik

x = int(input("Podaj x: "))

wynik = horner(2, 3, 4, x)

print("Wynik:", wynik)