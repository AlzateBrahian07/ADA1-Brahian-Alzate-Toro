"""
DATOS DE EJEMPLO PARA EL TALLER DE BÚSQUEDA LINEAL
==================================================

Este archivo contiene datos de ejemplo adicionales que pueden ser utilizados
para probar y experimentar con las funciones de búsqueda lineal.

Puedes importar estos datos en tus propios scripts de prueba.
"""

# =============================================================================
# DATOS DE PRODUCTOS EXTENDIDOS
# =============================================================================

PRODUCTOS_EXTENDIDOS = [
    # Smartphones
    {'id': 1, 'nombre': 'iPhone 15', 'marca': 'Apple', 'categoria': 'Smartphone', 'precio': 999.99, 'stock': 10, 'disponible': True},
    {'id': 2, 'nombre': 'iPhone 15 Pro', 'marca': 'Apple', 'categoria': 'Smartphone', 'precio': 1199.99, 'stock': 8, 'disponible': True},
    {'id': 3, 'nombre': 'Samsung Galaxy S24', 'marca': 'Samsung', 'categoria': 'Smartphone', 'precio': 899.99, 'stock': 12, 'disponible': True},
    {'id': 4, 'nombre': 'Samsung Galaxy S24 Ultra', 'marca': 'Samsung', 'categoria': 'Smartphone', 'precio': 1299.99, 'stock': 6, 'disponible': True},
    {'id': 5, 'nombre': 'Google Pixel 8', 'marca': 'Google', 'categoria': 'Smartphone', 'precio': 699.99, 'stock': 15, 'disponible': True},
    {'id': 6, 'nombre': 'OnePlus 12', 'marca': 'OnePlus', 'categoria': 'Smartphone', 'precio': 799.99, 'stock': 0, 'disponible': False},
    
    # Laptops
    {'id': 7, 'nombre': 'MacBook Air M3', 'marca': 'Apple', 'categoria': 'Laptop', 'precio': 1299.99, 'stock': 5, 'disponible': True},
    {'id': 8, 'nombre': 'MacBook Pro M3', 'marca': 'Apple', 'categoria': 'Laptop', 'precio': 1999.99, 'stock': 3, 'disponible': True},
    {'id': 9, 'nombre': 'Dell XPS 13', 'marca': 'Dell', 'categoria': 'Laptop', 'precio': 1199.99, 'stock': 0, 'disponible': False},
    {'id': 10, 'nombre': 'Dell XPS 15', 'marca': 'Dell', 'categoria': 'Laptop', 'precio': 1499.99, 'stock': 4, 'disponible': True},
    {'id': 11, 'nombre': 'HP Spectre x360', 'marca': 'HP', 'categoria': 'Laptop', 'precio': 1299.99, 'stock': 7, 'disponible': True},
    {'id': 12, 'nombre': 'Lenovo ThinkPad X1', 'marca': 'Lenovo', 'categoria': 'Laptop', 'precio': 1599.99, 'stock': 2, 'disponible': True},
    
    # Tablets
    {'id': 13, 'nombre': 'iPad Pro 12.9"', 'marca': 'Apple', 'categoria': 'Tablet', 'precio': 1099.99, 'stock': 7, 'disponible': True},
    {'id': 14, 'nombre': 'iPad Air', 'marca': 'Apple', 'categoria': 'Tablet', 'precio': 599.99, 'stock': 12, 'disponible': True},
    {'id': 15, 'nombre': 'Samsung Galaxy Tab S9', 'marca': 'Samsung', 'categoria': 'Tablet', 'precio': 799.99, 'stock': 4, 'disponible': True},
    {'id': 16, 'nombre': 'Microsoft Surface Pro 9', 'marca': 'Microsoft', 'categoria': 'Tablet', 'precio': 999.99, 'stock': 6, 'disponible': True},
    
    # Audífonos
    {'id': 17, 'nombre': 'AirPods Pro 2', 'marca': 'Apple', 'categoria': 'Audífonos', 'precio': 249.99, 'stock': 20, 'disponible': True},
    {'id': 18, 'nombre': 'AirPods Max', 'marca': 'Apple', 'categoria': 'Audífonos', 'precio': 549.99, 'stock': 8, 'disponible': True},
    {'id': 19, 'nombre': 'Sony WH-1000XM5', 'marca': 'Sony', 'categoria': 'Audífonos', 'precio': 399.99, 'stock': 15, 'disponible': True},
    {'id': 20, 'nombre': 'Bose QuietComfort 45', 'marca': 'Bose', 'categoria': 'Audífonos', 'precio': 329.99, 'stock': 10, 'disponible': True},
    {'id': 21, 'nombre': 'Sennheiser HD 660S', 'marca': 'Sennheiser', 'categoria': 'Audífonos', 'precio': 499.99, 'stock': 3, 'disponible': True},
    
    # Gaming
    {'id': 22, 'nombre': 'PlayStation 5', 'marca': 'Sony', 'categoria': 'Gaming', 'precio': 499.99, 'stock': 3, 'disponible': True},
    {'id': 23, 'nombre': 'Xbox Series X', 'marca': 'Microsoft', 'categoria': 'Gaming', 'precio': 499.99, 'stock': 5, 'disponible': True},
    {'id': 24, 'nombre': 'Nintendo Switch OLED', 'marca': 'Nintendo', 'categoria': 'Gaming', 'precio': 349.99, 'stock': 12, 'disponible': True},
    {'id': 25, 'nombre': 'Steam Deck', 'marca': 'Valve', 'categoria': 'Gaming', 'precio': 399.99, 'stock': 8, 'disponible': True},
    
    # Accesorios
    {'id': 26, 'nombre': 'Magic Mouse', 'marca': 'Apple', 'categoria': 'Accesorios', 'precio': 79.99, 'stock': 25, 'disponible': True},
    {'id': 27, 'nombre': 'Magic Keyboard', 'marca': 'Apple', 'categoria': 'Accesorios', 'precio': 99.99, 'stock': 18, 'disponible': True},
    {'id': 28, 'nombre': 'Apple Watch Series 9', 'marca': 'Apple', 'categoria': 'Wearables', 'precio': 399.99, 'stock': 14, 'disponible': True},
    {'id': 29, 'nombre': 'Samsung Galaxy Watch 6', 'marca': 'Samsung', 'categoria': 'Wearables', 'precio': 299.99, 'stock': 9, 'disponible': True},
    {'id': 30, 'nombre': 'Mac Studio', 'marca': 'Apple', 'categoria': 'Desktop', 'precio': 1999.99, 'stock': 1, 'disponible': True}
]

