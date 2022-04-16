foods = ["apples", "bread", "cheese", "milk", 
"bananas", "graves"]

for foods in foods: #recorre cada elemento de la lista foods
    if foods == "cheese":
        break #detiene el bucle
        continue #continua con el bucle ignorando cheese
    print(foods)

for number in range(1, 8): #en un rango del 1 al 8
    print(number)

for word in "Hello": #recorre todos los caracteres de "Hello" 
    #(Los bucles tambien se aplican en palabras [strings])
    print(word)

count = 4

while count <= 10: #mientras count sea menor o igual a 10 se va a ejecutar
   # print(count) #mientras count se mantenga en 4 se ejecutara infinitamente
    count = count + 1 #se repite el valor sumado mas 1
