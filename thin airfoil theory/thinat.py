import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import math

from sympy.core.symbol import Symbol


####SYMMETRIC AIRFOIL

#arrays to store respective values
a=[] #for storing values of angle of attack
c=[] #for storing values of lift coefficient w.r.t angle of attack
cm=[] #for values of moment coefficient at leading edge
V= int(input("Enter the free stream velocity"))


#Function to calculate angle of attack and corresponding values of lift coefficient

for i in range(0,180):
    alpha = math.radians(i)
    a.append(alpha)
    cl=2*np.pi*alpha
    c.append(cl)
print(c)
print(a)
plt.plot(c,a)
plt.show()

    #Function to caculate moment coefficient at leading edge

for i in c:
    cmle= -i/4
    cm.append(cmle)
plt.plot(cm,a)
plt.show()






