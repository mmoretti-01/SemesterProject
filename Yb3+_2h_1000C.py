#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 16:16:59 2024

@author: main
"""


import matplotlib.pyplot as plt
import numpy as np

"""----------Initialization----------"""


"""F1 = open('/Users/main/Desktop/Semesterarbeit/12.03/15%, 3.16W, 785nm, 15C.txt','r')
lines1 = F1.readlines()
F1.close()


F2 = open('/Users/main/Desktop/Semesterarbeit/12.03/15%, 3.16W, 785nm, 30C.txt','r')
lines2 = F2.readlines()
F2.close()

F3 = open('/Users/main/Desktop/Semesterarbeit/12.03/15%, 3.16W, 785nm, 45C.txt','r')
lines3 = F3.readlines()
F3.close()

F4 = open('/Users/main/Desktop/Semesterarbeit/12.03/15%, 3.16W, 785nm, 60C.txt','r')
lines4 = F4.readlines()
F4.close()"""

F1 = open('C:/Users/MEaTh/OneDrive/Desktop/Semesterarbeit/19.03/15%/15%, 70%, 750nm, 2nd, 15C, up.txt','r')
lines1 = F1.readlines()
F1.close()


F2 = open('C:/Users/MEaTh/OneDrive/Desktop/Semesterarbeit/19.03/15%/15%, 70%, 750nm, 2nd, 30C, up.txt','r')
lines2 = F2.readlines()
F2.close()

F3 = open('C:/Users/MEaTh/OneDrive/Desktop/Semesterarbeit/19.03/15%/15%, 70%, 750nm, 2nd, 45C, up.txt','r')
lines3 = F3.readlines()
F3.close()

F4 = open('C:/Users/MEaTh/OneDrive/Desktop/Semesterarbeit/19.03/15%/15%, 70%, 750nm, 2nd, 60C, up.txt','r')
lines4 = F4.readlines()
F4.close()

F5 = open('C:/Users/MEaTh/OneDrive/Desktop/Semesterarbeit/19.03/15%/15%, 70%, 750nm, 2nd, 15C, down.txt','r')
lines5 = F5.readlines()
F5.close()

F6 = open('C:/Users/MEaTh/OneDrive/Desktop/Semesterarbeit/19.03/15%/15%, 70%, 750nm, 2nd, 30C, down.txt','r')
lines6 = F6.readlines()
F6.close()

F7 = open('C:/Users/MEaTh/OneDrive/Desktop/Semesterarbeit/19.03/15%/15%, 70%, 750nm, 2nd, 45C, down.txt','r')
lines7 = F7.readlines()
F7.close()

F8 = open('C:/Users/MEaTh/OneDrive/Desktop/Semesterarbeit/19.03/15%/15%, 70%, 750nm, 2nd, 60C, down.txt','r')
lines8 = F8.readlines()
F8.close()

F9 = open('C:/Users/MEaTh/OneDrive/Desktop/Semesterarbeit/19.03/10%/10%, 70%, 750nm, 2nd, 15C, up.txt','r')
lines9 = F9.readlines()
F9.close()

F10 = open('C:/Users/MEaTh/OneDrive/Desktop/Semesterarbeit/19.03/10%/10%, 70%, 750nm, 2nd, 30C, up.txt','r')
lines10 = F10.readlines()
F10.close()

F11 = open('C:/Users/MEaTh/OneDrive/Desktop/Semesterarbeit/19.03/10%/10%, 70%, 750nm, 2nd, 45C, up.txt','r')
lines11 = F11.readlines()
F11.close()

F12 = open('C:/Users/MEaTh/OneDrive/Desktop/Semesterarbeit/19.03/10%/10%, 70%, 750nm, 2nd, 60C, up.txt','r')
lines12 = F12.readlines()
F12.close()

F13 = open('C:/Users/MEaTh/OneDrive/Desktop/Semesterarbeit/19.03/10%/10%, 70%, 750nm, 2nd, 15C, down.txt','r')
lines13 = F13.readlines()
F13.close()

F14 = open('C:/Users/MEaTh/OneDrive/Desktop/Semesterarbeit/19.03/10%/10%, 70%, 750nm, 2nd, 30C, down.txt','r')
lines14 = F14.readlines()
F14.close()

F15 = open('C:/Users/MEaTh/OneDrive/Desktop/Semesterarbeit/19.03/10%/10%, 70%, 750nm, 2nd, 45C, down.txt','r')
lines15 = F15.readlines()
F15.close()

F16 = open('C:/Users/MEaTh/OneDrive/Desktop/Semesterarbeit/19.03/10%/10%, 70%, 750nm, 2nd, 60C, down.txt','r')
lines16 = F16.readlines()
F16.close()

F17 = open('C:/Users/MEaTh/OneDrive/Desktop/Semesterarbeit/20.03/5%/5%, 70%, 750nm, 2nd, 15C, up.txt','r')
lines17 = F17.readlines()
F17.close()

F18 = open('C:/Users/MEaTh/OneDrive/Desktop/Semesterarbeit/20.03/5%/5%, 70%, 750nm, 2nd, 30C, up.txt','r')
lines18 = F18.readlines()
F18.close()

F19 = open('C:/Users/MEaTh/OneDrive/Desktop/Semesterarbeit/20.03/5%/5%, 70%, 750nm, 2nd, 45C, up.txt','r')
lines19 = F19.readlines()
F19.close()

F20 = open('C:/Users/MEaTh/OneDrive/Desktop/Semesterarbeit/20.03/5%/5%, 70%, 750nm, 2nd, 60C, up.txt','r')
lines20 = F20.readlines()
F20.close()

F21 = open('C:/Users/MEaTh/OneDrive/Desktop/Semesterarbeit/20.03/5%/5%, 70%, 750nm, 2nd, 15C, down.txt','r')
lines21 = F21.readlines()
F21.close()

F22 = open('C:/Users/MEaTh/OneDrive/Desktop/Semesterarbeit/20.03/5%/5%, 70%, 750nm, 2nd, 30C, down.txt','r')
lines22 = F22.readlines()
F22.close()

F23 = open('C:/Users/MEaTh/OneDrive/Desktop/Semesterarbeit/20.03/5%/5%, 70%, 750nm, 2nd, 45C, down.txt','r')
lines23 = F23.readlines()
F23.close()

F24 = open('C:/Users/MEaTh/OneDrive/Desktop/Semesterarbeit/20.03/5%/5%, 70%, 750nm, 2nd, 60C, down.txt','r')
lines24 = F24.readlines()
F24.close()


"""----------Saving into arrays----------"""
    
p = 0
a = 0
b = 0
data = np.zeros([512,2,24])


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

for line in lines22:
    words = line.split("-")  
    a = words[0].split()
    data[p,:,b] = a
    p = p+1

p = 0
b = b + 1

for line in lines23:
    words = line.split("-")  
    a = words[0].split()
    data[p,:,b] = a
    p = p+1

p = 0
b = b + 1

for line in lines24:
    words = line.split("-")  
    a = words[0].split()
    data[p,:,b] = a
    p = p+1

p = 0
b = b + 1

    
"""----------Plots----------"""

"""plt.plot(data[:150,0,0],data[:150,1,0],label='15C')
plt.plot(data[:150,0,1],data[:150,1,1],label='30C')
plt.plot(data[:150,0,2],data[:150,1,2],label='45C')
plt.plot(data[:150,0,3],data[:150,1,3],label='60C')
plt.grid()
plt.xlabel('Wavelength')
plt.ylabel('Counts')
plt.title('PL spectra of 15% 1')
plt.legend()
plt.show()

