demo_list = [1, 'hello', 1.34, True, [1, 2, 3]]
colors = ['red', 'green', 'blue', 'red']

numbers_list = list((1, 2, 3, 4))
print(numbers_list)
print(type(numbers_list))
r = list(range(1, 10))
print(r)
print(len(demo_list)) #pintar longitud de demo_list
print(colors[-2]) #escribir el indice -2 de la lista colors
print('green' in colors) #pintar si green esta en colors

print(colors)
colors[1] = 'yellow' #reemplazar el indice 1 por yellow
print(colors)

print(dir(colors)) #escribir funciones de lista

colors.append('violet') #agregar elemento
colors.extend(['violet', 'yellow']) #extender lista basado en tupla
colors.extend(['pink', 'black'])

colors.insert(-1, 'violet') #insertar elemento en posicion basado en indice
colors.insert(len(colors), 'violet') #insertar elemento basado en longitud de lista
print(colors)

colors.pop() #eliminar ultimo elemento

colors.remove('green') #eliminar elemento
colors.pop(1) #eliminar basado en indice
colors.clear() #limpiar lista

colors.sort() #ordenar alfabeticamente
colors.sort(reverse=True) #ordenar de manera inversa
print(colors)

print(colors.index('red')) #pintar el indice de elemento
print(colors.count('red')) #contar el numero de elementos 'red'
