import colorama
from colorama import Fore, Style

mapa = [
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1],
    [2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2],
    [3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3],
    [4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4],
    [5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5],
    [6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6],
    [7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7],
    [8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8],
    [9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
]
soluciones=[2468]
resuelto= [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]


for solucion in soluciones[:]:  # Iterate over a copy of the list to avoid infinite loop
    reversed_solucion = int(str(solucion)[::-1])  # Reverse the digits and convert back to int
    soluciones.append(reversed_solucion)

# Separate the digits in each value of soluciones
soluciones = [list(map(int, str(solucion))) for solucion in soluciones]

def check(mapa, solucion, i, j):
    length = len(solucion) - 1
    pasados = []
    pasados.append((i, j))
    resuelto[i][j] += 1

    for k in range(len(solucion)):
        if i + k < 11 and mapa[i + k][j] == solucion[k]:
            pasados.append((i + k, j))
            resuelto[i + k][j] += 1
            if k == length:
                return 1
            continue
        else:
            for paso in pasados:
                resuelto[paso[0]][paso[1]] -= 1
            break

    pasados = []
    for k in range(len(solucion)):
        if j - k >= 0 and mapa[i][j - k] == solucion[k]:
            pasados.append((i, j - k))
            resuelto[i][j - k] += 1
            if k == length:
                return 2
            continue
        else:
            for paso in pasados:
                resuelto[paso[0]][paso[1]] -= 1
            break

    pasados = []
    for k in range(len(solucion)):
        if i + k < 11 and j + k < 11 and mapa[i + k][j + k] == solucion[k]:
            pasados.append((i + k, j + k))
            resuelto[i + k][j + k] += 1
            if k == length:
                return 3
            continue
        else:
            for paso in pasados:
                resuelto[paso[0]][paso[1]] -= 1
            break

    pasados = []
    for k in range(len(solucion)):
        if i + k < 11 and j - k >= 0 and mapa[i + k][j - k] == solucion[k]:
            pasados.append((i + k, j - k))
            resuelto[i + k][j - k] += 1
            if k == length:
                return 4
            continue
        else:
            for paso in pasados:
                resuelto[paso[0]][paso[1]] -= 1
            break

    return 0

def explorar(mapa, soluciones):
    for i in range(11):
        for j in range(11):
            for solucion in soluciones:
                if mapa[i][j] == solucion[0]:
                    result = check(mapa, solucion, i, j)


def mostrar():
    colorama.init()

    for row in resuelto:
        for num in row:
            if num >= 1:
                print(Fore.RED + str(num) + Style.RESET_ALL, end='  ')
            else:
                print(num, end='  ')
        print()

explorar(mapa, soluciones)
mostrar()