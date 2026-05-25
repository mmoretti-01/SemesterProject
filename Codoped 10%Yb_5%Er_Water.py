#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 14 09:28:02 2024

@author: main
"""

import uncertainties 
import matplotlib.pyplot as plt
import numpy as np
from uncertainties import unumpy
from uncertainties import ufloat


"""----------Initialization----------"""

F1 = open('/Users/main/Desktop/Semesterarbeit/03.05/CaCuSiO_10%Yb_5%Er_70%_750nm_15C_H2O.txt','r')
lines1 = F1.readlines()
F1.close()


F2 = open('/Users/main/Desktop/Semesterarbeit/03.05/CaCuSiO_10%Yb_5%Er_70%_750nm_30C_H2O.txt','r')
lines2 = F2.readlines()
F2.close()

F3 = open('/Users/main/Desktop/Semesterarbeit/03.05/CaCuSiO_10%Yb_5%Er_70%_750nm_45C_H2O.txt','r')
lines3 = F3.readlines()
F3.close()

F4 = open('/Users/main/Desktop/Semesterarbeit/03.05/CaCuSiO_10%Yb_5%Er_70%_750nm_60C_H2O.txt','r')
lines4 = F4.readlines()
F4.close()

"""----------Saving into arrays----------"""

p = 0
a = 0
b = 0
data = np.zeros([512,2,16])


for line in lines1:
    words = line.split("-")  
    a = words[0].split()
    data[p,:,b] = a
    p = p+1

p = 0
b = b + 1

for line in lines2:
    words = line.split("-")  
    a = words[0].split()
    data[p,:,b] = a
    p = p+1

p = 0
b = b + 1

for line in lines3:
    words = line.split("-")  
    a = words[0].split()
    data[p,:,b] = a
    p = p+1

p = 0
b = b +1

for line in lines4:
    words = line.split("-")  
    a = words[0].split()
    data[p,:,b] = a
    p = p+1

p = 0
b = b + 1


"""----------Plots----------"""

plt.plot(data[:,0,0],data[:,1,0],label='15C')
plt.plot(data[:,0,1],data[:,1,1],label='30C')
plt.plot(data[:,0,2],data[:,1,2],label='45C')
plt.plot(data[:,0,3],data[:,1,3],label='60C')

plt.grid()
plt.xlabel('Wavelength')
plt.ylabel('Counts %')
plt.title('PL spectra of CaCuSiO Codoped 10%YB & 5%Er')
plt.legend()
plt.show()

temperature = np.array([15,30,45,60])
ratios = np.array([data[71,1,0]/data[368,1,0],data[71,1,1]/data[368,1,0],data[71,1,2]/data[368,1,0],data[71,1,3]/data[368,1,0]])

plt.plot(temperature,ratios)
plt.grid()
plt.xlabel('Temperature')
plt.ylabel('Ratio')
plt.title('Temperature dependence of peak ratios')
plt.show()





