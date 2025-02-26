
# EJERCICIO 1 

'''
Si enumeramos todos los números naturales por debajo de 10 que son múltiplos de 3 o 5, obtenemos 3, 5, 6 y 9. La suma de estos múltiplos es 23.

Termina la solución para que devuelva la suma de todos los múltiplos de 3 o 5 abajo el número pasó.

Además, si el número es negativo, devuelva 0.

Nota: Si el número es un múltiplo de ambos 3 Y 5, solo cuéntalo una vez.

'''

def multiplos(valor):

    suma = 0
    if valor != 0:
        for i in range(0,valor, 1):
            if i % 5 == 0 or i % 3 == 0:
                suma += i 
    else:
        return 0
    return suma


valoruser = int(input("Ingrese un valor: "))

print(multiplos(valoruser))