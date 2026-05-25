#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 29 16:10:23 2024

@author: main
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
Ordner = 'C:/Users/MEaTh/OneDrive/Desktop/Semesterarbeit/30.05/' 
Ordner_auslesen(Ordner)
    
Ordner ='C:/Users/MEaTh/OneDrive/Desktop/Semesterarbeit/28.05/'
Ordner_auslesen(Ordner)

Ordner ='C:/Users/MEaTh/OneDrive/Desktop/Semesterarbeit/29.05/'
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
def dFIR(T,p):
    f = 2*p[0]*T + p[1]
    return f

#Mit dieser Funktion kannst du die Relative Sensitivität ausgehend von deinem Fit bestimmen
def dFIR_R(T,p):
    f = dFIR(T,p)
    return np.abs(f/FIR(T,p))

#Die folgenden 4 Funktionen dienen dazu logarithmische fits zu erstellen und deren Ableitungen zu berechnen.
#Das vorgehen ist das selbe, nur dass du statt p, a&b bestimmen musst dies kannst du mit den folgenden 2 Zeilen:
#params, covariance = sp.optimize.curve_fit(log_func, x, y)
#a, b = params
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

"""----------Plots-----------"""

#Diese Plot Funktion plottet Counts als Funktion der Wellenlänge. A soll dabei ein Array der Form [ , , ,...] sein.
#In A kannst du angeben welchen Datensatz du geplottet haben willst. Willst du den 2en un 4en plotten so definiere A = [1,3].
#Mit Label kannst du die jeweiligen Datensätze beschriften z.B. Label = ['25C', '35C'].
#Mit Title kannst du den Titel des plots wählen z.B. Title = CaCuSiO
def plot(A, Label, Title):
    for a in A:
        plt.plot(data[:,0,a],data[:,1,a],label = Label[a])
    plt.grid()
    plt.xlabel('Wavelength')
    plt.ylabel('Counts')
    plt.title(Title)
    plt.legend()
    plt.show()
    return 0
#Beispiel:
    """ A = [0,1,2,3]
        Label = ['15C', '25C', '30C', '35C']
        Title = Codoped CaCuSiO
        plot(A, Label, Title)
    """

#Diese Funktion ist fast identisch, sie normalisiert zusätzlich auf einen von dir gewählten Peak.
#Finde dazu jenen Index der zum Peak gehört und definiere Peak = ___.
#Der Yb Peak den ich ständig benutze befindet sich z.B. an Stelle 71
#Benutze die Peak Funktion um den Peak für eine gegebene Wellenlänge zu finden.
def plot_normalised(Peak, A, Label, Title):
    for a in A:
        plt.plot(data[:,0,a],data[:,1,a]/data[Peak,1,a],label = Label[a])
    plt.grid()
    plt.xlabel('Wavelength')
    plt.ylabel('Normalized counts')
    plt.title(Title)
    plt.legend()
    plt.show()
    return 0
#Beispiel:
    """ A = [0,1,2,3]
        Label = ['15C', '25C', '30C', '35C']
        Title = Codoped CaCuSiO
        Peak = 399
        plot_normalised(Peak, A, Label, Title)
    """

#Mit dieser Funktion kannst du dir die Absolute Sensitivität plotten lassen
#Hierfür benötigst du die 2 Peaks welche du betrachten willst, dabei wird Peak1 durch Peak 2 geteilt.
#In Temperatures speicherst du die zu den Datensätzen A gehörigen Temperaturen
def plot_abs(A, Peak1, Peak2, Temperature, Title):
    Ratios = np.zeros(len(A))
    T = np.arange(14,61,0.01)
    i = 0
    for a in A:
        Ratios[i] = data[Peak1,1,a]/data[Peak2,1,a]
        i = i + 1
    params, covariance = sp.optimize.curve_fit(log_func, Temperature, Ratios)
    a, b = params
    plt.plot(T,dFIR_log(T, a, b)*100, label = 'logarithmic fit', linestyle ='--')
    plt.grid()
    plt.xlabel('Temperature in \u00b0C')
    plt.ylabel('Absolute sensitivity in %')
    plt.title(Title)
    plt.legend()
    plt.show()
    return 0
#Beispiel:
    """ A = [0,1,2,3]
        Title = Absolute Sensitivity
        Peak1 = 71
        Peak2 = 399
        Temperature = [15, 25, 30, 35]
        plot_abs(A, Peak1, Peak2, Temperature, Title)
    """
    
