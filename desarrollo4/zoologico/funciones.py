import csv
from animal import Animal

def cargar_csv(nombre_archivo):
    datos = []
    with open(nombre_archivo, newline='', encoding='utf-8') as f:
        lector = csv.reader(f)
        for fila in lector:
            datos.append(fila)
    return datos

def cargar_animales():
    datos = cargar_csv("zoo.csv")

    encabezados = datos [0][1:-1]
    animales = []
    for fila in datos[1:]:
        nombre = fila[0]
        caracteristicas = list(map(int, fila[1:-1]))
        clase = int(fila[-1])

        animales.append(Animal(nombre, caracteristicas, clase))
    return animales, encabezados

def cargar_clases():
    datos = cargar_csv("clases.csv")

    clases = {}

    for fila in datos[1:]:
        clases[int(fila[0])] = fila[1]

    return clases

def guardar_animales(animales, encabezados):
    with open("zoo.csv", "w", newline='', encoding='utf-8') as f:
        escritor = csv.writer(f)
        escritor.writerow(["nombre_animal"] + encabezados + ["Clase"])
        for a in animales:
            fila= ([a.nombre] + a.caracteristicas + [a.clase])
            escritor.writerow(fila)

# menu
def menu():

    print("\n--- ZOOLÓGICO ---")
    print("1. Listar animales por clase")
    print("2. Listar animales por característica")
    print("3. Agregar animal")
    print("4. Salir")

    return input("Seleccione opción: ")

# listar por clase
def listar_por_clase(animales, clases):

    print("\nClases disponibles:")

    for id_clase, nombre in clases.items():
        print(id_clase, "-", nombre)

    seleccion = int(input("Seleccione clase: "))

    print("\nAnimales encontrados:\n")

    for a in animales:
        if a.clase == seleccion:
            print(a.nombre)

def listar_por_caracteristica(animales, encabezados):

    print("\nCaracterísticas disponibles:")

    for i, nombre in enumerate(encabezados):
        print(i, "-", nombre)

    seleccion = int(input("Seleccione característica: "))

    print("\nAnimales encontrados:\n")

    for a in animales:
        if a.caracteristicas[seleccion] == 1:
            print(a.nombre)

def agregar_animal(animales, encabezados, clases):

    nombre = input("Nombre del animal: ")

    caracteristicas = []

    print("\nIngrese 1 si tiene la característica, 0 si no\n")

    for c in encabezados:
        valor = int(input(f"{c}: "))
        caracteristicas.append(valor)

    print("\nClases disponibles:")

    for id_clase, nombre_clase in clases.items():
        print(id_clase, "-", nombre_clase)

    clase = int(input("Clase del animal: "))

    nuevo = Animal(nombre, caracteristicas, clase)

    animales.append(nuevo)

    print("Animal agregado correctamente")

