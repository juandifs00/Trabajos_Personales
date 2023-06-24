# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 10:09:03 2019

@author: Juan Diego Rodriguez
"""

import random
# Se determina el tamaño de la matriz
m=int(input("Ingrese Número de estudiantes ...:"))
n=int(input("Ingrese Número de asignaturas ...:"))

#se declara el arreglo numerico de n*m 
a=[]
for i in range(0,m):
    a.append([0]*n)
b=[" "]*m
#se rellena los elementos de l amatriz con numeros aleatorios
# y el vector con nombre de estudiantes
for i in range(0,m):
    b[i]=str(input("Ingrese Nombre"))
    for j in range(0,n):
        a[i][j] = round(random.random()*5,1)
    #endfor
#endfor.
print()    

# se imprime la matriz por filas y el vector
for i in range(0,m):
    print (b[i],'\t',end="");
    for j in range(0,n):
        print(a[i][j],'\t',end="")
    #endfor
    print()
#endfor
print()

#se muestra promedio de cada fila y de la matriz    
acumtot=0  
for i in range(0,m):
    acumfil=0;
    for j in range(0,n):
        acumfil=acumfil+a[i][j]
    #endfor
    prom=round(acumfil/n,2);
    print("El promedio del estudiante   ",b[i],"es  ",prom);
    acumtot=acumtot+acumfil
    if (i==0):
        mejorprom=prom;
        mejorestu=b[0];
    else:
        if (prom>mejorprom):
            mejorprom=prom;
            mejorestu=b[i];
        #endif
#endfor
prom=round(acumtot/(m*n),2);
print("El promedio general del grupo es  ",prom);
print("El mejor promedio es  ",mejorprom,   "por el estudiante  ",mejorestu);
print()

#encuentra promedios por cada una de las columnas
for j in range(0,n):
    acumcol=0;
    for i in range(0,m):
        acumcol=acumcol+a[i][j]
    #endfor
    prom=round(acumcol/m,2);
    print("El promedio de la asignatura   ",j,"es  ",prom);
#endfor
print()

#se muestra mejor nota de cada materia y el estudiante que la obtui 
for j in range(0,n):
    mayornota=a[0][j];
    mayorestu=b[0]
    for i in range(0,m):
        if (a[i][j] > mayornota):
            mayornota=a[i][j];
            mayorestu=b[i];
        #endif
    #endfor
    print("La mejor nota de la asignatura   ",j,"es  ",mayornota," del estudiante  ",mayorestu);
#endfor    

#Encuentra numero de materias perdidas por estudiante
print()
estexp=0    
for i in range(0,m):
    perest=0;
    for j in range(0,n):
        if (a[i][j] < 3):
            perest=perest+1;
        #endif
    #endfor
    print ("El estudiante  ", b[i], "Perdió  ",perest)
    if(perest>n/2):
        estexp=estexp+1;
    #endif
#endfor
print ("El numero de estudiantes expulsados es ....   ",estexp)
    
#HALLAR EL PROMEDIO DE ASIGNATURA MAS "BAJITO" y decir de cual 
#asignatura es

for j in range(0,n):
    acucol=0    
    for i in range(0,m):
        acucol=acucol+a[i][j]
    #endfor
    promcol=round(acucol/n,2)
    print("El promedio de la asignatura   ",j,"  Es  ",promcol);
    if (j==0):
        peorprome=promcol;
        peorasign=0;
    else:
        if (promcol<peorprome):
            peorprome=promcol;
            peorasign=j;
        #endif
    #endif
#endfor
print("El peor promedio es   ", peorprome, "  En la asignatura  ",peorasign);