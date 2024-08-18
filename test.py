'''
print("Hello, World!")

print("Concatenación")
mensaje = "hola "
espacio = ""
nombre = "jose"
print(mensaje + espacio + nombre)

num1 = 4
num2 = 6
result1 = num1 + num2
result2 = str(result1)

print("El resultado de la primera suma es " + result2)
print(f"{num1} + {num2} = {result2}")

print("Búsqueda")
mensaje = "hola jose"
buscar_subcadena = mensaje.find("jose")
print(buscar_subcadena)

print("Extracción")
mensaje = "hola jose"
extraer_cadena = mensaje[1:7]
print(extraer_cadena)

# Estructura condicional
num_1 = 5
if num_1 == 5:
    print("El número es cinco")
    print("Fin.")

a = 4
b = 2
if b != 0:
    print(a / b)

print("Sistema para calcular promedio de notas de un estudiante")
name = input("Por favor, digite su nombre: ")
nota_1 = float(input(f"{name}, digite la calificación de la nota 1: "))
nota_2 = float(input(f"{name}, digite la calificación de la nota 2: "))
nota_3 = float(input(f"{name}, digite la calificación de la nota 3: "))
prom = (nota_1 + nota_2 + nota_3) / 3

if prom >= 3:
    print(f"Felicitaciones {name}, aprobaste y tu promedio es {prom}")
else:
    print(f"Lo siento {name}, reprobaste y tu promedio es {round(prom, 3)}")
print("Fin.")

x = 5
if x == 5:
    print("Es 5")
else:
    print("No es 5")

x = 7
if x == 5:
    print("Es 5")
elif x == 6:
    print("Es 6")
elif x == 7:
    print("Es 7")

# Actividad 1
print("===================")
print("***Conversor***")
print("===================")
num_1 = int(input("¿Cuál es el número que desea convertir? "))
if num_1 == 1:
    print("El número es 'uno'")
elif num_1 == 2:
    print("El número es 'dos'")
elif num_1 == 3:
    print("El número es 'tres'")
elif num_1 == 4:
    print("El número es 'cuatro'")
else:
    print("El número digitado no está en la lista")
print("Fin.")

# Convertir una cadena a minúsculas
cadena = "Hola Jose"
print(cadena.lower())
# Convertir una cadena a mayúsculas
print(cadena.upper())
# Convertir una cadena a mayúsculas y minúsculas
print(cadena.swapcase())
# Convertir una cadena a título
print(cadena.title())

# Actividad 3
print("===================")
print("***Conversor***")
print("===================")

print("Menú de opciones: \n")
print("Presiona 1 para convertir de número a palabra")
print("Presiona 2 para convertir de palabra a número")

opcion = int(input("¿Cuál es la opción deseada? "))
if opcion == 1:
    print("\nConversor de número a palabra.\n")
    opcion_uno = int(input("¿Cuál es el número que desea convertir? "))
    if opcion_uno == 1:
        print("El número es 'uno'")
    elif opcion_uno == 2:
        print("El número es 'dos'")
    elif opcion_uno == 3:
        print("El número es 'tres'")
    elif opcion_uno == 4:
        print("El número es 'cuatro'")
    elif opcion_uno == 5:
        print("El número es 'cinco'")
    else:
        print("El número digitado no está registrado")
elif opcion == 2:
    print("\nConversor de palabra a número.\n")
    opcion_dos = input("¿Cuál es la palabra que desea convertir a número? ")
    if opcion_dos == "uno":
        print("El número es '1'")
    elif opcion_dos == "dos":
        print("El número es '2'")
    elif opcion_dos == "tres":
        print("El número es '3'")
    elif opcion_dos == "cuatro":
        print("El número es '4'")
    elif opcion_dos == "cinco":
        print("El número es '5'")
    else:
        print("La palabra digitada no está registrada")
else:
    print("Debes digitar un número entre 1 y 3")
print("Fin.")

# Ejemplo de formato de cadenas
año = 2022
evento = 'semana'
print(f'Lo mejor de las fiestas de {evento} del {año}')

modelo = 'Optimus'
precio = 1900000
impuesto = precio * 19 / 100
print(f'Bicicleta {modelo} con un valor de ${precio + impuesto} pesos')

# Actividad 4
print("Bienvenidos al registro de usuario, digite la opción que desee:")
print("[1] Digitar su nombre")
print("[2] Digitar su edad")
print("[3] Digitar su correo electrónico")

opcion = input("Digite una opción de 1 a 3: ")

if opcion == '1':
    nombre = input('Digite su nombre: ')
    if nombre.isalpha():
        print("Su nombre es", nombre)
    else:
        print("Ha digitado un nombre no válido")
elif opcion == '2':
    edad = input('Digite su edad: ')
    if edad.isnumeric():
        print("Su edad es", edad)
    else:
        print("Ha digitado una edad no válida")
elif opcion == '3':
    email = input('Digite su correo electrónico: ')
    if email.find('@') >= 0 and email.find('.') >= 0:
        print("Su correo electrónico es", email)
    else:
        print("El correo electrónico es incorrecto")
else:
    print("Debes digitar un número entre 1 y 3")
print('****' * 20)

# Ejemplo de lista y tupla
lista = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
print(lista[3])

nums = [1, 2, 3, 4, 5, 6]
tupla = (10, 20, 30, 40, 50)
print(nums[2])
print(tupla[3])

nums[0] = 100
print(nums)
nums.append(6)

mi_lista = [1, 2, "hola", 3, 4]
print(mi_lista)
a = [1, 3, 5, 7, 9]
print(a)

objeto = (7, "hola", True, 3.14)
print(objeto)
mi_tupla = (10, 20, 30)
print(mi_tupla)

mi_conjunto = {1, 2, 3}
print(mi_conjunto)

mi_conjunto.add("hola")
mi_conjunto.discard("hola")
print(mi_conjunto)

# Ejemplo de diccionario
diccionario = {"azul": "blue", "a": "A"}
diccionario["uno"] = 1
print(diccionario["azul"])
diccionario["azul"] = "BLUE"
del diccionario["a"]
print(diccionario)

diccionario = {"Pedro": {"edad": 22, "estatura": 1.65}, "Ana": [25, 1.70], "Maria": [30, 1.75]}
print(diccionario)
print(diccionario["Pedro"]["edad"])

# Ciclo for
nums = [4, 8, 9, 81]
for n in nums:
    print(n)

for i in range(0, 5):
    print(i)
    if i == 2:
        print("OK")

# Ciclo while
x = 1
while x < 10:
    print(x)
    x += 1

x = 9
while x > 0:
    print(x)
    x -= 2

i = 0
while i < 7:
    print("cadena")
    i += 1

x = 0
while x < 100:
    x += 2
    if x > 10:
        break
print("El bucle ha finalizado")

# Ejemplo de función
def di_hola():
    print("Hola")

di_hola()#llamar la funcion
def holaConNombre(nombre):
    print("hola"+nombre)
 
def suma(n1,n2) :
    print(n1+n2)  
    suma(3,4)

def nul_por_5(num):
print(f'{num}*5={num*5}')
print ("inicio")
nul_por_5(1)
nul_por_5(2)
nul_por_5(3)
print('fin')

def saludo(nombre):
    print('hola{}'.format(nombre))
    print("el resultado es:")
    def gracias(gra)
    print('gracias{}'.format(gra))
    print('por su repuesta')
    
    saludo('ana')
    gracias('carlos')

def suma(a,b=4):
    return(a+b)

def resta(a,b):
    return(a-b)
resultS = suma (3)
resultR = resta(a=5,b=3)
print(resultS)
print(resultR)

# realizar programaque capture dos valores los compare y determine cual es el mayor
def nummayor(n1,n2):
    if n1>n2 :
        max=n1
    else:max = n2 
    return max
print('digitar primer numero:')
n1 = int (input('por favor digitar numero 1:'))
print('digitar segundo numero:')
n2 = int (input('por favor digitar numero 2:'))
mayor = nummayor(n1,n2)
print ('el numero mayor es :',mayor)

# clases y objetos
metodo __init__ #inicializar los atributo de un objeto
def _ _,init_ _ (self,parametros):#constructor de la clase
 class Nombre_de_la_clase(objeto):#declarar nuestra clase que viene eredad del objeto
 
 
 #clase auto
 class Auto:
     Marca = 'Mazda'
     Modelo= 2014
     
     taxi = auto()
     print(taxi.Marca)
     print(taxi.Modelo)

class Humano : #creando la clase
    def __init__ (self,edad,nombre,ocupacion):
        self.edad=edad # definimos atributo de edad
        self.nombre=nombre # definimos atributo de nombre
        self.ocupacion=ocupacion # definimos atributo de nombre
persona_1 = Humano(34,'jose','estudiante')
print (persona_1.edad)
print (persona_1.nombre)
print (persona_1.ocupacion)
print('soy' persona_1.nombre,'mi edad es:',persona_1.edad)
'''