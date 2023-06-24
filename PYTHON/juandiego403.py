#P.P.P.JUAN DIEGO RODRIGUEZ GUARIN - 403
"""
desarrollar una matriz de n filas por m columnas que genere numeros aleatorios:
    1 Mostrar la matriz en pantalla
    2 por cada fila mostrar  el mayor o menor elemento
    3 mostrar el menor y mayor valor de cada columna
    4 mostrar la posicion (numero de fila y numero de columna del menor de esamatriz)
    5 mostrar cual es la fila con el menor promedio
"""
import random
nom=[]
mes=[]
a=[]
n=int(input("Ingrese el numero de desempleados: "))
m=int(input("Ingrese el numero de meses del año: "))
nom=[" "]*n
mes=[" "]*m
for i in range (0,n):
    a.append([0]*m)
#endfor

for i in range (0,n):
    nom[i]=str(input("Ingrese el nombre del desempleado: "))
#endfor

for i in range (0,m):
    mes[i]=str(input("Ingrese el mes que no trabajó: "))
#endfor
    
print()
for i in range(0,n):
    for j in range(0,m):
        a[i][j]=random.randint(2000,10000)
    #endfor
    print()
#endfor
print()

for i in range (0,m):
    print(mes[i],'\t',end="")
#endfor
    
print()
for i in range (0,n):
    for j in range (0,m):
        print(a[i][j],'\t',end="")
    #endfor
    print(nom[i],"  ",end="")
    print()
#endfor



print("P.P.P.JUAN DIEGO RODRIGUEZ GUARIN - 403")