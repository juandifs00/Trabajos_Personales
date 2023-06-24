# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 23:23:24 2019

@author: Juan Diego Rodriguez
"""

#P.P.P.JUAN DIEGO RODRIGUEZ GUARIN
nom=[];
sal=[];
n=int(input("Ingrese el número de empleados de la empresa: "));
conmenor=0;
acum=0;
mayorsalario=0;
nom=["  "]*n;
sal=[0]*n;
for con in range (0, n):
    nom[con]=str(input("Ingrese el nombre del trabajador:  "));
    sal[con]=int(input("Ingrese el salario del trabajador: "));
    print("//////////////////////////////////////////////////////////////////");
    print("El empleado ", nom[con],"tiene un salario de ", sal[con]);
    print("//////////////////////////////////////////////////////////////////");
    acum=acum+sal[con];
    if(sal[con]>mayorsalario):
        mayorsalario=sal[con];
        mayornombre=nom[con];
    #endif
    if(sal[con]<1000000):
        conmenor=conmenor+1;
    #endif
#endfor
prom=acum/n;
prom=int(prom);
print("El promedio es :                                                 ", prom);
print("El nombre del empleado con mayor salario es :                    ",mayornombre);
print("El numero de empleados que ganan menos de un millón de pesos es: ",conmenor);
print("P.P.P.Juan Diego Rodríguez Guarín");
