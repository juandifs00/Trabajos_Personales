#Menu
import math
def main():
    print("\nPrograma para convertir entre sistemas numéricos\n\n")
    print("1. Decimal a binario")
    print("2. binario a decimal")
    print("3. Decimal a IEEE 754 de 32 bits")
    print("4. IEEE 32 bits a decimal")
    print("5. binario a IEEE 754 de 32 bits")
    print("6. IEEE 754 de 32 bits de 32 bits a binario")
    print("7. Decimal a IEEE 754 de 64 bits")
    print("8. IEEE 64 bits a decimal")
    print("9. binario a IEEE 754 de 64 bits")
    print("10. IEEE de 64 bits a binario")
    print("11. binario a hexadecimal")
    print("12. Hexadecimal a binario")
    print("13. Decimal a hexadecimal")
    print("14. Hexadecimal a decimal")
    print("15. Decimal a IEEE Hex")
    print("16. IEEE Hex a decimal")
    
    opc = input("\nIngrese la opción que desea ejecutar: ")
    
    if opc == "1":
        num = input("\nIngrese el número decimal para llevarlo binario\n\n")
        binario = dec2bin(float(num))
        print(binario," en binario, equivale a ", num, " en decimal.")
        ct = input("\nPresione 1 para continuar o 0 para salir: \n")
        if ct == "1":
            main()
        else:
            print("Adios!")

    elif opc == "2":
        num = input("\nIngrese el número binario para llevarlo a decimal\n\n")
        decimal = bin2dec(num)
        print(num," en binario, equivale a ", decimal, " en decimal.")
        ct = input("\nPresione 1 para continuar o 0 para salir: \n")
        if ct == "1":
            main()
        else:
            print("Adios!")

    elif opc == "3":
        num = input("\nIngrese el número decimal para llevarlo a IEEE 754 de 32 bits\n\n")
        IEEE = dec2ieee_32(num)
        print(num," en decimal, equivale a ", IEEE, " en IEEE 754 de 32 bits")
        ct = input("\nPresione 1 para continuar o 0 para salir: \n")
        if ct == "1":
            main()
        else:
            print("Adios!")

    elif opc == "5":
        num = input("\nIngrese el número binario para llevarlo a IEEE 754 de 32 bits\n\n")
        IEEE = bin2ieee_32(num)
        print(num," en binario, equivale a ", IEEE, " en IEEE 754 de 32 bits")
        ct = input("\nPresione 1 para continuar o 0 para salir: \n")
        if ct == "1":
            main()
        else:
            print("Adios!")

    elif opc == "7":
        num = input("\nIngrese el número decimal para llevarlo a IEEE 754 de 64 bits\n\n")
        IEEE = dec2ieee_64(num)
        print(num," en decimal, equivale a ", IEEE, " en IEEE 754 de 64 bits")
        ct = input("\nPresione 1 para continuar o 0 para salir: \n")
        if ct == "1":
            main()
        else:
            print("Adios!")

    elif opc == "9":
        num = input("\nIngrese el número binario para llevarlo a IEEE 754 de 64 bits\n\n")
        IEEE = bin2ieee_64(num)
        print(num," en binario, equivale a ", IEEE, " en IEEE 754 de 64 bits")
        ct = input("\nPresione 1 para continuar o 0 para salir: \n")
        if ct == "1":
            main()
        else:
            print("Adios!")


    elif opc == "11":
        num = input("\nIngrese el número binario para llevarlo a hexadecimal\n\n")
        hexadecimal = bin2hex(num)
        print(num," en decimal, equivale a ", hexadecimal, " en hexadecimal")
        ct = input("\nPresione 1 para continuar o 0 para salir:\n")
        if ct == "1":
            main()
        else:
            print("Adios!")

    elif opc == "12":
        num = input("\nIngrese el número hexadecimal para llevarlo a binario\n\n")
        binario = hex2bin(num)
        print(num," en decimal, equivale a ", binario, " en binario")
        ct = input("\nPresione 1 para continuar o 0 para salir:\n")
        if ct == "1":
            main()
        else:
            print("Adios!")
    
    elif opc == "13":
        num = input("\nIngrese el número decimal para llevarlo a hexadecimal\n\n")
        hexadecimal = decimal_a_hexadecimal(num)
        print(num," en decimal, equivale a ", hexadecimal, " en hexadecimal")
        ct = input("\nPresione 1 para continuar o 0 para salir:\n")
        if ct == "1":
            main()
        else:
            print("Adios!")

    elif opc == "14":
        num = input("\nIngrese el número hexadecimal para llevarlo a decimal\n\n")
        decimal = hexadecimal_a_decimal(num)
        print(num," en hexadecimal, equivale a ", decimal, " en decimal")
        ct = input("\nPresione 1 para continuar o 0 para salir:\n")
        if ct == "1":
            main()
        else:
            print("Adios!")

#conversor de decimal a binario
def dec2bin(num):
    """
    params : num type float
    retunr : numero equivalente en binario
    """

    resto = 0
    numero_binario = []
 
    if num <= 1:
        print("No se puede convertir")
    else:
        while num > 1:
            resto=num%2
            numero_binario.append(resto)
            num=num//2
        numero_binario.append(1)
        numero_binario.reverse()
        return numero_binario
 
