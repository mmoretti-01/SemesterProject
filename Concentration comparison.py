#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 14 15:32:06 2024

@author: main
"""

import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
from scipy.optimize import curve_fit

"""----------Initialization----------"""

F1 = open('C:/Users/MEaTh/OneDrive/Desktop/Semesterarbeit/14.05/Ca_20%YB_5%Er_750nm_70%_D2O_15C_down_m.txt','r')
lines1 = F1.readlines()
F1.close()

F2 = open('C:/Users/MEaTh/OneDrive/Desktop/Semesterarbeit/14.05/Ca_20%YB_5%Er_750nm_70%_D2O_25C_down_m.txt','r')
lines2 = F2.readlines()
F2.close()

F3 = open('C:/Users/MEaTh/OneDrive/Desktop/Semesterarbeit/14.05/Ca_20%YB_5%Er_750nm_70%_D2O_30C_down_m.txt','r')
lines3 = F3.readlines()
F3.close()

F4 = open('C:/Users/MEaTh/OneDrive/Desktop/Semesterarbeit/14.05/Ca_20%YB_5%Er_750nm_70%_D2O_35C_down_m.txt','r')
lines4 = F4.readlines()
F4.close()

F5 = open('C:/Users/MEaTh/OneDrive/Desktop/Semesterarbeit/14.05/Ca_20%YB_5%Er_750nm_70%_D2O_40C_down_m.txt','r')
lines5 = F5.readlines()
F5.close()

F6 = open('C:/Users/MEaTh/OneDrive/Desktop/Semesterarbeit/14.05/Ca_20%YB_5%Er_750nm_70%_D2O_50C_down_m.txt','r')
lines6 = F6.readlines()
F6.close()

F7 = open('C:/Users/MEaTh/OneDrive/Desktop/Semesterarbeit/14.05/Ca_20%YB_5%Er_750nm_70%_D2O_60C_down_m.txt','r')
lines7 = F7.readlines()
F7.close()

F8 = open('C:/Users/MEaTh/OneDrive/Desktop/Semesterarbeit/14.05/Ca_20%YB_5%Er_750nm_70%_D2O_60C_down.txt','r')
lines8 = F8.readlines()
F8.close()

F9 = open('C:/Users/MEaTh/OneDrive/Desktop/Semesterarbeit/14.05/Ca_20%YB_5%Er_750nm_70%_D2O_50C_down.txt','r')
lines9 = F9.readlines()
F9.close()

F10 = open('C:/Users/MEaTh/OneDrive/Desktop/Semesterarbeit/14.05/Ca_20%YB_5%Er_750nm_70%_D2O_40C_down.txt','r')
lines10 = F10.readlines()
F10.close()

F11 = open('C:/Users/MEaTh/OneDrive/Desktop/Semesterarbeit/14.05/Ca_20%YB_5%Er_750nm_70%_D2O_35C_down.txt','r')
lines11 = F11.readlines()
F11.close()

F12 = open('C:/Users/MEaTh/OneDrive/Desktop/Semesterarbeit/14.05/Ca_20%YB_5%Er_750nm_70%_D2O_30C_down.txt','r')
lines12 = F12.readlines()
F12.close()

F13 = open('C:/Users/MEaTh/OneDrive/Desktop/Semesterarbeit/14.05/Ca_20%YB_5%Er_750nm_70%_D2O_25C_down.txt','r')
lines13 = F13.readlines()
F13.close()

F14 = open('C:/Users/MEaTh/OneDrive/Desktop/Semesterarbeit/14.05/Ca_20%YB_5%Er_750nm_70%_D2O_15C_down.txt','r')
lines14 = F14.readlines()
F14.close()

F15 = open('C:/Users/MEaTh/OneDrive/Desktop/Semesterarbeit/14.05/Ca_20%YB_5%Er_750nm_70%_D2O_60C_down_l.txt','r')
lines15 = F15.readlines()
F15.close()

F16 = open('C:/Users/MEaTh/OneDrive/Desktop/Semesterarbeit/14.05/Ca_20%YB_5%Er_750nm_70%_D2O_50C_down_l.txt','r')
lines16 = F16.readlines()
F16.close()

F17 = open('C:/Users/MEaTh/OneDrive/Desktop/Semesterarbeit/14.05/Ca_20%YB_5%Er_750nm_70%_D2O_40C_down_l.txt','r')
lines17 = F17.readlines()
F17.close()

F18 = open('C:/Users/MEaTh/OneDrive/Desktop/Semesterarbeit/14.05/Ca_20%YB_5%Er_750nm_70%_D2O_35C_down_l.txt','r')
lines18 = F18.readlines()
F18.close()

F19 = open('C:/Users/MEaTh/OneDrive/Desktop/Semesterarbeit/14.05/Ca_20%YB_5%Er_750nm_70%_D2O_30C_down_l.txt','r')
lines19 = F19.readlines()
F19.close()

F20 = open('C:/Users/MEaTh/OneDrive/Desktop/Semesterarbeit/14.05/Ca_20%YB_5%Er_750nm_70%_D2O_25C_down_l.txt','r')
lines20 = F20.readlines()
F20.close()

F21 = open('C:/Users/MEaTh/OneDrive/Desktop/Semesterarbeit/14.05/Ca_20%YB_5%Er_750nm_70%_D2O_15C_down_l.txt','r')
lines21 = F21.readlines()
F21.close()

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

for line in lines15:
    words = line.split("-")  
    a = words[0].split()
    data[p,:,b] = a
    p = p+1

p = 0
b = b + 1

for line in lines16:
    words = line.split("-")  
    a = words[0].split()
    data[p,:,b] = a
    p = p+1

p = 0
b = b + 1

for line in lines17:
    words = line.split("-")  
    a = words[0].split()
    data[p,:,b] = a
    p = p+1

p = 0
b = b + 1

for line in lines18:
    words = line.split("-")  
    a = words[0].split()
    data[p,:,b] = a
    p = p+1

p = 0
b = b + 1

for line in lines19:
    words = line.split("-")  
    a = words[0].split()
    data[p,:,b] = a
    p = p+1

p = 0
b = b + 1

for line in lines20:
    words = line.split("-")  
    a = words[0].split()
    data[p,:,b] = a
    p = p+1

p = 0
b = b + 1

for line in lines21:
    words = line.split("-")  
    a = words[0].split()
    data[p,:,b] = a
    p = p+1

p = 0
b = b + 1

"""----------Functions-----------"""

"""0.5(2843.2/3999.9/2843.7)->0.43mg/ml; 0.2(2850.5/4096.1/2850.7)->0.16mg/ml; 0.1(2821.9/4369.1/2822.0)->0.07mg/ml"""
"""" +-0.1mg"""
"""best with deg 4"""

