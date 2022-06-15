# PRE: la matriz debe ser cuadrada, y n un valor mayor que cero perro menor a la cantidad de elementos por fila
# POS: Retorna una lista con los elementos de la columna N en la matriz.
# En caso de no encontrar la columna "N" en la matriz, deculeve una lista vacia.
def DameColumnaN(matriz, n):
    columna = []
    if (n >= 0) and (n < len(matriz)):
        for fila in matriz:
            columna.append(fila[n])
    return columna


def MostrarColumnaParadita(columna):
    for casilla in columna:
        print(casilla)


def TieneAlMenosUnBarco(columna):
    for casillero in columna:
        if casillero != 0:
            return True
    return False


# PRE: La matriz debe ser cuadrada,los parametros fila y columna deben ser enteros
# entre 0 y el largo de la fila.
# POS: Retorna "x" si existe un barco en la posicion (fila,columna) indicada.
def ActualizarMatriz(matriz, fila, columna):
    if (matriz[fila][columna] != "0"):
        matriz[fila][columna] = "x"
    else:
        matriz[fila][columna] = "~"
    return matriz


# PRE: La matriz debe ser cuadrada,el parametro columna deben ser enteros
# entre 0 y el largo de la fila. y LA FILA UNA LETRA DE LA A LA c
# POS: Retorna "x" si existe un barco en la posicion (fila,columna) indicada.
# Si la fila o la columna no es valida, retorna el oceano sin modificaciones.
def ActualizarOceano(oceano, fila, columna):
    if (oceano[fila][columna] != "0"):
        oceano[fila][columna] = "x"
    else:
        oceano[fila][columna] = "~"
    return oceano


# PP

matriz = [["1", "0", "3"],
          ["4", "0", "6"],
          ["7", "8", "9"]]

oceano = {"A": ["1", "0", "3"],
          "B": ["4", "0", "6"],
          "C": ["7", "8", "9"]}

oceanoPremium = {"A":{"A":"1","B":"0", "C":"3"},
                 "B":{"A":"4","B":"0", "C":"6"},
                 "C":{"A":"7","B":"8", "C":"9"}}

""""columna = DameColumnaN(matriz, 1)
MostrarColumnaParadita(columna)
if (TieneAlMenosUnBarco(columna)):
    print("Hay un barco")
else:
    print("NO hay un barco")"""

oceanoPremium = ActualizarMatriz(oceanoPremium, "B", "A")
print(oceanoPremium)
