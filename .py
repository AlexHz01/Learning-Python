x = 5
while True:
    x -= 1
    print(x)
    if x == 0:
        break
    print("fin del bucle")

cadena = 'Python'
for letra in cadena:
    if letra == 'P':
        continue
    print(letra)

f = 5
while f > 0:
    f -= 1
    if f == 3:
        continue
    print(f)

a = [1, 2]
b = ["Uno", "Dos"]
c = zip(a, b)

print(list(c))
# [(1, 'Uno'), (2, 'Dos')]

a = [1, 2]
b = ["Uno", "Dos"]
c = zip(a, b)

for numero, texto in zip(a, b):
    print("Número", numero, "Letra", texto)

numeros = [1, 2]
espanol = ["Uno", "Dos"]
ingles = ["One", "Two"]
frances = ["Un", "Deux"]
c = zip(numeros, espanol, ingles, frances)

for n, e, i, f in zip(numeros, espanol, ingles, frances):
    print(n, e, i, f)

# ejemplos zip ( )

esp = {'1': 'Uno', '2': 'Dos', '3': 'Tres'}
eng = {'1': 'One', '2': 'Two', '3': 'Three'}

for a, b in zip(esp, eng):
    print(a, b)

# 1 1
# 2 2
# 3 3

# Sin embargo, si hacemos uso de la función items,
# podemos acceder al key y value de cada elemento.

esp = {'1': 'Uno', '2': 'Dos', '3': 'Tres'}
eng = {'1': 'One', '2': 'Two', '3': 'Three'}

for (k1, v1), (k2, v2) in zip(esp.items(), eng.items()):
    print(k1, v1, v2)

# 1 Uno One
# 2 Dos Two
# 3 Tres Three

# hacer el zip en una sola linea
a = [1, 2, 3]
b = ["One", "Two", "Three"]
c = zip(a, b)

print(list(c))

# unpacking
c = [(1, 'One'), (2, 'Two'), (3, 'Three')]
a, b = zip(*c)

print(a)  # (1, 2, 3)
print(b)  # ('One', 'Two', 'Three')

