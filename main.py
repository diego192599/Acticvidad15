estudiantes={}
def agregar_Estudiantes():
    print("==Agregar estudiante==")
    cantidad=int(input("Ingrese la cantidad de estudiantes a agregar: "))
    while True:
        try:
            if cantidad == 0:
                print("La cantidad ingresada no es valida vuelva a intentar")
                break
            elif cantidad<0:
                print("La cantidad no puede ser menor a 0")
            else:
                for i in range(cantidad):
                    nombre=input(f"Ingrese el nombre del estudiante #{i+1}")
                    if nombre:
                        estudiantes[nombre]={}
                        print(f"El {nombre} se ha guardado correctamente")
                    else:
                        print("El nombre no puede quedar vacio intente nuevamente")
                break
        except ValueError
