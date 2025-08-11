estudiantes={}
def agregar_Estudiantes():
    print("== Agregar estudiante ==")
    while True:
        cantidad = input("Ingrese la cantidad de estudiantes a agregar (0 para cancelar): ").strip()
        if cantidad == "0":
            print("Cancelando registro de estudiantes...")
            return
        if not cantidad.isdigit() or int(cantidad) <= 0:
            print("Cantidad inválida.")
            continue
        cantidad = int(cantidad)

        for i in range(cantidad):
            while True:
                carnet = input(f"Ingrese el carnet del estudiante #{i + 1} (0 para cancelar): ").strip()
                if carnet == "0":
                    print("Cancelando ingreso de este estudiante...")
                    break
                if not carnet:
                    print("El carnet no puede quedar vacío.")
                    continue
                if carnet in estudiantes:
                    print("Este carnet ya está registrado.")
                    continue

                nombre = input("Ingrese el nombre del estudiante: ").strip()
                if not nombre:
                    print("El nombre no puede quedar vacío.")
                    continue

                estudiantes[carnet] = nombre
                print(f"Estudiante {nombre} registrado con carnet {carnet}.")
                break
        break
def Mostrar():
    print("==Mostrar Informacion==")
    if estudiantes:
        for carnet, nombre in estudiantes.items():
            print(f"Carnet: {carnet} | Nombre: {nombre}")
    else:
        print("No hay estiduiantes")

def buscar():
    while True:
        print("\n== Buscar estudiante ==")
        seleccion = input("Seleccione (1)Nombre, (2)Carnet o (0)Salir: ").strip()
        if seleccion == "0":
            print("Saliendo de búsqueda...")
            break

        if seleccion == "1":
            nombre_buscado = input("Ingrese el nombre: ").strip()
            encontrado = False
            for carnet, nombre in estudiantes.items():
                if nombre.lower() == nombre_buscado.lower():
                    print(f"Encontrado → Carnet: {carnet} | Nombre: {nombre}")
                    encontrado = True
            if not encontrado:
                print("No se encontró ningún estudiante con ese nombre.")

        elif seleccion == "2":
            carnet_buscado = input("Ingrese el carnet: ").strip()
            if carnet_buscado in estudiantes:
                print(f"Encontrado → Carnet: {carnet_buscado} | Nombre: {estudiantes[carnet_buscado]}")
            else:
                print("No se encontró ningún estudiante con ese carnet.")
        else:
            print("Opción inválida.")

def eliminar():
    while True:
        print("\n== Eliminar estudiante ==")
        carnet = input("Ingrese el carnet a eliminar (0 para cancelar): ").strip()
        if carnet == "0":
            print("Cancelando eliminación...")
            break
        if carnet in estudiantes:
            eliminado = estudiantes.pop(carnet)
            print(f"Estudiante {eliminado} eliminado correctamente.")
        else:
            print("Ese carnet no existe.")


while True:
    print("\n===== MENÚ PRINCIPAL =====")
    print("1. Agregar estudiante")
    print("2. Mostrar estudiantes")
    print("3. Buscar estudiante")
    print("4. Eliminar estudiante")
    print("0. Salir")

    opcion = input("Seleccione una opción: ").strip()

    match opcion:
        case "1":
            agregar_Estudiantes()
        case "2":
            Mostrar()
        case "3":
            buscar()
        case "4":
            eliminar()
        case "0":
            print("Saliendo del programa...")
            break
        case _:
            print("Opción inválida.")