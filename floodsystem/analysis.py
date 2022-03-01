from symtable import Symbol
import matplotlib
import numpy as np
from sympy import Symbol, Derivative
"""
def polyfit(dates, levels, p):
    x = np.array(matplotlib.dates.date2num(dates))
    p_coeff = np.polyfit(x-x[0], levels, p)
    poly = np.poly1d(p_coeff)
    return (poly, x[0])

def poly_deriv(poly):
    deriv = np.polyder(poly, m=1)
    return deriv
"""

def polyfit(dates, levels, p):
    """Produces a polynomial to match the data, returning a tuple of the polynomial object and the shift of the time axis required in order to reduce rounding errors"""
    s=[]
    if len(levels) != 0:
        x = np.array(matplotlib.dates.date2num(dates))
        for i in range(len(x)):
            s.append(x[i] - x[0])
        p_coeff = np.polyfit(s, levels, p)
        poly = np.poly1d(p_coeff)
        print((poly, x[0]))
        return (poly, x[0])

def poly_deriv(poly):
    deriv = np.polyder(poly, m=1)
    return deriv


