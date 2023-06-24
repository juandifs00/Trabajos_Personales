import random

m=int(input("Ingrese Numero de Estudiantes: "))
n=int(input("Ingrese Numero de Asignaturas: "))

a=[]
for i in range(0,m):
    a.append([0]*n)
  
b=[" "]*m
for i in range(0,m):
    b[i]=str(input("Ingrese Nombre: "))
    
    for j in range(0,n):
        
        a[i][j] =round(random.random()*5,1);
    #endfor  
#endfor
    
print()    

for i in range(0,m):
    print(b[i], " ", end = "");
    for j in range(0,n):    
        print(a[i][j],'\t',end="")
    #endfor
    print()
#endfor
    
print("");    
acumto=0 

for i in range(0,m):
    acum=0;
    for j in range(0,n):
        acum=acum+a[i][j]
        #,end="")
    #endfor
    acum = acum/n
    acum = round(acum, 1)
    print("El Promedio del Estuadiante ",b[i],"es: ",acum);
    acumto=acumto+a[i][j]
#endfor
    
print()
acumto = acumto / (m * n)
acumto = round(acumto, 1)
print("El Promedio del Grupo ",acumto);  
print("");  

for j in range(0,n):
    ACol = 0;
    for i in range(0,m):
       ACol = ACol + a[i][j]
    #endfor
    ACol = round((ACol/m),1)
    print("El Promedio de La Asignatura  ",j,"es  ",ACol);
#endfor

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
    print("El la mejor nota del Estudiante ",b[i],"es: ",mayorfil);
#endfor
print()
print("La Mejor Nota del Grupo: ",mayormat);
 
for j in range(0,n):
    mayorCol=a[0][j];
    Name=b[0];
    for i in range(0,m):
        
        if (a[i][j]>mayorCol):
            mayorCol=a[i][j];
            Name = b[i];
            
    #endfor
    print("La Mejor Nota de la Asignatura ",j," del Estudiante ", Name ,"es: ",mayorCol);
#endfor
print()

