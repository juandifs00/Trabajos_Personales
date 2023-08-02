# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 08:40:11 2023

@author: juand
"""

print('Eliminar duplicados \n')

frutas = ['manzana', 'platano', 'melocoton', 'pera', 'manzana', 'pera', 'limon', 'platano', 'naranja']

for fruta in frutas:
    while(frutas.count(fruta) > 1):
        frutas.remove(fruta)
        
print('forma 1:',frutas)
print()

no_repetidos = set(frutas)

print('forma 2:',no_repetidos)
print()

lista_sin_duplicados = []
for elemento in no_repetidos:
    lista_sin_duplicados.append(elemento)
    
print('forma 3:', lista_sin_duplicados)
print()

def dividir_2(numero):
    resultado = numero/2
    return print('resultado de la division =',resultado)

numeros = [20,18,8,4,10,40,6]

numeros_divididos = list(map(dividir_2,numeros))