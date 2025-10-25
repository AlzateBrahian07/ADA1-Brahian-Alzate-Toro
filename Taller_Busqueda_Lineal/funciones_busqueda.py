"""
EJERCICIOS PRÁCTICOS - BÚSQUEDA LINEAL
======================================

Este archivo contiene ejercicios paso a paso para practicar la implementación
del algoritmo de búsqueda lineal en el contexto de una tienda de electrónica.

INSTRUCCIONES:
- Completa cada función según las especificaciones
- Prueba tu código con los casos de prueba proporcionados
- No modifiques las funciones de prueba
"""

# =============================================================================
print("EJERCICIO 1: IMPLEMENTACIÓN BÁSICA DE BÚSQUEDA LINEAL")
# =============================================================================

def busqueda_lineal_simple(lista, elemento):
    """
    Busca un elemento en una lista recorriéndola de forma lineal.
    Parámetros:
      - lista: lista de elementos
      - elemento: valor a buscar
    Retorna:
      - índice del primer elemento igual a 'elemento' o -1 si no se encuentra
    """
    for i in range(len(lista)):
        # comparar elemento en la posición i
        if lista[i] == elemento:
            return i
    # no se encontró el elemento
    return -1
    
# Pruebas
lista = [64, 34, 25, 12, 22, 11, 90]
print("1. Buscar el índice del elemento 25 (está en la lista)")
print(busqueda_lineal_simple(lista, 25))  # Debe retornar 2
print("2. Buscar el índice del elemento 99 (no está en la lista)")
print(busqueda_lineal_simple(lista, 99))  # Debe retornar -1
print("3. Buscar el índice del primer elemento 64")
print(busqueda_lineal_simple(lista, 64))  # Debe retornar 0
print("4. Buscar el índice del último elemento 90")
print(busqueda_lineal_simple(lista, 90))  # Debe retornar 6

# =============================================================================
print("EJERCICIO 2: BÚSQUEDA EN LISTA DE PRODUCTOS")
# =============================================================================
def busqueda_lineal_productos(lista, clave, valor):
    """
    Búsqueda lineal en una lista de diccionarios (productos).
    Parámetros:
      - lista: lista de diccionarios
      - clave: clave dentro del diccionario a comparar (ej. 'nombre', 'id')
      - valor: valor esperado para la clave
    Retorna:
      - índice del primer diccionario que cumple dic[clave] == valor o -1
    """
    for i in range(len(lista)):
        # obtener valor seguro con .get y comparar
        if lista[i].get(clave) == valor:
            return i
    return -1

# función para buscar producto por nombre:
def buscar_producto_por_nombre(productos, nombre):
    # wrapper que busca por la clave 'nombre'
    return busqueda_lineal_productos(productos, 'nombre', nombre)

# función para buscar producto por ID:
def buscar_producto_por_id(productos, id_producto):
    # wrapper que busca por la clave 'id'
    return busqueda_lineal_productos(productos, 'id', id_producto)

# función para buscar producto por categoría:
def buscar_producto_por_categoria(productos, categoria):
    # wrapper que busca por la clave 'categoria'
    return busqueda_lineal_productos(productos, 'categoria', categoria)

# Pruebas
productos = [
    {'id': 1, 'nombre': 'iPhone 15', 'marca': 'Apple', 'categoria': 'Smartphone', 'precio': 999.99, 'stock': 10, 'disponible': True},
    {'id': 2, 'nombre': 'Samsung Galaxy S24', 'marca': 'Samsung', 'categoria': 'Smartphone', 'precio': 899.99, 'stock': 8, 'disponible': True},
    {'id': 3, 'nombre': 'MacBook Air M3', 'marca': 'Apple', 'categoria': 'Laptop', 'precio': 1299.99, 'stock': 5, 'disponible': True},
    {'id': 4, 'nombre': 'Dell XPS 13', 'marca': 'Dell', 'categoria': 'Laptop', 'precio': 1199.99, 'stock': 0, 'disponible': False},
    {'id': 5, 'nombre': 'Sony WH-1000XM5', 'marca': 'Sony', 'categoria': 'Audífonos', 'precio': 399.99, 'stock': 15, 'disponible': True}
]
print("1. Buscar producto por nombre 'MacBook Air M3'")
print(buscar_producto_por_nombre(productos, 'MacBook Air M3'))  # Debe retornar 2
print("2. Buscar producto por ID '4'")
print(buscar_producto_por_id(productos, 4))  # Debe retornar 3
print("3. Buscar producto por categoría 'Audífonos'")
print(buscar_producto_por_categoria(productos, 'Audífonos'))  # Debe retornar 4

