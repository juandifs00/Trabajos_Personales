# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 10:13:11 2019

@author: Juan Diego Rodriguez
"""

"""
Leer el nombre de n vendedores, donde cada uno de ellos tiene una comisión ganada en los 
últimos m meses. 
Formar un vector[n] con los nombres de los vendedores y un vector[m] con los nombres de los meses. 
También formar una matriz de m por n que contenga la comisión de cada uno de los n vendedores 
en cada una de las m meses. Se debe mostrar el nombre de cada vendedor, sus respectivas comisiones, 
el promedio y número de comisiones menores de $ 10.000, mostrar el promedio general de todos 
los vendedores, el número de vendedores que en los m meses no cumplieron la meta (meta > m * 10.000).

OJO. LA MATRIZ ES m * n
"""
#P.P.P.JUAN DIEGO RODRIGUEZ GUARIN
a=[]
nom=[]
mes=[]
convend=0
import random
n=int(input("Ingrese el numero de vendedores: "))
m=int(input("Ingrese el numero de meses trabajados: "))
print("//////////////////////////////////////////////////////////////////////////")

nom=["  "]*n
mes=["  "]*n
com=[0]*n
conmen=0

for con in range (0,n):
    nom[con]=str(input("Ingrese el nombre del vendedor: "))
#endfor
print()

for con in range (0,m):
    mes[con]=str(input("Ingrese el mes trabajado: "))
#endfor
print()

for con in range (0,m):
    a.append([0]*n)
#endfor

for con in range(0,m):
    for cont in range(0,n):
        a[con][cont]=random.randint(7000,25000)
    #endif
    print()
#endfor
print()

for con in range (0,n):
    print(nom[con],'\t',end="")
#endfor
print()
for con in range (0,m):
    for cont in range (0,n):
        print(a[con][cont],'\t',end="")
    #endfor
    print(mes[con],"  ",end="")
    print()
#endfor

sumtot=0
nocumple=0

for cont in range (0,n):
    sum=0
    prom=0
    comis=0
    for con in range (0,m):
        sum=sum+a[con][cont]
        if(a[con][cont]<10000):
            conmen=conmen+1
    #endfor
    if(sum<(m*10000)):
        nocumple=nocumple+1
    #endif
    prom=int(sum/m)
    print("El empleado",nom[con],"tuvo un promedio de: $",prom,"y un total de",conmen,"comisiones menores a 10.000 perdidas.")
    sumtot=sumtot+sum
#endfor
promtot=int(sumtot/(n*m))
print()
print("El promedio general es: $",promtot)
print("El numero de vendedores que no cumplio con la meta es: ",nocumple)
print("//////////////////////////////////////////////////////////////////////////")
print("P.P.P.JUAN DIEGO RODRIGUEZ GUARIN")