# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 19:45:19 2019

@author: Juan Diego Rodriguez
"""

import random
m=int(input("Ingrese la cantidad de FILAS a procesar...:"))
n=int(input("Ingrese la cantidad de COLUMNAS a procesar...:"))
a=[]
for i in range(0,m):
    a.append([0]*n)
#endfor

for i in range(0,m):
    for j in range(0,n):
        a[i][j] =random.randint(0,10)
    #endfor
#endfor.
print()    
for i in range(0,m):
    for j in range(0,n):
        print(a[i][j],'\t',end="")
    #endfor
    print()
#endfor
acumto=0
for i in range(0,m):
    acum=0;
    for j in range(0,n):
        acum=acum+a[i][j]
    print("la Suma de la fila   ",i,"es  ",acum);
    acumto=acumto+acum
#endfor
print()
print("la Suma de la Matriz es    ",acumto);

print()
mayormat=a[0][0]  
for i in range(0,m):
    mayorfil=a[i][0];
    for j in range(0,n):
        if (a[i][j]>mayorfil):
            mayorfil=a[i][j];
        #endif
        if (a[i][j]>mayormat):
            mayormat=a[i][j];
        #endif
    #endfor
    print("El mayor de la fila   ",i,"es  ",mayorfil);
#endfor
print()
print("El mayor de la Matriz es    ",mayormat);