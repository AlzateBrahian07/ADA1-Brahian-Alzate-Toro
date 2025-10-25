"""
SISTEMA DE TIENDA DE ELECTRÓNICA - BÚSQUEDA LINEAL
==================================================

Este archivo contiene la implementación completa del sistema de tienda de electrónica
que utiliza algoritmos de búsqueda lineal para encontrar productos y empleados.
"""

# =============================================================================
# IMPORTACIONES
# =============================================================================

import json
from typing import List, Dict, Any, Optional, Tuple

# =============================================================================
# DATOS DE EJEMPLO
# =============================================================================

# Lista de productos de la tienda
PRODUCTOS = [
    {'id': 1, 'nombre': 'iPhone 15', 'marca': 'Apple', 'categoria': 'Smartphone', 'precio': 999.99, 'stock': 10, 'disponible': True},
    {'id': 2, 'nombre': 'Samsung Galaxy S24', 'marca': 'Samsung', 'categoria': 'Smartphone', 'precio': 899.99, 'stock': 8, 'disponible': True},
    {'id': 3, 'nombre': 'MacBook Air M3', 'marca': 'Apple', 'categoria': 'Laptop', 'precio': 1299.99, 'stock': 5, 'disponible': True},
    {'id': 4, 'nombre': 'Dell XPS 13', 'marca': 'Dell', 'categoria': 'Laptop', 'precio': 1199.99, 'stock': 0, 'disponible': False},
    {'id': 5, 'nombre': 'Sony WH-1000XM5', 'marca': 'Sony', 'categoria': 'Audífonos', 'precio': 399.99, 'stock': 15, 'disponible': True},
    {'id': 6, 'nombre': 'AirPods Pro 2', 'marca': 'Apple', 'categoria': 'Audífonos', 'precio': 249.99, 'stock': 20, 'disponible': True},
    {'id': 7, 'nombre': 'iPad Pro 12.9"', 'marca': 'Apple', 'categoria': 'Tablet', 'precio': 1099.99, 'stock': 7, 'disponible': True},
    {'id': 8, 'nombre': 'Samsung Galaxy Tab S9', 'marca': 'Samsung', 'categoria': 'Tablet', 'precio': 799.99, 'stock': 4, 'disponible': True},
    {'id': 9, 'nombre': 'Nintendo Switch OLED', 'marca': 'Nintendo', 'categoria': 'Gaming', 'precio': 349.99, 'stock': 12, 'disponible': True},
    {'id': 10, 'nombre': 'PlayStation 5', 'marca': 'Sony', 'categoria': 'Gaming', 'precio': 499.99, 'stock': 3, 'disponible': True}
]

# Lista de empleados de la tienda
EMPLEADOS = [
    {'id': 101, 'nombre': 'Ana', 'apellido': 'García', 'departamento': 'Ventas', 'salario': 35000, 'activo': True},
    {'id': 102, 'nombre': 'Carlos', 'apellido': 'López', 'departamento': 'Técnico', 'salario': 42000, 'activo': True},
    {'id': 103, 'nombre': 'María', 'apellido': 'Rodríguez', 'departamento': 'Ventas', 'salario': 38000, 'activo': False},
    {'id': 104, 'nombre': 'José', 'apellido': 'Martínez', 'departamento': 'Inventario', 'salario': 30000, 'activo': True},
    {'id': 105, 'nombre': 'Laura', 'apellido': 'Fernández', 'departamento': 'Ventas', 'salario': 36000, 'activo': True},
    {'id': 106, 'nombre': 'Roberto', 'apellido': 'González', 'departamento': 'Técnico', 'salario': 45000, 'activo': True},
    {'id': 107, 'nombre': 'Carmen', 'apellido': 'Sánchez', 'departamento': 'Inventario', 'salario': 32000, 'activo': True},
    {'id': 108, 'nombre': 'David', 'apellido': 'Pérez', 'departamento': 'Gerencia', 'salario': 55000, 'activo': True}
]

# =============================================================================
# FUNCIONES DE BÚSQUEDA LINEAL BÁSICAS
# =============================================================================

