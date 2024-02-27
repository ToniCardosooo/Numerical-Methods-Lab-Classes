

""" soma = 0
for i in range(100):
    soma += 0.1
    if i%10 == 0:
        print(soma)

print(f"Soma final = {soma}") """


""" eps = 1
while 1+eps != 1:
    eps /= 2

print(f"eps para 1 = {eps}")

eps = 1
while 1000+eps != 1000:
    eps /= 2

print(f"eps para 1000 = {eps}") """


import math

def f(x):
    return x * (math.sqrt(x+1) - math.sqrt(x))

def f_estavel(x):
    return x / (math.sqrt(x+1) + math.sqrt(x))

for i in range(1, 25+1):
    print(f"x = 10**{i} --> f_estavel(x) = {f_estavel(10**i)}")