def FIR(T,p):
    return np.polyval(p,T)

def dFIR(T,p):
    f = p[0]*T**0 
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

"""plt.plot(data[:,0,12],data[:,1,12]/data[21,1,12],label='25C')
plt.plot(data[:,0,1],data[:,1,1]/data[21,1,1],label='25C')
plt.plot(data[:,0,19],data[:,1,19]/data[21,1,19],label='25C')
plt.grid()
plt.xlabel('Wavelength')
plt.ylabel('Counts %')
plt.title('PL spectra of CaCuSiO Codoped 20%YB & 5%Er different concentrations')
plt.legend()
plt.show()


plt.plot(data[:,0,0],data[:,1,0],label='15C')
plt.plot(data[:,0,1],data[:,1,1],label='25C')
plt.plot(data[:,0,2],data[:,1,2],label='30C')
plt.plot(data[:,0,3],data[:,1,3],label='35C')
plt.plot(data[:,0,4],data[:,1,4],label='40C')
plt.plot(data[:,0,5],data[:,1,5],label='50C')
plt.plot(data[:,0,6],data[:,1,6],label='60C')
plt.grid()
plt.xlabel('Wavelength')
plt.ylabel('Counts %')
plt.title('PL spectra of CaCuSiO Codoped 20%YB & 5%Er mediumC')
plt.legend()
plt.show()

plt.plot(data[:,0,0],data[:,1,0]/data[21,1,0],label='15C')
plt.plot(data[:,0,1],data[:,1,1]/data[21,1,1],label='25C')
plt.plot(data[:,0,2],data[:,1,2]/data[21,1,2],label='30C')
plt.plot(data[:,0,3],data[:,1,3]/data[21,1,3],label='35C')
plt.plot(data[:,0,4],data[:,1,4]/data[21,1,4],label='40C')
plt.plot(data[:,0,5],data[:,1,5]/data[21,1,5],label='50C')
plt.plot(data[:,0,6],data[:,1,6]/data[21,1,6],label='60C')
plt.grid()
plt.xlabel('Wavelength')
plt.ylabel('Counts %')
plt.title('PL spectra of CaCuSiO Codoped 20%YB & 5%Er normalised mediumC')
plt.legend()
plt.show()

plt.plot(data[:,0,7],data[:,1,7],label='60C')
plt.plot(data[:,0,8],data[:,1,8],label='50C')
plt.plot(data[:,0,9],data[:,1,9],label='40C')
plt.plot(data[:,0,10],data[:,1,10],label='35C')
plt.plot(data[:,0,11],data[:,1,11],label='30C')
plt.plot(data[:,0,12],data[:,1,12],label='25C')
plt.plot(data[:,0,13],data[:,1,13],label='15C')
plt.grid()
plt.xlabel('Wavelength')
plt.ylabel('Counts %')
plt.title('PL spectra of CaCuSiO Codoped 10%YB & 5%Er highC')
plt.legend()
plt.show()

plt.plot(data[:,0,7],data[:,1,7]/data[21,1,7],label='60C')
plt.plot(data[:,0,8],data[:,1,8]/data[21,1,8],label='50C')
plt.plot(data[:,0,9],data[:,1,9]/data[21,1,9],label='40C')
plt.plot(data[:,0,10],data[:,1,10]/data[21,1,10],label='35C')
plt.plot(data[:,0,11],data[:,1,11]/data[21,1,11],label='30C')
plt.plot(data[:,0,12],data[:,1,12]/data[21,1,12],label='25C')
plt.plot(data[:,0,13],data[:,1,13]/data[21,1,13],label='15C')
plt.grid()
plt.xlabel('Wavelength')
plt.ylabel('Counts %')
plt.title('PL spectra of CaCuSiO Codoped 10%YB & 5%Er normalised highC')
plt.legend()
plt.show()

plt.plot(data[:,0,14],data[:,1,14],label='60C')
plt.plot(data[:,0,15],data[:,1,15],label='50C')
plt.plot(data[:,0,16],data[:,1,16],label='40C')
plt.plot(data[:,0,17],data[:,1,17],label='35C')
plt.plot(data[:,0,18],data[:,1,18],label='30C')
plt.plot(data[:,0,19],data[:,1,19],label='25C')
plt.plot(data[:,0,20],data[:,1,20],label='15C')
plt.grid()
plt.xlabel('Wavelength')
plt.ylabel('Counts %')
plt.title('PL spectra of CaCuSiO Codoped 20%YB & 5%Er lowC')
plt.legend()
plt.show()

plt.plot(data[:,0,14],data[:,1,14]/data[21,1,14],label='60C')
plt.plot(data[:,0,15],data[:,1,15]/data[21,1,15],label='50C')
plt.plot(data[:,0,16],data[:,1,16]/data[21,1,16],label='40C')
plt.plot(data[:,0,17],data[:,1,17]/data[21,1,17],label='35C')
plt.plot(data[:,0,18],data[:,1,18]/data[21,1,18],label='30C')
plt.plot(data[:,0,19],data[:,1,19]/data[21,1,19],label='25C')
plt.plot(data[:,0,20],data[:,1,20]/data[21,1,20],label='15C')
plt.grid()
plt.xlabel('Wavelength')
plt.ylabel('Counts %')
plt.title('PL spectra of CaCuSiO Codoped 20%YB & 5%Er normalised lowC')
plt.legend()
plt.show()



Ratios_high = np.array([data[71,1,13]/data[368,1,13], data[71,1,12]/data[368,1,12], data[71,1,11]/data[368,1,11], data[71,1,10]/data[368,1,10], data[71,1,9]/data[368,1,9], data[71,1,8]/data[368,1,8], data[71,1,7]/data[368,1,7]])
Ratios_medium = np.array([data[71,1,0]/data[368,1,0], data[71,1,1]/data[368,1,1], data[71,1,2]/data[368,1,2], data[71,1,3]/data[368,1,3], data[71,1,4]/data[368,1,4], data[71,1,5]/data[368,1,5], data[71,1,6]/data[368,1,6]])
Ratios_low = np.array([data[71,1,20]/data[368,1,20], data[71,1,19]/data[368,1,19], data[71,1,18]/data[368,1,18], data[71,1,17]/data[368,1,17], data[71,1,16]/data[368,1,16], data[71,1,15]/data[368,1,15], data[71,1,14]/data[368,1,14]])


Temperature = np.array([15,25,30,35,40,50,60])
T_err = np.array([1,1,1,1,1,1,1])
y_err_high = err_R(data[71,1,7:14],data[368,1,7:14])
y_err_medium = err_R(data[71,1,0:7],data[368,1,0:7])
y_err_low = err_R(data[71,1,14:21],data[368,1,14:21])

params, covariance = sp.optimize.curve_fit(log_func, Temperature, Ratios_high)
a0, b0 = params
params, covariance = sp.optimize.curve_fit(log_func, Temperature, Ratios_medium)
a1, b1 = params
params, covariance = sp.optimize.curve_fit(log_func, Temperature, Ratios_low)
a2, b2 = params

p0 = np.polyfit(Temperature,Ratios_high,deg=6) 
p1 = np.polyfit(Temperature,Ratios_medium,deg=6) 
p2 = np.polyfit(Temperature,Ratios_low,deg=6) 

plt.plot(Temperature,Ratios_high,' k')
plt.errorbar(Temperature, Ratios_high, yerr = y_err_high, xerr = T_err, linestyle = '', color = 'black')
plt.plot(T,log_func(T, a0, b0),linestyle ='--', label='(0.4g +- 0.1)g/l ')
plt.plot(Temperature,Ratios_medium,' k')
plt.errorbar(Temperature, Ratios_medium, yerr = y_err_medium, xerr = T_err, linestyle = '', color = 'black')
plt.plot(T,log_func(T, a1, b1),linestyle ='--', label='(0.2g +- 0.1)g/l ')
plt.plot(Temperature,Ratios_low,' k')
plt.errorbar(Temperature, Ratios_low, yerr = y_err_low, xerr = T_err, linestyle = '', color = 'black')
plt.plot(T,log_func(T, a2, b2),linestyle ='--', label='(0.06 +- 0.09)g/l ')
plt.grid()
plt.xlabel('Temperature in \u00b0C')
plt.ylabel('Peak Ratios')
plt.title('Temperature dependence of peak ratios')
plt.legend()
plt.show()


Ratios_high = np.array([data[368,1,13]/data[71,1,13], data[368,1,12]/data[71,1,12], data[368,1,11]/data[71,1,11], data[368,1,10]/data[71,1,10], data[368,1,9]/data[71,1,9], data[368,1,8]/data[71,1,8], data[368,1,7]/data[71,1,7]])
Ratios_medium = np.array([data[368,1,0]/data[71,1,0], data[368,1,1]/data[71,1,1], data[368,1,2]/data[71,1,2], data[368,1,3]/data[71,1,3], data[368,1,4]/data[71,1,4], data[368,1,5]/data[71,1,5], data[368,1,6]/data[71,1,6]])
Ratios_low = np.array([data[368,1,20]/data[71,1,20], data[368,1,19]/data[71,1,19], data[368,1,18]/data[71,1,18], data[368,1,17]/data[71,1,17], data[368,1,16]/data[71,1,16], data[368,1,15]/data[71,1,15], data[368,1,14]/data[71,1,14]])

Temperature = np.array([15,25,30,35,40,50,60])
y_err_high = err_R(data[368,1,7:14],data[71,1,7:14])
y_err_medium = err_R(data[368,1,0:7],data[71,1,0:7])
y_err_low = err_R(data[368,1,14:21],data[71,1,14:21])

params, covariance = sp.optimize.curve_fit(log_func, Temperature, Ratios_high)
a3, b3 = params
params, covariance = sp.optimize.curve_fit(log_func, Temperature, Ratios_medium)
a4, b4 = params
params, covariance = sp.optimize.curve_fit(log_func, Temperature, Ratios_low)
a5, b5 = params

p3 = np.polyfit(Temperature,Ratios_high,deg=1)
p4 = np.polyfit(Temperature,Ratios_medium,deg=1)
p5 = np.polyfit(Temperature,Ratios_low,deg=1)

plt.plot(Temperature,Ratios_high,' k')
plt.errorbar(Temperature, Ratios_high, yerr = y_err_high, xerr = T_err, linestyle = '', color = 'black')
plt.plot(T,np.polyval(p3,T),linestyle ='--', label='(0.4g +- 0.1)g/l ')
plt.plot(Temperature,Ratios_medium,' k')
plt.errorbar(Temperature, Ratios_medium, yerr = y_err_medium, xerr = T_err, linestyle = '', color = 'black')
plt.plot(T,np.polyval(p4,T),linestyle ='--', label='(0.2g +- 0.1)g/l ')
plt.plot(Temperature,Ratios_low,' k')
plt.errorbar(Temperature, Ratios_low, yerr = y_err_low, xerr = T_err, linestyle = '', color = 'black')
plt.plot(T,np.polyval(p5,T),linestyle ='--', label='(0.06 +- 0.09)g/l ')
plt.grid()
plt.xlabel('Temperature in \u00b0C')
plt.ylabel('Peak Ratios')
plt.title('Temperature dependence of peak ratios')
plt.legend()
plt.show()

Lit = np.array([1.1,3.9,1.3,1.62,3.3,2.5,1.17,5,2.17,1.87,1.1,1.90])
bins = [1,1.5,2,2.5,3,3.5,4,4.5,4.75,5.25,6]

plt.hist(Lit,bins)
plt.grid()
plt.xlabel('relative Sensitivities')
plt.ylabel('Appearences')
plt.title('Sensitivities NIR II+ (290K - 335K)')
plt.legend()
plt.show()

plt.plot(T,dFIR_R_log(T, a0, b0), label = 'highC', linestyle ='--')
plt.plot(T,dFIR_R_log(T, a1, b1), label = 'mediumC', linestyle ='--')
plt.plot(T,dFIR_R_log(T, a2, b2), label = 'lowC', linestyle ='--')
plt.grid()
plt.xlabel('Temperature in in \u00b0C')
plt.ylabel('Relative Sensitivity')
plt.title('Temperature dependence of the relative sensitivity')
plt.legend()
plt.show()

plt.plot(T,dFIR_R_log(T, a3, b3), label = 'highC', linestyle ='--')
plt.plot(T,dFIR_R_log(T, a4, b4), label = 'mediumC', linestyle ='--')
plt.plot(T,dFIR_R_log(T, a5, b5), label = 'lowC', linestyle ='--')
plt.grid()
plt.xlabel('Temperature in \u00b0C')
plt.ylabel('Relative Sensitivity')
plt.title('Temperature dependence of the relative sensitivity (logarithmic)')
plt.legend()
plt.show()

plt.plot(T,dFIR_R(T,p3), label = 'highC', linestyle ='--')
plt.plot(T,dFIR_R(T,p4), label = 'mediumC', linestyle ='--')
plt.plot(T,dFIR_R(T,p5), label = 'lowC', linestyle ='--')
plt.grid()
plt.xlabel('Temperature in \u00b0C')
plt.ylabel('Relative Sensitivity')
plt.title('Temperature dependence of the relative sensitivity (linear)')
plt.legend()
plt.show()

plt.plot(T,dFIR_log(T, a0, b0), label = 'highC', linestyle ='--')
plt.plot(T,dFIR_log(T, a1, b1), label = 'mediumC', linestyle ='--')
plt.plot(T,dFIR_log(T, a2, b2), label = 'lowC', linestyle ='--')
plt.grid()
plt.xlabel('Temperature in in \u00b0C')
plt.ylabel('Relative Sensitivity')
plt.title('Temperature dependence of the absolute sensitivity')
plt.legend()
plt.show()
"""


