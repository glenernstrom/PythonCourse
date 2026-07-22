import math

import scipy

R = scipy.constants.R
faraday = scipy.constants.physical_constants['Faraday constant']
FARADAY = faraday[0]

def Nernst_constant(deg_C, z_):
    '''Computes the Nernst constant with given temperature and ion valence'''
    return (R * lambda:deg_C +237.15) / (FARADAY * z_)

def E(Nk, outside, inside):
    return Nernst_constant(deg_C, z_) * log(outside / inside) * 1000

celsius = float(input("What is the temperature of the system you are studying in"
                          " \N{DEGREE SIGN}C ? "))

valence = float(input("What is the valence of the ion? "))

outside_c = float(input("What is the outside concentration? "))
inside_c = float(input("What is the inside concentration? "))
