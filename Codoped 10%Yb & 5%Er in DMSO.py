#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 16:57:25 2024

@author: main
"""

import uncertainties 
import matplotlib.pyplot as plt
import numpy as np
from uncertainties import unumpy
from uncertainties import ufloat

"""----------Initialization----------"""

F1 = open('/Users/main/Desktop/Semesterarbeit/30.04/CaCuSiO_10%Yb_5%Er_70%_750nm_15C_up_lowC.txt','r')
lines1 = F1.readlines()
F1.close()


F2 = open('/Users/main/Desktop/Semesterarbeit/30.04/CaCuSiO_10%Yb_5%Er_70%_750nm_25C_up_lowC.txt','r')
lines2 = F2.readlines()
F2.close()

F3 = open('/Users/main/Desktop/Semesterarbeit/30.04/CaCuSiO_10%Yb_5%Er_70%_750nm_30C_up_lowC.txt','r')
lines3 = F3.readlines()
F3.close()

F4 = open('/Users/main/Desktop/Semesterarbeit/30.04/CaCuSiO_10%Yb_5%Er_70%_750nm_35C_up_lowC.txt','r')
lines4 = F4.readlines()
F4.close()

F5 = open('/Users/main/Desktop/Semesterarbeit/30.04/CaCuSiO_10%Yb_5%Er_70%_750nm_45C_up_lowC.txt','r')
lines5 = F5.readlines()
F5.close()

F6 = open('/Users/main/Desktop/Semesterarbeit/30.04/CaCuSiO_10%Yb_5%Er_70%_750nm_55C_up_lowC.txt','r')
lines6 = F6.readlines()
F6.close()

F7 = open('/Users/main/Desktop/Semesterarbeit/30.04/CaCuSiO_10%Yb_5%Er_70%_750nm_65C_up_lowC.txt','r')
lines7 = F7.readlines()
F7.close()

F8 = open('/Users/main/Desktop/Semesterarbeit/30.04/CaCuSiO_10%Yb_5%Er_70%_750nm_65C_down_lowC.txt','r')
lines8 = F8.readlines()
F8.close()

F9 = open('/Users/main/Desktop/Semesterarbeit/30.04/CaCuSiO_10%Yb_5%Er_70%_750nm_55C_down_lowC.txt','r')
lines9 = F9.readlines()
F9.close()

F10 = open('/Users/main/Desktop/Semesterarbeit/30.04/CaCuSiO_10%Yb_5%Er_70%_750nm_45C_down_lowC.txt','r')
lines10 = F10.readlines()
F10.close()

F11 = open('/Users/main/Desktop/Semesterarbeit/30.04/CaCuSiO_10%Yb_5%Er_70%_750nm_35C_down_lowC.txt','r')
lines11 = F11.readlines()
F11.close()

F12 = open('/Users/main/Desktop/Semesterarbeit/30.04/CaCuSiO_10%Yb_5%Er_70%_750nm_30C_down_lowC.txt','r')
lines12 = F12.readlines()
F12.close()

F13 = open('/Users/main/Desktop/Semesterarbeit/30.04/CaCuSiO_10%Yb_5%Er_70%_750nm_25C_down_lowC.txt','r')
lines13 = F13.readlines()
F13.close()

F14 = open('/Users/main/Desktop/Semesterarbeit/30.04/CaCuSiO_10%Yb_5%Er_70%_750nm_15C_down_lowC.txt','r')
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


"""----------Plots----------"""

plt.plot(data[:,0,0],data[:,1,0],label='15C')
plt.plot(data[:,0,1],data[:,1,1],label='25C')
plt.plot(data[:,0,2],data[:,1,2],label='30C')
plt.plot(data[:,0,3],data[:,1,3],label='35C')
plt.plot(data[:,0,4],data[:,1,4],label='45C')
plt.plot(data[:,0,5],data[:,1,5],label='55C')
plt.plot(data[:,0,6],data[:,1,6],label='65C')
plt.grid()
plt.xlabel('Wavelength')
plt.ylabel('Counts %')
plt.title('PL spectra of CaCuSiO Codoped 10%YB & 5%Er')
plt.legend()
plt.show()

plt.plot(data[:,0,7],data[:,1,7],label='65C')
plt.plot(data[:,0,8],data[:,1,8],label='55C')
plt.plot(data[:,0,9],data[:,1,9],label='45C')
plt.plot(data[:,0,10],data[:,1,10],label='35C')
plt.plot(data[:,0,11],data[:,1,11],label='30C')
plt.plot(data[:,0,12],data[:,1,12],label='25C')
plt.plot(data[:,0,13],data[:,1,13],label='15C')
plt.grid()
plt.xlabel('Wavelength')
plt.ylabel('Counts %')
plt.title('PL spectra of CaCuSiO Codoped 10%YB & 5%Er')
plt.legend()
plt.show()

Ratios_down = np.array([data[71,1,13]/data[368,1,13], data[71,1,12]/data[368,1,12], data[71,1,11]/data[368,1,11], data[71,1,10]/data[368,1,10], data[71,1,9]/data[368,1,9], data[71,1,8]/data[368,1,8], data[71,1,7]/data[368,1,7]])

data[:,:,0] = (data[:,:,13] + data[:,:,0])/2
data[:,:,1] = (data[:,:,12] + data[:,:,1])/2
data[:,:,2] = (data[:,:,11] + data[:,:,2])/2
data[:,:,3] = (data[:,:,10] + data[:,:,3])/2
data[:,:,4] = (data[:,:,9] + data[:,:,4])/2
data[:,:,5] = (data[:,:,8] + data[:,:,5])/2
data[:,:,6] = (data[:,:,7] + data[:,:,6])/2

plt.plot(data[:,0,0],data[:,1,0]/data[21,1,0],label='15C')
plt.plot(data[:,0,1],data[:,1,1]/data[21,1,1],label='25C')
plt.plot(data[:,0,2],data[:,1,2]/data[21,1,2],label='30C')
plt.plot(data[:,0,3],data[:,1,3]/data[21,1,3],label='35C')
plt.plot(data[:,0,4],data[:,1,4]/data[21,1,4],label='45C')
plt.plot(data[:,0,5],data[:,1,5]/data[21,1,5],label='55C')
plt.plot(data[:,0,6],data[:,1,6]/data[21,1,6],label='65C')
plt.grid()
plt.xlabel('Wavelength')
plt.ylabel('Counts %')
plt.title('Averaged PL spectra of CaCuSiO Codoped 10%YB & 5%Er')
plt.legend()
plt.show()


Temperature = np.array([15,25,30,35,45,55,65])
T_err = np.array([1,1,1,1,1,1,1])
Ratios_averaged = np.array([data[71,1,0]/data[368,1,0], data[71,1,1]/data[368,1,1], data[71,1,2]/data[368,1,2], data[71,1,3]/data[368,1,3], data[71,1,4]/data[368,1,4], data[71,1,5]/data[368,1,5], data[71,1,6]/data[368,1,6]])

plt.plot(Temperature,Ratios_down,'o',label='down')
plt.errorbar(Temperature,Ratios_down,yerr=None,xerr=T_err,color='black',linestyle='')
plt.plot(Temperature,Ratios_averaged,'o',label='average')
plt.errorbar(Temperature,Ratios_averaged,yerr=None,xerr=T_err,color='black',linestyle='')
plt.grid()
plt.xlabel('Temperature')
plt.ylabel('Ratio')
plt.title('Temperature dependence of peak ratios')
plt.legend()
plt.show()


