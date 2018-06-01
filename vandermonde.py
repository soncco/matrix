#!/usr/bin/env python3

import numpy as np
print(np.version.version)

# x con valores tabulados de 0 a 3
x = np.array([0, 1, 2, 3])

# Matriz de Vandermonde
vandermonde = np.vander(x)
vandermonde = np.vander()

print (vandermonde)

# Poli 1
# 1-2x
a1 = np.array([[1],
              [-2],
              [0],
              [0]])

# Poli 2
# 1-x
a2 = np.array([[1],
               [-1],
               [0],
               [0]])

# DFT a1
dfta1 = vandermonde * a1
print(dfta1)

# DFT a2
dfta2 = vandermonde * a2
print(dfta2)

