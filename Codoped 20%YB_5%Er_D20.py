#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 14 09:44:18 2024

@author: main
"""

import uncertainties 
import matplotlib.pyplot as plt
import numpy as np
from uncertainties import unumpy
from uncertainties import ufloat
import scipy as sp
from scipy.optimize import curve_fit

"""----------Initialization----------"""

F1 = open('/Users/main/Desktop/Semesterarbeit/14.05/Ca_20%YB_5%Er_750nm_70%_D2O_15C_up.txt','r')
lines1 = F1.readlines()
F1.close()

F2 = open('/Users/main/Desktop/Semesterarbeit/14.05/Ca_20%YB_5%Er_750nm_70%_D2O_25C_up.txt','r')
lines2 = F2.readlines()
F2.close()

F3 = open('/Users/main/Desktop/Semesterarbeit/14.05/Ca_20%YB_5%Er_750nm_70%_D2O_30C_up.txt','r')
lines3 = F3.readlines()
F3.close()

F4 = open('/Users/main/Desktop/Semesterarbeit/14.05/Ca_20%YB_5%Er_750nm_70%_D2O_35C_up.txt','r')
lines4 = F4.readlines()
F4.close()

F5 = open('/Users/main/Desktop/Semesterarbeit/14.05/Ca_20%YB_5%Er_750nm_70%_D2O_40C_up.txt','r')
lines5 = F5.readlines()
F5.close()

F6 = open('/Users/main/Desktop/Semesterarbeit/14.05/Ca_20%YB_5%Er_750nm_70%_D2O_50C_up.txt','r')
lines6 = F6.readlines()
F6.close()

F7 = open('/Users/main/Desktop/Semesterarbeit/14.05/Ca_20%YB_5%Er_750nm_70%_D2O_60C_up.txt','r')
lines7 = F7.readlines()
F7.close()

F8 = open('/Users/main/Desktop/Semesterarbeit/14.05/Ca_20%YB_5%Er_750nm_70%_D2O_60C_down.txt','r')
lines8 = F8.readlines()
F8.close()

F9 = open('/Users/main/Desktop/Semesterarbeit/14.05/Ca_20%YB_5%Er_750nm_70%_D2O_50C_down.txt','r')
lines9 = F9.readlines()
F9.close()

F10 = open('/Users/main/Desktop/Semesterarbeit/14.05/Ca_20%YB_5%Er_750nm_70%_D2O_40C_down.txt','r')
lines10 = F10.readlines()
F10.close()

F11 = open('/Users/main/Desktop/Semesterarbeit/14.05/Ca_20%YB_5%Er_750nm_70%_D2O_35C_down.txt','r')
lines11 = F11.readlines()
F11.close()

F12 = open('/Users/main/Desktop/Semesterarbeit/14.05/Ca_20%YB_5%Er_750nm_70%_D2O_30C_down.txt','r')
lines12 = F12.readlines()
F12.close()

F13 = open('/Users/main/Desktop/Semesterarbeit/14.05/Ca_20%YB_5%Er_750nm_70%_D2O_25C_down.txt','r')
lines13 = F13.readlines()
F13.close()

F14 = open('/Users/main/Desktop/Semesterarbeit/14.05/Ca_20%YB_5%Er_750nm_70%_D2O_15C_down.txt','r')
lines14 = F14.readlines()
F14.close()

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

for line in lines8:
    words = line.split("-")  
    a = words[0].split()
    data[p,:,b] = a
    p = p+1

p = 0
b = b + 1

for line in lines9:
    words = line.split("-")  
    a = words[0].split()
    data[p,:,b] = a
    p = p+1

p = 0
b = b + 1

for line in lines10:
    words = line.split("-")  
    a = words[0].split()
    data[p,:,b] = a
    p = p+1

p = 0
b = b + 1

for line in lines11:
    words = line.split("-")  
    a = words[0].split()
    data[p,:,b] = a
    p = p+1

p = 0
b = b + 1

for line in lines12:
    words = line.split("-")  
    a = words[0].split()
    data[p,:,b] = a
    p = p+1

p = 0
b = b + 1

for line in lines13:
    words = line.split("-")  
    a = words[0].split()
    data[p,:,b] = a
    p = p+1

p = 0
b = b + 1

for line in lines14:
    words = line.split("-")  
    a = words[0].split()
    data[p,:,b] = a
    p = p+1

p = 0
b = b + 1

"""----------Functions-----------"""

def FIR(T,p):
    return np.polyval(p,T)

def dFIR(T,p):
    f = 4*p[0]*T**3 + 3*p[1]*T**2 + 2*p[2]*T +p[3]
    return f

def Temp(R,p):
    T = np.arange(15,60,0.05)
    k = 10
    P = 0
    for T_1 in T:
        s = np.abs(R-FIR(T_1,p))
        if s<k :
            k = s
            P = T_1
        else:
            k = k
    return P

def dFIR_R(T,p):
    f = dFIR(T,p)
    return np.abs(f/FIR(T,p))

def log_func(x, a, b):
    return a * np.log(x) + b

def FIR_log(T, a, b):
    return log_func(T, a, b)

def dFIR_log(T, a, b):
    return np.abs(a/T)

def dFIR_R_log(T, a, b):
    f = dFIR_log(T, a, b)
    return np.abs(f/FIR_log(T, a, b))

def err_R(I1,I2):
    err1 = np.sqrt(I1)
    err2 = np.sqrt(I2)
    err = np.sqrt((err1/I2)**2 + (I1*err2/(I2**2))**2)
    return err



"""----------Plots----------"""

T = np.arange(15,60,0.5)

plt.plot(data[:,0,0],data[:,1,0],label='15\u00b0C')
plt.plot(data[:,0,1],data[:,1,1],label='25\u00b0C')
plt.plot(data[:,0,2],data[:,1,2],label='30\u00b0C')
plt.plot(data[:,0,3],data[:,1,3],label='35\u00b0C')
"plt.plot(data[:,0,4],data[:,1,4],label='40\u00b0C')"
plt.plot(data[:,0,5],data[:,1,5],label='50\u00b0C')
plt.plot(data[:,0,6],data[:,1,6],label='60\u00b0C')
plt.grid()
plt.xlabel('Wavelength in nm')
plt.ylabel('Counts %')
plt.title('PL spectra of CaCuSiO Codoped 20%YB & 5%Er up')
plt.legend()
plt.show()

plt.plot(data[:,0,0],data[:,1,0]/data[368,1,0],label='15\u00b0C')
plt.plot(data[:,0,1],data[:,1,1]/data[368,1,1],label='25\u00b0C')
plt.plot(data[:,0,2],data[:,1,2]/data[368,1,2],label='30\u00b0C')
plt.plot(data[:,0,3],data[:,1,3]/data[368,1,3],label='35\u00b0C')
"plt.plot(data[:,0,4],data[:,1,4]/data[368,1,4],label='40\u00b0C')"
plt.plot(data[:,0,5],data[:,1,5]/data[368,1,5],label='50\u00b0C')
plt.plot(data[:,0,6],data[:,1,6]/data[368,1,6],label='60\u00b0C')
plt.grid()
plt.xlabel('Wavelength in nm')
plt.ylabel('Normalised Intensity')
plt.title('PL spectra of CaCuSiO Codoped 20%YB & 5%Er normalised up')
plt.legend()
plt.show()

plt.plot(data[:,0,7],data[:,1,7],label='60\u00b0C')
plt.plot(data[:,0,8],data[:,1,8],label='50\u00b0C')
plt.plot(data[:,0,9],data[:,1,9],label='40\u00b0C')
plt.plot(data[:,0,10],data[:,1,10],label='35\u00b0C')
plt.plot(data[:,0,11],data[:,1,11],label='30\u00b0C')
plt.plot(data[:,0,12],data[:,1,12],label='25\u00b0C')
plt.plot(data[:,0,13],data[:,1,13],label='15\u00b0C')
plt.grid()
plt.xlabel('Wavelength in nm')
plt.ylabel('Counts %')
plt.title('PL spectra of CaCuSiO Codoped 10%YB & 5%Er down')
plt.legend()
plt.show()

plt.plot(data[:,0,7],data[:,1,7]/data[368,1,7],label='60\u00b0C')
plt.plot(data[:,0,8],data[:,1,8]/data[368,1,8],label='50\u00b0C')
plt.plot(data[:,0,9],data[:,1,9]/data[368,1,9],label='40\u00b0C')
plt.plot(data[:,0,10],data[:,1,10]/data[368,1,10],label='35\u00b0C')
plt.plot(data[:,0,11],data[:,1,11]/data[368,1,11],label='30\u00b0C')
plt.plot(data[:,0,12],data[:,1,12]/data[368,1,12],label='25\u00b0C')
plt.plot(data[:,0,13],data[:,1,13]/data[368,1,13],label='15\u00b0C')
plt.grid()
plt.xlabel('Wavelength in nm')
plt.ylabel('Normalised Intensity')
plt.title('PL spectra of 20%Yb & 5%Er codoped CaCuSiO')
plt.legend()
plt.show()

Ratios_down = np.array([data[71,1,13]/data[368,1,13], data[71,1,12]/data[368,1,12], data[71,1,11]/data[368,1,11], data[71,1,10]/data[368,1,10], data[71,1,9]/data[368,1,9], data[71,1,8]/data[368,1,8], data[71,1,7]/data[368,1,7]])
Ratios_up = np.array([data[71,1,0]/data[368,1,0], data[71,1,1]/data[368,1,1], data[71,1,2]/data[368,1,2], data[71,1,3]/data[368,1,3], data[71,1,5]/data[368,1,5], data[71,1,6]/data[368,1,6]])
Ratios_down_inv = np.array([data[368,1,13]/data[71,1,13], data[368,1,12]/data[71,1,12], data[368,1,11]/data[71,1,11], data[368,1,10]/data[71,1,10], data[368,1,9]/data[71,1,9], data[368,1,8]/data[71,1,8], data[368,1,7]/data[71,1,7]])


data[:,:,0] = (data[:,:,13] + data[:,:,0])/2
data[:,:,1] = (data[:,:,12] + data[:,:,1])/2
data[:,:,2] = (data[:,:,11] + data[:,:,2])/2
data[:,:,3] = (data[:,:,10] + data[:,:,3])/2
data[:,:,4] = (data[:,:,9] + data[:,:,4])/2
data[:,:,5] = (data[:,:,8] + data[:,:,5])/2
data[:,:,6] = (data[:,:,7] + data[:,:,6])/2

plt.plot(data[:,0,0],data[:,1,0]/data[368,1,0],label='15\u00b0C')
plt.plot(data[:,0,1],data[:,1,1]/data[368,1,1],label='25\u00b0C')
plt.plot(data[:,0,2],data[:,1,2]/data[368,1,2],label='30\u00b0C')
plt.plot(data[:,0,3],data[:,1,3]/data[368,1,3],label='35\u00b0C')
"plt.plot(data[:,0,4],data[:,1,4]/data[368,1,4],label='40\u00b0C')"
plt.plot(data[:,0,5],data[:,1,5]/data[368,1,5],label='50\u00b0C')
plt.plot(data[:,0,6],data[:,1,6]/data[368,1,6],label='60\u00b0C')
plt.grid()
plt.xlabel('Wavelength in nm')
plt.ylabel('Counts %')
plt.title('Averaged PL spectra of CaCuSiO Codoped 20%YB & 5%Er')
plt.legend()
plt.show()

Temperature = np.array([15,25,30,35,40,50,60])
Temperature_av = np.array([15,25,30,35,50,60])
Ratios_averaged = np.array([data[71,1,0]/data[368,1,0], data[71,1,1]/data[368,1,1], data[71,1,2]/data[368,1,2], data[71,1,3]/data[368,1,3], data[71,1,5]/data[368,1,5], data[71,1,6]/data[368,1,6]])

p_down = np.polyfit(Temperature, Ratios_down, deg = 4)
p_down_inv = np.polyfit(Temperature, Ratios_down_inv, deg = 4)
params, covariance = sp.optimize.curve_fit(log_func, Temperature, Ratios_down)
a0, b0 = params

plt.plot(Temperature,Ratios_down,' k')
T_err = np.array([1,1,1,1,1,1,1])
y_err = err_R(data[71,1,7:14],data[368,1,7:14])
plt.errorbar(Temperature, Ratios_down, yerr = y_err, xerr = T_err, linestyle = '', color = 'black')
plt.plot(T,log_func(T, a0, b0), label ='Logarithmic fit', color = 'brown')
"""
plt.plot(Temperature_av,Ratios_up,label='up')
plt.plot(Temperature_av,Ratios_averaged,label='average')"""
plt.grid()
plt.xlabel('Temperature in \u00b0C')
plt.ylabel('Peak Ratios')
plt.title('Temperature dependence of peak ratios')
plt.legend()
plt.show()

p0 = np.polyfit(Temperature_av[:],Ratios_averaged[:],deg=4)
T = np.arange(15,60,0.5)

    



