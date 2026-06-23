"""
PARTE 1, SIN FUNCIONES, SOLO CON EL BUCLE PRINCIPAL.

Plataforma de Videojuegos
• Contexto: Una tienda digital necesita registrar jugadores y la cantidad de videojuegos
comprados.
ENTREGA 1
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
"""

# --- Inicialización de la lista de socios ---
socios = []

# --- Función para ingresar un socio ---
def ingresar_socio():
    # Validación del nombre
    nombre = input("Ingrese el nombre del socio: ")
    while nombre == "" or nombre.isnumeric():
        print("# ERROR: El nombre no puede estar vacío ni ser puramente numérico.")
        nombre = input("Ingrese su nombre: ")
    
    # Validación de la cantidad de juegos
    cant_juegos = input("Ingrese la cantidad de juegos: ")
    while not cant_juegos.isdigit() or int(cant_juegos) < 1:
        print("# ERROR: Ingrese un número entero positivo.")
        cant_juegos = input("Ingrese cantidad de juegos: ")
    
    # Creación del diccionario y agregado a la lista
    socio = {"nombre": nombre, "cant_juegos": cant_juegos}
    socios.append(socio)

# --- Función para visualizar la lista de socios ---
def ver_socios():
    if not socios:
        print("\n# ERROR. La lista está vacía. Registre un socio primero.")
    else:
        print("\n*** Lista de socios registrada: ***")
        for socio in socios:
            print(f"• {socio['nombre']}")

# --- Función para visualizar la cantidad de juegos por socio ---
def ver_cant_juegos(socios):
    if not socios:
        print("\n# ERROR. La lista está vacía. Registre un socio primero.")
    else:
        print("\n*** Cantidad de juegos por socio: ***")
        for socio in socios:
            print(f"• {socio['nombre']}: {socio['cant_juegos']}")

# --- Función para mostrar el menú y manejar las opciones ---
def menu():
    while True:
        print("*** BIENVENIDO A NEXO-GAMES ***\n")
        print("\n*** Menú: ***")
        print("1. Ingresar socio")
        print("2. Ver lista de socios")
        print("3. Ver cantidad de juegos por socio")
        print("4. Salir")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            ingresar_socio()
        elif opcion == "2":
            ver_socios()
        elif opcion == "3":
            ver_cant_juegos(socios)
        elif opcion == "4":
            print("\nGracias por usar la plataforma. ¡Hasta luego!")
            break
        else:
            print("\n# ERROR. Opción no válida. Intente nuevamente.")

# --- Inicio del programa ---
menu()