# =============================================================================
# DATOS DE EMPLEADOS EXTENDIDOS
# =============================================================================

EMPLEADOS_EXTENDIDOS = [
    # Ventas
    {'id': 101, 'nombre': 'Ana', 'apellido': 'García', 'departamento': 'Ventas', 'salario': 35000, 'activo': True},
    {'id': 102, 'nombre': 'Carlos', 'apellido': 'López', 'departamento': 'Ventas', 'salario': 38000, 'activo': True},
    {'id': 103, 'nombre': 'María', 'apellido': 'Rodríguez', 'departamento': 'Ventas', 'salario': 36000, 'activo': False},
    {'id': 104, 'nombre': 'Laura', 'apellido': 'Fernández', 'departamento': 'Ventas', 'salario': 37000, 'activo': True},
    {'id': 105, 'nombre': 'Pedro', 'apellido': 'González', 'departamento': 'Ventas', 'salario': 34000, 'activo': True},
    {'id': 106, 'nombre': 'Sofia', 'apellido': 'Martínez', 'departamento': 'Ventas', 'salario': 39000, 'activo': True},
    
    # Técnico
    {'id': 201, 'nombre': 'Roberto', 'apellido': 'Sánchez', 'departamento': 'Técnico', 'salario': 45000, 'activo': True},
    {'id': 202, 'nombre': 'Diego', 'apellido': 'Herrera', 'departamento': 'Técnico', 'salario': 42000, 'activo': True},
    {'id': 203, 'nombre': 'Carmen', 'apellido': 'Jiménez', 'departamento': 'Técnico', 'salario': 44000, 'activo': True},
    {'id': 204, 'nombre': 'Miguel', 'apellido': 'Ruiz', 'departamento': 'Técnico', 'salario': 43000, 'activo': False},
    
    # Inventario
    {'id': 301, 'nombre': 'José', 'apellido': 'Pérez', 'departamento': 'Inventario', 'salario': 30000, 'activo': True},
    {'id': 302, 'nombre': 'Elena', 'apellido': 'Gómez', 'departamento': 'Inventario', 'salario': 32000, 'activo': True},
    {'id': 303, 'nombre': 'Antonio', 'apellido': 'Díaz', 'departamento': 'Inventario', 'salario': 31000, 'activo': True},
    {'id': 304, 'nombre': 'Isabel', 'apellido': 'Moreno', 'departamento': 'Inventario', 'salario': 33000, 'activo': True},
    
    # Gerencia
    {'id': 401, 'nombre': 'David', 'apellido': 'Torres', 'departamento': 'Gerencia', 'salario': 65000, 'activo': True},
    {'id': 402, 'nombre': 'Patricia', 'apellido': 'Vargas', 'departamento': 'Gerencia', 'salario': 60000, 'activo': True},
    {'id': 403, 'nombre': 'Francisco', 'apellido': 'Ramos', 'departamento': 'Gerencia', 'salario': 58000, 'activo': False},
    
    # Recursos Humanos
    {'id': 501, 'nombre': 'Andrea', 'apellido': 'Castro', 'departamento': 'Recursos Humanos', 'salario': 40000, 'activo': True},
    {'id': 502, 'nombre': 'Luis', 'apellido': 'Morales', 'departamento': 'Recursos Humanos', 'salario': 41000, 'activo': True},
    
    # Marketing
    {'id': 601, 'nombre': 'Valentina', 'apellido': 'Ortega', 'departamento': 'Marketing', 'salario': 42000, 'activo': True},
    {'id': 602, 'nombre': 'Gabriel', 'apellido': 'Silva', 'departamento': 'Marketing', 'salario': 43000, 'activo': True},
    {'id': 603, 'nombre': 'Camila', 'apellido': 'Mendoza', 'departamento': 'Marketing', 'salario': 41000, 'activo': True}
]

