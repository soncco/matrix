#!/usr/bin/env python

import numpy as np
print(np.version.version)

# x con valores tabulados de 0 a 3
x = np.array([0, 1, 2, 3])
# Matriz de Vandermonde
vandermonde = np.matrix(np.vander(x, increasing=True))
#vandermonde = np.vander()

print (vandermonde)

# Poli 1
# 1-2x
a1 = np.matrix([[1],
              [-2],
              [0],
              [0]])

# Poli 2
# 1-x
a2 = np.matrix([[1],
               [-1],
               [0],
               [0]])

# DFT a1
dfta1 = vandermonde * a1
print(dfta1)

# DFT a2
dfta2 = vandermonde * a2
print(dfta2)

#producto punto
yk = np.multiply(dfta1, dfta2)
print(yk)

a = vandermonde.I*yk
print(a)