def busqueda_lineal_simple(lista: List[Any], elemento: Any) -> int:
    """
    Busca un elemento en una lista usando búsqueda lineal.
    
    Args:
        lista: Lista de elementos donde buscar
        elemento: Elemento a buscar
    
    Returns:
        int: Índice del elemento si se encuentra, -1 si no se encuentra
    
    Complejidad: O(n) - tiempo lineal
    """
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return -1

def busqueda_lineal_comparaciones(lista: List[Any], elemento: Any) -> Tuple[int, int]:
    """
    Busca un elemento en una lista y cuenta las comparaciones realizadas.
    
    Args:
        lista: Lista de elementos donde buscar
        elemento: Elemento a buscar
    
    Returns:
        Tuple[int, int]: (índice, número_de_comparaciones)
    
    Complejidad: O(n) - tiempo lineal
    """
    comparaciones = 0
    for i in range(len(lista)):
        comparaciones += 1
        if lista[i] == elemento:
            return i, comparaciones
    return -1, comparaciones

# =============================================================================
# FUNCIONES DE BÚSQUEDA EN PRODUCTOS
# =============================================================================

def buscar_producto_por_id(productos: List[Dict], id_buscado: int) -> Optional[Dict]:
    """
    Busca un producto por su ID usando búsqueda lineal.
    
    Args:
        productos: Lista de diccionarios de productos
        id_buscado: ID del producto a buscar
    
    Returns:
        Optional[Dict]: Diccionario del producto si se encuentra, None si no
    """
    for producto in productos:
        if producto['id'] == id_buscado:
            return producto
    return None

def buscar_producto_por_nombre(productos: List[Dict], nombre_buscado: str) -> Optional[Dict]:
    """
    Busca un producto por nombre (búsqueda exacta).
    
    Args:
        productos: Lista de diccionarios de productos
        nombre_buscado: Nombre del producto a buscar
    
    Returns:
        Optional[Dict]: Diccionario del producto si se encuentra, None si no
    """
    for producto in productos:
        if producto['nombre'].lower() == nombre_buscado.lower():
            return producto
    return None

def buscar_productos_por_marca(productos: List[Dict], marca_buscada: str) -> List[Dict]:
    """
    Busca todos los productos de una marca específica.
    
    Args:
        productos: Lista de diccionarios de productos
        marca_buscada: Marca a buscar
    
    Returns:
        List[Dict]: Lista de productos que coinciden con la marca
    """
    productos_encontrados = []
    for producto in productos:
        if producto['marca'].lower() == marca_buscada.lower():
            productos_encontrados.append(producto)
    return productos_encontrados

def buscar_productos_por_categoria(productos: List[Dict], categoria_buscada: str) -> List[Dict]:
    """
    Busca todos los productos de una categoría específica.
    
    Args:
        productos: Lista de diccionarios de productos
        categoria_buscada: Categoría a buscar
    
    Returns:
        List[Dict]: Lista de productos que coinciden con la categoría
    """
    productos_encontrados = []
    for producto in productos:
        if producto['categoria'].lower() == categoria_buscada.lower():
            productos_encontrados.append(producto)
    return productos_encontrados

def buscar_productos_disponibles(productos: List[Dict]) -> List[Dict]:
    """
    Busca todos los productos disponibles (stock > 0).
    
    Args:
        productos: Lista de diccionarios de productos
    
    Returns:
        List[Dict]: Lista de productos disponibles
    """
    productos_disponibles = []
    for producto in productos:
        if producto['disponible'] and producto['stock'] > 0:
            productos_disponibles.append(producto)
    return productos_disponibles

def buscar_productos_por_rango_precio(productos: List[Dict], precio_min: float, precio_max: float) -> List[Dict]:
    """
    Busca productos dentro de un rango de precios.
    
    Args:
        productos: Lista de diccionarios de productos
        precio_min: Precio mínimo
        precio_max: Precio máximo
    
    Returns:
        List[Dict]: Lista de productos dentro del rango de precios
    """
    productos_en_rango = []
    for producto in productos:
        if precio_min <= producto['precio'] <= precio_max:
            productos_en_rango.append(producto)
    return productos_en_rango

