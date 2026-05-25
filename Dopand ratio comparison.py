#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 16 13:57:10 2024

@author: main
"""

import uncertainties 
import matplotlib.pyplot as plt
import numpy as np
from uncertainties import unumpy
from uncertainties import ufloat

"""----------Initialization----------"""

F1 = open('/Users/main/Desktop/Semesterarbeit/24.04/Cadopd 10%er 5%yb, 785nm.txt','r')
lines1 = F1.readlines()
F1.close()

F2 = open('/Users/main/Desktop/Semesterarbeit/24.04/Cadopd 10%yb 5%er, 785nm.txt','r')
lines2 = F2.readlines()
F2.close()

F3 = open('/Users/main/Desktop/Semesterarbeit/08.05/Ca_15%Yb_5%Er_750nm_30-40%.txt','r')
lines3 = F3.readlines()
F3.close()

F4 = open('/Users/main/Desktop/Semesterarbeit/08.05/Ca_20%Yb_5%Er_750nm_30-40%.txt','r')
lines4 = F4.readlines()
F4.close()

F5 = open('/Users/main/Desktop/Semesterarbeit/08.05/Sr_codoped_750nm_30-40%.txt','r')
lines5 = F5.readlines()
F5.close()

F6 = open('/Users/main/Desktop/Semesterarbeit/17.04/CaCuSiO_15%Yb_1000C_2h.txt','r')
lines6 = F6.readlines()
F6.close()

F7 = open('/Users/main/Desktop/Semesterarbeit/17.04/CaCuSiO_Codoped_1000C_2h.txt','r')
lines7 = F7.readlines()
F7.close()


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
    
for line in lines5:
    words = line.split("-")  
    a = words[0].split()
    data[p,:,b] = a
    p = p+1

p = 0
b = b + 1

for line in lines6:
    words = line.split("-")  
    a = words[0].split()
    data[p,:,b] = a
    p = p+1

p = 0
b = b + 1

for line in lines7:
    words = line.split("-")  
    a = words[0].split()
    data[p,:,b] = a
    p = p+1

p = 0
b = b + 1






"""----------Plots----------"""


plt.plot(data[:,0,3],data[:,1,3]/data[21,1,3],label='20%Yb 5%Er', color = '#007894')
plt.plot(data[:,0,2],data[:,1,2]/data[21,1,2],label='15%Yb 5%Er', color= '#B7352D')
plt.plot(data[:,0,1],data[:,1,1]/data[21,1,1],label='10%Yb 5%Er', color= '#6F6F6F')
plt.grid()
plt.xlabel('Wavelength in nm')
plt.ylabel('Relative Intensity')
plt.title('Comparison of different dopand ratios')
plt.legend()
plt.show()

plt.plot(data[:,0,5],data[:,1,5]/data[21,1,5],label='15%Yb 0%Er', color='#B7352D')
plt.plot(data[:,0,2],data[:,1,2]/data[21,1,2],label='15%Yb 5%Er', color='#007894')
plt.grid()
plt.xlabel('Wavelength in nm')
plt.ylabel('Relative Intensity')
plt.title('Comparison of different dopand ratios')
plt.legend()
plt.show()

plt.plot(data[:,0,6],data[:,1,6]/data[21,1,6],label='10%Yb 2.5%Er', color = '#8E6713')
plt.plot(data[:,0,1],data[:,1,1]/data[21,1,1],label='10%Yb 5%Er', color = '#6F6F6F')
plt.grid()
plt.xlabel('Wavelength')
plt.ylabel('Relative Intensity')
plt.title('PL spectra of codoped EB')
plt.legend()
plt.show()