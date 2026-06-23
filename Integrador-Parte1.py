socios = []

def ingresar_socio():
    
    nombre = input("Ingrese el nombre del socio: ")
#Todo chekiado  
    while nombre == "" or nombre.isnumeric():
            print("# Error: El nombre no puede estar vacío ni ser puramente numérico.")
            nombre = input("Ingrese su nombre: ")
    
    cant_juegos = input("Ingrese la cantidad de juegos: ")
    
    while not cant_juegos.isdigit() or int(cant_juegos) < 1:
            print("# Error: Ingrese un número entero positivo.")
            cant_juegos = input("Ingrese cantidad de juegos: ")
    
    socio = {"nombre": nombre, "cant_juegos": cant_juegos}
    socios.append(socio)

def ver_socios():
    if not socios:
        print("# La lista está vacía. Registre un socio primero.")
        
    print("\n*** Lista de socios registrada: ***")
    for socio in socios:
        print(f"• {socio['nombre']}")

def ver_cant_juegos(socios):
    print("\n*** Cantidad de juegos por socio: ***")
    if not socios:
        print("# La lista está vacía. Registre un socio primero.")
    for socio in socios:
        print(f"• {socio['nombre']}: {socio['cant_juegos']}")

def menu():
    while True:
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
            print("Gracias por usar la plataforma. ¡Hasta luego!")
            break
        else:
            print("# Opción no válida. Intente nuevamente.")
            
menu()
