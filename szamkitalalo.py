from random import randint as rnd
szam:int = rnd(1, 100)
print("Gondoltam egy számra [1, 100] között, próbáld meg kitalálni!")
probak_szama:int = 0
tipp:int = -1

while tipp != szam:
    probak_szama += 1
    tipp = int(input('tipp: '))
    if szam > tipp:
        print(f'nem, ennél nagyobb számra gondoltam!')
    elif szam < tipp:
        print('nem, ennél kisebb számra gondoltam!')
    else: print('így van, eltaláltad!')
print(f'próbálkozások száma: {probak_szama}')