#Analog wie oben, hier wird jedoch die Relative Sensitivität geplottet
def plot_rel(A, Peak1, Peak2, Temperature, Title):
    Ratios = np.zeros(len(A))
    T = np.arange(14,61,0.01)
    i = 0
    for a in A:
        Ratios[i] = data[Peak1,1,a]/data[Peak2,1,a]
        i = i + 1
    params, covariance = sp.optimize.curve_fit(log_func, Temperature, Ratios)
    a, b = params
    plt.plot(T,dFIR_R_log(T, a, b)*100, label = 'logarithmic fit', linestyle ='--')
    plt.grid()
    plt.xlabel('Temperature in \u00b0C')
    plt.ylabel('Relative Sensitivity in %')
    plt.title(Title)
    plt.legend()
    plt.show()
    return 0

#Wenn du lediglich die Peak Ratios als Funktion der Temperatur geplottet haben willst bist du hier richtig.
#Input der Funktion ist wie oben.
#Die Messwerte werden mittels schwarzer x markiert und zudem wird ein logarithmischerer fit geplottet
def plot_ratios(A, Peak1, Peak2, Temperature, Title):
    Ratios = np.zeros(len(A))
    T = np.arange(14,61,0.01)
    i = 0
    for a in A:
        Ratios[i] = data[Peak1,1,a]/data[Peak2,1,a]
        i = i + 1
    params, covariance = sp.optimize.curve_fit(log_func, Temperature, Ratios)
    a, b = params
    plt.plot(T,log_func(T,a,b), label = 'logarithmic fit', linestyle = '--')
    plt.plot(Temperature,Ratios,'kx')
    plt.grid()
    plt.xlabel('Temperature in \u00b0C')
    plt.ylabel('Peak Ratios')
    plt.title(Title)
    plt.legend()
    plt.show()
    return 0

#Oft ist ein logarithmischer fit nicht adequat, besonders wenn die Ratios < 0 sind.
#Deshalb hier noch plots für jene fälle.

def plot_abs_quad(A, Peak1, Peak2, Temperature, Title):
    Ratios = np.zeros(len(A))
    T = np.arange(14,61,0.01)
    i = 0
    for a in A:
        Ratios[i] = data[Peak1,1,a]/data[Peak2,1,a]
        i = i + 1
    p = np.polyfit(Temperature, Ratios, deg = 2)
    plt.plot(T,dFIR(T, p)*100, label = 'quadratic fit', linestyle ='--')
    plt.grid()
    plt.xlabel('Temperature in \u00b0C')
    plt.ylabel('Absolute sensitivity in %')
    plt.title(Title)
    plt.legend()
    plt.show()
    return 0

def plot_rel_quad(A, Peak1, Peak2, Temperature, Title):
    Ratios = np.zeros(len(A))
    T = np.arange(14,61,0.01)
    i = 0
    for a in A:
        Ratios[i] = data[Peak1,1,a]/data[Peak2,1,a]
        i = i + 1
    p = np.polyfit(Temperature, Ratios, deg = 2)
    plt.plot(T,dFIR_R(T, p)*100, label = 'quadratic fit', linestyle ='--')
    plt.grid()
    plt.xlabel('Temperature in \u00b0C')
    plt.ylabel('Relative Sensitivity in %')
    plt.title(Title)
    plt.show()
    return 0

def plot_ratios_quad(A, Peak1, Peak2, Temperature, Title):
    Ratios = np.zeros(len(A))
    T = np.arange(14,61,0.01)
    i = 0
    for a in A:
        Ratios[i] = data[Peak1,1,a]/data[Peak2,1,a]
        i = i + 1
    p = np.polyfit(Temperature, Ratios, deg = 2)
    plt.plot(T,np.polyval(p,T), label = 'quadratic fit', linestyle = '--')
    plt.plot(Temperature,Ratios,'kx')
    plt.grid()
    plt.xlabel('Temperature in \u00b0C')
    plt.ylabel('Peak Ratios')
    plt.title(Title)
    plt.legend()
    plt.show()
    return 0


"""----------DIY-----------"""

