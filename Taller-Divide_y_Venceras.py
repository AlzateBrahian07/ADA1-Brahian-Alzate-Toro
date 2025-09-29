# Este codigo se encarga de recibir una lista de productos en formato CSV, para luego dividirlos y ordenarlos
# utilizando el algoritmo Merge Sort, segun las condiciónes dadas: calificación (de mayor a menor) y precio (de menor a mayor).

import csv

# Creamos la función Merge Sort para ordenar los productos
def merge_sort_productos(productos):
    if len(productos) <= 1:
        return productos
    # Los dividimos en 2 mitades
    medio = len(productos) // 2
    izquierda = merge_sort_productos(productos[:medio])
    derecha = merge_sort_productos(productos[medio:])
    return merge(izquierda, derecha)

def merge(izquierda, derecha):
    resultado = []
    i = j = 0
    #Aplicamos las condiciónes de ordenamiento dadas
    while i < len(izquierda) and j < len(derecha):
        # Compararamos primero por  la calificación (En un orden descendente)
        if izquierda[i]["calificacion"] > derecha[j]["calificacion"]:
            resultado.append(izquierda[i])
            i += 1
        elif izquierda[i]["calificacion"] < derecha[j]["calificacion"]:
            resultado.append(derecha[j])
            j += 1
        else:
            # En caso de que la calificación sea igual, compararamos por precio (En un orden ascendente)
            if izquierda[i]["precio"] <= derecha[j]["precio"]:
                resultado.append(izquierda[i])
                i += 1
            else:
                resultado.append(derecha[j])
                j += 1
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado

# Creamos una función que nos permita leer el archivo CSV con los productos, dado por el profesor
def leer_csv(ruta_csv):
    productos = []
    with open(ruta_csv, newline='', encoding="utf-8-sig") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            productos.append({
                "id": int(fila["id"]),
                "nombre": fila["nombre"],
                "precio": float(fila["precio"]),
                "calificacion": int(fila["calificacion"]),
                "stock": int(fila["stock"])
            })
    return productos

# Leer el archivo CSV y ordenar los productos
ruta = "productos.csv"  # Ponemos la ruta del archivo CSV
productos = leer_csv(ruta)
print(" Cantidad de productos leídos:", len(productos))
ordenados = merge_sort_productos(productos)
# Imprimimos los 10 mejores productos
print("\n Mejores productos (top 10):")
for p in ordenados[:10]:
    print(p)

# Guardamos automaticamente el resultado en un nuevo archivo CSV con los productos ordenados
with open("productos_ordenados.csv", "w", newline='', encoding="utf-8") as archivo:
    columnas = ["id", "nombre", "precio", "calificacion", "stock"]
    escritor = csv.DictWriter(archivo, fieldnames=columnas)
    escritor.writeheader()
    escritor.writerows(ordenados)

print("\n Archivo 'productos_ordenados.csv' generado correctamente.")