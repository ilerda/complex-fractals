'''
Program to investigate how complex roots can be found using the Newton Raphson
method and how this results in both chaotic and fractal effects.
'''

from __future__ import division
import numpy


def f(z):
    '''
    Intend to find the roots of this function
    '''
    return z**4 - 1


def f_prime(z):
    '''
    First Derivative required for NR method.
    '''
    return 4 * z**3


def NRmethod(z):
    '''
    Basic implemetation of Newton Raphson
    '''
    MAX_ITER = 30
    z_prev = 0
    a = MAX_ITER
    for i in range(MAX_ITER):
        z = z - f(z) / f_prime(z)
        if abs(z - z_prev) < 0.001:
            a = i
            break
        z_prev = z
    return [numpy.angle(z+0.001j), a] # The found root is shifted a little bit
    # in the positive direction on the imaginary axis. This prevents the function
    # from returning two different values for the angle where it should only
    # return one (+pi and -pi are the same for our purposes).
