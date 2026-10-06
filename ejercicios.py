import random

# ---------- EJERCICIO 1 ----------
def recorrer(actual, fin, paso, resultado):
    if (paso == 1 and actual > fin) or (paso == -1 and actual < fin):
        return resultado

    if actual % 3 == 0:
        if resultado is None:
            resultado = actual
        elif paso == 1:
            resultado = max(resultado, actual)   
        else:
            resultado = min(resultado, actual)   

    return recorrer(actual + paso, fin, paso, resultado)


def multiplo_de_3(inicio, fin):
    paso = 1 if inicio <= fin else -1
    return recorrer(inicio, fin, paso, None)


def ejercicio1():
    print("\n--- Ejercicio 1: múltiplo de 3 en un rango ---")
    inicio = int(input("Ingrese el número de inicio: "))
    fin = int(input("Ingrese el número de fin: "))

    resultado = multiplo_de_3(inicio, fin)

    if resultado is None:
        print("No hay múltiplos de 3 en ese rango")
    elif inicio <= fin:
        print("Va hacia adelante. Máximo múltiplo de 3:", resultado)
    else:
        print("Va hacia atrás. Mínimo múltiplo de 3:", resultado)


# ---------- EJERCICIO 2 ----------
def generar_lista(n):
    if n == 0:
        return []
    return generar_lista(n - 1) + [random.randint(10, 99)]


def sumar_multiplos_de_3(lista, i=0):
   
    if i == len(lista):
        return 0
    if lista[i] % 3 == 0:
        return lista[i] + sumar_multiplos_de_3(lista, i + 1)
    return sumar_multiplos_de_3(lista, i + 1)


def ejercicio2():
    print("\n--- Ejercicio 2: suma de múltiplos de 3 ---")
    cantidad = int(input("¿Cuántos elementos desea generar? "))
    numeros = generar_lista(cantidad)

    print("Lista generada:", numeros)
    print("Suma de los múltiplos de 3:", sumar_multiplos_de_3(numeros))



def menu():
    print("\n===== MENÚ =====")
    print("1. Ejercicio 1")
    print("2. Ejercicio 2")
    print("3. Salir")
    opcion = input("Elija una opción: ")

    if opcion == "1":
        ejercicio1()
    elif opcion == "2":
        ejercicio2()
    elif opcion == "3":
        print("Hasta luego")
        return                     
    else:
        print("Opción no válida")

    menu()                          

menu()