plt.plot(data[:150,0,12],data[:150,1,12],label='15C')
plt.plot(data[:150,0,13],data[:150,1,13],label='30C')
plt.plot(data[:150,0,14],data[:150,1,14],label='45C')
plt.plot(data[:150,0,15],data[:150,1,15],label='60C')
plt.grid()
plt.xlabel('Wavelength')
plt.ylabel('Counts')
plt.title('PL spectra of 15% 2')
plt.legend()
plt.show()"""



data[:,:,0] = (data[:,:,4] + data[:,:,0])/2
data[:,:,1] = (data[:,:,5] + data[:,:,1])/2
data[:,:,2] = (data[:,:,6] + data[:,:,2])/2
data[:,:,3] = (data[:,:,7] + data[:,:,3])/2

data[:,:,8] = (data[:,:,12] + data[:,:,8])/2
data[:,:,9] = (data[:,:,13] + data[:,:,9])/2
data[:,:,10] = (data[:,:,14] + data[:,:,10])/2
data[:,:,11] = (data[:,:,15] + data[:,:,11])/2

data[:,:,16] = (data[:,:,20] + data[:,:,16])/2
data[:,:,17] = (data[:,:,21] + data[:,:,17])/2
data[:,:,18] = (data[:,:,22] + data[:,:,18])/2
data[:,:,19] = (data[:,:,23] + data[:,:,19])/2

plt.plot(data[:150,0,0],data[:150,1,0]/data[21,1,0],label='15C')
plt.plot(data[:150,0,1],data[:150,1,1]/data[21,1,1],label='30C')
plt.plot(data[:150,0,2],data[:150,1,2]/data[21,1,2],label='45C')
plt.plot(data[:150,0,3],data[:150,1,3]/data[21,1,3],label='60C')
plt.grid()
plt.xlabel('Wavelength')
plt.ylabel('Counts %')
plt.title('PL spectra of 15% normalised & averaged')
plt.legend()
plt.show()

plt.plot(data[:150,0,0],data[:150,1,0],label='15C')
plt.plot(data[:150,0,1],data[:150,1,1],label='30C')
plt.plot(data[:150,0,2],data[:150,1,2],label='45C')
plt.plot(data[:150,0,3],data[:150,1,3],label='60C')
plt.grid()
plt.xlabel('Wavelength')
plt.ylabel('Counts %')
plt.title('PL spectra of 15% & averaged')
plt.legend()
plt.show()

"""plt.plot(data[:150,0,12],data[:150,1,12]/data[21,1,12],label='15C')
plt.plot(data[:150,0,13],data[:150,1,13]/data[21,1,13],label='30C')
plt.plot(data[:150,0,14],data[:150,1,14]/data[21,1,14],label='45C')
plt.plot(data[:150,0,15],data[:150,1,15]/data[21,1,15],label='60C')
plt.grid()
plt.xlabel('Wavelength')
plt.ylabel('Counts %')
plt.title('PL spectra of 15% normalised 2')
plt.legend()
plt.show()

