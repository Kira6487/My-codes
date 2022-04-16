def hello(name= "Person"): #define una funcion
    #la funcion recive un valor llamado name
    #el valor por defecto de name es Person
    print("Hello " + name) 
    #imprime "Hello" concatenado con el valor name

hello("joe") #ejecuta la funcion hello con el valor joe
hello("ryan")
hello("Fazt")

def add(num1, num2):
    return num1 + num2 #regresa el valor de n1 mas n2

print(add(10, 30))
print(add (600, 10))

add = lambda n1, n2: n1 + n2 #otro metodo

print(add(10, 40))