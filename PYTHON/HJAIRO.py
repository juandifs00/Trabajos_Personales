def main():
    import random;
    m=int(input("Ingrese numero de filas: "));
    n=int(input("Ingrese numero de columnas: "));
    a=[]
    for i in range (m):
        a.append([0]*n)
    #endfor
    def llenarmatriz(x,y,z):
        for i in range(y):
            for j in range(z):
                x[i][j]=random.randint(0,10);
			#endfor
		#endfor
        return;
    
    def imprimirmatriz(x,y,z):
        for i in range(y):
            for j in range(z):
                print (x[i][j],'\t',end="");
			#endfor
            print();
        #endfor
        return;

    def sumamatriz(x,y,z):
        sum=0;
        for i in range(y):
            for j in range(z):
                sum=sum+x[i][j];
			#endfor
		#endfor
        return sum;

    def sumadiagprincipal(x,y,z):
        sum=0;
        for i in range(y):
            sum=sum+x[i][i]
		#endfor
        return sum;
    
    def sumadiagsecundaria(x,y,z):
        sum=0;
        fila=0;
        colu=n-1;
        while (fila<m):
            sum=sum+x[fila][colu];
            fila=fila+1;
            colu=colu-1;
		#endwhile;
        return sum;
    
    llenarmatriz(a,m,n);
    imprimirmatriz(a,m,n);
    valor1= sumamatriz(a,m,n);
    valor2= sumadiagprincipal(a,m,n);
    valor3= sumadiagsecundaria(a,m,n);
    print("suma de la matriz                     ", valor1);
    print("suma de la Diag. Principal            ", valor2);
    print("suma de la Diag. Secundaria           ", valor3);
main();