from random import randint 

# 31
print(f'31F: {randint(100, 999)}')

# 32
print(f'32F: {randint(0, 250) / 10}')

# 33
print(f'33F: {randint(150, 250) / 10}')

# 34
print(f'34F: {randint(0, 49) * 2}')

# 35
print(f'35F: {randint(20, 40) * 5}')

# 39 --------------------
a:int = randint(10, 50)
b:int = randint(10, 50)

tipp:int = int(input(f"{a} + {b} = "))

if tipp == a + b: print('helyes!')
else: print(f'nem, az összeg {a + b}!')