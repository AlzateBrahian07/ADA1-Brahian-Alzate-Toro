# Búsqueda Binaria
def busqueda_binaria(arr, x):
    inicio, fin = 0, len(arr) - 1
    while inicio <= fin:
        mid = (inicio + fin) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            inicio = mid + 1
        else:
            fin = mid - 1
    return -1

# Arreglo con 20 datos
arr = sorted([38, 27, 43, 3, 9, 82, 10, 17, 25, 6, 1, 50, 75, 32, 29, 19, 44, 90, 2, 11])
print("Arreglo Ordenado:", arr)
print("Búsqueda Binaria (25):", busqueda_binaria(arr, 25))
print("Complejidad Final: O(log n)")

"""
Complejidad Final: O(log n)
T(n) = T(n/2) + O(1)
Caso 2 del Método Maestro → O(log n)
Significa que cada paso corta el arreglo a la mitad, por eso es logarítmica.
"""
