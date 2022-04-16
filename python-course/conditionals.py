color = "red"

if color == "red": #si el color es igual a "red"
    print("the color is red")

elif color == "blue": #alternativa
    print("the color is blue")

else: #en el caso contrario
    print("Acceso denegado")

name = "John"
lastname = "Carter"

if name == "John":
    if lastname == "Carter": #se puede colocar un if debajo de otro
        print("You are John Carter")
    else:
        print("You are not John Carter") #invalida el ultimo conditional
else:
    print("You are not John") #invalida el primer conditional

x = 5
y = 7
if x > 2 and x <= 10:
    print("x is greater than two and less than or equal to ten")

if x > 2 or x <= 20:
    print("x is greater than two or less or equal to twenty")
if (not(x == y)):
    print("x is not equal than y")

#lee dos números
numero1 = int (input("Ingresa el primer número:"))
numero2 = int (input("Ingresa el segundo número:"))

#elegir el número más grande
if numero1> numero2:
    nmasGrande = numero1
else:
    nmasGrande = numero2

#imprimir el resultado
print("El número más grande es:", nmasGrande)

#OTRO METODO:

#lee dos números
numero1 = int (input("Ingresa el primer número:"))
numero2 = int (input("Ingresa el segundo número:"))

# elegir el número más grande
if numero1 > numero2: nmasGrande = numero1
else: nmasGrande = numero2

#imprimir el resultado
print("El número más grande es: ", nmasGrande)

#MISMO CODIGO CON 3 VARIABLES:

#lee tres números
numero1 = int (input("Ingresa el primer número:"))
numero2 = int (input("Ingresa el segundo número:"))
numero3 = int (input("Ingresa el tercer número:"))

#asumimos temporalmente que el primer número
#es el más grande
#lo verificaremos pronto
nmasGrande = numero1

#comprobamos si el segundo número es más grande que el mayor número actual
#y actualiza el número más grande si es necesario
if numero2 > nmasGrande:
    nmasGrande = numero2

#comprobamos si el tercer número es más grande que el mayor número actual
#y actualiza el número más grande si es necesario
if numero3 > nmasGrande:
    nmasGrande = numero3

#imprimir el resultado
print("El número más grande es:", nmasGrande)

max() #Encuentra el mayor de los numeros
min() #Encuentra el menor de los numeros

# lee tres números
numero1 = int(input("Ingresa el primer número:"))
numero2 = int(input("Ingresa el segundo número:"))
numero3 = int(input("Ingresa el tercer número:"))

# verifica cuál de los números es el mayor
# y pásalo a la variable de mayor número

numeroMayor = max(numero1,numero2,numero3)

# imprimir el resultado
print("El número más grande es:", numeroMayor) 

#EJEMPLO USANDO ESPATIFILO:
entrada = input("Planta: ")
if entrada == "Espatifilo":
    print("Si, ¡El Espatifilo es la mejor planta de todos los tiempos!")
elif entrada == "espatifilo":
    print("No, ¡quiero un gran Espatifilo!")
else:
    print(f"¡Espatifilo! ¡No {entrada}!")