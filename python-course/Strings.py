myStr = "Hello World"

print("my name is " + myStr) #Imprime "My name is " concatenado con mySrt
print(f"my name is {myStr}") #la f identifica que hay una variable dentro del string y se marca entre llaves
print("my name is {0}".format(myStr)) #Se utiliza el comando format para indicar que el valor de myStr
#se ubicara en la posicion 0 que se marca entre llaves 

print(dir(myStr)) #Imprime todas las funciones para esta variable
print(myStr.upper()) #Escribe todo en mayusculas
print(myStr.lower()) #Escribe todo en minusculas
print(myStr.swapcase()) #Invierte las mayusculas y minusculas
print(myStr.capitalize()) #Escribe solo la primera letra en mayuscula
print(myStr.replace('Hello', 'bye').upper()) #Reemplaza Hello por bye y lo escribe en mayusculas
print(myStr.count('l')) #Cuenta las veces que se encuentra el caracter "l"
print(myStr.startswith('hola')) #Pregunta si myStr comienza con la palabra 'hola' y retorna True o False
print(myStr.startswith('Hello')) #Pregunta si myStr comienza con la palabra 'Hello' y retorna True o False

print(myStr.split(',')) #Separa las palabras por cada ','
print(myStr.split('o')) #Separa las palabras por cada letra 'o'
print(myStr.find(' ')) #busca la posicion de ' '

print(len(myStr)) #Especifica el numero de caracterer de myStr
print(myStr.index('e')) #Especifica el la posicion de la letra 'e'
print(myStr.isnumeric()) #Pregunta si myStr es un valor numerico
print(myStr.isalpha()) #Pregunta si myStr es un valor alfa

print(myStr[4]) #imprime el caracter ubicado en la posicion 4 de myStr
print(myStr[0]) #imprime el caracter ubicado en la posicion 0 de myStr
print(myStr[-1]) #imprime el caracter ubicado en la posicion -1 de myStr (Cuenta de derecha a izquierda)
print(myStr[-5]) #imprime el caracter ubicado en la posicion -5 de myStr (Cuenta de derecha a izquierda)