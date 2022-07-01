# lsita de compresion

cuadrados = [i**2 for i in range(5)]

print(cuadrados)
# cuadrados = []
# for i in range(5):
#     cuadrados.append(i**2)
#[0, 1, 4, 9, 16]


unos = [1 for i in range(5)]
#[1, 1, 1, 1, 1]


def eleva_al_2(i):
    return i**2

cuadrados1 = [eleva_al_2(i) for i in range(5)]

print(cuadrados1)

# ejemplos de como dividir una lista

lista = [10, 20, 30, 40 , 50]
nueva_lista = [i/10 for i in lista]

frase = "El perro de san roque no tiene rabo"
erres = [i for i in frase if i == 'r']

print(erres)

# sets Comprehension

lista1 = ['nombre', 'edad', 'región']
lista2 = ['Pelayo', 30, 'Asturias']

mi_dict = {i:j for i,j in zip(lista1, lista2)}

# ITERADORES ITERABLES

# Mal uso
lista = [5, 4, 9, 2]
i = 0
while i < len(lista):
    elemento = lista[i]
    print(elemento)
    i += 1
# Salida: 5, 4, 9, 2

# USO DE ITERADORES EN PYTHON
lista = [5, 4, 9, 2]
for elemento in lista:
    print(elemento)
# Salida 5, 4, 9, 2

cadena = "KIKE"
for c in cadena:
    print(c)

#
# class Animal:
#     def __init__(self, especie, edad):
#         self.especie = especie
#         self.edad = edad
#
#     # Método genérico pero con implementación particular
#     def hablar(self):
#         # Método vacío
#         pass
#
#     # Método genérico pero con implementación particular
#     def moverse(self):
#         # Método vacío
#         pass
#
#     # Método genérico con la misma implementación
#     def describeme(self):
#         print("Soy un Animal del tipo", type(self).__n

# Perro hereda de Animal
# class Perro(Animal):
#     pass

# clase eredada
# mi_perro = Perro('mamífero', 10)
# mi_perro.describeme()
# Soy un Animal del tipo Perro

# ******************************
class Perro(Animal):
    def hablar(self):
        print("Guau!")
    def moverse(self):
        print("Caminando con 4 patas")

class Vaca(Animal):
    def hablar(self):
        print("Muuu!")
    def moverse(self):
        print("Caminando con 4 patas")

class Abeja(Animal):
    def hablar(self):
        print("Bzzzz!")
    def moverse(self):
        print("Volando")

    # Nuevo método
    def picar(self):
        print("Picar!")
# *************************************

mi_perro = Perro('mamífero', 10)
mi_vaca = Vaca('mamífero', 23)
mi_abeja = Abeja('insecto', 1)

mi_perro.hablar()
mi_vaca.hablar()
# Guau!
# Muuu!

mi_vaca.describeme()
mi_abeja.describeme()
# Soy un Animal del tipo Vaca
# Soy un Animal del tipo Abeja

mi_abeja.picar()
# Picar!

# *********************
# USO DEL METOSO SUPER

# podemos uasar esto para llamara a init y colocar la nueva variable

class Perro(Animal):
    def __init__(self, especie, edad, dueño):
        # Alternativa 1
        # self.especie = especie
        # self.edad = edad
        # self.dueño = dueño

        # Alternativa 2
        super().__init__(especie, edad)
        self.dueño = dueño
