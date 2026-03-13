from funciones import *

def main():

    animales, encabezados = cargar_animales()
    clases = cargar_clases()

    while True:

        opcion = menu()

        if opcion == "1":
            listar_por_clase(animales, clases)

        elif opcion == "2":
            listar_por_caracteristica(animales, encabezados)

        elif opcion == "3":
            agregar_animal(animales, encabezados, clases)

        elif opcion == "4":

            guardar_animales(animales, encabezados)

            print("Cambios guardados")
            break

        else:
            print("Opción inválida")


if __name__ == "__main__":
    main()