#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 16 16:57:45 2024

@author: main
"""

import matplotlib.pyplot as plt
import numpy as np



"""----------Initialization----------"""

F1 = open('C:/Users/MEaTh/OneDrive/Desktop/Semesterarbeit/03.05/CaCuSiO_10%Yb_5%Er_70%_750nm_30C_H2O.txt','r')
lines1 = F1.readlines()
F1.close()


F2 = open('C:/Users/MEaTh/OneDrive/Desktop/Semesterarbeit/30.04/CaCuSiO_10%Yb_5%Er_70%_750nm_30C_down_lowC.txt','r')
lines2 = F2.readlines()
F2.close()

F3 = open('C:/Users/MEaTh/OneDrive/Desktop/Semesterarbeit/14.05/Ca_20%YB_5%Er_750nm_70%_D2O_30C_down.txt','r')
lines3 = F3.readlines()
F3.close()


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
b = b + 1

"""----------Plots----------"""

SIZE_DEFAULT = 14
SIZE_LARGE = 16
plt.rc("font", weight="normal")  # controls default font
plt.rc("font", size=SIZE_DEFAULT)  # controls default text sizes
plt.rc("axes", titlesize=SIZE_LARGE)  # fontsize of the axes title
plt.rc("axes", labelsize=SIZE_LARGE)  # fontsize of the x and y labels
plt.rc("xtick", labelsize=SIZE_DEFAULT)  # fontsize of the tick labels
plt.rc("ytick", labelsize=SIZE_DEFAULT)  # fontsize of the tick labels

fig, ax = plt.subplots(figsize=(6, 5))

ax.plot(data[300:,0,2],data[300:,1,2]/data[21,1,2]*100,label='D2O', color = '#00596D')
ax.text(data[300,0,2]+220, 50, '$D_2O$', color='#00596D',fontweight="bold",horizontalalignment="left",verticalalignment="center",)
ax.plot(data[300:,0,1],data[300:,1,1]/data[21,1,1]*100,label='DMSO', color = '#96272D')
ax.text(data[300,0,1]+220, 45, '$DMSO$', color='#96272D',fontweight="bold",horizontalalignment="left",verticalalignment="center",)
ax.plot(data[300:,0,0],data[300:,1,0]/data[21,1,0]*100,label='H2O', color = '#575757')
ax.text(data[300,0,0]+220, 40, '$H_2O$', color='#575757',fontweight="bold",horizontalalignment="left",verticalalignment="center",)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.spines["top"].set_visible(False)
ax.grid()
ax.set_xlabel('Wavelength in nm')
ax.set_ylabel('Relative Intensity (%)')
plt.savefig("great.png", dpi=300)
plt.show()