# =============================================================================
# DATOS PARA PRUEBAS DE RENDIMIENTO
# =============================================================================

# Lista de números para pruebas básicas
NUMEROS_PARA_BUSQUEDA = [64, 34, 25, 12, 22, 11, 90, 5, 77, 30, 45, 18, 88, 67, 42]

# Lista de palabras para pruebas de texto
PALABRAS_PARA_BUSQUEDA = [
    'algoritmo', 'búsqueda', 'lineal', 'tienda', 'electrónica',
    'producto', 'empleado', 'disponible', 'stock', 'precio',
    'marca', 'categoría', 'departamento', 'salario', 'activo'
]

# =============================================================================
# FUNCIONES DE UTILIDAD PARA DATOS
# =============================================================================

def obtener_productos_por_precio(precio_maximo):
    """
    Retorna productos con precio menor o igual al especificado.
    
    Args:
        precio_maximo: Precio máximo a considerar
    
    Returns:
        list: Lista de productos que cumplen el criterio
    """
    productos_filtrados = []
    for producto in PRODUCTOS_EXTENDIDOS:
        if producto['precio'] <= precio_maximo:
            productos_filtrados.append(producto)
    return productos_filtrados

def obtener_empleados_por_departamento(departamento):
    """
    Retorna empleados de un departamento específico.
    
    Args:
        departamento: Nombre del departamento
    
    Returns:
        list: Lista de empleados del departamento
    """
    empleados_filtrados = []
    for empleado in EMPLEADOS_EXTENDIDOS:
        if empleado['departamento'].lower() == departamento.lower():
            empleados_filtrados.append(empleado)
    return empleados_filtrados

def generar_lista_numeros(tamaño, inicio=1):
    """
    Genera una lista de números para pruebas de rendimiento.
    
    Args:
        tamaño: Número de elementos en la lista
        inicio: Número inicial (por defecto 1)
    
    Returns:
        list: Lista de números consecutivos
    """
    return list(range(inicio, inicio + tamaño))

