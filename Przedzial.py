def f(x):
    return x*(x*(x-3)+2)-6


def bisekcja(a, b, epsilon):
    while (b - a) > epsilon:
        s = (a + b) / 2

        if f(a) * f(s) < 0:
            b = s
        else:
            a = s

    return (a + b) / 2


a = float(input("Podaj a: "))
b = float(input("Podaj b: "))

epsilon = 0.00001

wynik = bisekcja(a, b, epsilon)

print("Miejsce zerowe:", format(wynik, ".5f"))