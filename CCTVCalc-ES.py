# -*- coding: utf-8 -*-
#**********************************************************************************************************
#
# 
# Programa que calcula la distancia focal, ángulo de apertura vertical / horizontal e inclinación 
# necesaria para una cámara CCTV con respecto a la vertical.
# -------------------------------------------------------------------------------------------------
# Autor: Yonathan Moreno
# Email: yonathan.morenog@gmail.com
#

# Función que comprueba si un número tiene decimal con coma, y en caso de tenerlo lo convierte a punto.

def escomacheck(numero):
    escoma = numero.find(',')
    if escoma != -1:
        numero = numero[:escoma] + '.' + numero[escoma+1:]
    return numero

# Defino variables del programa.
rad2deg = 180 / 3.1416 # Variable para pasar de rad a deg.

# Inicio del programa.
print " "
print "..............................................................................................."
print " Programa que calcula la distancia focal, ángulo de apertura vertical / horizontal e inclinación"
print " necesaria para una cámara CCTV con respecto a la vertical."
print "..............................................................................................."
print " "

# Introducir párametros por el usuario, convirtiendo texto a entero con decimales. Si el usuario escribe
# con coma lo convierte a punto.
print " Altura de la cámara desde el suelo (en metros):"
h = raw_input('')
h = escomacheck (h)
h = int (float(h))
print "Ancho de la escena (en metros): "
H = raw_input ('')
H = escomacheck (H)
H = int (float(H))

print "Distancia del eje de la cámara hasta el centro de la escena (en metros):"
d = raw_input ('')
d = escomacheck (d)
d = int (float(d))

print "Tamaño del sensor CCD a emplear en pulgadas: (1/2, 1/3, 1/4)"
lentepul = raw_input ('')

if lentepul == '1/2':
    lente = 3.6
elif lentepul == '1/3':
    lente = 4.8
elif lentepul == '1/4':
    lente = 6.4
else:
    print 'Error, ha de introducir el tipo de sensor en pulgadas (1/2,1/3,1/4)'

# Calculos de D redondeando a dos decimales y convirtiendo posteriormente a texto.
from math import sqrt
D= sqrt ( (h*h) + (d*d))
D= round (D,2)
D2= str (D)

# Calculos de f y f estandarizado redondeando a dos decimales y convirtiendo posteriormente a texto.
f = lente * (D/H)
f = round (f,2)
fr = int (round (f))
f = str (f)
fr = str (fr)

# Calculos de AH y AV redondeando a dos decimales.
from math import atan
AH = atan ((lente/2)/3)
AH = 2 * (AH * rad2deg)
AV = AH * 3/4
AH = round (AH,2)
AH = str (AH)
AV = round (AV,2)
AV2 = str (AV)

# Calculos de x, AF e IV, redondeando IV a dos decimales.
X = sqrt ((h-2)*(h-2)+d*d)
calc = ((h-2)/X)
from math import acos
AF = (acos (calc) * rad2deg)
IV = AF - (AV/2)
IV = round (IV,2)
IV = str (IV)

# Muestro los resultados
print " "
print "Resultados"
print "----------------------------------------------------------------------------------------------"
print 'La distancia desde el centro óptico de la lente hasta el centro de la escena es D=' + D2 + ' m'
print 'La distancia focal necesaria de lente es f=' + fr + '  mm'
print 'El ángulo de apertura horizontal de la lente es AH=' + AH + º'
print 'El ángulo de apertura vertical de la lente es AV=' + AV2 + ' º'
print 'El ángulo de inclinación necesario de la cámara con respecto a la vertical es IV=' + IV + ' º'
print "----------------------------------------------------------------------------------------------"
