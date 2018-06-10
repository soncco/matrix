#!/usr/bin/env python

import numpy as np
from numpy.linalg import inv, det

def roots(n, k):
    """
      Return a root.

      Parameters
      ----------
      n : int
          The length of w.
      k : int
          Iteration item
      
      Returns
      -------
      c : complex
          A complex root

      Examples
      --------
      >>> c = roots(4, 1)
        1j
      """
    root = 2 * np.pi * k/n
    w = np.cos(root) + 1j * np.sin(root)
    c = np.round(w)
    return c

def complex_matrix(n):
    """
      Return an vandermonde array of complex.

      Parameters
      ----------
      n : int
          The length of the array.
      
      Returns
      -------
      matrix : matrix
          A complex matrix

      Examples
      --------
      >>> matrix = complex_matrix(4)
        [[ 1.+0.j  1.+0.j  1.+0.j  1.+0.j]
        [ 1.+0.j  0.+1.j -1.+0.j -0.-1.j]
        [ 1.+0.j -1.+0.j  1.+0.j -1.+0.j]
        [ 1.+0.j -0.-1.j -1.+0.j  0.+1.j]]
      """

    matrix = np.zeros(shape=(n, n), dtype=complex)

    for row in np.arange(n):
        if row == 0:
            for col in np.arange(n):
                matrix[row, col] = 1
        else:
            for col in np.arange(n):
                if col == 0:
                    matrix[row, col] = 1
                else:
                    matrix[row, col] = roots(n, col*row)

    return matrix

