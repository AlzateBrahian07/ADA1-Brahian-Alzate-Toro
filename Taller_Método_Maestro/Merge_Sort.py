# Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Arreglo con 20 datos
arr = [38, 27, 43, 3, 9, 82, 10, 17, 25, 6, 1, 50, 75, 32, 29, 19, 44, 90, 2, 11]
print("Merge Sort:", merge_sort(arr))
print("Complejidad Final: O(n log n)")

"""""
Complejidad Final: O(n log n)
T(n) = 2T(n/2) + O(n)
Caso 2 del Método Maestro → O(n log n)
Significa que divide el arreglo en mitades y al juntar cuesta O(n).
"""""