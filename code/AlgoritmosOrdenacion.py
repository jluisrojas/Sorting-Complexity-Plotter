# Diferentes algoritmos de ordenacion
# Algoritmo de ordenacion burbuja
def BubbleSort(lista):
    for num in range(len(lista)-1, 0, -1):
        for i in range(num):
            if lista[i] > lista[i+1]:
                temp = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = temp

# Algoritmo de ordenacion mezcla
def MergeSort(arr, l, r):
    if l < r:
        m = (l+(r-1))/2
        MergeSort(arr, l, m)
        MergeSort(arr, m+1, r)
        Merge(arr, l, m, r)

def Merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    #Arreglos temporales
    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(0, n1):
        L[i] = arr[l+i]
    
    for j in range(0, n2):
        R[j] =  arr[m+1+j]
    
    i = 0
    j = 0
    k = l

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

# Algoritmo de ordenacion por insercion
def InsertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = key
