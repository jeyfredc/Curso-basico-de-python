# def run():
#     numero = int(input("Por favor digite un numero: "))
#     for potencia in range(1001):
#         potencia
#         #resultado = numero **potencia
#         print(f"{numero} a la {potencia} ") #y el resultado es {resultado}


# if __name__ == "__main__":
#     run()

def run():
    LIMITE = 1000

    contador = 0
    potencia_2 = 2 ** contador
    while potencia_2 < LIMITE:
        print('2 elevado a ' + str(contador) + ' es igual a: ' + str(potencia_2))
        contador = contador + 1
        potencia_2 = 2**contador
    


if __name__ == "__main__":
    run()