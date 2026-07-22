# A program to convert the Nernst equation in natural log form to
# log10 form given user-provided system temperature in Celsius.

# The Nernst equation is an important neurophysiology concept defining
# electrochemical equilibrium potentials for a given permeant ion.

# E = (R * T / z * F) * log(x), where R = molar gas constant, T = temperature in Kelvin,
# z = ion valence, F = Faraday's consant, and x is the cocentration gradient (more precisely
# the ion activity ratio) of the ions outside to inside the cell. E is the equilibrium
# potential in volts. log(x) is the natural log.

# This is the most general form of the Nernst equation. Many textbooks
# simplify the above equation to 58 * log10(x) where the T is 20 degrees Celsisus. And
# this form of the Nernst equation returns the equilibrium potential in millivolts.


# Glen Ernstrom
# 2026-07-15

import math

import scipy

R = scipy.constants.R
faraday = scipy.constants.physical_constants['Faraday constant']
FARADAY = faraday[0]


def kelvin_converter(degrees_celsius):
    '''Takes an integer as degrees ceslius and returns temp in Kelvin'''
    return (degrees_celsius) + 273.15


def gas_constant_times_kelvin(degrees_celsius):
    return R * (kelvin_converter(degrees_celsius))


def RT_divided_by_Faradays_constant(degrees_celsius):
    return  (gas_constant_times_kelvin(degrees_celsius)) / FARADAY


if __name__ == '__main__':
    
    celsius = float(input("What is the temperature of the system you are studying in"
                          " \N{DEGREE SIGN}C ? "))
    
    
    kelvin = kelvin_converter(celsius)
    gas_temp_prod = gas_constant_times_kelvin(celsius)
    rt_f = RT_divided_by_Faradays_constant(celsius)
    
    rt_f_converted = rt_f * (1 / math.log10(math.e)) * 1000
    
    Ek = rt_f_converted * math.log10((3 / 135))
    ENa = rt_f_converted * math.log10((145 / 12.5))
    
    print(f"The temperature is equivalent to {kelvin:.2f} K.")
    print(f"The gas constant is 8.3145 Joules per mol \u22c5 Kelvin.")
    print(f"The gas constant times temperature in Kelvin is {gas_temp_prod:.3f}")
    print(f"Faraday's constant is 96485 Coulombs per mole.")
    print(f"RT/F = {rt_f}.")
    print(f"Switching bases from e to base 10 and multiplying by 1000 we have {rt_f_converted:.0f}.")
    print(f"If [K+] outside is 3 mM and [K+] inside 135 mM, then 58 * log10(3 / 135) = {Ek:.0f} mV.")
    print(f"If [Na+] outside is 145 mM and [Na+] inside 12.5 mM, then 58 * log10(145 / 12.5) = {ENa:.0f} mV")