def buscar_productos_bajo_stock(productos: List[Dict], stock_minimo: int = 5) -> List[Dict]:
    """
    Busca productos con stock bajo (para reposición).
    
    Args:
        productos: Lista de diccionarios de productos
        stock_minimo: Stock mínimo considerado como "bajo"
    
    Returns:
        List[Dict]: Lista de productos con stock bajo
    """
    productos_bajo_stock = []
    for producto in productos:
        if producto['stock'] < stock_minimo and producto['stock'] > 0:
            productos_bajo_stock.append(producto)
    return productos_bajo_stock

# =============================================================================
# FUNCIONES DE BÚSQUEDA EN EMPLEADOS
# =============================================================================

def buscar_empleado_por_id(empleados: List[Dict], id_buscado: int) -> Optional[Dict]:
    """
    Busca un empleado por su ID usando búsqueda lineal.
    
    Args:
        empleados: Lista de diccionarios de empleados
        id_buscado: ID del empleado a buscar
    
    Returns:
        Optional[Dict]: Diccionario del empleado si se encuentra, None si no
    """
    for empleado in empleados:
        if empleado['id'] == id_buscado:
            return empleado
    return None

def buscar_empleado_por_nombre_completo(empleados: List[Dict], nombre: str, apellido: str) -> Optional[Dict]:
    """
    Busca un empleado por nombre y apellido.
    
    Args:
        empleados: Lista de diccionarios de empleados
        nombre: Nombre del empleado
        apellido: Apellido del empleado
    
    Returns:
        Optional[Dict]: Diccionario del empleado si se encuentra, None si no
    """
    for empleado in empleados:
        if (empleado['nombre'].lower() == nombre.lower() and 
            empleado['apellido'].lower() == apellido.lower()):
            return empleado
    return None

def buscar_empleados_por_departamento(empleados: List[Dict], departamento: str) -> List[Dict]:
    """
    Busca todos los empleados de un departamento específico.
    
    Args:
        empleados: Lista de diccionarios de empleados
        departamento: Departamento a buscar
    
    Returns:
        List[Dict]: Lista de empleados del departamento
    """
    empleados_departamento = []
    for empleado in empleados:
        if empleado['departamento'].lower() == departamento.lower():
            empleados_departamento.append(empleado)
    return empleados_departamento

def buscar_empleados_activos(empleados: List[Dict]) -> List[Dict]:
    """
    Busca todos los empleados activos.
    
    Args:
        empleados: Lista de diccionarios de empleados
    
    Returns:
        List[Dict]: Lista de empleados activos
    """
    empleados_activos = []
    for empleado in empleados:
        if empleado['activo']:
            empleados_activos.append(empleado)
    return empleados_activos

def buscar_empleados_por_rango_salario(empleados: List[Dict], salario_min: float, salario_max: float) -> List[Dict]:
    """
    Busca empleados dentro de un rango de salarios.
    
    Args:
        empleados: Lista de diccionarios de empleados
        salario_min: Salario mínimo
        salario_max: Salario máximo
    
    Returns:
        List[Dict]: Lista de empleados dentro del rango de salarios
    """
    empleados_en_rango = []
    for empleado in empleados:
        if salario_min <= empleado['salario'] <= salario_max:
            empleados_en_rango.append(empleado)
    return empleados_en_rango

# =============================================================================
# FUNCIONES DE UTILIDAD Y ESTADÍSTICAS
# =============================================================================

def contar_productos_por_categoria(productos: List[Dict]) -> Dict[str, int]:
    """
    Cuenta cuántos productos hay en cada categoría.
    
    Args:
        productos: Lista de diccionarios de productos
    
    Returns:
        Dict[str, int]: Diccionario con categorías y sus conteos
    """
    conteo = {}
    for producto in productos:
        categoria = producto['categoria']
        conteo[categoria] = conteo.get(categoria, 0) + 1
    return conteo

def obtener_valor_total_inventario(productos: List[Dict]) -> float:
    """
    Calcula el valor total del inventario.
    
    Args:
        productos: Lista de diccionarios de productos
    
    Returns:
        float: Valor total del inventario
    """
    valor_total = 0.0
    for producto in productos:
        valor_total += producto['precio'] * producto['stock']
    return valor_total