# =============================================================================
print("EJERCICIO 3: BÚSQUEDA DE EMPLEADOS")
# =============================================================================
def busqueda_lineal_empleados(lista, clave, valor):
    """
    Búsqueda lineal genérica para listas de empleados (diccionarios).
    Igual funcionamiento que busqueda_lineal_productos pero pensado para empleados.
    """
    for i in range(len(lista)):
        if lista[i].get(clave) == valor:
            return i
    return -1

# función para buscar empleado por nombre completo:
def buscar_empleado_por_nombre_completo(empleados, nombre, apellido):
    """
    Busca un empleado comparando las claves 'nombre' y 'apellido' simultáneamente.
    Retorna el índice del primer empleado que coincida o -1.
    """
    for i in range(len(empleados)):
        # comparar ambos campos
        if empleados[i].get('nombre') == nombre and empleados[i].get('apellido') == apellido:
            return i
    return -1

# función para buscar empleado por departamento:
def buscar_empleado_por_departamento(empleados, departamento):
    # wrapper para buscar por la clave 'departamento'
    return busqueda_lineal_empleados(empleados, 'departamento', departamento)

# función para buscar empleados activos:
def buscar_empleado_activo(empleados):
    """
    Busca el primer empleado con el campo 'activo' == True.
    Retorna índice o -1 si no hay ninguno activo.
    """
    for i in range(len(empleados)):
        if empleados[i].get('activo') == True:
            return i
    return -1

empleados = [
    {'id': 101, 'nombre': 'Ana', 'apellido': 'García', 'departamento': 'Ventas', 'salario': 35000, 'activo': True},
    {'id': 102, 'nombre': 'Carlos', 'apellido': 'López', 'departamento': 'Técnico', 'salario': 42000, 'activo': True},
    {'id': 103, 'nombre': 'María', 'apellido': 'Rodríguez', 'departamento': 'Ventas', 'salario': 38000, 'activo': False},
    {'id': 104, 'nombre': 'José', 'apellido': 'Martínez', 'departamento': 'Inventario', 'salario': 30000, 'activo': True}
]
# Pruebas
print("1. Buscar empleado por nombre completo 'Carlos López'")
print(buscar_empleado_por_nombre_completo(empleados, 'Carlos', 'López'))  # Debe retornar 1
print("2. Buscar empleado por departamento 'Ventas'")
print(buscar_empleado_por_departamento(empleados, 'Ventas'))  # Debe retornar 0
print("3. Buscar primer empleado activo")
print(buscar_empleado_activo(empleados))  # Debe retornar 0

# =============================================================================
print("EJERCICIO 4: BÚSQUEDA POR DISPONIBILIDAD")
# =============================================================================
# stock>0
def buscar_producto_disponible(productos):
    """
    Busca el primer producto cuyo stock sea mayor que 0.
    Retorna el índice del producto disponible o -1 si no existe.
    """
    for i in range(len(productos)):
        # usar get con valor por defecto 0 para evitar KeyError
        if productos[i].get('stock', 0) > 0:
            return i
    return -1

# precio dentro de un rango
def buscar_producto_por_rango_precio(productos, precio_min, precio_max):
    """
    Busca el primer producto cuyo precio esté entre precio_min y precio_max (inclusive).
    Retorna índice o -1.
    """
    for i in range(len(productos)):
        precio = productos[i].get('precio', 0)
        if precio_min <= precio <= precio_max:
            return i
    return -1

def buscar_producto_por_marca(productos, marca):
    # wrapper que busca por la clave 'marca'
    return busqueda_lineal_productos(productos, 'marca', marca)

def contar_productos_en_una_categoria(productos, categoria):
    """
    Cuenta cuántos productos pertenecen a una categoría determinada.
    Retorna un entero con el contador.
    """
    contador = 0
    for i in range(len(productos)):
        if productos[i].get('categoria') == categoria:
            contador += 1
    return contador

# Pruebas
print("1. Buscar primer producto con stock > 0")
print(buscar_producto_disponible(productos))  # Debe retornar 0
print("2. Buscar primer producto con precio entre 500 y 1000")
print(buscar_producto_por_rango_precio(productos, 500, 1000))  # Debe retornar 0
print("3. Buscar producto por marca 'Apple'")
print(buscar_producto_por_marca(productos, 'Apple'))  # Debe retornar 0
print("4. Contar productos en la categoría 'Laptop'")
print(contar_productos_en_una_categoria(productos, 'Laptop'))  # Debe retornar 2

# =============================================================================
print("EJERCICIO 5: SISTEMA INTEGRADO DE BÚSQUEDA")
# =============================================================================
"""
EJERCICIO 5: SISTEMA INTEGRADO DE BÚSQUEDA
Autor: [Tu nombre aquí]
Descripción:
Menú interactivo que utiliza las funciones de búsqueda lineal implementadas
en ejercicios anteriores.
"""

