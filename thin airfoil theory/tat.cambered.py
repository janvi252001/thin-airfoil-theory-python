import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
import matplotlib.pyplot as plt
import scipy.spatial as spatial
import scipy.integrate as integrate
import math
from sympy.core.function import Function
from sympy.core.symbol import Symbol



##READING A .DAT FILE WITH RECORD OF AIRFOIL

X,Y=[],[]
file= open('naca0006.dat')
next(file)
for line in file:
    X.append([line.split()[0]])
    Y.append([line.split()[1]])

c=int(input("enter the chord length:-"))
alpha=int(input("enter the angle of attack:-"))
alpha=math.radians(alpha)

theta=Symbol('theta')
x= 0.5*c*(1-sp.cos(theta))
function=sp.lambdify(theta,x, modules ='numpy')

#fourier coefficients
coefficients=[]
Ao= alpha-(1/np.pi)*integrate.quad(function,0,np.pi)[0]
coefficients.append(Ao)
for i in np.arange(1,4):
   coefficients.append((2/np.pi)*integrate.quad(lambda a : function(a)*np.cos(i*a),0,np.pi)[0])

cl= np.pi*(2*coefficients[0] + coefficients[1])
print("lift coefficieent",cl)
cm = np.pi/4*(coefficients[2]-coefficients[1])
print("cm(c/4) = ",cm)

cmle= [-cl/4 - np.pi*(coefficients[1]-coefficients[2])/4]
print("cmle", cmle)

