# Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivote = arr[len(arr) // 2]
    menores = [x for x in arr if x < pivote]
    iguales = [x for x in arr if x == pivote]
    mayores = [x for x in arr if x > pivote]
    
    return quick_sort(menores) + iguales + quick_sort(mayores)

# Arreglo con 20 datos
arr = [38, 27, 43, 3, 9, 82, 10, 17, 25, 6, 1, 50, 75, 32, 29, 19, 44, 90, 2, 11]
print("Quick Sort:", quick_sort(arr))
print("Complejidad: O(n log n) en promedio, O(n^2) en el peor caso")

"""
Complejidad de Quick Sort:
Mejor caso:
T(n) = 2T(n/2) + O(n) → O(n log n)
Peor caso:
T(n) = T(n-1) + O(n) → O(n^2)
Significa que normalmente es muy rápido (n log n), pero puede ser lento si el pivote se escoge mal.
"""
