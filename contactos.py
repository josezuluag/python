class Contacto:
    def __init__(self, nombre, telefono):  # Se inicializa la clase y se declaran los atributos
        self.nombre = nombre
        self.telefono = telefono

def mostrar_menu():
    print("Gestión de Contactos")
    print("1. Agregar contacto")
    print("2. Mostrar contactos")
    print("3. Buscar contacto")
    print("4. Eliminar contacto")
    print("5. Salir")

contactos = []

while True:
    mostrar_menu()
    opcion = input("Elige una opción: ")

    if opcion == "5":
        print("Saliendo del programa")
        break
    elif opcion == "1":
        nombre = input("Ingresa el nombre: ")
        telefono = input("Ingresa el teléfono: ")
        contacto = Contacto(nombre, telefono)
        contactos.append(contacto)
        print("Contacto agregado")
    elif opcion == "2":
        if contactos:
            for c in contactos:
                print(f'Nombre: {c.nombre}, Teléfono: {c.telefono}')
        else:
            print("No hay contactos para mostrar")
    elif opcion == "3":
        nombre = input("Ingresa el nombre a buscar: ")
        encontrado = False
        for c in contactos:
            if c.nombre == nombre:
                print(f'Nombre: {c.nombre}, Teléfono: {c.telefono}')
                encontrado = True
                break
        if not encontrado:
            print("Contacto no encontrado")
    elif opcion == "4":
        nombre = input("Ingresa el nombre a eliminar: ")
        encontrado = False
        for c in contactos:
            if c.nombre == nombre:
                contactos.remove(c)
                print("Contacto eliminado")
                encontrado = True
                break
        if not encontrado:
            print("Contacto no encontrado")
    else:
        print("Opción no válida, intenta nuevamente")