SIZE_DEFAULT = 14
SIZE_LARGE = 16
plt.rc("font", weight="normal")  # controls default font
plt.rc("font", size=SIZE_DEFAULT)  # controls default text sizes
plt.rc("axes", titlesize=SIZE_LARGE)  # fontsize of the axes title
plt.rc("axes", labelsize=SIZE_LARGE)  # fontsize of the x and y labels
plt.rc("xtick", labelsize=SIZE_DEFAULT)  # fontsize of the tick labels
plt.rc("ytick", labelsize=SIZE_DEFAULT)  # fontsize of the tick labels


fig, ax = plt.subplots(figsize=(6, 5))

ax.plot(data[:,0,12],data[:,1,12]/data[23,1,12]*100, color='#00596D')
ax.text(data[450,0,12]-510, data[450,1,12]/data[21,1,12]*100+80, '$(0.4 \pm 0.1)gl^{-1}$', color='#00596D',fontweight="bold",horizontalalignment="left",verticalalignment="center",)
ax.plot(data[:,0,1],data[:,1,1]/data[23,1,1]*100,label='Sr', color ='#96272D')
ax.text(data[450,0,1]-510, data[450,1,1]/data[21,1,1]*100+76, '$(0.2 \pm 0.1)gl^{-1}$', color='#96272D',fontweight="bold",horizontalalignment="left",verticalalignment="center",)
ax.plot(data[:,0,19],data[:,1,19]/data[23,1,19]*100,label='Ba', color='#575757')
ax.text(data[450,0,19]-510, data[450,1,19]/data[21,1,19]*100+70, '$(0.06 \pm 0.09)gl^{-1}$', color='#575757',fontweight="bold",horizontalalignment="left",verticalalignment="center",)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.spines["top"].set_visible(False)
ax.grid()
ax.set_xlabel('Wavelength in nm')
ax.set_ylabel('Relative Intensity (%)')
plt.savefig("great.png", dpi=300)
plt.show()

fig, ax = plt.subplots(figsize=(6, 5))

ax.plot(data[:,0,0],data[:,1,0]/data[23,1,0]*100, color='#08407E')
ax.text(data[450,0,0]-510, 100, '$15\u00b0C$', color='#08407E',fontweight="bold",horizontalalignment="left",verticalalignment="center",)
ax.plot(data[:,0,1],data[:,1,1]/data[23,1,1]*100,label='Sr', color ='#3395AB')
ax.text(data[450,0,1]-510, 92, '$25\u00b0C$', color='#3395AB',fontweight="bold",horizontalalignment="left",verticalalignment="center",)
ax.plot(data[:,0,2],data[:,1,2]/data[23,1,2]*100,label='Ba', color='#818F42')
ax.text(data[450,0,2]-510, 84, '$30\u00b0C$', color='#818F42',fontweight="bold",horizontalalignment="left",verticalalignment="center",)
ax.plot(data[:,0,3],data[:,1,3]/data[23,1,3]*100, color='#A1AB71')
ax.text(data[450,0,3]-510, 76, '$35\u00b0C$', color='#A1AB71',fontweight="bold",horizontalalignment="left",verticalalignment="center",)
ax.plot(data[:,0,4],data[:,1,4]/data[23,1,4]*100,label='Sr', color ='#BBA471')
ax.text(data[450,0,4]-510, 68, '$40\u00b0C$', color='#BBA471',fontweight="bold",horizontalalignment="left",verticalalignment="center",)
ax.plot(data[:,0,5],data[:,1,5]/data[23,1,5]*100,label='Ba', color='#D48681')
ax.text(data[450,0,5]-510, 60, '$50\u00b0C$', color='#D48681',fontweight="bold",horizontalalignment="left",verticalalignment="center",)
ax.plot(data[:,0,6],data[:,1,6]/data[23,1,6]*100,label='Ba', color='#96272D')
ax.text(data[450,0,6]-510, 52, '$60\u00b0C$', color='#96272D',fontweight="bold",horizontalalignment="left",verticalalignment="center",)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.spines["top"].set_visible(False)
ax.grid()
ax.set_xlabel('Wavelength in nm')
ax.set_ylabel('Relative Intensity (%)')
plt.show()

fig, ax = plt.subplots(figsize=(6, 5))

ax.plot(data[:,0,13],data[:,1,13]/data[368,1,13]*100, color='#4D7DBF')
ax.text(data[450,0,0]-510, 400, '$15\u00b0C$', color='#4D7DBF',fontweight="bold",horizontalalignment="left",verticalalignment="center",)
ax.plot(data[:,0,12],data[:,1,12]/data[368,1,12]*100,label='Sr', color ='#3395AB')
ax.text(data[450,0,1]-510, 375, '$25\u00b0C$', color='#3395AB',fontweight="bold",horizontalalignment="left",verticalalignment="center",)
ax.plot(data[:,0,11],data[:,1,11]/data[368,1,11]*100,label='Ba', color='#818F42')
ax.text(data[450,0,2]-510, 350, '$30\u00b0C$', color='#818F42',fontweight="bold",horizontalalignment="left",verticalalignment="center",)
ax.plot(data[:,0,10],data[:,1,10]/data[368,1,10]*100, color='#A58542')
ax.text(data[450,0,3]-510, 325, '$35\u00b0C$', color='#A58542',fontweight="bold",horizontalalignment="left",verticalalignment="center",)
ax.plot(data[:,0,9],data[:,1,9]/data[368,1,9]*100,label='Sr', color ='#C55D57')
ax.text(data[450,0,4]-510, 300, '$40\u00b0C$', color='#C55D57',fontweight="bold",horizontalalignment="left",verticalalignment="center",)
ax.plot(data[:,0,8],data[:,1,8]/data[368,1,8]*100,label='Ba', color='#B73B92')
ax.text(data[450,0,5]-510, 275, '$50\u00b0C$', color='#B73B92',fontweight="bold",horizontalalignment="left",verticalalignment="center",)
ax.plot(data[:,0,7],data[:,1,7]/data[368,1,7]*100,label='Ba', color='#8C8C8C')
ax.text(data[450,0,6]-510, 250, '$60\u00b0C$', color='#8C8C8C',fontweight="bold",horizontalalignment="left",verticalalignment="center",)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.spines["top"].set_visible(False)
ax.grid()
ax.set_xlabel('Wavelength in nm')
ax.set_ylabel('Relative Intensity (%)')
plt.show()


fig, ax = plt.subplots(figsize=(6, 5))

ax.plot(data[:,0,20],data[:,1,20]/data[368,1,20]*100, color='#4D7DBF')
ax.text(data[450,0,0]-510, 600, '$15\u00b0C$', color='#4D7DBF',fontweight="bold",horizontalalignment="left",verticalalignment="center",)
ax.plot(data[:,0,19],data[:,1,19]/data[368,1,19]*100,label='Sr', color ='#3395AB')
ax.text(data[450,0,1]-510, 565, '$25\u00b0C$', color='#3395AB',fontweight="bold",horizontalalignment="left",verticalalignment="center",)
ax.plot(data[:,0,18],data[:,1,18]/data[368,1,18]*100,label='Ba', color='#818F42')
ax.text(data[450,0,2]-510, 530, '$30\u00b0C$', color='#818F42',fontweight="bold",horizontalalignment="left",verticalalignment="center",)
ax.plot(data[:,0,17],data[:,1,17]/data[368,1,17]*100, color='#A58542')
ax.text(data[450,0,3]-510, 495, '$35\u00b0C$', color='#A58542',fontweight="bold",horizontalalignment="left",verticalalignment="center",)
ax.plot(data[:,0,16],data[:,1,16]/data[368,1,16]*100,label='Sr', color ='#C55D57')
ax.text(data[450,0,4]-510, 460, '$40\u00b0C$', color='#C55D57',fontweight="bold",horizontalalignment="left",verticalalignment="center",)
ax.plot(data[:,0,15],data[:,1,15]/data[368,1,15]*100,label='Ba', color='#B73B92')
ax.text(data[450,0,5]-510, 425, '$50\u00b0C$', color='#B73B92',fontweight="bold",horizontalalignment="left",verticalalignment="center",)
ax.plot(data[:,0,14],data[:,1,14]/data[368,1,14]*100,label='Ba', color='#8C8C8C')
ax.text(data[450,0,6]-510, 390, '$60\u00b0C$', color='#8C8C8C',fontweight="bold",horizontalalignment="left",verticalalignment="center",)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.spines["top"].set_visible(False)
ax.grid()
ax.set_xlabel('Wavelength in nm')
ax.set_ylabel('Relative Intensity (%)')
plt.show()

fig, ax = plt.subplots(figsize=(6, 5))


ax.plot(data[:,0,0],data[:,1,0]/data[23,1,0]*100, color='#08407E')
ax.text(data[450,0,0]-510, 100, '$15\u00b0C$', color='#08407E',fontweight="bold",horizontalalignment="left",verticalalignment="center",)
ax.plot(data[:,0,6],data[:,1,6]/data[23,1,6]*100,label='Ba', color='#96272D')
ax.text(data[450,0,6]-510, 92, '$60\u00b0C$', color='#96272D',fontweight="bold",horizontalalignment="left",verticalalignment="center",)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.spines["top"].set_visible(False)
ax.grid()
ax.set_xlabel('Wavelength in nm')
ax.set_ylabel('Relative Intensity (%)')

