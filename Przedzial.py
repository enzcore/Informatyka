def f(x):
    return x*(x*(x-3)+2)-6


def polowienie_przedzialow(a, b, epsilon):

    if f(a) == 0.0:
        return a

    if f(b) == 0.0:
        return b

    while (b - a) > epsilon:
        srodek = (a + b) / 2

        if f(srodek) == 0:
            return srodek

        if f(a) * f(srodek) < 0:
            b = srodek
        else:
            a = srodek

    return (a + b) / 2


a = -10
b = 10
epsilon = 0.00001

wynik = polowienie_przedzialow(a, b, epsilon)

print("Znalezione miejsce zerowe wynosi:", format(wynik, ".5f"))