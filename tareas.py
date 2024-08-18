class Tarea:
    def __init__(self, titulo, descripcion, estado="pendiente"):
        self.titulo = titulo
        self.descripcion = descripcion
        self.estado = estado

    def __str__(self):
        return f"Título: {self.titulo}, Descripción: {self.descripcion}, Estado: {self.estado}"

def mostrar_menu():
    print("\nSistema de Gestión de Tareas")
    print("1. Agregar tarea")
    print("2. Mostrar todas las tareas")
    print("3. Buscar tarea por título")
    print("4. Actualizar estado de tarea")
    print("5. Eliminar tarea")
    print("6. Filtrar tareas por estado")
    print("7. Salir")

def agregar_tarea(tareas):
    try:
        titulo = input("Ingresa el título de la tarea: ")
        descripcion = input("Ingresa la descripción de la tarea: ")
        tarea = Tarea(titulo, descripcion)
        tareas.append(tarea)
        print("Tarea agregada exitosamente.")
    except Exception as e:
        print(f"Error: {e}")

def mostrar_tareas(tareas):
    if tareas:
        print("\nLista de Tareas:")
        for t in tareas:
            print(t)
    else:
        print("No hay tareas para mostrar.")

def buscar_tarea(tareas):
    titulo = input("Ingresa el título de la tarea a buscar: ")
    encontrado = False
    for t in tareas:
        if t.titulo.lower() == titulo.lower():
            print(t)
            encontrado = True
            break
    if not encontrado:
        print("Tarea no encontrada.")

def actualizar_estado_tarea(tareas):
    titulo = input("Ingresa el título de la tarea para actualizar su estado: ")
    encontrado = False
    for t in tareas:
        if t.titulo.lower() == titulo.lower():
            t.estado = "completada"
            print("Estado de la tarea actualizado a 'completada'.")
            encontrado = True
            break
    if not encontrado:
        print("Tarea no encontrada.")

def eliminar_tarea(tareas):
    titulo = input("Ingresa el título de la tarea a eliminar: ")
    encontrado = False
    for t in tareas:
        if t.titulo.lower() == titulo.lower():
            tareas.remove(t)
            print("Tarea eliminada correctamente.")
            encontrado = True
            break
    if not encontrado:
        print("Tarea no encontrada.")

def filtrar_tareas_por_estado(tareas):
    estado = input("Ingresa el estado a filtrar (pendiente/completada): ").lower()
    filtradas = [t for t in tareas if t.estado.lower() == estado]
    
    if filtradas:
        print(f"\nTareas con estado '{estado}':")
        for t in filtradas:
            print(t)
    else:
        print(f"No hay tareas con el estado '{estado}'.")

def sistema_gestion_tareas():
    tareas = []
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == "1":
            agregar_tarea(tareas)
        elif opcion == "2":
            mostrar_tareas(tareas)
        elif opcion == "3":
            buscar_tarea(tareas)
        elif opcion == "4":
            actualizar_estado_tarea(tareas)
        elif opcion == "5":
            eliminar_tarea(tareas)
        elif opcion == "6":
            filtrar_tareas_por_estado(tareas)
        elif opcion == "7":
            print("Saliendo del sistema de gestión de tareas.")
            break
        else:
            print("Opción no válida, intenta nuevamente.")

if __name__ == "__main__":
    sistema_gestion_tareas()
