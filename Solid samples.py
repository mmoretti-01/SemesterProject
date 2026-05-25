#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 14:16:46 2024

@author: main
"""


import matplotlib.pyplot as plt
import numpy as np

"""----------Initialization----------"""

F1 = open('C:/Users/MEaTh/OneDrive/Desktop/Semesterarbeit/17.04/BaCuSiO_5%Er_1000C_2h.txt','r')
lines1 = F1.readlines()
F1.close()


F2 = open('C:/Users/MEaTh/OneDrive/Desktop/Semesterarbeit/17.04/BaCuSiO_10%Er_900C_30min.txt','r')
lines2 = F2.readlines()
F2.close()

F3 = open('C:/Users/MEaTh/OneDrive/Desktop/Semesterarbeit/17.04/BaCuSiO_10%Er_1000C_30min.txt','r')
lines3 = F3.readlines()
F3.close()

F4 = open('C:/Users/MEaTh/OneDrive/Desktop/Semesterarbeit/17.04/BaCuSiO_10%Er_1100C_30min.txt','r')
lines4 = F4.readlines()
F4.close()

F5 = open('C:/Users/MEaTh/OneDrive/Desktop/Semesterarbeit/17.04/BaCuSiO_10%Er_1000C_2h.txt','r')
lines5 = F5.readlines()
F5.close()

F6 = open('C:/Users/MEaTh/OneDrive/Desktop/Semesterarbeit/17.04/CaCuSiO_5%Yb_1000C_2h.txt','r')
lines6 = F6.readlines()
F6.close()

F7 = open('C:/Users/MEaTh/OneDrive/Desktop/Semesterarbeit/17.04/CaCuSiO_10%Yb_1000C_2h.txt','r')
lines7 = F7.readlines()
F7.close()

F8 = open('C:/Users/MEaTh/OneDrive/Desktop/Semesterarbeit/17.04/CaCuSiO_15%Yb_1000C_2h.txt','r')
lines8 = F8.readlines()
F8.close()

F9 = open('C:/Users/MEaTh/OneDrive/Desktop/Semesterarbeit/17.04/CaCuSiO_10%Er_1000C_2h.txt','r')
lines9 = F9.readlines()
F9.close()

F10 = open('C:/Users/MEaTh/OneDrive/Desktop/Semesterarbeit/17.04/CaCuSiO_15%Er_1000C_2h.txt','r')
lines10 = F10.readlines()
F10.close()

F11 = open('C:/Users/MEaTh/OneDrive/Desktop/Semesterarbeit/17.04/CaCuSiO_Codoped_1000C_2h.txt','r')
lines11 = F11.readlines()
F11.close()

F12 = open('C:/Users/MEaTh/OneDrive/Desktop/Semesterarbeit/24.04/Sr 10%Er 785nm.txt','r')
lines12 = F12.readlines()
F12.close()

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


"""----------Plots----------"""


"""plt.plot(data[:,0,0],data[:,1,0]/data[45,1,0],label='5%')
plt.plot(data[:,0,4],data[:,1,4]/data[45,1,4],label='10%')
plt.grid()
plt.xlabel('Wavelength')
plt.ylabel('Relative Intensity')
plt.title('PL spectra of Er doped BaCuSiO ')
plt.legend()
plt.show()

plt.plot(data[:,0,8],data[:,1,8]/data[25,1,8],label='10%')
plt.plot(data[:,0,9],data[:,1,9]/data[25,1,8],label='15%')
plt.grid()
plt.xlabel('Wavelength in nm')
plt.ylabel('Relative Intensity')
plt.title('PL spectra of Er doped CaCuSiO ')
plt.legend()
plt.show()

plt.plot(data[:,0,10],data[:,1,10]/data[21,1,10],label='10%Yb 2.5%Er', color = '#8E6713')
plt.grid()
plt.xlabel('Wavelength')
plt.ylabel('Relative Intensity')
plt.title('PL spectra of codoped EB')
plt.legend()
plt.show()

plt.plot(data[:,0,1],data[:,1,1]/data[39,1,1],label='900C')
plt.plot(data[:,0,2],data[:,1,2]/data[39,1,1],label='1000C')
plt.plot(data[:,0,3],data[:,1,3]/data[39,1,1],label='1100C')
plt.grid()
plt.xlabel('Wavelength')
plt.ylabel('Relative Intensity')
plt.title('PL spectra of 10%Er doped BaCuSiO ')
plt.legend()
plt.show()

