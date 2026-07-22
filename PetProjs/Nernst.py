"""
Glen Ernstrom
2026-07-21

Computes an ion's equilibrium potential
with user-provided system temp in Celsius,
ion valence, and out and inside ion
concentrations in millimolar units.
"""

import math

import scipy

R = scipy.constants.R
faraday = scipy.constants.physical_constants['Faraday constant']
FARADAY = faraday[0]
ZERO_CELSIUS_IN_KELVIN =scipy.constants.zero_Celsius

def Nernst_constant(deg_C, z_):
    '''Computes the Nernst constant with given temperature and ion valence'''
    T = deg_C + ZERO_CELSIUS_IN_KELVIN
    return (R * T) / (FARADAY * z_)

def E(constant, outside, inside):
    '''Computes the equilibrium potential in mV '''
    return constant * (math.log(outside / inside)) * 1000

if __name__ == '__main__':
    celsius = float(input("What is the temperature of the system in"
                          " \N{DEGREE SIGN}C ? "))
    valence = int(input("What is the valence of the ion? "))

    print("")
    outside_c = float(input("What is the outside concentration? "))
    inside_c = float(input("What is the inside concentration? "))
    print("")

    N_k = Nernst_constant(celsius, valence)
    E_i = E( N_k, outside_c, inside_c )

    print(f"The equilibrium potential is {E_i:.1f} mV")