# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 13:45:20 2024

@author: MEaTh
"""


import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
from scipy.optimize import curve_fit
import os


"""----------Initialization----------"""

#Nr soll gleich der Anzahl an Datensätzen sein, die du auslesen willst. Im Beispiel unten also genau 7.
Nr = 21

Lines = [0]*(Nr)
F = []
Doc = []
#Diese Funktion liest den angegebenen Ordner aus, ordnet die Dateien alphabetisch und hängt sie in Doc an.
def Ordner_auslesen(Ordner):
    Dateien = os.listdir(Ordner)
    Dateien.sort()
    DiO = len(Dateien)
    for j in range(DiO):
        Doc.append(open(Ordner + Dateien[j],'r'))
    return 0

#Du kannst mit dem Befehl in den nächsten Zeilen bestimmte Ordner auswählen und diese alphabetisch sortieren.
#Anschließend werden die Dateien im Ordner ausgelehsen und in der Liste Doc vermerkt.
Ordner = 'C:/Users/MEaTh/OneDrive/Desktop/Semesterarbeit/30.05/'  #high
Ordner_auslesen(Ordner)
    
Ordner ='C:/Users/MEaTh/OneDrive/Desktop/Semesterarbeit/28.05/'   #med
Ordner_auslesen(Ordner)

Ordner ='C:/Users/MEaTh/OneDrive/Desktop/Semesterarbeit/29.05/'   #low
Ordner_auslesen(Ordner)

#Wenn du zusätzliche Datensätze verwenden willst kannst du diese einfach mit Doc.append(open(....)) anhängen.
#Wenn du zudem Nr anpasst, dann macht das Skript den rest alleine.

#Um die Daten zu speichern habe ich hier einen Array "data" erstellt. Der Array hat die Struktur 512*2*Nr. Dabei gibt data[:,0,a] die Wellenlängen und data[:,1,a] die dazugehörigen Counts
#Die restlichen Funktionen bauen auf der Form von "data" auf, versuche diesen Array also zu verstehen.
data = np.zeros([512,2,Nr])

for i in range(0,Nr):
    a = Doc[i].readlines()
    Lines[i] = a
    
    
for p in range(0,Nr):
    b = 0
    for line in Lines[p]:
        words = line.split("-")  
        a = words[0].split()
        data[b,:,p] = a
        b = b + 1
        
"""----------Functions-----------"""

#Die ersten 3 Funktionen beruhen auf np.polyfit und bestimmen polynomiale Fits und deren Ableitungen
#Willst du einen polynomialen Fit erstellen so kannst du einfach: p = np.polyfit(x,y,deg = ...) und jenes p für diese Funktion benutzen
#Diese Funktion erstellt einen fit mit polynom von ordnung deg.
def FIR(T,p):
    return np.polyval(p,T)

#Dies gibt die Ableitung des fits, by default habe ich es auf einen quadratischen fit eingestellt
def dFIR_lin(T,p):
    f = p[0]*T**0
    return f

#Mit dieser Funktion kannst du die Relative Sensitivität ausgehend von deinem Fit bestimmen
def dFIR_R_lin(T,p):
    f = dFIR_lin(T,p)
    return np.abs(f/FIR(T,p))

def dFIR_quad(T,p):
    f = 2*p[0]*T + p[1]
    return f

def dFIR_R_quad(T,p):
    f = dFIR_quad(T,p)
    return np.abs(f/FIR(T,p))

#Die folgenden 4 Funktionen dienen dazu logarithmische fits zu erstellen und deren Ableitungen zu berechnen.
#Das vorgehen ist das selbe, nur dass du statt p, a&b bestimmen musst dies kannst du mit den folgenden 2 Zeilen:
#params, covariance = sp.optimize.curve_fit(log_func, x, y)
#a, b = params
def log_func(x, a, b):
    return a * np.log(x) + b

def sig_func(x, a, b, c, d):
    return a / (1 + np.exp(-c*(x-b))) + d

def dFIR_sig(x,a,b,c,d):
    return a*c*np.exp(-c*(x-b))/(1+np.exp(-c*(x-b)))**(2)

def dFIR_R_sig(x,a,b,c,d):
    f = dFIR_sig(x,a,b,c,d)
    return np.abs(f/(sig_func(x,a,b,c,d)))

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

#Hiermit kannst du, gegeben die Counts des Peak1 und Counts des Peak 2, den Fehler auf die Ratio der beiden bestimmen.
def err_R(I1,I2):
    err1 = np.sqrt(I1)
    err2 = np.sqrt(I2)
    err = np.sqrt((err1/I2)**2 + (I1*err2/(I2**2))**2)
    return err

#Dies war eine Testfunktion um die Temperatur zu bestimmen, wenn man eine Ratio gegeben hat. Die funktion basiert auf fits mit np.polyfit
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

def Temp_log(R,a,b):
    T = np.arange(15,60,0.05)
    k = 10
    P = 0
    for T_1 in T:
        s = np.abs(R-FIR_log(T_1,a,b))
        if s<k :
            k = s
            P = T_1
        else:
            k = k
    return P

def logarithmic_fit(A,Peak1,Peak2,Temperature):
    Ratios = np.zeros(len(A))
    T = np.arange(14,61,0.01)
    i = 0
    for a in A:
        Ratios[i] = data[Peak1,1,a]/data[Peak2,1,a]
        i = i + 1
    params, covariance = sp.optimize.curve_fit(log_func, Temperature, Ratios)
    a, b = params
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

def quadratic_fit(A,Peak1,Peak2,Temperature):
    Ratios = np.zeros(len(A))
    T = np.arange(14,61,0.01)
    i = 0
    for a in A:
        Ratios[i] = data[Peak1,1,a]/data[Peak2,1,a]
        i = i + 1
    p = np.polyfit(Temperature,Ratios,deg = 2)
    return p[0] * T **2 + p[1]*T + p[2]

def quadratic_fit_coeff(A,Peak1,Peak2,Temperature):
    Ratios = np.zeros(len(A))
    T = np.arange(14,61,0.01)
    i = 0
    for a in A:
        Ratios[i] = data[Peak1,1,a]/data[Peak2,1,a]
        i = i + 1
    p = np.polyfit(Temperature,Ratios,deg = 2)
    return p

def quadratic_fit_full(A,Peak1,Peak2,Temperature):
    Ratios = np.zeros(len(A))
    T = np.arange(14,61,0.01)
    i = 0
    for a in A:
        Ratios[i] = data[Peak1,1,a]/data[Peak2,1,a]
        i = i + 1
    p = np.polyfit(Temperature,Ratios,deg = 2,cov=True)
    return p

def Ratios_func(A,Peak1,Peak2):
    Ratios = np.zeros(len(A))
    T = np.arange(14,61,0.01)
    i = 0
    for a in A:
        Ratios[i] = data[Peak1,1,a]/data[Peak2,1,a]
        i = i + 1
    return Ratios

"""----------DIY----------"""

SIZE_DEFAULT = 14
SIZE_LARGE = 16
plt.rc("font", weight="normal")  # controls default font
plt.rc("font", size=SIZE_DEFAULT)  # controls default text sizes
plt.rc("axes", titlesize=SIZE_LARGE)  # fontsize of the axes title
plt.rc("axes", labelsize=SIZE_LARGE)  # fontsize of the x and y labels
plt.rc("xtick", labelsize=SIZE_DEFAULT)  # fontsize of the tick labels
plt.rc("ytick", labelsize=SIZE_DEFAULT)  # fontsize of the tick labels


fig, ax = plt.subplots(figsize=(6, 5))

ax.plot(data[:,0,14],data[:,1,14]/data[23,1,14]*100, color='#08407E')
ax.text(data[450,0,0]-510, 100, '$15\u00b0C$', color='#08407E',fontweight="bold",horizontalalignment="left",verticalalignment="center",)
"""
ax.plot(data[:,0,15],data[:,1,15]/data[23,1,15]*100,label='Sr', color ='#3395AB')
ax.text(data[450,0,1]-510, 92, '$25\u00b0C$', color='#3395AB',fontweight="bold",horizontalalignment="left",verticalalignment="center",)
ax.plot(data[:,0,16],data[:,1,16]/data[23,1,16]*100,label='Ba', color='#818F42')
ax.text(data[450,0,2]-510, 84, '$30\u00b0C$', color='#818F42',fontweight="bold",horizontalalignment="left",verticalalignment="center",)
ax.plot(data[:,0,17],data[:,1,17]/data[23,1,17]*100, color='#A1AB71')
ax.text(data[450,0,3]-510, 76, '$35\u00b0C$', color='#A1AB71',fontweight="bold",horizontalalignment="left",verticalalignment="center",)
ax.plot(data[:,0,18],data[:,1,18]/data[23,1,18]*100,label='Sr', color ='#BBA471')
ax.text(data[450,0,4]-510, 68, '$40\u00b0C$', color='#BBA471',fontweight="bold",horizontalalignment="left",verticalalignment="center",)
ax.plot(data[:,0,19],data[:,1,19]/data[23,1,19]*100,label='Ba', color='#D48681')
ax.text(data[450,0,5]-510, 60, '$50\u00b0C$', color='#D48681',fontweight="bold",horizontalalignment="left",verticalalignment="center",)
"""
ax.plot(data[:,0,20],data[:,1,20]/data[23,1,20]*100,label='Ba', color='#96272D')
ax.text(data[450,0,6]-510, 92, '$60\u00b0C$', color='#96272D',fontweight="bold",horizontalalignment="left",verticalalignment="center",)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.spines["top"].set_visible(False)
ax.grid()
ax.set_xlabel('Wavelength in nm')
ax.set_ylabel('Relative Intensity (%)')
plt.savefig("great.png", dpi=300)
plt.show()


""" 20mg +- 1m;  20ml +- 1ml, 20ml +- 1ml"""

T = np.arange(14,61,0.01)
T_err = [1,1,1,1,1,1,1]
y_err_high = err_R(data[71,1,7:14],data[379,1,7:14])
y_err_medium = err_R(data[71,1,0:7],data[379,1,0:7])
y_err_low = err_R(data[71,1,14:21],data[379,1,14:21])
Temperature = [15,25,30,35,40,50,60]

fig, ax = plt.subplots(figsize=(6, 5))
Temperature = [15,25,30,35,40,50,60]
A = np.arange(14,21)
ax.plot(T,logarithmic_fit(A,72,379,Temperature),label='Ba', color='#00596D', linestyle = '--')
plt.errorbar(Temperature, Ratios_func(A,72,379), yerr = y_err_low, xerr = T_err, linestyle = '', color = 'black')
ax.text(40, 60.66, '$logarithmic-fit$', color='#00596D',fontweight="bold",horizontalalignment="left",verticalalignment="center",)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.spines["top"].set_visible(False)
ax.grid()
ax.set_xlabel('Temperature in $\u00b0C$')
ax.set_ylabel('Peak Ratios') 
plt.savefig("great.png", dpi=300)
plt.show()


fig, ax = plt.subplots(figsize=(6, 5))
Temperature = [15,25,30,35,40,50,60]
A = np.arange(14,21)
ax.plot(T,quadratic_fit(A,72,379,Temperature),label='Ba', color='#00596D', linestyle = '--')
plt.errorbar(Temperature, Ratios_func(A,72,379), yerr = y_err_low, xerr = T_err, linestyle = '', color = 'black')
ax.text(40, 60.75, '$quadratic-fit$', color='#00596D',fontweight="bold",horizontalalignment="left",verticalalignment="center",)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.spines["top"].set_visible(False)
ax.grid()
ax.set_xlabel('Temperature in $\u00b0C$')
ax.set_ylabel('Peak Ratios') 
plt.savefig("great.png", dpi=300)
plt.show()

y_err_high = err_R(data[379,1,7:14],data[71,1,7:14])
y_err_medium = err_R(data[379,1,0:7],data[71,1,0:7])
y_err_low = err_R(data[379,1,14:21],data[71,1,14:21])



fig, ax = plt.subplots(figsize=(6, 5))
A = np.arange(14,21)
ax.plot(T,quadratic_fit(A,379,72,Temperature),label='Ba', color='#00596D', linestyle = '--')
plt.errorbar(Temperature, Ratios_func(A,379,72), yerr = y_err_high, xerr = T_err, linestyle = '', color = 'black')
ax.text(40, 0.01, '$linear-fit$', color='#00596D',fontweight="bold",horizontalalignment="left",verticalalignment="center",)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.spines["top"].set_visible(False)
ax.grid()
ax.set_xlabel('Temperature in $\u00b0C$')
ax.set_ylabel('Peak Ratios')

plt.show()

fig, ax = plt.subplots(figsize=(6, 5))

A = np.arange(14,21)
a,b = logarithmic_coef(A,72,399,Temperature)
ax.plot(T,dFIR_R_log(T,a,b)*100, color='#00596D', linestyle = '--')
ax.text(40, 3.21, '$logarithmic-fit$', color='#00596D',fontweight="bold",horizontalalignment="left",verticalalignment="center",)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.spines["top"].set_visible(False)
ax.grid()
ax.set_xlabel('Temperature in $\u00b0C$')
ax.set_ylabel('Relative Sensitivity in %$K^{-1}$') 

plt.show()

fig, ax = plt.subplots(figsize=(6, 5))

A = np.arange(14,21)
p = quadratic_fit_coeff(A, 72, 399, Temperature)
ax.plot(T,dFIR_R_quad(T,p)*100, color='#00596D', linestyle = '--')
ax.text(45, 3.05, '$quadratic-fit$', color='#00596D',fontweight="bold",horizontalalignment="left",verticalalignment="center",)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.spines["top"].set_visible(False)
ax.grid()
ax.set_xlabel('Temperature in $\u00b0C$')
ax.set_ylabel('Relative Sensitivity in %$K^{-1}$') 
plt.savefig("great.png", dpi=300)
plt.show()

fig, ax = plt.subplots(figsize=(7, 5))

A = np.arange(14,21)
p = quadratic_fit_coeff(A, 399, 72, Temperature)
ax.plot(T,FIR(T,p), color='#00596D', linestyle = '--')
plt.errorbar(Temperature, Ratios_func(A,399,72), yerr = y_err_high, xerr = T_err, linestyle = '', color = 'black')
ax.text(45, 0.1015, '$quadratic-fit$', color='#00596D',fontweight="bold",horizontalalignment="left",verticalalignment="center",)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.spines["top"].set_visible(False)
ax.grid()
ax.set_xlabel('Temperature in $\u00b0C$')
ax.set_ylabel('Peak Ratios') 
plt.savefig("great.png", dpi=300)
plt.show()

fig, ax = plt.subplots(figsize=(6, 5))

A = np.arange(14,21)
p = quadratic_fit_coeff(A, 399, 72, Temperature)
ax.plot(T,dFIR_R_quad(T,p)*100, color='#00596D', linestyle = '--')
ax.text(45, 3.43, '$quadratic-fit$', color='#00596D',fontweight="bold",horizontalalignment="left",verticalalignment="center",)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.spines["top"].set_visible(False)
ax.grid()
ax.set_xlabel('Temperature in $\u00b0C$')
ax.set_ylabel('Relative Sensitivity in %$K^{-1}$') 
plt.show()

print(max(dFIR_R_quad(T,p)*100))
print(dFIR_R_quad(15,p)*100)

p = quadratic_fit_full(A, 399, 72, Temperature)
del_a = p[1][0,0]
del_b = p[1][1,1]
del_c = p[1][2,2]


print(del_a,del_b,del_c)
print(p[0][0],p[0][1],p[0][2])



fig, ax = plt.subplots(figsize=(6, 5))

A = np.arange(14,21)
p = quadratic_fit_coeff(A, 72, 379, Temperature)
ax.plot(T,np.abs(dFIR_quad(T,p)), color='#00596D', linestyle = '--')
ax.text(40, 1.6, '$logarithmic-fit$', color='#00596D',fontweight="bold",horizontalalignment="left",verticalalignment="center",)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.spines["top"].set_visible(False)
ax.grid()
ax.set_xlabel('Temperature in $\u00b0C$')
ax.set_ylabel('Absolute Sensitivity in $K^{-1}$') 

plt.show()


x0 = 1015
y0 = 1537
a = 15
b = 15

def square1(y):
    x = np.copy(y)
    for i in range(0,len(x)):
        if x[i] < x0-a:
            x[i] = 0
        if x[i] > x0 + a: 
            x[i] = 0
        if x[i] >= x0-a and x[i] <= x0+a:
            x[i] = 1
    return x


def square2(x):
    y = np.copy(x)
    for i in range(0,len(y)):
        if y[i] < y0-a:
            y[i] = 0
        if y[i] > y0 + a:
            y[i] = 0
        if y[i] >= y0-a and y[i] <= y0+a:
            y[i] = 1
    return y

def Ratios_func_s(A,Peak1,Peak2):
    Ratios = np.zeros(len(A))
    T = np.arange(14,61,0.01)
    i = 0
    for a in A:
        Ratios[i] = sum(data_s[(Peak1)-25:(Peak1)+25,1,a]/data_s[(Peak2)-25:(Peak2)+25,1,a])
        i = i + 1
    return Ratios

def sum_ratios(A,Peak1,Peak2):
    Ratios = np.zeros(len(A))
    T = np.arange(14,61,0.01)
    i = 0
    r = 0
    for a in A:
        r = 0
        for j in range (0,18):
            r = r + data_s[Peak1-9+j,1,a]/data_s[(Peak2)-9+j,1,a]
        Ratios[i] = r
        i = i + 1
    return Ratios/18

def sum_err(I1,I2):
    a = 0
    b = 0
    err = np.zeros(18)
    for i in range(18):
        a = np.sqrt(I1[i])
        b = np.sqrt(I2[i])
        err[i] = (a/I2[i])**2 + (I1[i]*b/(I2[i]**2))**2
    error = np.sqrt(sum(err))
    return error/18

data_s = np.copy(data)

for i in range(14,21):
    data_s[:150,1,i] = data[:150,1,i]*square1(data[:150,0,0])
    
for i in range(14,21):
    data_s[150:,1,i] = data[150:,1,i]*square2(data[150:,0,0])

fig, ax = plt.subplots(figsize=(6, 5))

ax.plot(data_s[:,0,14],data_s[:,1,14]/data[23,1,14]*100, color='#08407E')
ax.text(data[450,0,0]-510, 100, '$15\u00b0C$', color='#08407E',fontweight="bold",horizontalalignment="left",verticalalignment="center",)
ax.plot(data_s[:,0,15],data_s[:,1,15]/data[23,1,15]*100,label='Sr', color ='#3395AB')
ax.text(data[450,0,1]-510, 92, '$25\u00b0C$', color='#3395AB',fontweight="bold",horizontalalignment="left",verticalalignment="center",)
ax.plot(data_s[:,0,16],data_s[:,1,16]/data[23,1,16]*100,label='Ba', color='#818F42')
ax.text(data[450,0,2]-510, 84, '$30\u00b0C$', color='#818F42',fontweight="bold",horizontalalignment="left",verticalalignment="center",)
ax.plot(data_s[:,0,17],data_s[:,1,17]/data[23,1,17]*100, color='#A1AB71')
ax.text(data[450,0,3]-510, 76, '$35\u00b0C$', color='#A1AB71',fontweight="bold",horizontalalignment="left",verticalalignment="center",)
ax.plot(data_s[:,0,18],data_s[:,1,18]/data[23,1,18]*100,label='Sr', color ='#BBA471')
ax.text(data[450,0,4]-510, 68, '$40\u00b0C$', color='#BBA471',fontweight="bold",horizontalalignment="left",verticalalignment="center",)
ax.plot(data_s[:,0,19],data_s[:,1,19]/data[23,1,19]*100,label='Ba', color='#D48681')
ax.text(data[450,0,5]-510, 60, '$50\u00b0C$', color='#D48681',fontweight="bold",horizontalalignment="left",verticalalignment="center",)
ax.plot(data_s[:,0,20],data_s[:,1,20]/data[23,1,20]*100,label='Ba', color='#96272D')
ax.text(data[450,0,6]-510, 52, '$60\u00b0C$', color='#96272D',fontweight="bold",horizontalalignment="left",verticalalignment="center",)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.spines["top"].set_visible(False)
ax.grid()
ax.set_xlabel('Wavelength in nm')
ax.set_ylabel('Relative Intensity (%)')
plt.savefig("great.png", dpi=300)
plt.show()

T_err = [1,1,1,1,1,1,1]
y_err = np.zeros(7)
for i in range(7):
    y_err[i] = sum_err(data_s[72-9:72+9,1,14+i],data_s[399-9:399+9,1,14+i])



fig, ax = plt.subplots(figsize=(7, 5))
Temperature = [15,25,30,35,40,50,60]
A = np.arange(14,21)
p0 = [max(sum_ratios(A,72,399)), np.median(Temperature),1,min(sum_ratios(A,72,399))]
params, covariance = sp.optimize.curve_fit(log_func, Temperature, sum_ratios(A,72,399))
a, b = params
p = np.polyfit(Temperature,sum_ratios(A,72,399),deg = 2)
ax.plot(T,np.polyval(p,T),label='Ba', color='#00596D', linestyle = '--')
plt.errorbar(Temperature, sum_ratios(A,72,399), yerr = y_err, xerr = T_err, linestyle = '', color = 'black')
ax.text(40,25.2, '$quadratic-fit$', color='#00596D',fontweight="bold",horizontalalignment="left",verticalalignment="center",)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.spines["top"].set_visible(False)
ax.grid()
ax.set_xlabel('Temperature in $\u00b0C$')
ax.set_ylabel('Peak Ratios') 

plt.show()

fig, ax = plt.subplots(figsize=(7, 5))

A = np.arange(14,21)
p = np.polyfit(Temperature,sum_ratios(A, 72, 399), deg=2)
ax.plot(T,dFIR_R_quad(T,p)*100, color='#00596D', linestyle = '--')
ax.text(45, 3.83, '$quadratic-fit$', color='#00596D',fontweight="bold",horizontalalignment="left",verticalalignment="center",)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.spines["top"].set_visible(False)
ax.grid()
ax.set_xlabel('Temperature in $\u00b0C$')
ax.set_ylabel('Relative Sensitivity in %$K^{-1}$') 

plt.show()

fig, ax = plt.subplots(figsize=(7, 5))

A = np.arange(14,21)
p = np.polyfit(Temperature,sum_ratios(A, 399, 72), deg=2)
ax.plot(T,dFIR_R_quad(T,p)*100, color='#00596D', linestyle = '--')
ax.text(45, 2.81, '$quadratic-fit$', color='#00596D',fontweight="bold",horizontalalignment="left",verticalalignment="center",)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.spines["top"].set_visible(False)
ax.grid()
ax.set_xlabel('Temperature in $\u00b0C$')
ax.set_ylabel('Relative Sensitivity in %$K^{-1}$') 

plt.show()


fig, ax = plt.subplots(figsize=(6, 5))

A = np.arange(14,21)
ax.plot(T,dFIR_R_log(T,a,b)*100, color='#00596D', linestyle = '--')
ax.text(40, 3.02, '$logarithmic-fit$', color='#00596D',fontweight="bold",horizontalalignment="left",verticalalignment="center",)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.spines["top"].set_visible(False)
ax.grid()
ax.set_xlabel('Temperature in $\u00b0C$')
ax.set_ylabel('Relative Sensitivity in %$K^{-1}$') 

plt.show()

print(np.max(dFIR_R_log(T,a,b)*100))

fig, ax = plt.subplots(figsize=(7, 5))

A = np.arange(14,21)
ax.plot(T,log_func(T,a,b), color='#00596D', linestyle = '--')
plt.errorbar(Temperature, sum_ratios(A,72,399), yerr = y_err, xerr = T_err, linestyle = '', color = 'black')
ax.text(40, 10, '$sigmoidal-fit$', color='#00596D',fontweight="bold",horizontalalignment="left",verticalalignment="center",)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.spines["top"].set_visible(False)
ax.grid()
ax.set_xlabel('Temperature in $\u00b0C$')
ax.set_ylabel('Peak Ratios')

plt.show()