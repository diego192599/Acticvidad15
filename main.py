estudiantes={}
def agregar_Estudiantes():
    print("== Agregar estudiante ==")
    cantidad = int(input("Ingrese la cantidad de estudiantes a agregar: "))
    if cantidad <= 0:
        print("Cantidad inválida.")
        return

    for i in range(cantidad):
        while True:
            try:
                carnet = input(f"Ingrese el carnet del estudiante #{i + 1}: ").strip()
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
            except ValueError:
                print("Entrada inválida.")


def Mostrar():
    print("==Mostrar Informacion==")
    if estudiantes:
        for carnet, nombre in estudiantes.items():
            print(f"Carnet: {carnet} | Nombre: {nombre}")
    else:
        print("No hay estiduiantes")

def buscar():
    print("Buscar estudiante")
    seleccion=int(input("Seleccione una opcion de busqueda (1)Nombre o (2)Carnet: "))
    if seleccion==1:
        print("Buscar por nombre")
        nombre_buscado=input("Ingrese el nombre del estudiante: ").strip()
        encontrado=False
        for carnet,nombre in estudiantes.items():
            if nombre.lower()==nombre_buscado.lower():
                print(f"Encontrado numero de carnet: {carnet} | Nombre: {nombre}")
                encontrado=True
            if not encontrado:
                print("EL nombre no se encuentra ese nombre en la base de datos del sistema")
    elif seleccion==2:
        carnet_buscado=input("Ingrese el carnet del estudiantea buscar: ").strip()
        if carnet_buscado in estudiantes:
            print(f"")
def eliminar():
    print("Eliminar estudiante")
    nombre=input("Ingrese el nombre del estudiante a eliminar(para terminar de eliminar estudiantes presione 0): ")
    if nombre==0:
        print("Opereacion cancelada")
    elif nombre in estudiantes:
