#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 22 16:13:59 2024

@author: main
"""


import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
from scipy.optimize import curve_fit

"""----------Initialization----------"""

F1 = open('C:/Users/MEaTh/OneDrive/Desktop/Semesterarbeit/22.05/CaCuSiO_70%_750nm_20%Yb_5%Er_Agar_15C.txt','r')
lines1 = F1.readlines()
F1.close()

F2 = open('C:/Users/MEaTh/OneDrive/Desktop/Semesterarbeit/22.05/CaCuSiO_70%_750nm_20%Yb_5%Er_Agar_25C.txt','r')
lines2 = F2.readlines()
F2.close()

F3 = open('C:/Users/MEaTh/OneDrive/Desktop/Semesterarbeit/22.05/CaCuSiO_70%_750nm_20%Yb_5%Er_Agar_30C.txt','r')
lines3 = F3.readlines()
F3.close()

F4 = open('C:/Users/MEaTh/OneDrive/Desktop/Semesterarbeit/22.05/CaCuSiO_70%_750nm_20%Yb_5%Er_Agar_35C.txt','r')
lines4 = F4.readlines()
F4.close()

F5 = open('C:/Users/MEaTh/OneDrive/Desktop/Semesterarbeit/22.05/CaCuSiO_70%_750nm_20%Yb_5%Er_Agar_40C.txt','r')
lines5 = F5.readlines()
F5.close()

F6 = open('C:/Users/MEaTh/OneDrive/Desktop/Semesterarbeit/22.05/CaCuSiO_70%_750nm_20%Yb_5%Er_Agar_50C.txt','r')
lines6 = F6.readlines()
F6.close()

F7 = open('C:/Users/MEaTh/OneDrive/Desktop/Semesterarbeit/22.05/CaCuSiO_70%_750nm_20%Yb_5%Er_Agar_60C.txt','r')
lines7 = F7.readlines()
F7.close()


"""----------Saving into arrays----------"""

p = 0
a = 0
b = 0
data = np.zeros([512,2,21])


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

"""----------Functions-----------"""

def FIR(T,p):
    return np.polyval(p,T)

def dFIR(T,p):
    f = 2*p[0]*T +p[1]
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

T = np.arange(14,61,0.5)

plt.plot(data[:,0,0],data[:,1,0],label='15C', color = 'royalblue')
plt.plot(data[:,0,1],data[:,1,1],label='25C', color = 'cyan')
plt.plot(data[:,0,2],data[:,1,2],label='30C', color = 'lime')
plt.plot(data[:,0,3],data[:,1,3],label='35C', color = 'yellow')
plt.plot(data[:,0,4],data[:,1,4],label='40C', color = 'orange')
plt.plot(data[:,0,5],data[:,1,5],label='50C', color = 'orangered')
plt.plot(data[:,0,6],data[:,1,6],label='60C', color = 'crimson')
plt.grid()
plt.xlabel('Wavelength')
plt.ylabel('Peak Ratios')
plt.title('PL spectra of CaCuSiO Codoped 20%YB & 5%Er Agar')
plt.legend()
plt.show()

plt.plot(data[:,0,0],data[:,1,0]/data[399,1,0],label='15C', color = 'royalblue')
plt.plot(data[:,0,1],data[:,1,1]/data[399,1,1],label='25C', color = 'cyan')
plt.plot(data[:,0,2],data[:,1,2]/data[399,1,2],label='30C', color = 'lime')
plt.plot(data[:,0,3],data[:,1,3]/data[399,1,3],label='35C', color = 'yellow')
plt.plot(data[:,0,4],data[:,1,4]/data[399,1,4],label='40C', color = 'orange')
plt.plot(data[:,0,5],data[:,1,5]/data[399,1,5],label='50C', color = 'orangered')
plt.plot(data[:,0,6],data[:,1,6]/data[399,1,6],label='60C', color = 'crimson')
plt.grid()
plt.xlabel('Wavelength')
plt.ylabel('Peak Ratios')
plt.title('Codoped 20%YB & 5%Er normalised Agar')
plt.legend()
plt.show()

Ratios_medium = np.array([data[71,1,0]/data[399,1,0], data[71,1,1]/data[399,1,1], data[71,1,2]/data[399,1,2], data[71,1,3]/data[399,1,3], data[71,1,4]/data[399,1,4], data[71,1,5]/data[399,1,5], data[71,1,6]/data[399,1,6]])

Temperature = np.array([15,25,30,35,40,50,60])
T_err = np.array([1,1,1,1,1,1,1])
y_err = err_R(data[71,1,0:7],data[399,1,0:7])

params, covariance = sp.optimize.curve_fit(log_func, Temperature, Ratios_medium)
a1, b1 = params


plt.plot(Temperature,Ratios_medium,' k')
plt.errorbar(Temperature, Ratios_medium, yerr = y_err, xerr = T_err, linestyle = '', color = 'black')
plt.plot(T,log_func(T, a1, b1),linestyle ='--', label='logarithmic fit')
plt.grid()
plt.xlabel('Temperature in \u00b0C')
plt.ylabel('Peak Ratios')
plt.title('Temperature dependence of peak ratios')
plt.legend()
plt.show()

plt.plot(T,dFIR_R_log(T, a1, b1), label = 'logarithmic fit', linestyle ='--')
plt.grid()
plt.xlabel('Temperature in in \u00b0C')
plt.ylabel('Relative Sensitivity')
plt.title('Temperature dependence of the relative sensitivity')
plt.legend()
plt.show()

Ratios_medium = np.array([data[399,1,0]/data[71,1,0], data[399,1,1]/data[71,1,1], data[399,1,2]/data[71,1,2], data[399,1,3]/data[71,1,3], data[399,1,4]/data[71,1,4], data[399,1,5]/data[71,1,5], data[399,1,6]/data[71,1,6]])
y_err_medium = err_R(data[399,1,0:7],data[71,1,0:7])
params, covariance = sp.optimize.curve_fit(log_func, Temperature, Ratios_medium)
a4, b4 = params
p4 = np.polyfit(Temperature,Ratios_medium,deg=2)

plt.plot(Temperature,Ratios_medium,' k')
plt.errorbar(Temperature, Ratios_medium, yerr = y_err_medium, xerr = T_err, linestyle = '', color = 'black')
plt.plot(T,np.polyval(p4,T),linestyle ='--', label='quadratic fit')
plt.grid()
plt.xlabel('Temperature in \u00b0C')
plt.ylabel('Peak Ratios')
plt.title('Temperature dependence of the peak ratios')
plt.legend()
plt.show()


plt.plot(T,dFIR_R(T,p4), label = 'quadratic fit', linestyle ='--')
plt.grid()
plt.xlabel('Temperature in \u00b0C')
plt.ylabel('Relative Sensitivity')
plt.title('Temperature dependence of the relative sensitivity')
plt.legend()
plt.show()





