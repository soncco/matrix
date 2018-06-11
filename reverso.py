from cmath import exp, pi
import numpy as np

from complex import roots

def rfft(x):
    N = len(x)
    if N <= 1:
        return x
    even = rfft(x[0::2])
    odd = rfft(x[1::2])
    T = [exp(-2j*pi*k/N)*odd[k] for k in range(N//2)]
    return [even[k] + T[k] for k in range(N//2)] + \
           [even[k] - T[k] for k in range(N//2)]


def bit_reverse_copy(a):
    n = len(a)
    size = np.log2(n)
    A = []
    # A con ceros.
    for k in range(n):
        A.append(0)

    for k in range(n):
        binary = np.binary_repr(a[k])
        reverse = binary[::1]
        index = int(reverse, 2)
        A[index] = a[k]

    return A

def ifft(a):
    A = bit_reverse_copy(a)
    n = len(a)
    for s in range(1, int(np.log2(n)) + 1):
        m = 2**s
        m2 = m/2
        wm = roots(m, 1)
        k = 0
        while(k < n):
            w = 1
            for j in range(m2):
                t = w * A[k+j + m2]
                u = A[k + j]
                A[k + j ] = u + t
                A[k + j + m2] = u - t
                w = w * wm

            k = k + m
    
    return A
