#!/usr/bin/env python

import numpy as np

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
          matrix[row, col] = 1j**(col*row)

  return matrix
