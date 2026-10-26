tablero = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]


def validar(num, f, c):
    if num in tablero[f]:
        return False

    for i in range(9):
        if tablero[i][c] == num:
            return False

    inicio_f = f - f % 3
    inicio_c = c - c % 3
    for i in range(inicio_f, inicio_f + 3):
        for j in range(inicio_c, inicio_c + 3):
            if tablero[i][j] == num:
                return False

    return True


def fcdisponible():
    for f in range(9):
        for c in range(9):
            if tablero[f][c] == 0:
                return f, c
    return -1, -1


def sudoku():
    f, c = fcdisponible()
    if f == -1 and c == -1:
        return True
    else:
        for num in range(1, 10):
            if validar(num, f, c):
                tablero[f][c] = num        
                if sudoku():              
                    return True
                tablero[f][c] = 0         
        return False


def mostrar():
    for fila in tablero:
        print(" ".join(str(x) for x in fila))


if sudoku():
    print("Solución encontrada:")
    mostrar()
else:
    print("No tiene solución")