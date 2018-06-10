#!/usr/bin/env python
import numpy as np

def tabular(p, n):
    """
      Return an tabular data.

      Parameters
      ----------
      p : array
          Coeficients of a polinomy, example [-1 1] = -1*x + 1.
      n : int
          Lenght of tabulation
      
      Returns
      -------
      yk : array
          Tabulated data

      Examples
      --------
      >>> yk = tabular([-1 1], 4)
        [1 0 -1 -2]
      """
    y = []
    for x in range(n):
        yk = 0
        for k, c in enumerate(p):
            power = len(p)-k-1
            yk = yk + c*(x**power)
        y.append(yk)
        
    return y
