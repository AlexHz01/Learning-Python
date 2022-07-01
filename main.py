# nivel python

print("duck typing")

class pato:
    def hablar(self):
        print("cua! cuac")
    def caminar(self):
        print("dar 10 pasos")


p = pato()
p.caminar()


class Perro:
    def hablar(self):
        print("gua gua ")

class Gato:
    def hablar(self):
        print("miau miau")

class Vaca:
    def hablar(self):
        print("muuuu, muuuu")


lista = [Perro(), Gato(), Vaca()]
for animal in lista:
    animal.hablar()


# uso de las condiconales
a = 4
b = 2
if b != 0:
    c = a/b
    d = c + 1
    print(d)

# else
x = 6

if x == 5:
    print("es 5")
else:
    print("no es 5")


x = 5
if x == 5:
    print("es 5")
elif x == 6:
    print("es 6")
elif x == 7:
    print("es 7")


# operadpr ternario

x = 5
print("es 5" if x == 5 else "no es 5")

a = 10
b = 5
c = a/b if b != 0 else -1
print(c)


# bucle for

for i in  range(0, 5):
    print(i)

for i in "python":
    print(i)

# from collections import Iterable
# lista = [1, 2, 3, 4]
# cadena = "Python"
# numero = 10
# print(isinstance(lista, Iterable))  #True
# print(isinstance(cadena, Iterable)) #True
# print(isinstance(numero, Iterable)) #False

# for anindados

lista = [[56, 34, 1],
         [12, 4, 5],
         [9, 4, 3]]

for i in lista:
    for j in i:
        print(j)


# ejemplos for
texto = "python"
for i in texto[::-1]:
    print(i)

print(sum(i for i in range(10)))

# USO DEL RANGO EN PYTHON

for i in (0, 1 ,2, 3 ,4 ,5):
    print(i)

for i in range(6):
    print(i)

# range(inicio, fin, salto)

print(list(range(5, 20, 2)))
# for i in range(5, 20, 2):
#     print(i)

# salto inverso
for i in range (5 , 0 , -1):
    print(i)

# bucle while

x = 5
while x > 0:
    x =-1
    print(x)

    # # No ejecutes esto, en serio
    # while True:
    #     print("Bucle infinito")

# podemos tener en un mismo while todo en la misma linea

x = 5
while x >0: x-=1; print(x)

    # EL USO DE ELSE Y WHILE

X = 5
while x > 0:
    x -=1
    print(x)
else:
    print("el bucle a finalizado")


# usando un break
x = 5
while True:
    x -= 1
    print(x) #4, 3, 2, 1, 0
    if x == 0:
        break
else:
    # El print no se ejecuta
    print("Fin del bucle")

# Permutación a generar
i = 0
j = 0
while i < 3:
    while j < 3:
        print(i,j)
        j += 1
    i += 1
    j = 0


# ejemplos

i, j, k = 0, 0, 0
while i < 3:
    while j < 3:
        while k < 3:
            print(i,j,k)
            k += 1
            j += 1
        k = 0
    i += 1
    j = 0


# ejemplos de while haciendo un arbol con *

z = 7
x = 1
while z > 0:
    print(' ' * z + 'A' * x + ' ' * z)
    x += 2
    z -= 1

text = "python"
i = 0
while i  < len(text):
    print(text[:i + 1])
    i += 1

# sucesion de Fibonacci

a, b = 0, 1
while b < 25:
    print(b)
    a, b = b, a + b
print("****************************************")
# Swith en python emulando

def opera1(operador, a, b):
    if operador == 'suma':
        return print(a + b)
    elif operador == 'resta':
        return print(a - b)
    elif operador == 'multiplica':
        return a * b
    elif operador == 'divide':
        return a / b
    else:
        return None

    # def opera2(operador, a, b):
    #     return {
    #         'suma': lambda: a + b,
    #         'resta': lambda: a - b,
    #         'multiplica': lambda: a * b,
    #         'divide': lambda: a / b
    #     }.get(operador, lambda: None)

opera1('suma', 5, 8)
# Salida: 14

opera1('resta', 5, 9)()
# Salida: 14

# midiendo el tiempo de ejecucuion

# import time
# def mide_tiempo(funcion):
#     def funcion_medida(*args, **kwargs):
#         inicio = time.time()
#         c = funcion(*args, **kwargs)
#         print(f"Entrada: {args[1]}. Tiempo: {time.time() - inicio}")
#         return c
#     return funcion_medida
#
# @mide_tiempo
# def repite_funcion(funcion, entrada):
#     return [funcion(entrada) for i in range(10000000)]

cadena = 'Python'
for letra in cadena:
    if letras == 'h':
        print("Se encontró la h")
        break
    print(letras)


# break con bucle while

x = 5
while True:
    x -= 1
    print(x)
    if x == 0:
        break
    print("fin del bucle")
