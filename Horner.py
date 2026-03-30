# horner
def horner(wsp, st, x):
    if st == 0:
    return wsp[0]
    return x * horner(wsp, st - 1, x) + wsp[st]


# deklaracja zmiennych
stopien = 0
argument = 0

# pobranie stopnia wielomianu
stopien = int(input("Podaj stopien wielomianu: "))

# deklaracja dynamicznej tablicy
wspolczynnik = [0] * (stopien + 1)

# wczytywanie współczynników
for i in range(stopien, -1, -1):
    wspolczynnik[i] = int(input(f"Podaj wspolczynnik stojacy przy potedze {1}: "))

# pobranie argumentu
argument = int(input("Podaj argument: "))

# wywołanie funkcji Hornera
wynik = horner(wspolczynnik, stopien, argument)

# wynik działania programu
print("W(", argument, ") =", wynik)

# usunięcie tablicy
del wspolczynnik