def obtener_estadisticas_empleados(empleados: List[Dict]) -> Dict[str, Any]:
    """
    Calcula estadísticas básicas de los empleados.
    
    Args:
        empleados: Lista de diccionarios de empleados
    
    Returns:
        Dict[str, Any]: Diccionario con estadísticas
    """
    if not empleados:
        return {}
    
    salarios = [emp['salario'] for emp in empleados if emp['activo']]
    empleados_activos = len([emp for emp in empleados if emp['activo']])
    
    estadisticas = {
        'total_empleados': len(empleados),
        'empleados_activos': empleados_activos,
        'salario_promedio': sum(salarios) / len(salarios) if salarios else 0,
        'salario_minimo': min(salarios) if salarios else 0,
        'salario_maximo': max(salarios) if salarios else 0
    }
    
    return estadisticas

# =============================================================================
# FUNCIONES DE PRESENTACIÓN
# =============================================================================

def mostrar_producto(producto: Dict) -> None:
    """Muestra la información de un producto de forma legible."""
    if producto:
        print(f"📱 {producto['nombre']} - {producto['marca']}")
        print(f"   Categoría: {producto['categoria']}")
        print(f"   Precio: ${producto['precio']:.2f}")
        print(f"   Stock: {producto['stock']} unidades")
        print(f"   Disponible: {'✅ Sí' if producto['disponible'] else '❌ No'}")
        print("-" * 50)
    else:
        print("❌ Producto no encontrado")

def mostrar_empleado(empleado: Dict) -> None:
    """Muestra la información de un empleado de forma legible."""
    if empleado:
        print(f"👤 {empleado['nombre']} {empleado['apellido']}")
        print(f"   ID: {empleado['id']}")
        print(f"   Departamento: {empleado['departamento']}")
        print(f"   Salario: ${empleado['salario']:,.2f}")
        print(f"   Estado: {'✅ Activo' if empleado['activo'] else '❌ Inactivo'}")
        print("-" * 50)
    else:
        print("❌ Empleado no encontrado")

def mostrar_lista_productos(productos: List[Dict], titulo: str = "Productos") -> None:
    """Muestra una lista de productos de forma legible."""
    if productos:
        print(f"\n📋 {titulo} ({len(productos)} encontrados):")
        print("=" * 60)
        for producto in productos:
            mostrar_producto(producto)
    else:
        print(f"\n❌ No se encontraron {titulo.lower()}")

def mostrar_lista_empleados(empleados: List[Dict], titulo: str = "Empleados") -> None:
    """Muestra una lista de empleados de forma legible."""
    if empleados:
        print(f"\n👥 {titulo} ({len(empleados)} encontrados):")
        print("=" * 60)
        for empleado in empleados:
            mostrar_empleado(empleado)
    else:
        print(f"\n❌ No se encontraron {titulo.lower()}")

# =============================================================================
# FUNCIÓN PRINCIPAL Y MENÚ
# =============================================================================

def menu_principal():
    """Muestra el menú principal del sistema."""
    while True:
        print("\n" + "="*60)
        print("🏪 SISTEMA DE TIENDA DE ELECTRÓNICA - TALLER BÚSQUEDA LINEAL")
        print("="*60)
        print("1. 🔍 Búsqueda de Productos")
        print("2. 👥 Búsqueda de Empleados")
        print("3. 📊 Estadísticas y Reportes")
        print("4. 🧪 Pruebas de Búsqueda Lineal")
        print("5. ❌ Salir")
        print("-"*60)
        
        opcion = input("Seleccione una opción (1-5): ").strip()
        
        if opcion == "1":
            menu_productos()
        elif opcion == "2":
            menu_empleados()
        elif opcion == "3":
            menu_estadisticas()
        elif opcion == "4":
            menu_pruebas()
        elif opcion == "5":
            print("\n👋 ¡Gracias por usar el sistema de tienda!")
            break
        else:
            print("\n❌ Opción no válida. Por favor, seleccione una opción del 1 al 5.")

