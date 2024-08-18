'''
num1= 20
num2= 0
print("la division de {0}entre{1}es:".format(num1,num2(num1/num2)))
resultado =num1/num2
except:
   print ("errror de la ejecucion del programa")
   print ("hasta aqui va el programa")
'''

class Producto:
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"

def mostrar_menu():
    print("\nSistema de Inventario Tienda")
    print("1. Agregar producto")
    print("2. Mostrar todos los productos")
    print("3. Buscar producto por nombre")
    print("4. Actualizar cantidad de producto")
    print("5. Eliminar producto")
    print("6. Salir")

def agregar_producto(productos):
    try:
        nombre = input("Ingresa el nombre del producto: ")
        cantidad = int(input("Ingresa la cantidad del producto: "))
        precio = float(input("Ingresa el precio del producto: "))
        producto = Producto(nombre, cantidad, precio)
        productos.append(producto)
        print("Producto agregado exitosamente.")
    except ValueError:
        print("Error: La cantidad y el precio deben ser numéricos.")

def mostrar_productos(productos):
    if productos:
        print("\nProductos en Inventario:")
        for p in productos:
            print(p)
    else:
        print("No hay productos en el inventario.")

def buscar_producto(productos):
    nombre = input("Ingresa el nombre del producto a buscar: ")
    encontrado = False
    for p in productos:
        if p.nombre.lower() == nombre.lower():#agrego esta regla para mejorar la busqueda
            print(p)
            encontrado = True
            break
    if not encontrado:
        print("Producto no encontrado.")

def actualizar_cantidad(productos):
    nombre = input("Ingresa el nombre del producto para actualizar la cantidad: ")
    encontrado = False
    for p in productos:
        if p.nombre.lower() == nombre.lower():
            try:
                nueva_cantidad = int(input("Ingresa la nueva cantidad: "))
                p.cantidad = nueva_cantidad
                print("Cantidad actualizada correctamente.")
                encontrado = True
            except ValueError:
                print("Error: La cantidad debe ser un número entero.")
            break
    if not encontrado:
        print("Producto no encontrado.")

def eliminar_producto(productos):
    nombre = input("Ingresa el nombre del producto a eliminar: ")
    encontrado = False
    for p in productos:
        if p.nombre.lower() == nombre.lower():
            productos.remove(p)
            print("Producto eliminado correctamente.")
            encontrado = True
            break
    if not encontrado:
        print("Producto no encontrado.")

def sistema_inventario():
    productos = []
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == "1":
            agregar_producto(productos)
        elif opcion == "2":
            mostrar_productos(productos)
        elif opcion == "3":
            buscar_producto(productos)
        elif opcion == "4":
            actualizar_cantidad(productos)
        elif opcion == "5":
            eliminar_producto(productos)
        elif opcion == "6":
            print("Saliendo del sistema de inventario.")
            break
        else:
            print("Opción no válida, intenta nuevamente.")

if __name__ == "__main__":
    sistema_inventario()