plt.plot(data[:,0,11],data[:,1,11]/data[21,1,11],label='10%')
plt.grid()
plt.xlabel('Wavelength')
plt.ylabel('Relative Intensity')
plt.title('PL spectra of Er doped SrCuSiO ')
plt.legend()
plt.show()"""

SIZE_DEFAULT = 14
SIZE_LARGE = 16
plt.rc("font", weight="normal")  # controls default font
plt.rc("font", size=SIZE_DEFAULT)  # controls default text sizes
plt.rc("axes", titlesize=SIZE_LARGE)  # fontsize of the axes title
plt.rc("axes", labelsize=SIZE_LARGE)  # fontsize of the x and y labels
plt.rc("xtick", labelsize=SIZE_DEFAULT)  # fontsize of the tick labels
plt.rc("ytick", labelsize=SIZE_DEFAULT)  # fontsize of the tick labels


fig, ax = plt.subplots(figsize=(6, 5))

ax.plot(data[:,0,8],data[:,1,8]/data[26,1,8]*100, color='#00596D')
ax.text(data[450,0,8]-510, data[450,1,8]/data[26,1,8]*100+5, '$CaCuSi_4O_{10}:Er_{0.10}$', color='#00596D',fontweight="bold",horizontalalignment="left",verticalalignment="center",)
ax.plot(data[:,0,11],data[:,1,11]/data[21,1,11]*100,label='Sr', color ='#96272D')
ax.text(data[450,0,8]-510, data[450,1,8]/data[26,1,8]*100-5, '$SrCuSi_4O_{10}:Er_{0.10}$', color='#96272D',fontweight="bold",horizontalalignment="left",verticalalignment="center",)
ax.plot(data[:,0,4],data[:,1,4]/data[45,1,4]*100,label='Ba', color='#575757')
ax.text(data[450,0,8]-510, data[450,1,8]/data[26,1,8]*100-15, '$BaCuSi_4O_{10}:Er_{0.10}$', color='#575757',fontweight="bold",horizontalalignment="left",verticalalignment="center",)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.spines["top"].set_visible(False)
ax.grid()
ax.set_xlabel('Wavelength in nm')
ax.set_ylabel('Relative Intensity (%)')
plt.savefig("great.png", dpi=300)
plt.show()

fig, ax = plt.subplots(figsize=(6, 5))

ax.plot(data[:150,0,7],data[:150,1,7]/data[23,1,7]*100, color='#00596D')
ax.text(data[100,0,7]-35, data[450,1,8]/data[26,1,7]*100+80, '$CaCuSi_4O_{10}:Yb_{0.15}$', color='#00596D',fontweight="bold",horizontalalignment="left",verticalalignment="center",)
ax.plot(data[:150,0,6],data[:150,1,6]/data[23,1,6]*100, color='#96272D')
ax.text(data[100,0,6]-35, data[450,1,8]/data[26,1,6]*100+72, '$CaCuSi_4O_{10}:Yb_{0.10}$', color='#96272D',fontweight="bold",horizontalalignment="left",verticalalignment="center",)
ax.plot(data[:150,0,8],data[:150,1,8]/data[23,1,8]*100, color='#575757')
ax.text(data[100,0,8]-35, data[450,1,8]/data[26,1,8]*100+75, '$CaCuSi_4O_{10}$', color='#575757',fontweight="bold",horizontalalignment="left",verticalalignment="center",)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.spines["top"].set_visible(False)
ax.grid()
ax.set_xlabel('Wavelength in nm')
ax.set_ylabel('Relative Intensity (%)')
plt.savefig("great.png", dpi=300)
plt.show()


fig, ax = plt.subplots(figsize=(6, 5))

ax.plot(data[:,0,9],data[:,1,9]/data[25,1,9]*100, color='#00596D')
ax.text(data[100,0,9], data[450,1,9]/data[26,1,9]*100, '$CaCuSi_4O_{10}:Er_{0.15}$', color='#00596D',fontweight="bold",horizontalalignment="left",verticalalignment="center",)
ax.plot(data[:,0,8],data[:,1,8]/data[25,1,8]*100,color='#96272D')
ax.text(data[100,0,8], data[450,1,8]/data[26,1,8]*100, '$CaCuSi_4O_{10}:Er_{0.10}$', color='#96272D',fontweight="bold",horizontalalignment="left",verticalalignment="center",)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.spines["top"].set_visible(False)
ax.grid()
ax.set_xlabel('Wavelength in nm')
ax.set_ylabel('Relative Intensity (%)')
plt.savefig("great.png", dpi=300)
plt.show()


