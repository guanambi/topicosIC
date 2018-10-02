
import matplotlib.pyplot as plt
import math
from scipy.optimize import minimize
from scipy.optimize import  differential_evolution

#rastrigin
A=10
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def rastrigin(x):
    s = 0
    for i in range(0,len(x)):
        s = s + x[i]**2 - A * np.cos(2 * math.pi * x[i])
        #print(s)
    s =  A*len(x) + s
    return  s

x = np.linspace(-5.12,5.12,4)

limites=[(-5.12,5.12),(-5.12,5.12),(-5.12,5.12),(-5.12,5.12)]
#print(rastrigin([0,0,0,0]))
resultado = differential_evolution(rastrigin,limites)
print(resultado.x)
print(resultado.fun)