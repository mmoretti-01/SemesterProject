#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 15:47:07 2024

@author: main
"""

import uncertainties 
import matplotlib.pyplot as plt
import numpy as np
from uncertainties import unumpy
from uncertainties import ufloat

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

F1 = open('/Users/main/Desktop/Semesterarbeit/12.03/15%, 70%, 750nm, 15C.txt','r')
lines1 = F1.readlines()
F1.close()


F2 = open('/Users/main/Desktop/Semesterarbeit/12.03/15%, 70%, 750nm, 30C.txt','r')
lines2 = F2.readlines()
F2.close()

F3 = open('/Users/main/Desktop/Semesterarbeit/12.03/15%, 70%, 750nm, 45C.txt','r')
lines3 = F3.readlines()
F3.close()

F4 = open('/Users/main/Desktop/Semesterarbeit/12.03/15%, 70%, 750nm, 60C.txt','r')
lines4 = F4.readlines()
F4.close()

F5 = open('/Users/main/Desktop/Semesterarbeit/13.03/10%, 70%, 750nm, 15C.txt','r')
lines5 = F5.readlines()
F5.close()

F6 = open('/Users/main/Desktop/Semesterarbeit/13.03/10%, 70%, 750nm, 30C.txt','r')
lines6 = F6.readlines()
F6.close()

F7 = open('/Users/main/Desktop/Semesterarbeit/13.03/10%, 70%, 750nm, 45C.txt','r')
lines7 = F7.readlines()
F7.close()

F8 = open('/Users/main/Desktop/Semesterarbeit/13.03/10%, 70%, 750nm, 60C.txt','r')
lines8 = F8.readlines()
F8.close()

F9 = open('/Users/main/Desktop/Semesterarbeit/13.03/5%, 70%, 750nm, 15C.txt','r')
lines9 = F9.readlines()
F9.close()

F10 = open('/Users/main/Desktop/Semesterarbeit/13.03/5%, 70%, 750nm, 30C.txt','r')
lines10 = F10.readlines()
F10.close()

F11 = open('/Users/main/Desktop/Semesterarbeit/13.03/5%, 70%, 750nm, 45C.txt','r')
lines11 = F11.readlines()
F11.close()

F12 = open('/Users/main/Desktop/Semesterarbeit/13.03/5%, 70%, 750nm, 60C.txt','r')
lines12 = F12.readlines()
F12.close()

F13 = open('/Users/main/Desktop/Semesterarbeit/15.03/15%, 70%, 750nm, 15C.txt','r')
lines13 = F13.readlines()
F13.close()

F14 = open('/Users/main/Desktop/Semesterarbeit/15.03/15%, 70%, 750nm, 30C.txt','r')
lines14 = F14.readlines()
F14.close()

F15 = open('/Users/main/Desktop/Semesterarbeit/15.03/15%, 70%, 750nm, 45C.txt','r')
lines15 = F15.readlines()
F15.close()

F16 = open('/Users/main/Desktop/Semesterarbeit/15.03/15%, 70%, 750nm, 60C.txt','r')
lines16 = F16.readlines()
F16.close()

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

plt.plot(data[:150,0,0],data[:150,1,0]/data[21,1,0],label='15C')
plt.plot(data[:150,0,1],data[:150,1,1]/data[21,1,1],label='30C')
plt.plot(data[:150,0,2],data[:150,1,2]/data[21,1,2],label='45C')
plt.plot(data[:150,0,3],data[:150,1,3]/data[21,1,3],label='60C')
plt.grid()
plt.xlabel('Wavelength')
plt.ylabel('Counts %')
plt.title('PL spectra of 15% normalised 1')
plt.legend()
plt.show()

plt.plot(data[:150,0,12],data[:150,1,12]/data[21,1,12],label='15C')
plt.plot(data[:150,0,13],data[:150,1,13]/data[21,1,13],label='30C')
plt.plot(data[:150,0,14],data[:150,1,14]/data[21,1,14],label='45C')
plt.plot(data[:150,0,15],data[:150,1,15]/data[21,1,15],label='60C')
plt.grid()
plt.xlabel('Wavelength')
plt.ylabel('Counts %')
plt.title('PL spectra of 15% normalised 2')
plt.legend()
plt.show()

"""plt.plot(data[:150,0,4],data[:150,1,4],label='15C')
plt.plot(data[:150,0,5],data[:150,1,5],label='30C')
plt.plot(data[:150,0,6],data[:150,1,6],label='45C')
plt.plot(data[:150,0,7],data[:150,1,7],label='60C')
plt.grid()
plt.xlabel('Wavelength')
plt.ylabel('Counts %')
plt.title('PL spectra of 10%')
plt.legend()
plt.show()"""

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

"""plt.plot(data[:150,0,8],data[:150,1,8],label='15C')
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
plt.title('PL spectra of 5% normalised')
plt.legend()
plt.show()

plt.plot(data[:150,0,12],data[:150,1,12]/data[21,1,12],label='15C')
plt.plot(data[:150,0,4],data[:150,1,4]/data[21,1,4],label='15C')
plt.plot(data[:150,0,8],data[:150,1,8]/data[21,1,8],label='15C')
plt.grid()
plt.xlabel('Wavelength')
plt.ylabel('Counts %')
plt.title('Comparison')
plt.legend()
plt.show()

print(data[71,1,0])
print(data[71,1,4])
print(data[71,1,8])

"""----------Data Analysis----------"""
"21---71"
'Additional change per Temperature at 1010'
diff1 = data[71,:,0] - data[71,:,1]
diff2 = data[71,:,1] - data[71,:,2]
diff3 = data[71,:,2] - data[71,:,3]
print(diff1[1],diff2[1],diff3[1])
print(diff1[1]/15,diff2[1]/15,diff3[1]/15)


