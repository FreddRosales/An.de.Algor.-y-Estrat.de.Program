UMBRAL = 4  # Con <= 4 dígitos se multiplica directo; si no, se divide en mitades

def tamano(n):
    return len(str(abs(n)))


def mult_clasica(u, v):
    return u * v


def mult(u, v):
    if u < 0 or v < 0:
        signo = -1 if (u < 0) != (v < 0) else 1
        return signo * mult(abs(u), abs(v))

    n = max(tamano(u), tamano(v))

    if n <= UMBRAL:
        return mult_clasica(u, v)

    s = n // 2
    w = u // 10**s
    x = u % 10**s
    y = v // 10**s
    z = v % 10**s

    return (mult(w, y) * 10**(2 * s)
            + (mult(w, z) + mult(x, y)) * 10**s
            + mult(x, z))


def leer_entero(mensaje):
    while True:
        try:
            return int(input(mensaje).strip())
        except ValueError:
            print("Entrada inválida. Ingresa solo un número entero.")


def main():
    while True: 
        print("\n=== CALCULADORA DE ENTEROS GRANDES ===")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        opcion = input("Elige una opción: ")

        a = int(input("Primer número: "))
        b = int(input("Segundo número: "))

        match opcion:  # equivale a switch (opcion)
            case "1":
                print("Resultado:", a + b)
            case "2":
                print("Resultado:", a - b)
            case "3":
                print("Resultado:", mult(a, b))
            case _: 
                print("Opción no válida")

        continuar = input("¿Desea realizar otra operación? (s/n): ")
        if continuar.lower() != "s":
            break


if __name__ == "__main__":
    main()