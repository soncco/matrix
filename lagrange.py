#!/usr/bin/env python
import numpy as np

def tabular(p, n):
    y = []
    for x in range(n):
        yk = 0
        for k, c in enumerate(p):
            power = len(p)-k-1
            yk = yk + c*(x**power)
        y.append(yk)
        
    return y
