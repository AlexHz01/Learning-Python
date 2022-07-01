import keyword

print("hola mundo")
x = 5 +5
print(x)
# salida: 5

a = 11
if a == 10:
    print("es el numero correcto")
else:
    print("no es el valor correspondiente")

    valor_decimal = 1.2225
    mi_cadena = "Empezando a progrmar en python"

x = ("el valor de la funcion es")

a, b, c = 10, 5, 6

d = (a + b) * c

# Definimos una variable x con una cadena
x = "El valor de (a+b)*c es"

# Podemos realizar múltiples asignaciones
a, b, c = 4, 3, 2

# Realizamos unas operaciones con a,b,c
d = (a + b) * c

# Definimos una variable booleana
imprimir = True

# Si imprimir, print()
if imprimir:
    print(x, d)

# Salida: El valor de (a+b)*c es 14

print("con print podemos imprimir lo que queramos")

Name = list("enrique")
print(Name)

import keyword
print(keyword.kwlist)

lenguaje = "python"

if lenguaje == "python" :
    print("es el mejor lenguaje de programacion")
elif lenguaje == "java" :
    print("Este lenguaje no mola")
else :
    print("Python es el mejor lenguaje que hay")



print("usando bucles")
x = 1
while x < 3:
    print(x)
    x += 1

print("uso del for")

for i in range(3):
    print(i)

print("usando el continue")

for i in range(3):
    if i == 1:
        continue
    print(i)

print("usando el break")

x = 0
while True:
    print(x)
    if x == 5:
        break
    x += 1

print(True and False) # False
print(True or False)  # True
print(not True)       # False


print("creando una funcion rapida con --def--")
def funcion_suma(a, b):
    print("la suma es", a + b)

funcion_suma(3, 5)

print("uso de la funcion lamda")

print("la suma es", (lambda a, b: a * b )(3,5))

def funcion_suma(a ,b):
    pass

print("usando la funcion Yield")

def generador():
    n = 1
    yield n

    n += 1
    yield n

    n += 1
    yield n

for i in generador():
    print(i)


class MiClase:
    def __init__(self):
        print("Creando objeto de MiClase")


print("exepciones")

x = "10"

valor = None
try:
    valor = int(x)
except exeption as e:
    print("hubo un error", e)
finally:
    print("el valor es ", valor)

    print("variable global, noncal")

    a = 0
    def suma_uno():
        global a
        a = a + 1

    suma_uno()
    print(a)


def funcion_a():
    x = 10

    def funcion_b():
        nonlocal x
        x = 20
        print("funcion_b", x)

    funcion_b()
    print("funcion_a", x)


list = ["a", "b", "c"]
print("a" in list)

a = [1, 2]
b = [1, 2]
c = a

print(a is b)
print(a is c)


print("eliminar variables:del")

a = 10
# del a  ----- el uso del del nos elimana la variable del escope
print(a)

print("context managers : whit, as ")

with open ('fichero.txt', 'r') as file:
    print(file.read())

import asyncio


async def proceso(id_proceso):
    print("Empieza proceso:", id_proceso)
    await asyncio.sleep(10)
    print("Acaba proceso:", id_proceso)

async def main():
    await asyncio.gather(proceso(1), proceso(2), proceso(3))

asyncio.run(main())