plt.show()


def logarithmic_fit(A,Peak1,Peak2,Temperature):
    Ratios = np.zeros(len(A))
    T = np.arange(14,61,0.01)
    i = 0
    for a in A:
        Ratios[i] = data[Peak1,1,a]/data[Peak2,1,a]
        i = i + 1
    params, covariance = sp.optimize.curve_fit(log_func, Temperature, Ratios)
    a, b = params
    T = np.arange(15,60,0.5)
    return a * np.log(T) + b

def logarithmic_coef(A,Peak1,Peak2,Temperature):
    Ratios = np.zeros(len(A))
    T = np.arange(14,61,0.01)
    i = 0
    for a in A:
        Ratios[i] = data[Peak1,1,a]/data[Peak2,1,a]
        i = i + 1
    params, covariance = sp.optimize.curve_fit(log_func, Temperature, Ratios)
    a, b = params
    T = np.arange(15,60,0.5)
    return a, b

def logarithmic_fit_full(A,Peak1,Peak2,Temperature):
    Ratios = np.zeros(len(A))
    T = np.arange(14,61,0.01)
    i = 0
    for a in A:
        Ratios[i] = data[Peak1,1,a]/data[Peak2,1,a]
        i = i + 1
    params, covariance = sp.optimize.curve_fit(log_func, Temperature, Ratios)
    a, b = params
    T = np.arange(15,60,0.5)
    return a, b, covariance

def Ratios_func(A,Peak1,Peak2):
    Ratios = np.zeros(len(A))
    T = np.arange(14,61,0.01)
    i = 0
    for a in A:
        Ratios[i] = data[Peak1,1,a]/data[Peak2,1,a]
        i = i + 1
    return Ratios

def log_func(x, a, b):
    return a * np.log(x) + b

#Hiermit kannst du den logarithmischen plot bestimmen.
def FIR_log(T, a, b):
    return log_func(T, a, b)

#Dies ist das logarithmische Analog der dFIR Funktion von oben
def dFIR_log(T, a, b):
    return np.abs(a/T)

#Genau wie zuvor.
def dFIR_R_log(T, a, b):
    f = dFIR_log(T, a, b)
    return np.abs(f/FIR_log(T, a, b))

Temperature = [15,25,30,35,40,50,60]

y_err_high = err_R(data[71,1,7:14],data[368,1,7:14])
y_err_medium = err_R(data[71,1,0:7],data[368,1,0:7])
y_err_low = err_R(data[71,1,14:21],data[368,1,14:21])
T_err = np.array([1,1,1,1,1,1,1])
        
print(y_err_medium)
fig, ax = plt.subplots(figsize=(6, 5))

A = np.arange(0,7)
ax.plot(T,logarithmic_fit(A,72,368,Temperature), color='#96272D', linestyle = '--')
plt.errorbar(Temperature, Ratios_func(A,72,368), yerr = y_err_medium, xerr = T_err, linestyle = '', color = 'black')
ax.text(40, 6.6, '$(0.2 \pm 0.1)gl^{-1}$', color='#96272D',fontweight="bold",horizontalalignment="left",verticalalignment="center",)
A = np.arange(7,14)
Temperature = [60,50,40,35,30,25,15]
ax.plot(T,logarithmic_fit(A,72,368,Temperature),label='Ba', color='#00596D', linestyle = '--')
plt.errorbar(Temperature, Ratios_func(A,72,368), yerr = y_err_high, xerr = T_err, linestyle = '', color = 'black')
ax.text(40, 7.1, '$(0.4 \pm 0.1)gl^{-1}$', color='#00596D',fontweight="bold",horizontalalignment="left",verticalalignment="center",)
A = np.arange(14,21)
ax.plot(T,logarithmic_fit(A,72,368,Temperature),label='Ba', color='#575757', linestyle = '--')
plt.errorbar(Temperature, Ratios_func(A,72,368), yerr = y_err_low, xerr = T_err, linestyle = '', color = 'black')
ax.text(40, 6.1, '$(0.06 \pm 0.09)gl^{-1}$', color='#575757',fontweight="bold",horizontalalignment="left",verticalalignment="center",)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.spines["top"].set_visible(False)
ax.grid()
ax.set_xlabel('Temperature in $\u00b0C$')
ax.set_ylabel('Peak Ratios') 

plt.show()


fig, ax = plt.subplots(figsize=(6, 5))
A = np.arange(0,7)
Temperature = [15,25,30,35,40,50,60]
ax.plot(T,logarithmic_fit(A,72,368,Temperature), color='#00596D', linestyle = '--')
plt.errorbar(Temperature, Ratios_func(A,72,368), yerr = y_err_medium, xerr = T_err, linestyle = '', color = 'black')
ax.text(40, 6.05, '$logarithmic-fit$', color='#00596D',fontweight="bold",horizontalalignment="left",verticalalignment="center",)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.spines["top"].set_visible(False)
ax.grid()
ax.set_xlabel('Temperature in $\u00b0C$')
ax.set_ylabel('Peak Ratios') 

