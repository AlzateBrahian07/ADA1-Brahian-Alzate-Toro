import sqlite3

def cargar_personas_db(nombre_db):
    personas = []
    conn = sqlite3.connect(nombre_db)
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre, direccion, telefono, email, fecha_nacimiento FROM personas")
    for fila in cursor.fetchall():
        personas.append({
            "id": str(fila[0]),  # Convertimos a str para facilitar la comparación
            "nombre": fila[1],
            "direccion": fila[2],
            "telefono": fila[3],
            "email": fila[4],
            "fecha_nacimiento": fila[5]
        })
    conn.close()
    return personas

def buscar_recursivo(personas, inicio, fin, condicion):
    n = fin - inicio
    if n == 0:
        return []
    if n == 1:
        return [personas[inicio]] if condicion(personas[inicio]) else []
    mid = inicio + n // 2
    izquierda = buscar_recursivo(personas, inicio, mid, condicion)
    derecha = buscar_recursivo(personas, mid, fin, condicion)
    return izquierda + derecha

if __name__ == "__main__":
    personas = cargar_personas_db("personas.db")
    atributos = ["id", "nombre", "direccion", "telefono", "email", "fecha_nacimiento"]
    print("Atributos disponibles para filtrar:", ", ".join(atributos))
    atributo = input("¿Por qué atributo quieres filtrar?: ").strip()
    valor = input("¿Qué valor debe tener (o empezar con)?: ").strip()
    if atributo not in atributos:
        print("Atributo no válido.")
    else:
        condicion = lambda p: p[atributo].startswith(valor)
        resultados = buscar_recursivo(personas, 0, len(personas), condicion)
        print("Resultados encontrados:", len(resultados))
        for r in resultados[:10]:  # Muestra solo los 10 primeros
            print(r)