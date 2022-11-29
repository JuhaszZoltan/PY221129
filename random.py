import random

# [10; 20] intervallumból kiválaszt egy véletlen egész számot
r1:int = random.randint(a=10, b=20)

# [0, 1) intervallumból lebegőpontos véletlen szám
r2:float = random.random()

# [10, 20) számintervallumot 'step'-esével veszi, és ebből választ egy számot véletlenszerűen.
r3:int = random.randrange(start=10, stop=20, step=2)

random.seed(2022)

for x in range(10):
    print(random.randint(0, 9), end=' ')