def menu_productos():
    """Menú de búsqueda de productos."""
    while True:
        print("\n" + "="*50)
        print("🔍 BÚSQUEDA DE PRODUCTOS")
        print("="*50)
        print("1. Buscar por ID")
        print("2. Buscar por nombre")
        print("3. Buscar por marca")
        print("4. Buscar por categoría")
        print("5. Productos disponibles")
        print("6. Productos por rango de precio")
        print("7. Productos con stock bajo")
        print("8. ← Volver al menú principal")
        print("-"*50)
        
        opcion = input("Seleccione una opción (1-8): ").strip()
        
        if opcion == "1":
            try:
                id_buscado = int(input("Ingrese el ID del producto: "))
                producto = buscar_producto_por_id(PRODUCTOS, id_buscado)
                mostrar_producto(producto)
            except ValueError:
                print("❌ Por favor, ingrese un ID válido (número entero)")
                
        elif opcion == "2":
            nombre = input("Ingrese el nombre del producto: ").strip()
            producto = buscar_producto_por_nombre(PRODUCTOS, nombre)
            mostrar_producto(producto)
            
        elif opcion == "3":
            marca = input("Ingrese la marca a buscar: ").strip()
            productos = buscar_productos_por_marca(PRODUCTOS, marca)
            mostrar_lista_productos(productos, f"Productos de la marca {marca}")
            
        elif opcion == "4":
            categoria = input("Ingrese la categoría a buscar: ").strip()
            productos = buscar_productos_por_categoria(PRODUCTOS, categoria)
            mostrar_lista_productos(productos, f"Productos de la categoría {categoria}")
            
        elif opcion == "5":
            productos = buscar_productos_disponibles(PRODUCTOS)
            mostrar_lista_productos(productos, "Productos Disponibles")
            
        elif opcion == "6":
            try:
                precio_min = float(input("Ingrese el precio mínimo: $"))
                precio_max = float(input("Ingrese el precio máximo: $"))
                productos = buscar_productos_por_rango_precio(PRODUCTOS, precio_min, precio_max)
                mostrar_lista_productos(productos, f"Productos entre ${precio_min} y ${precio_max}")
            except ValueError:
                print("❌ Por favor, ingrese precios válidos")
                
        elif opcion == "7":
            try:
                stock_minimo = int(input("Ingrese el stock mínimo (por defecto 5): ") or "5")
                productos = buscar_productos_bajo_stock(PRODUCTOS, stock_minimo)
                mostrar_lista_productos(productos, f"Productos con stock bajo ({stock_minimo})")
            except ValueError:
                print("❌ Por favor, ingrese un número válido")
                
        elif opcion == "8":
            break
        else:
            print("❌ Opción no válida. Por favor, seleccione una opción del 1 al 8.")

def menu_empleados():
    """Menú de búsqueda de empleados."""
    while True:
        print("\n" + "="*50)
        print("👥 BÚSQUEDA DE EMPLEADOS")
        print("="*50)
        print("1. Buscar por ID")
        print("2. Buscar por nombre completo")
        print("3. Buscar por departamento")
        print("4. Empleados activos")
        print("5. Empleados por rango de salario")
        print("6. ← Volver al menú principal")
        print("-"*50)
        
        opcion = input("Seleccione una opción (1-6): ").strip()
        
        if opcion == "1":
            try:
                id_buscado = int(input("Ingrese el ID del empleado: "))
                empleado = buscar_empleado_por_id(EMPLEADOS, id_buscado)
                mostrar_empleado(empleado)
            except ValueError:
                print("❌ Por favor, ingrese un ID válido (número entero)")
                
        elif opcion == "2":
            nombre = input("Ingrese el nombre: ").strip()
            apellido = input("Ingrese el apellido: ").strip()
            empleado = buscar_empleado_por_nombre_completo(EMPLEADOS, nombre, apellido)
            mostrar_empleado(empleado)
            
        elif opcion == "3":
            departamento = input("Ingrese el departamento: ").strip()
            empleados = buscar_empleados_por_departamento(EMPLEADOS, departamento)
            mostrar_lista_empleados(empleados, f"Empleados del departamento {departamento}")
            
        elif opcion == "4":
            empleados = buscar_empleados_activos(EMPLEADOS)
            mostrar_lista_empleados(empleados, "Empleados Activos")
            
        elif opcion == "5":
            try:
                salario_min = float(input("Ingrese el salario mínimo: $"))
                salario_max = float(input("Ingrese el salario máximo: $"))
                empleados = buscar_empleados_por_rango_salario(EMPLEADOS, salario_min, salario_max)
                mostrar_lista_empleados(empleados, f"Empleados con salario entre ${salario_min} y ${salario_max}")
            except ValueError:
                print("❌ Por favor, ingrese salarios válidos")
                
        elif opcion == "6":
            break
        else:
            print("❌ Opción no válida. Por favor, seleccione una opción del 1 al 6.")