def generar_lista_nombres_productos(tamaño):
    """
    Genera una lista de nombres de productos para pruebas.
    
    Args:
        tamaño: Número de nombres a generar
    
    Returns:
        list: Lista de nombres de productos
    """
    nombres_base = [
        'Smartphone', 'Laptop', 'Tablet', 'Audífonos', 'Mouse',
        'Teclado', 'Monitor', 'Impresora', 'Router', 'Cámara'
    ]
    
    nombres_generados = []
    for i in range(tamaño):
        base = nombres_base[i % len(nombres_base)]
        nombres_generados.append(f"{base} {i+1}")
    
    return nombres_generados

# =============================================================================
# FUNCIONES DE ESTADÍSTICAS
# =============================================================================

def obtener_estadisticas_productos():
    """Retorna estadísticas básicas de los productos."""
    total_productos = len(PRODUCTOS_EXTENDIDOS)
    productos_disponibles = len([p for p in PRODUCTOS_EXTENDIDOS if p['disponible']])
    valor_total = sum(p['precio'] * p['stock'] for p in PRODUCTOS_EXTENDIDOS)
    precio_promedio = sum(p['precio'] for p in PRODUCTOS_EXTENDIDOS) / total_productos
    
    categorias = {}
    for producto in PRODUCTOS_EXTENDIDOS:
        categoria = producto['categoria']
        categorias[categoria] = categorias.get(categoria, 0) + 1
    
    return {
        'total_productos': total_productos,
        'productos_disponibles': productos_disponibles,
        'valor_total_inventario': valor_total,
        'precio_promedio': precio_promedio,
        'categorias': categorias
    }

def obtener_estadisticas_empleados():
    """Retorna estadísticas básicas de los empleados."""
    total_empleados = len(EMPLEADOS_EXTENDIDOS)
    empleados_activos = len([e for e in EMPLEADOS_EXTENDIDOS if e['activo']])
    
    salarios = [e['salario'] for e in EMPLEADOS_EXTENDIDOS if e['activo']]
    salario_promedio = sum(salarios) / len(salarios) if salarios else 0
    
    departamentos = {}
    for empleado in EMPLEADOS_EXTENDIDOS:
        dept = empleado['departamento']
        departamentos[dept] = departamentos.get(dept, 0) + 1
    
    return {
        'total_empleados': total_empleados,
        'empleados_activos': empleados_activos,
        'salario_promedio': salario_promedio,
        'salario_minimo': min(salarios) if salarios else 0,
        'salario_maximo': max(salarios) if salarios else 0,
        'departamentos': departamentos
    }

# =============================================================================
# FUNCIÓN DE DEMOSTRACIÓN
# =============================================================================

def demostrar_datos():
    """Demuestra el uso de los datos de ejemplo."""
    print("📊 DATOS DE EJEMPLO - DEMOSTRACIÓN")
    print("=" * 50)
    
    # Estadísticas de productos
    stats_productos = obtener_estadisticas_productos()
    print(f"\n📱 PRODUCTOS:")
    print(f"   Total: {stats_productos['total_productos']}")
    print(f"   Disponibles: {stats_productos['productos_disponibles']}")
    print(f"   Valor inventario: ${stats_productos['valor_total_inventario']:,.2f}")
    print(f"   Precio promedio: ${stats_productos['precio_promedio']:.2f}")
    
    # Estadísticas de empleados
    stats_empleados = obtener_estadisticas_empleados()
    print(f"\n👥 EMPLEADOS:")
    print(f"   Total: {stats_empleados['total_empleados']}")
    print(f"   Activos: {stats_empleados['empleados_activos']}")
    print(f"   Salario promedio: ${stats_empleados['salario_promedio']:,.2f}")
    
    # Ejemplos de búsqueda
    print(f"\n🔍 EJEMPLOS DE BÚSQUEDA:")
    
    # Buscar productos de Apple
    productos_apple = [p for p in PRODUCTOS_EXTENDIDOS if p['marca'] == 'Apple']
    print(f"   Productos de Apple: {len(productos_apple)}")
    
    # Buscar empleados de Ventas
    empleados_ventas = obtener_empleados_por_departamento('Ventas')
    print(f"   Empleados de Ventas: {len(empleados_ventas)}")
    
    # Buscar productos baratos
    productos_baratos = obtener_productos_por_precio(500)
    print(f"   Productos bajo $500: {len(productos_baratos)}")

if __name__ == "__main__":
    demostrar_datos()