plt.plot(data[:150,0,4],data[:150,1,4],label='15C')
plt.plot(data[:150,0,5],data[:150,1,5],label='30C')
plt.plot(data[:150,0,6],data[:150,1,6],label='45C')
plt.plot(data[:150,0,7],data[:150,1,7],label='60C')
plt.grid()
plt.xlabel('Wavelength')
plt.ylabel('Counts %')
plt.title('PL spectra of 10%')
plt.legend()
plt.show()

plt.plot(data[:150,0,4],data[:150,1,4]/data[21,1,4],label='15C')
plt.plot(data[:150,0,5],data[:150,1,5]/data[21,1,5],label='30C')
plt.plot(data[:150,0,6],data[:150,1,6]/data[21,1,6],label='45C')
plt.plot(data[:150,0,7],data[:150,1,7]/data[21,1,7],label='60C')
plt.grid()
plt.xlabel('Wavelength')
plt.ylabel('Counts %')
plt.title('PL spectra of 10% normalised')
plt.legend()
plt.show()

plt.plot(data[:150,0,8],data[:150,1,8],label='15C')
plt.plot(data[:150,0,9],data[:150,1,9],label='30C')
plt.plot(data[:150,0,10],data[:150,1,10],label='45C')
plt.plot(data[:150,0,11],data[:150,1,11],label='60C')
plt.grid()
plt.xlabel('Wavelength')
plt.ylabel('Counts %')
plt.title('PL spectra of 5%')
plt.legend()
plt.show()"""

plt.plot(data[:150,0,8],data[:150,1,8]/data[21,1,8],label='15C')
plt.plot(data[:150,0,9],data[:150,1,9]/data[21,1,9],label='30C')
plt.plot(data[:150,0,10],data[:150,1,10]/data[21,1,10],label='45C')
plt.plot(data[:150,0,11],data[:150,1,11]/data[21,1,11],label='60C')
plt.grid()
plt.xlabel('Wavelength')
plt.ylabel('Counts %')
plt.title('PL spectra of 10% normalised and averaged')
plt.legend()
plt.show()

plt.plot(data[:150,0,8],data[:150,1,8],label='15C')
plt.plot(data[:150,0,9],data[:150,1,9],label='30C')
plt.plot(data[:150,0,10],data[:150,1,10],label='45C')
plt.plot(data[:150,0,11],data[:150,1,11],label='60C')
plt.grid()
plt.xlabel('Wavelength')
plt.ylabel('Counts %')
plt.title('PL spectra of 10% and averaged')
plt.legend()
plt.show()

plt.plot(data[:150,0,16],data[:150,1,16]/data[21,1,16],label='15C')
plt.plot(data[:150,0,17],data[:150,1,17]/data[21,1,17],label='30C')
plt.plot(data[:150,0,18],data[:150,1,18]/data[21,1,18],label='45C')
plt.plot(data[:150,0,19],data[:150,1,19]/data[21,1,19],label='60C')
plt.grid()
plt.xlabel('Wavelength')
plt.ylabel('Counts %')
plt.title('PL spectra of 5% normalised and averaged')
plt.legend()
plt.show()

plt.plot(data[:150,0,16],data[:150,1,16],label='15C')
plt.plot(data[:150,0,17],data[:150,1,17],label='30C')
plt.plot(data[:150,0,18],data[:150,1,18],label='45C')
plt.plot(data[:150,0,19],data[:150,1,19],label='60C')
plt.grid()
plt.xlabel('Wavelength')
plt.ylabel('Counts')
plt.title('PL spectra of 5% and averaged')
plt.legend()
plt.show()



"""----------Data Analysis----------"""
"21-30-71"

x0 = 930
y0 = 1010
a = -0.01
b = -0.01

def Gauss1(x):
    return np.exp(a*(x-x0)**2)

def Gauss2(y):
    return np.exp(b*(y-y0)**2)

plt.plot(data[:150,0,0],Gauss1(data[:150,0,0]))
plt.plot(data[:150,0,0],Gauss2(data[:150,0,0]))
plt.show()

data11 = data[:,1,0]*Gauss1(data[:,0,0])
data12 = data[:,1,1]*Gauss1(data[:,0,1])
data13 = data[:,1,2]*Gauss1(data[:,0,2])
data14 = data[:,1,3]*Gauss1(data[:,0,3])
data21 = data[:,1,0]*Gauss2(data[:,0,0])
data22 = data[:,1,1]*Gauss2(data[:,0,1])
data23 = data[:,1,2]*Gauss2(data[:,0,2])
data24 = data[:,1,3]*Gauss2(data[:,0,3])

plt.plot(data[:150,0,0],data11[:150])
plt.plot(data[:150,0,0],data12[:150])
plt.plot(data[:150,0,0],data13[:150])
plt.plot(data[:150,0,0],data14[:150])
plt.plot(data[:150,0,0],data21[:150])
plt.plot(data[:150,0,0],data22[:150])
plt.plot(data[:150,0,0],data23[:150])
plt.plot(data[:150,0,0],data24[:150])
plt.title('Multiplicated with Gaussian profile 15%')
plt.ylabel('Counts')
plt.xlabel('Wavelength')
plt.show()

plt.plot(data[:150,0,0],data11[:150]/np.max(data11[:50]))
plt.plot(data[:150,0,0],data12[:150]/np.max(data12[:50]))
plt.plot(data[:150,0,0],data13[:150]/np.max(data13[:50]))
plt.plot(data[:150,0,0],data14[:150]/np.max(data14[:50]))
plt.plot(data[:150,0,0],data21[:150]/np.max(data11[:50]))
plt.plot(data[:150,0,0],data22[:150]/np.max(data12[:50]))
plt.plot(data[:150,0,0],data23[:150]/np.max(data13[:50]))
plt.plot(data[:150,0,0],data24[:150]/np.max(data14[:50]))
plt.title('Multiplicated with Gaussian profile, normalised 15%')
plt.ylabel('Counts')
plt.xlabel('Wavelength')
plt.show()

data31 = data[:,1,8]*Gauss1(data[:,0,8])
data32 = data[:,1,9]*Gauss1(data[:,0,9])
data33 = data[:,1,10]*Gauss1(data[:,0,10])
data34 = data[:,1,11]*Gauss1(data[:,0,11])
data41 = data[:,1,8]*Gauss2(data[:,0,8])
data42 = data[:,1,9]*Gauss2(data[:,0,9])
data43 = data[:,1,10]*Gauss2(data[:,0,10])
data44 = data[:,1,11]*Gauss2(data[:,0,11])

plt.plot(data[:150,0,4],data31[:150])
plt.plot(data[:150,0,4],data32[:150])
plt.plot(data[:150,0,4],data33[:150])
plt.plot(data[:150,0,4],data34[:150])
plt.plot(data[:150,0,4],data41[:150])
plt.plot(data[:150,0,4],data42[:150])
plt.plot(data[:150,0,4],data43[:150])
plt.plot(data[:150,0,4],data44[:150])
plt.title('Multiplicated with Gaussian profile 10%')
plt.ylabel('Counts')
plt.xlabel('Wavelength')
plt.show()

plt.plot(data[:150,0,4],data31[:150]/np.max(data31[:50]))
plt.plot(data[:150,0,4],data32[:150]/np.max(data32[:50]))
plt.plot(data[:150,0,4],data33[:150]/np.max(data33[:50]))
plt.plot(data[:150,0,4],data34[:150]/np.max(data34[:50]))
plt.plot(data[:150,0,4],data41[:150]/np.max(data31[:50]))
plt.plot(data[:150,0,4],data42[:150]/np.max(data32[:50]))
plt.plot(data[:150,0,4],data43[:150]/np.max(data33[:50]))
plt.plot(data[:150,0,4],data44[:150]/np.max(data34[:50]))
plt.title('Multiplicated with Gaussian profile, normalised 10%')
plt.ylabel('Counts')
plt.xlabel('Wavelength')
plt.show()

data51 = data[:,1,16]*Gauss1(data[:,0,16])
data52 = data[:,1,17]*Gauss1(data[:,0,17])
data53 = data[:,1,18]*Gauss1(data[:,0,18])
data54 = data[:,1,19]*Gauss1(data[:,0,19])
data61 = data[:,1,16]*Gauss2(data[:,0,16])
data62 = data[:,1,17]*Gauss2(data[:,0,17])
data63 = data[:,1,18]*Gauss2(data[:,0,18])
data64 = data[:,1,19]*Gauss2(data[:,0,19])

plt.plot(data[:150,0,4],data51[:150])
plt.plot(data[:150,0,4],data52[:150])
plt.plot(data[:150,0,4],data53[:150])
plt.plot(data[:150,0,4],data54[:150])
plt.plot(data[:150,0,4],data61[:150])
plt.plot(data[:150,0,4],data62[:150])
plt.plot(data[:150,0,4],data63[:150])
plt.plot(data[:150,0,4],data64[:150])
plt.title('Multiplicated with Gaussian profile 5%')
plt.ylabel('Counts')
plt.xlabel('Wavelength')
plt.show()

plt.plot(data[:150,0,4],data51[:150]/np.max(data51[:50]))
plt.plot(data[:150,0,4],data52[:150]/np.max(data52[:50]))
plt.plot(data[:150,0,4],data53[:150]/np.max(data53[:50]))
plt.plot(data[:150,0,4],data54[:150]/np.max(data54[:50]))
plt.plot(data[:150,0,4],data61[:150]/np.max(data51[:50]))
plt.plot(data[:150,0,4],data62[:150]/np.max(data52[:50]))
plt.plot(data[:150,0,4],data63[:150]/np.max(data53[:50]))
plt.plot(data[:150,0,4],data64[:150]/np.max(data54[:50]))
plt.title('Multiplicated with Gaussian profile, normalised 5%')
plt.ylabel('Counts')
plt.xlabel('Wavelength')
plt.show()


T = np.array([15,30,45,60])
max11 = np.array([np.max(data11[:50]),np.max(data12[:50]),np.max(data13[:50]),np.max(data14[:50])])
max12 = np.array([np.max(data21[50:]),np.max(data22[50:]),np.max(data23[50:]),np.max(data24[50:])])
max21 = np.array([np.max(data31[:50]),np.max(data32[:50]),np.max(data33[:50]),np.max(data34[:50])])
max22 = np.array([np.max(data41[50:]),np.max(data42[50:]),np.max(data43[50:]),np.max(data44[50:])])
max31 = np.array([np.max(data51[:50]),np.max(data52[:50]),np.max(data53[:50]),np.max(data54[:50])])
max32 = np.array([np.max(data61[50:]),np.max(data62[50:]),np.max(data63[50:]),np.max(data64[50:])])

plt.plot(T,max11,':',label='15%')
plt.plot(T,max12,':',label='15%')


plt.plot(T,max21,':',label='10%')
plt.plot(T,max22,':',label='10%')

plt.plot(T,max31,':',label='5%')
plt.plot(T,max32,':',label='5%')

plt.legend()
plt.show()


print(data)