def menu_estadisticas():
    """Menú de estadísticas y reportes."""
    print("\n" + "="*50)
    print("📊 ESTADÍSTICAS Y REPORTES")
    print("="*50)
    
    # Estadísticas de productos
    print("\n📱 ESTADÍSTICAS DE PRODUCTOS:")
    print("-" * 30)
    conteo_categorias = contar_productos_por_categoria(PRODUCTOS)
    for categoria, cantidad in conteo_categorias.items():
        print(f"   {categoria}: {cantidad} productos")
    
    valor_inventario = obtener_valor_total_inventario(PRODUCTOS)
    print(f"\n   Valor total del inventario: ${valor_inventario:,.2f}")
    
    productos_disponibles = buscar_productos_disponibles(PRODUCTOS)
    print(f"   Productos disponibles: {len(productos_disponibles)}/{len(PRODUCTOS)}")
    
    # Estadísticas de empleados
    print("\n👥 ESTADÍSTICAS DE EMPLEADOS:")
    print("-" * 30)
    stats = obtener_estadisticas_empleados(EMPLEADOS)
    print(f"   Total empleados: {stats['total_empleados']}")
    print(f"   Empleados activos: {stats['empleados_activos']}")
    print(f"   Salario promedio: ${stats['salario_promedio']:,.2f}")
    print(f"   Salario mínimo: ${stats['salario_minimo']:,.2f}")
    print(f"   Salario máximo: ${stats['salario_maximo']:,.2f}")
    
    input("\nPresione Enter para continuar...")

def menu_pruebas():
    """Menú de pruebas de búsqueda lineal."""
    print("\n" + "="*50)
    print("🧪 PRUEBAS DE BÚSQUEDA LINEAL")
    print("="*50)
    
    # Prueba básica
    print("\n1. Prueba de búsqueda lineal básica:")
    numeros = [64, 34, 25, 12, 22, 11, 90]
    elemento_buscado = 25
    
    indice, comparaciones = busqueda_lineal_comparaciones(numeros, elemento_buscado)
    print(f"   Lista: {numeros}")
    print(f"   Buscando: {elemento_buscado}")
    print(f"   Resultado: Índice {indice}, Comparaciones: {comparaciones}")
    
    # Prueba con elemento no encontrado
    elemento_no_encontrado = 99
    indice, comparaciones = busqueda_lineal_comparaciones(numeros, elemento_no_encontrado)
    print(f"\n   Buscando: {elemento_no_encontrado}")
    print(f"   Resultado: Índice {indice}, Comparaciones: {comparaciones}")
    
    # Prueba de búsqueda en productos
    print("\n2. Prueba de búsqueda en productos:")
    producto_encontrado = buscar_producto_por_id(PRODUCTOS, 3)
    if producto_encontrado:
        print(f"   Producto encontrado: {producto_encontrado['nombre']}")
    
    # Prueba de búsqueda en empleados
    print("\n3. Prueba de búsqueda en empleados:")
    empleado_encontrado = buscar_empleado_por_id(EMPLEADOS, 102)
    if empleado_encontrado:
        print(f"   Empleado encontrado: {empleado_encontrado['nombre']} {empleado_encontrado['apellido']}")
    
    input("\nPresione Enter para continuar...")

# =============================================================================
# FUNCIÓN PRINCIPAL
# =============================================================================

def main():
    """Función principal del programa."""
    print("🚀 Iniciando Sistema de Tienda de Electrónica...")
    print("📚 Taller de Búsqueda Lineal")
    print("\n💡 Tip: Este sistema demuestra el uso del algoritmo de búsqueda lineal")
    print("   en un contexto real de gestión de tienda.")
    
    try:
        menu_principal()
    except KeyboardInterrupt:
        print("\n\n👋 Programa interrumpido por el usuario. ¡Hasta luego!")
    except Exception as e:
        print(f"\n❌ Error inesperado: {e}")
        print("Por favor, reporte este error al instructor.")

if __name__ == "__main__":
    main()