plt.show()

A = np.arange(7,14)
Temperature = [60,50,40,35,30,25,15]
a,b = logarithmic_coef(A,72,368,Temperature)
fig, ax = plt.subplots(figsize=(6, 5))
ax.plot(T,dFIR_R_log(T,a,b)*100, color='#00596D', linestyle = '--')
ax.text(40, 2.618, '$logarithmic-fit$', color='#00596D',fontweight="bold",horizontalalignment="left",verticalalignment="center",)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.spines["top"].set_visible(False)
ax.grid()
ax.set_xlabel('Temperature in $\u00b0C$')
ax.set_ylabel('Relative Sensitivity in %$K^{-1}$') 
plt.savefig("great.png", dpi=300)
plt.show()
print(np.max(dFIR_R_log(T,a,b)*100))

A = np.arange(7,14)
Temperature = [60,50,40,35,30,25,15]
a,b = logarithmic_coef(A,72,368,Temperature)
fig, ax = plt.subplots(figsize=(6, 5))
ax.plot(T,dFIR_log(T,a,b)*100, color='#00596D', linestyle = '--')
ax.text(40, 12.15, '$logarithmic-fit$', color='#00596D',fontweight="bold",horizontalalignment="left",verticalalignment="center",)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.spines["top"].set_visible(False)
ax.grid()
ax.set_xlabel('Temperature in $\u00b0C$')
ax.set_ylabel('Absolute Sensitivity in %$K^{-1}$') 

plt.show()

def linear_fit(A,Peak1,Peak2,Temperature):
    Ratios = np.zeros(len(A))
    T = np.arange(14,61,0.01)
    i = 0
    for a in A:
        Ratios[i] = data[Peak1,1,a]/data[Peak2,1,a]
        i = i + 1
    p = np.polyfit(Temperature,Ratios,deg = 1)
    return p[0] * T + p[1]

def linear_fit_coeff(A,Peak1,Peak2,Temperature):
    Ratios = np.zeros(len(A))
    T = np.arange(14,61,0.01)
    i = 0
    for a in A:
        Ratios[i] = data[Peak1,1,a]/data[Peak2,1,a]
        i = i + 1
    p = np.polyfit(Temperature,Ratios,deg = 1)
    return p

y_err_high = err_R(data[368,1,7:14],data[71,1,7:14])
y_err_medium = err_R(data[368,1,0:7],data[71,1,0:7])
y_err_low = err_R(data[368,1,14:21],data[71,1,14:21])
T = np.arange(14,61,0.01)


fig, ax = plt.subplots(figsize=(6, 5))
A = np.arange(7,14)
Temperature = [60,50,40,35,30,25,15]
ax.plot(T,linear_fit(A,368,72,Temperature),label='Ba', color='#00596D', linestyle = '--')
plt.errorbar(Temperature, Ratios_func(A,368,72), yerr = y_err_high, xerr = T_err, linestyle = '', color = 'black')
ax.text(40, 0.455, '$linear-fit$', color='#00596D',fontweight="bold",horizontalalignment="left",verticalalignment="center",)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.spines["top"].set_visible(False)
plt.yticks(np.arange(0.2, 0.6, 0.05))
ax.grid()
plt.yticks(np.arange(0.2, 0.6, 0.1))
ax.set_xlabel('Temperature in $\u00b0C$')
ax.set_ylabel('Peak Ratios')

plt.show()

fig, ax = plt.subplots(figsize=(6, 5))

A = np.arange(7,14)
Temperature = [60,50,40,35,30,25,15]
p = linear_fit_coeff(A,368,72,Temperature)
ax.plot(T,dFIR_R(T,p)*100,label='Ba', color='#00596D', linestyle = '--')
ax.text(40,2.78, '$linear-fit$', color='#00596D',fontweight="bold",horizontalalignment="left",verticalalignment="center",)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.spines["top"].set_visible(False)
ax.grid()
plt.yticks(np.arange(1.2, 3.2, 0.3))
ax.set_xlabel('Temperature in $\u00b0C$')
ax.set_ylabel('Relative Sensitivity (%)')

plt.show()

def linear_fit_full(A,Peak1,Peak2,Temperature):
    Ratios = np.zeros(len(A))
    T = np.arange(14,61,0.01)
    i = 0
    for a in A:
        Ratios[i] = data[Peak1,1,a]/data[Peak2,1,a]
        i = i + 1
    p = np.polyfit(Temperature,Ratios,deg = 1,cov=True)
    return p

print(max(dFIR_R(T,p)*100))
print(dFIR_R(14,p)*100)

p = linear_fit_full(A, 368, 72, Temperature)
del_a = p[1][0,0]
del_b = p[1][1,1]


print(p)
print(del_a,del_b)


a, b, cov = logarithmic_fit_full(A,72,368,Temperature)
del_a = cov[0,0]
del_b = cov[1,1]
print(a,b)
print(del_a,del_b)
