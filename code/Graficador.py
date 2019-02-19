# Algoritmos y Complejidad
# Profesor: Juan Carlos Cueva Tello
# Alumno: Rojas Aranda Jose Luis

import datetime as time
import numpy as np
from matplotlib import pyplot as plt
import AlgoritmosOrdenacion as sort

# Configuaracion
inicio = 0        # Tamano inicial del arreglo
aumento = 1       # Aumento del tamano del arreglo
tamMax = 1000001     # Tamano maximo del arreglo
#arr = []            # Arreglo generado aleatoriamente

bubbleT = []        # Tiempo del bubble sort
insertionT = []     # Tiempo del insertion sort
mergeT = []         # Tiempo del merge sort
tamX = []           # Valores de la grafica en X

# Prueba los algoritmos de ordenacion y regresa un arreglo con los tiempos de ejecucion
def ProbarOrdenacion(n):
    res = []
    arr = []
    # Bubble sort
    arr = np.random.randint(1, 1000, size=n)
    a = time.datetime.now()
    sort.BubbleSort(arr)
    b = time.datetime.now()
    res.append(int((b-a).total_seconds() * 1000000))

    # Insertion sort
    arr = np.random.randint(1, 1000, size=n)
    a = time.datetime.now()
    sort.InsertionSort(arr)
    b = time.datetime.now()
    res.append(int((b-a).total_seconds() * 1000000))

     # Merge sort
    arr = np.random.randint(1, 1000, size=n)
    a = time.datetime.now()
    sort.MergeSort(arr, 0, n-1)
    b = time.datetime.now()
    res.append(int((b-a).total_seconds() * 1000000))

    return res

# Dibuja la grafica
def dibujar():
    # plt.scatter(i, y)
    plt.plot(tamX, bubbleT, 'b')
    plt.plot(tamX, insertionT, 'r')
    plt.plot(tamX, mergeT, 'g')
    plt.title("Algoritmos de ordenacion")
    plt.xlabel("Tamano del arreglo")
    plt.ylabel("Tiempo")
    plt.legend(["bubble sort", "insertion sort", "merge sort"])

# Funcion main
def main():
    tam = inicio
    while tam < tamMax:
        res = ProbarOrdenacion(tam)

        bubbleT.append(res[0])
        insertionT.append(res[1])
        mergeT.append(res[2])

        tamX.append(tam)
        tam += aumento

        dibujar()
        plt.pause(0.05)


    print("----------------------------------")
    print("Tiempos:")
    print(tamX)
    print("Bubble Sort:")
    print(bubbleT)
    print("Insertion Sort:")
    print(insertionT)
    print("Merge Sort:")
    print(mergeT)


main()
dibujar()
plt.show()