def dec2bin_decimal(decimal):
    """
    params : num type string
    retunr : numero equivalente en decimal
    """

    aux=decimal*2
    numero_binario=""
    lista=[]
    valor=0
    while aux not in lista :
            lista.append(aux)
            partes=math.modf(aux)
            valor= int(round(partes[1],2))
            numero_binario += str(valor)
            if int(round(partes[1],2)) == 1 and round(partes[0],2)== 0.0:
                break
            aux=round(partes[0],2) * 2
 
    return numero_binario

#conversor de binario a decimal
def bin2dec(n):
    """
    params : num type string
    retunr : numero equivalente en decimal
    """

    l = str(n).split(".")
    if len(l) == 2:
        ent = l[0][::-1]
        dec = l[1]
        nent = bin_parte_ent(ent)
        ndec = bin_parte_dec(dec)
        num = str(nent)+"."+str(ndec)[2:]
    else:
        ent = l[0][::-1]
        num = bin_parte_ent(ent)
    return num

def bin_parte_ent(n):
    cant = 0
    p=0
    for i in n:
        cant = cant + int(i)*2**p
        p=p+1
    return cant

def bin_parte_dec(n):
    cant = 0
    p=-1
    for i in n:
        cant = cant + int(i)*2**p
        p=p-1
    return cant

def obtener_caracter_hexadecimal(valor):    
    valor = str(valor)
    equivalencias = {
        "10": "a",
        "11": "b",
        "12": "c",
        "13": "d",
        "14": "e",
        "15": "f",
    }
    if valor in equivalencias:
        return equivalencias[valor]
    else:
        return valor

def decimal_a_hexadecimal(decimal):
    """
    params : num type string
    retunr : numero equivalente en hexadecimal
    """

    decimal = int(decimal)
    hexadecimal = ""
    while decimal > 0:
        residuo = decimal % 16
        verdadero_caracter = obtener_caracter_hexadecimal(residuo)
        hexadecimal = verdadero_caracter + hexadecimal
        decimal = int(decimal / 16)
    return hexadecimal

def obtener_valor_real(caracter_hexadecimal):
    equivalencias = {
        "f": 15,
        "e": 14,
        "d": 13,
        "c": 12,
        "b": 11,
        "a": 10,
    }
    if caracter_hexadecimal in equivalencias:
        return equivalencias[caracter_hexadecimal]
    else:
        return int(caracter_hexadecimal)

def hexadecimal_a_decimal(hexadecimal):
    """
    params : num type string
    retunr : numero equivalente en decimal
    """

    hexadecimal = hexadecimal.lower()
    # La debemos recorrer del final al principio, así que la invertimos
    hexadecimal = hexadecimal[::-1]
    decimal = 0
    posicion = 0
    for digito in hexadecimal:
        valor = obtener_valor_real(digito)
        elevado = 16 ** posicion
        equivalencia = elevado * valor
        decimal += equivalencia
        posicion += 1
    return decimal

def hex2bin(hexadecimal):
    """
    params : num type string
    retunr : numero equivalente en binario
    """

    decimal = hexadecimal_a_decimal(hexadecimal)
    binario = dec2bin(decimal)
    return binario

def bin2hex(binario):
    """
    params : num type string
    retunr : numero equivalente en hexadecimal
    """
    decimal = bin2dec(binario)
    hexadecimal = decimal_a_hexadecimal(decimal)
    return hexadecimal

def dec2ieee_32(real_no):
    """
    params : num type string
    retunr : numero equivalente en IEEE_32
    """
    sign_bit = 0

    real_no = float(real_no)

    if(real_no < 0):

        sign_bit = 1
        
    real_no = abs(real_no)

    int_str = bin(int(real_no))[2 : ]

    fraction_str = str(dec2bin_decimal(abs(real_no - int(real_no))))

    ind = int_str.index('1')

    exp_str = bin((len(int_str) - ind - 1) + 127)[2 : ]

    mant_str = int_str[ind + 1 : ] + fraction_str

    mant_str = mant_str + ('0' * (23 - len(mant_str)))

    return sign_bit, exp_str, mant_str
    
def dec2ieee_64(real_no):
    """
    params : num type string
    retunr : numero equivalente en IEEE_64
    """
    sign_bit = 0

    real_no = float(real_no)

    if(real_no < 0):

        sign_bit = 1
        
    real_no = abs(real_no)

    int_str = bin(int(real_no))[2 : ]

    fraction_str = str(dec2bin_decimal(abs(real_no - int(real_no))))

    ind = int_str.index('1')

    exp_str = bin((len(int_str) - ind - 1) + 1023)[2 : ]

    mant_str = int_str[ind + 1 : ] + fraction_str

    mant_str = mant_str + ('0' * (52 - len(mant_str)))

    return sign_bit, exp_str, mant_str

def bin2ieee_64(num):
    """
    params : num type string
    retunr : numero equivalente en IEEE_64
    """
    decimal = bin2dec(num)
    binario = dec2ieee_64(decimal)
    return binario

def bin2ieee_32(num):
    """
    params : num type string
    retunr : numero equivalente en IEEE_32
    """
    decimal = bin2dec(num)
    binario = dec2ieee_32(decimal)
    return binario

main()