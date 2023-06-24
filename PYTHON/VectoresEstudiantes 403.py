# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 21:00:09 2019

@author: Juan Diego Rodriguez
"""
"""
Con base en el ejemplo anterior, desarrolle un programa python que:
    1 Lea el nombre de n estudiantes y forme un vector con ellos
    2 Lea las m notas de los estudiantes y forme una matriz de n*m
    3 Imprimir el nombre de cada estudiante, su promedio y el numero de asignaturas perdidas
    4 Mostrar el promedio general de c/u de las asignaturas
    5 Mostrar el numero de estudiantes que fueron expulasados (Perdieron mas de m/2 de materias)
    6 Mostrar el mejor promedio del grupo y el nombre del estudiante que lo sacó
    7 Mostrar cual fue la asignatura a la que los estudiantes les fue más mal
"""
#P.P.P.JUAN DIEGO RODRIGUEZ GUARIN
import random
n=int(input("Ingrese el numero de estudiantes: "))
m=int(input("Ingrese el numero de asginaturas: "))
a=[]
for i in range (0,n):
    a.append([0]*m)
#endfor
nom=[" "]*n
for i in range (0,n):
    nom[i]=str(input("Ingrese nombre del estudiante: "))
    for j in range (0,m):
        a[i][j]=round(random.random()*5,1)
    #endfor
    print()
#endfor
print("")
for i in range(0,n):
    print(nom[i]," ",end="")
    for j in range (0,m):
        print(a[i][j],'\t',end="")
    #endfor
    print()
#endfor
print("")
acumto=0
contexp=0
mejorprom=0
for i in range (0,n):
    acum=0
    contnot=0
    for j in range(0,m):
        acum=acum+a[i][j]
        if(a[i][j]<3):
            contnot=contnot+1
        #endif
    #endfor
    acum=acum/m
    acum=round(acum,1)
    print("El promedio del estudiante", nom[i],"es: ",acum)
    print("El numero de asginaturas perdias por el estudiantes",nom[i],"son: ",contnot)
    if(contnot>(m/2)):
        contexp=contexp+1
    #endif
    if(acum>mejorprom):
        mejorprom=acum
        meestu=nom[i]
    #endif
    acumto=acumto+a[i][j]
#endfor
print()
for j in range (0,m):
    promas=0
    for i in range (0,n):
        promas=promas+a[i][j]
    #endfor
    promas=round((promas/n),1)
    print("El promedio de la asginatura ",j,"es:",promas)
#endfor
print()
print("El mejor promedio es",mejorprom,"obtenido por ",meestu)
print()
print("El numero de estudantes que fueron expulsados es: ",contexp)
print()
print("P.P.P.JUAN DIEGO RODRIGUEZ GUARIN")