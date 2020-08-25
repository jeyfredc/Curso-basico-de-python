# Los números pares no podrán ser primos, pues todos los números pares son divisibles, además de por dos, por un número determinado que da por resultado dos. Una excepción a esto lo constituye el propio número dos, que es primo al cumplir la condición esencial de ser únicamente divisible por sí mismo y por la unidad.
# Los números impares, en cambio, sí podrán ser primos, en la medida que no se pueden expresar como el producto de otros dos números.



def run():
    numero = int(input('Por favor ingrese un numero: '))
    if numero==2 : #Como es la primer opcion no entra a la segunda por tanto se cumple la condicion
        modulo = numero % 2
        cociente = numero / 2
        print(f'el modulo de 2 es {modulo} pero su cociente es {int(cociente)}  por tanto es primo')
    elif numero % 2 ==0:
        print('no es primo')
    else:
        print('es primo')
        
            
if __name__ == "__main__":
    run()