Temperature = [15, 25, 30, 35, 40, 50, 60]
T = np.arange(14,61,0.01)
A = np.arange(0,7)
Peak = 399
Title = 'Nope'
Label = ['15\u00b0C', '25\u00b0C', '30\u00b0C', '35\u00b0C', '40\u00b0C', '50\u00b0C', '60\u00b0C', '15\u00b0C', '25\u00b0C', '30\u00b0C', '35\u00b0C', '40\u00b0C', '50\u00b0C', '60\u00b0C', '15\u00b0C', '25\u00b0C', '30\u00b0C', '35\u00b0C', '40\u00b0C', '50\u00b0C', '60\u00b0C']


def max_rel(A, Peak1, Peak2):
    Ratios = np.zeros(len(A))
    T = np.arange(14,61,0.01)
    i = 0
    for a in A:
        Ratios[i] = data[Peak1,1,a]/data[Peak2,1,a]
        i = i + 1
    params, covariance = sp.optimize.curve_fit(log_func, Temperature, Ratios)
    a, b = params
    return np.abs(np.max(dFIR_R_log(T, a, b)*100))

def max_rel_quad(A, Peak1, Peak2):
    Ratios = np.zeros(len(A))
    T = np.arange(14,61,0.01)
    i = 0
    for a in A:
        Ratios[i] = data[Peak1,1,a]/data[Peak2,1,a]
        i = i + 1
    p = np.polyfit(Temperature, Ratios, deg = 2)
    return np.abs(np.max(dFIR_R(T, p)*100))

A = np.arange(0,7,1)
x = 0
y = 0
z = 0
for i in range(65,80):
    for j in range(355,400):
        if max_rel(A,i,j) > z:
            z = max_rel(A,i,j)
            x = i
            y = j
            
for i in range(355,400):
    for j in range(65,80):
        if max_rel_quad(A,i,j) > z:
            z = max_rel_quad(A,i,j)
            x = i
            y = j
         
plot_ratios(A,x,y,Temperature,Title)
plot_rel(A,x,y,Temperature,Title)
print(x,y,z)

A = np.arange(7,14,1)
x = 0
y = 0
z = 0
for i in range(65,80):
    for j in range(355,400):
        if max_rel(A,i,j) > z:
            z = max_rel(A,i,j)
            x = i
            y = j
            
for i in range(355,400):
    for j in range(65,80):
        if max_rel_quad(A,i,j) > z:
            z = max_rel_quad(A,i,j)
            x = i
            y = j
   
plot_ratios(A,x,y,Temperature,Title)
plot_rel(A,x,y,Temperature,Title)
print(x,y,z)

A = np.arange(14,21,1)
x = 0
y = 0
z = 0
for i in range(65,80):
    for j in range(355,400):
        if max_rel(A,i,j) > z:
            z = max_rel(A,i,j)
            x = i
            y = j
         
for i in range(355,400):
    for j in range(65,80):
        if max_rel_quad(A,i,j) > z:
            z = max_rel_quad(A,i,j)
            x = i
            y = j

plot_ratios_quad(A,x,y,Temperature,Title)
plot_rel_quad(A,x,y,Temperature,Title)
print(x,y,z)

""" 
Als nächstes sellet i des tian wos mir Oscar empfohlen hot, also a intervall, maybe 20nm nemmen.
Ums realistisch zu mochen maybe a Gaussian shape weil der Filter sell a hoben weart.
Die besten werte kriag man plus minus ba dia peaks dei i schun gnummen hon.
I kannt die Erbium peaks weck lossen und lei iber die Yb und Ca peaks reiden, vlt mit die messungen vom ounfong des Semesters damit Oscar froa isch.
"""



x0 = 1015
y0 = 1493
a = 15
b = 15

def Gauss1(y):
    x = np.copy(y)
    for i in range(0,len(x)):
        if x[i] < x0-a:
            x[i] = 0
        if x[i] > x0 + a: 
            x[i] = 0
        if x[i] >= x0-a and x[i] <= x0+a:
            x[i] = 1
    return x

"""np.exp(-((x-x0)**2)/(2*a**2))"""

def Gauss2(x):
    y = np.copy(x)
    for i in range(0,len(y)):
        if y[i] < y0-a:
            y[i] = 0
        if y[i] > y0 + a:
            y[i] = 0
        if y[i] >= y0-a and y[i] <= y0+a:
            y[i] = 1
    return y

"""np.exp(-((y-y0)**2)/(2*b**2))"""


