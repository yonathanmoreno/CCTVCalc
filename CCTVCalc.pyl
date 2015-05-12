# -*- coding: utf-8 -*-
#**********************************************************************************************************
#
# 
# Application that calculates the focal distance, horizontal, vertical aperture angles and the 
# needed vertical inclination for a CCTV camera.
# -------------------------------------------------------------------------------------------------
# Author: Yonathan Moreno
# Email: yonathan.morenog@gmail.com
#

# Check if a number has comma and convert it to a dot.

def escomacheck(numero):
    escoma = numero.find(',')
    if escoma != -1:
        numero = numero[:escoma] + '.' + numero[escoma+1:]
    return numero

# Variables.
rad2deg = 180 / 3.1416 # Converting rad to deg.

# Begin.
print " "
print "..............................................................................................."
print " Application that calculates the focal distance, horizontal, vertical aperture angles and the 
print " needed vertical inclination for a CCTV camera."
print "..............................................................................................."
print " "

# Parameters
# .
print " Height from the floor (in meters):"
h = raw_input('')
h = escomacheck (h)
h = int (float(h))
print "Scene Width (in meters): "
H = raw_input ('')
H = escomacheck (H)
H = int (float(H))

print "Distance between the camera and the center of the scene :"
d = raw_input ('')
d = escomacheck (d)
d = int (float(d))

print "CCD size in inches: (1/2, 1/3, 1/4)"
lentepul = raw_input ('')

if lentepul == '1/2':
    lente = 3.6
elif lentepul == '1/3':
    lente = 4.8
elif lentepul == '1/4':
    lente = 6.4
else:
    print 'Error, the size must to be in inches (1/2,1/3,1/4)'

# Calcs of D, rounding it with 2 decimals and converting to String.
from math import sqrt
D= sqrt ( (h*h) + (d*d))
D= round (D,2)
D2= str (D)

# Calcs of f and standarized f, rounding them with 2 decimals and converting to String.
f = lente * (D/H)
f = round (f,2)
fr = int (round (f))
f = str (f)
fr = str (fr)

# Calcs of AV and AH, rounding them with 2 decimals.
from math import atan
AH = atan ((lente/2)/3)
AH = 2 * (AH * rad2deg)
AV = AH * 3/4
AH = round (AH,2)
AH = str (AH)
AV = round (AV,2)
AV2 = str (AV)

# Calcs of X, AF and IV, rounding IV with 2 decimals.
X = sqrt ((h-2)*(h-2)+d*d)
calc = ((h-2)/X)
from math import acos
AF = (acos (calc) * rad2deg)
IV = AF - (AV/2)
IV = round (IV,2)
IV = str (IV)

# Show the results
print " "
print "Results"
print "----------------------------------------------------------------------------------------------"
print 'The distance between the sensor lense to the center of the scene is D=' + D2 + ' m'
print 'The focal distance needed is f=' + fr + '  mm'
print 'The horizontal aperture angle is AH=' + AH + º'
print 'The vertical aperture angle is AV=' + AV2 + ' º'
print 'The needed vertical inclination for the camera is IV=' + IV + ' º'
print "----------------------------------------------------------------------------------------------"
