def f(x):
    return x*x - 4

a = 0
b = 5

for i in range(10):
    s = (a + b) / 2
    
    if f(a) * f(s) < 0:
        b = s
    else:
        a = s

print("Przybliżone miejsce zerowe:", s)