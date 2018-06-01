#!/usr/bin/env python

import numpy as np
from numpy.polynomial import Polynomial as P
p = P([6, 7, -10, 9])
p2 = P([-2, 0, 4, -5])
print(np.poly1d(p*p2, fmt='%-7.2f'))
#-12, -14, 44, -20, -75, 86, -45


p = P([1, -1])
print(p**2)
#1, -2, 1