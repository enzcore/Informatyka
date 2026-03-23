def dziesietna_na_binarna(n):
    wynik = ""
    
    while n > 0:
        reszta = n % 2
        wynik = str(reszta) + wynik
        n = n // 2
        
    return wynik


liczba = int(input("Podaj liczbę dziesiętną: "))


binarnie = dziesietna_na_binarna(liczba)


print("Liczba w systemie binarnym:", binarnie)