from funciones_busqueda import *

def mostrar_producto(productos, indice):
    """Muestra la información de un producto encontrado."""
    if indice == -1:
        print("⚠️ Producto no encontrado.")
    else:
        p = productos[indice]
        # mostrar campos más relevantes del producto
        print(f"✅ Producto encontrado:")
        print(f"ID: {p['id']} | Nombre: {p['nombre']} | Marca: {p['marca']} | "
              f"Categoría: {p['categoria']} | Precio: ${p['precio']} | Stock: {p['stock']}")

def mostrar_empleado(empleados, indice):
    """Muestra la información de un empleado encontrado."""
    if indice == -1:
        print("⚠️ Empleado no encontrado.")
    else:
        e = empleados[indice]
        estado = "Activo ✅" if e['activo'] else "Inactivo ❌"
        print(f"✅ Empleado encontrado:")
        print(f"ID: {e['id']} | {e['nombre']} {e['apellido']} | "
              f"Departamento: {e['departamento']} | Salario: ${e['salario']} | Estado: {estado}")

def menu_principal():
    """
    Menú principal interactivo.
    Permite acceder al menú de productos, empleados o salir del programa.
    """
    while True:
        print("\n=== 🏪 SISTEMA DE TIENDA TECHSTORE ===")
        print("1. Buscar producto")
        print("2. Buscar empleado")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_productos()
        elif opcion == "2":
            menu_empleados()
        elif opcion == "3":
            print("👋 Gracias por usar el sistema TechStore.")
            break
        else:
            print("❌ Opción no válida. Intente nuevamente.")

def menu_productos():
    """
    Submenú de productos.
    Permite distintas búsquedas y consultas sobre la lista 'productos'.
    """
    while True:
        print("\n--- 🔍 BÚSQUEDA DE PRODUCTOS ---")
        print("1. Buscar por nombre")
        print("2. Buscar por ID")
        print("3. Buscar por categoría")
        print("4. Buscar por marca")
        print("5. Buscar producto disponible (stock > 0)")
        print("6. Buscar por rango de precios")
        print("7. Contar productos por categoría")
        print("8. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del producto: ")
            mostrar_producto(productos, buscar_producto_por_nombre(productos, nombre))

        elif opcion == "2":
            try:
                id_producto = int(input("Ingrese el ID del producto: "))
                mostrar_producto(productos, buscar_producto_por_id(productos, id_producto))
            except ValueError:
                print("⚠️ Debe ingresar un número válido.")

        elif opcion == "3":
            categoria = input("Ingrese la categoría: ")
            mostrar_producto(productos, buscar_producto_por_categoria(productos, categoria))

        elif opcion == "4":
            marca = input("Ingrese la marca: ")
            mostrar_producto(productos, buscar_producto_por_marca(productos, marca))

        elif opcion == "5":
            mostrar_producto(productos, buscar_producto_disponible(productos))

        elif opcion == "6":
            try:
                minimo = float(input("Precio mínimo: "))
                maximo = float(input("Precio máximo: "))
                mostrar_producto(productos, buscar_producto_por_rango_precio(productos, minimo, maximo))
            except ValueError:
                print("⚠️ Ingrese valores numéricos válidos.")

        elif opcion == "7":
            categoria = input("Ingrese la categoría: ")
            cantidad = contar_productos_en_una_categoria(productos, categoria)
            print(f"📦 Hay {cantidad} productos en la categoría '{categoria}'.")

        elif opcion == "8":
            break
        else:
            print("❌ Opción no válida, intente de nuevo.")

def menu_empleados():
    """
    Submenú de empleados.
    Permite buscar por nombre completo, por departamento o el primer activo.
    """
    while True:
        print("\n--- 👥 BÚSQUEDA DE EMPLEADOS ---")
        print("1. Buscar por nombre completo")
        print("2. Buscar por departamento")
        print("3. Buscar primer empleado activo")
        print("4. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            mostrar_empleado(empleados, buscar_empleado_por_nombre_completo(empleados, nombre, apellido))

        elif opcion == "2":
            departamento = input("Departamento: ")
            mostrar_empleado(empleados, buscar_empleado_por_departamento(empleados, departamento))

        elif opcion == "3":
            mostrar_empleado(empleados, buscar_empleado_activo(empleados))

        elif opcion == "4":
            break
        else:
            print("❌ Opción no válida, intente de nuevo.")

# ---------------- EJECUCIÓN ----------------
if __name__ == "__main__":
    menu_principal()