plt.plot(data[:150,0,1],data[:150,1,0]*Gauss1(data[:150,0,0])/data[372,1,0],color = 'black')
plt.plot(data[150:,0,1],data[150:,1,0]*Gauss2(data[150:,0,0])/data[372,1,0], color = 'black')
plt.plot(data[:150,0,1],data[:150,1,1]*Gauss1(data[:150,0,0])/data[372,1,0],color = 'blue')
plt.plot(data[150:,0,1],data[150:,1,1]*Gauss2(data[150:,0,0])/data[372,1,0], color = 'blue')
plt.plot(data[:150,0,1],data[:150,1,2]*Gauss1(data[:150,0,0])/data[372,1,0],color = 'red')
plt.plot(data[150:,0,1],data[150:,1,2]*Gauss2(data[150:,0,0])/data[372,1,0], color = 'red')
plt.plot(data[:150,0,1],data[:150,1,3]*Gauss1(data[:150,0,0])/data[372,1,0],color = 'green')
plt.plot(data[150:,0,1],data[150:,1,3]*Gauss2(data[150:,0,0])/data[372,1,0], color = 'green')
plt.plot(data[:150,0,1],data[:150,1,4]*Gauss1(data[:150,0,0])/data[372,1,0],color = 'yellow')
plt.plot(data[150:,0,1],data[150:,1,4]*Gauss2(data[150:,0,0])/data[372,1,0], color = 'yellow')
plt.plot(data[:150,0,1],data[:150,1,5]*Gauss1(data[:150,0,0])/data[372,1,0],color = 'brown')
plt.plot(data[150:,0,1],data[150:,1,5]*Gauss2(data[150:,0,0])/data[372,1,0], color = 'brown')
plt.plot(data[:150,0,1],data[:150,1,6]*Gauss1(data[:150,0,0])/data[372,1,0],color = 'grey')
plt.plot(data[150:,0,1],data[150:,1,6]*Gauss2(data[150:,0,0])/data[372,1,0], color = 'grey')
plt.grid()
plt.xlabel('Temperature in \u00b0C')
plt.ylabel('Peak Ratios')
plt.title(Title)
plt.legend()
plt.show()

for i in range(0,21):
    data[:150,1,i] = data[:150,1,i]*Gauss1(data[:150,0,0])/data[372,1,i]

def max_rel_gauss(A, Peak1, Peak2):
    Ratios = np.zeros(len(A))
    T = np.arange(14,61,0.01)
    i = 0
    for a in A:
        Ratios[i] = sum(data[(Peak1)-10:(Peak1)+10,1,a])
        i = i + 1
    Ratios = Ratios/20
    params, covariance = sp.optimize.curve_fit(log_func, Temperature, Ratios)
    a, b = params
    return np.abs(np.max(dFIR_R_log(T, a, b)*100))

def max_rel_quad_gauss(A, Peak1, Peak2):
    Ratios = np.zeros(len(A))
    T = np.arange(14,61,0.01)
    i = 0
    for a in A:
        Ratios[i] = sum(data[Peak1-10:Peak1+10,1,a])
        i = i + 1
    Ratios = Ratios/20
    p = np.polyfit(Temperature, Ratios, deg = 2)
    return np.abs(np.max(dFIR_R(T, p)*100))

A = np.arange(0,7,1)
x = 0
y = 0
z = 0
for i in range(65,80):
    for j in range(355,400):
        if max_rel_gauss(A,i,j) > z:
            z = max_rel_gauss(A,i,j)
            x = i
            y = j
            
for i in range(355,400):
    for j in range(65,80):
        if max_rel_quad_gauss(A,i,j) > z:
            z = max_rel_quad_gauss(A,i,j)
            x = i
            y = j
         

print(x,y,z)

A = np.arange(7,14,1)
x = 0
y = 0
z = 0
for i in range(65,80):
    for j in range(355,400):
        if max_rel_gauss(A,i,j) > z:
            z = max_rel_gauss(A,i,j)
            x = i
            y = j
            
for i in range(355,400):
    for j in range(65,80):
        if max_rel_quad_gauss(A,i,j) > z:
            z = max_rel_quad_gauss(A,i,j)
            x = i
            y = j
   

print(x,y,z)

A = np.arange(14,21,1)
x = 0
y = 0
z = 0
for i in range(65,80):
    for j in range(355,400):
        if max_rel_gauss(A,i,j) > z:
            z = max_rel_gauss(A,i,j)
            x = i
            y = j
         
for i in range(355,400):
    for j in range(65,80):
        if max_rel_quad_gauss(A,i,j) > z:
            z = max_rel_quad_gauss(A,i,j)
            x = i
            y = j


print(x,y,z)