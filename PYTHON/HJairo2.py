def main():
    import random
    m=int(input("Ingrese la cantidad de FILAS a procesar...: "))
    n=int(input("Ingrese la cantidad de COLUMNAS a procesar...: "))
    a=[]
    for i in range(0,m):
        a.append([0]*n)
    #AQUI COMIENZA LA PARTE MODULAR
    def LlenarMatriz(ma,z,w): # Aqui inicia el mÃ³dulo para llenar la matriz
        for i in range(0,z):
            for j in range(0,w):
                ma[i][j] =random.randint(0,50)
                ma[i][j]=a[i][j]
        return # Aqui finaliza el mÃ³dulo que llena la matriz

    def ImprimirMatriz(ma,z,w):
        for i in range(0,z):
            print()
            for j in range(0,w):
                print(ma[i][j],'\t',end="")
        return

    def SumarMatriz(ma,z,w):  # Aqui inicia el mÃ³dulo que acumula los datos de la matriz
        sum=0
        for i in range(0,z):
            for j in range(0,w):
                sum=sum+ma[i][j]
        return sum

    def ValorMayorMatriz(ma,z,w):  # Aqui inicia el mÃ³dulo que busca el mayor
        may=ma[0][0]
        for i in range(0,z):
            for j in range(0,w):
                if ma[i][j]>may:
                    may=ma[i][j]
        return may  # Aqui finaliza el mÃ³dulo que busca el mayor

    def ValorMenorMatriz(ma,z,w):
        men=ma[0][0]
        for i in range(0,z):
            for j in range(0,w):
                if ma[i][j]<men:
                    men=ma[i][j]
        return men

    def OperarMatriz(ma,z,w):
        for i in range(0,z):
            for j in range(0,w):
                if ma[i][j]% 2==0:
                   ma[i][j]=ma[i][j]*ma[i][j]
                else:
                   ma[i][j]=ma[i][j]*3
        return
    #AQUI TERMINA LOS MODULOS Y SE COMIENZAN A INVOCAR
    LlenarMatriz(a,m,n) # Aqui se llama el módulo de llenar matriz y le entregan la matriz a y n como parametros
    print("MATRIZ ORIGINAL")
    ImprimirMatriz(a,m,n) # Aqui se llama el módulo imprimir matriz
    suma=SumarMatriz(a,m,n) # Aqui se invoca el módulo para sumar el matriz, observe la diferencia en el llamado
    #cuando el mÃ³dulo retorna un valor, aquÃ­ recibe el valor de la suma en la variable suma.
    print()
    print('La suma de los elementos del matriz es...:',suma)
    mayor=ValorMayorMatriz(a,m,n) #Aqui se invoca el módulo busca el mayor de la matriz
    print()
    print('EL MAYOR DE LA MATRIZ...:',mayor)
    menor=ValorMenorMatriz(a,m,n)  #Aqui se invoca el módulo busca el menor de la matriz
    print()
    print('EL MENOR DE LA MATRIZ...:',menor)
    OperarMatriz(a,m,n)   #Aquí­ se aplica lo de parámetro por referencia ya que el matriz retorna modificado
    print()
    print('MATRIZ DESPUES DE LAS OPERACIONES')
    ImprimirMatriz(a,m,n) #Observe la reutilización del módulo imprimir matriz
main()