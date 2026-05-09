def merge_sort(lista):

    if len(lista) <= 1:
        return lista

    srodek = len(lista) // 2

    lewa = merge_sort(lista[:srodek])
    prawa = merge_sort(lista[srodek:])

    wynik = []

    while lewa and prawa:

        if lewa[0] < prawa[0]:
            wynik.append(lewa[0])
            lewa.remove(lewa[0])

        else:
            wynik.append(prawa[0])
            prawa.remove(prawa[0])

    wynik = wynik + lewa + prawa

    return wynik


dane = input("Podaj liczby oddzielone spacją: ")

liczby = list(map(int, dane.split()))

print("Przed sortowaniem:", liczby)

posortowane = merge_sort(liczby)

print("Po sortowaniu:", posortowane)