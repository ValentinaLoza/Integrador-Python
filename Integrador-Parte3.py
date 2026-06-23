"""
GRUPO III

INTEGRANTES:
• Arispe Gabriel
• Cardozo Camila
• López Cristian
• Loza Valentina
• Zárate Elías
"""

"""
Plataforma de Videojuegos
• Contexto: Una tienda digital necesita registrar socio y la cantidad de videojuegos
comprados.

PARTE 1, SIN FUNCIONES, SOLO CON EL BUCLE PRINCIPAL.

Desarrollar un programa en consola que:
• Permita ingresar un socio (nombre + cantidad de videojuegos).
• Permita visualizar la lista completa de socios.
• Utilice una lista para almacenar los datos.
• Implemente un menú que se repita hasta que el usuario elija salir.
• Controle errores de ingreso de datos (cantidad debe ser numérica y positiva).


PARTE 2, CON FUNCIONES Y DICCIONARIOS.

Modificar el programa para que:
• La estructura de almacenamiento sea un diccionario.
• Clave: nombre del socio.
• Valor: cantidad de clases/libros/videojuegos/donaciones.
• Agregar una nueva opción:
• Consultar la cantidad de clases/libros/videojuegos/donaciones. de un socio.
• Validar que el socio exista antes de mostrar la información.
• Evitar que el programa finalice por errores.

PARTE 3, FUNCIONES Y CONTROL DE ERRORES.

Refactorizar el programa utilizando funciones:
• validar_nombre()
• validar_cantidad()
• agregar_socio() p2
• mostrar_socios()
• buscar_socio()
• El código debe estar organizado y evitar repetición innecesaria.
    *Plataforma de Videojuegos
    Agregar:
• Mostrar el socio con más compras.
• Mostrar el total de juegos vendidos.
• Permitir buscar socio
• Eliminar socio

"""

socios = []

# --- Funciones para validar--- 
def validar_nombre():
    nombre = input("Ingrese el nombre del socio: ")
    while nombre == "" or nombre.isdecimal():
        print("# Error: El nombre no puede estar vacío ni ser puramente numérico.")
        nombre = input("Ingrese un nombre válido: ")
    return nombre

def validar_cantidad():
    cant_juegos = input("Ingrese la cantidad de juegos comprados: ")
    while not cant_juegos.isdecimal() or int(cant_juegos) < 1:
        print("# Error: Ingrese un número entero positivo.")
        cant_juegos = input("Ingrese una cantidad válida: ")
    return int(cant_juegos)

# --- Función para ingresar un socio ---
def agregar_socio():
    nombre = validar_nombre()
    cant_juegos = validar_cantidad()
    
    socio = {"nombre": nombre, "cant_juegos": cant_juegos}
    socios.append(socio)
    print(f"\n¡socio '{nombre}' agregado con éxito!")

# --- Función para visualizar socios ---
def mostrar_socios():
    if validar_lista_vacia():
        return
    
    print("\n*** Lista de socios y cantidad de juegos: ***")
    for socio in socios:
        print(f"• {socio['nombre']}: {socio['cant_juegos']} juegos")

# --- Función para buscar con socios ---
def buscar_socio():
    if validar_lista_vacia():
        return

    nombre_buscar = input("\nIngrese el nombre del socio a buscar: ")
    encontrado = False
    
    for socio in socios:
        if socio['nombre'].lower() == nombre_buscar.lower():
            print(f"\n*** socio encontrado ***\n• Nombre: {socio['nombre']} | Juegos comprados: {socio['cant_juegos']}")
            encontrado = True
            break
            
    if not encontrado:
        print("\n# Error: El socio no fue encontrado en el sistema.")

# --- Función para eliminar socios ---
def eliminar_socio():
    if validar_lista_vacia():
        return
    
    mostrar_socios()  # Mostrar socios antes de eliminar para facilitar la selección

    nombre_eliminar = input("\nIngrese el nombre del socio a eliminar: ")
    encontrado = False
    
    for i in range(len(socios)):
        if socios[i]['nombre'].lower() == nombre_eliminar.lower():
            nombre_borrado = socios[i]['nombre']
            del socios[i]  # Instrucción de borrado vista en clase
            #socios.pop(i) Otra forma de eliminar un elemento de la lista por índice
            print(f"\n¡El socio '{nombre_borrado}' ha sido eliminado con éxito!")
            encontrado = True
            break

    if not encontrado:
        print("\n# Error: El socio no fue encontrado.")

# --- Función para visualizar al socio mas compras ---
def socio_mas_compras():
    if validar_lista_vacia():
        return

    mayor_cantidad = 0
    socio_mayor = ""

    for socio in socios:
        if socio['cant_juegos'] > mayor_cantidad:
            mayor_cantidad = socio['cant_juegos']
            socio_mayor = socio['nombre']

    print(f"\n*** El socio con más compras es '{socio_mayor}' con {mayor_cantidad} juegos. ***)")

# --- Función para visualizar el total de juegos vendidos ---
def total_juegos_vendidos():
    if validar_lista_vacia():
        return

    total = sum(socio['cant_juegos'] for socio in socios)
    print(f"\n*** Total de juegos vendidos: {total} ***")
        

# --- Función para mostrar el menú y manejar las opciones ---
def validar_lista_vacia():
    if len(socios) == 0:
        print("\n# La lista está vacía. Registre un socio primero.")
        return True
    return False



def menu():
    while True:
        print("\n" + "="*45)
        print(" *** Menú: Plataforma de Videojuegos ***")
        print("="*45)
        print("1. Agregar socio")
        print("2. Mostrar todos los socios")
        print("3. Buscar un socio")
        print("4. Eliminar un socio")
        print("5. Mostrar el socio con más compras")
        print("6. Mostrar el total de juegos vendidos")
        print("7. Salir")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            agregar_socio()
        elif opcion == "2":
            mostrar_socios()
        elif opcion == "3":
            buscar_socio()
        elif opcion == "4":
            eliminar_socio()
        elif opcion == "5":
            socio_mas_compras()
        elif opcion == "6":
            total_juegos_vendidos()
        elif opcion == "7":
            print("\nGracias por usar la plataforma. ¡Hasta luego!")
            break
        else:
            print("\n# Opción no válida. Intente nuevamente.")

# --- Inicio del programa ---
menu()

