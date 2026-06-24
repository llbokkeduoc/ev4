descripcion = ""
prioridad = int
tiempo_estimado = float
estado = bool
tareas = {
    "descripcion": descripcion,
    "prioridad": prioridad,
    "tiempo_estimado": tiempo_estimado,
    "estado": False
}
def menu():
    print("""
    ========== MENÚ PRINCIPAL ==========
    1. Agregar tarea
    2. Buscar tarea
    3. Eliminar tarea
    4. Actualizar estado
    5. Mostrar tareas
    6. Salir
    =====================================
    """)
    
def op_menu():
    while True:
        try:
            op = int(input("Eliga una opcion: "))
            if op < 1 or op > 6:
                print("Ingrese una opcion entre 1-6")
            else:
                return op
        except ValueError:
            print("Ingrese un numero o dato valido.")
def agregar_tarea(tareas):
    while True:
        try:
            descripcion_input = str(input("Ingrese la descripcion de su tarea: "))
            if descripcion_input == "":
                print("Descripcion no puede estar vacia.")
                pass
            else:
                tareas[descripcion] = (descripcion_input)
                break
        except ValueError:
            print("Ingrese un dato valido")
    while True:
        try:
            prioridad_input = int(input("Ingrese la prioridad de su tarea (1-10): "))
            if prioridad_input > 0 and prioridad_input < 11:
                tareas[prioridad] = (prioridad_input)
                break
            else:
                print("La prioridad debe ser mayor a 0 y menor 10.")
                pass
        except ValueError:
            print("Ingrese un dato valido")
    while True:
            try:
                tiempo_input = float(input("Ingrese el tiempo estimado de su tarea: "))
                if tiempo_input > 0:
                    tareas[tiempo_estimado] = (tiempo_input)
                    break
                else:
                    print("El tiempo debe ser mayor a 0 o debe ser un numero flotante.")
                    pass
            except ValueError:
                print("Ingrese un dato valido")

def buscar_tarea(tareas):
    print("")
    for i in tareas:
        print()

def mostrar_tareas(tareas):
    print("Mostrar todas las tareas")
while True:
    menu()
    op = op_menu()
    match op:
        case 1:
            print("Agregar Tarea")
            agregar_tarea(tareas)
        case 2:
            print("")
        case 5:
            mostrar_tareas(tareas)


#trate de hacer lo posible profe 