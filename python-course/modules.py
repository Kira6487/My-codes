# mis propios modulos
# modulos de internet
# modulos de python

import datetime #importa el modulo datetime de la bibloteca de python
print(datetime.date.today()) #imprime la funcion date.today del modulo datetime
print(datetime.timedelta(minutes=70))

from datetime import timedelta #desde el modulo datetime, importa la funcion timedelta
print(timedelta(minutes=100))

import fmath #importa el modulo fmath desde mi biblioteca

fmath.add(1, 2) #ejecuta la funcion add del modulo fmath
fmath.substract(1, 2) #ejecuta la funcion substract del modulo fmath