def run():
    numero = int(input('POr favor ingrese un numero para hacer la multiplicacion'))
    contador = 0
    resultado = numero*contador
    while contador <100:
        contador += 1 
        resultado = numero*contador
        print(resultado)
        if resultado > 50:
            print('Vaya, te exediste, listillo(a)')
            break



if __name__ == "__main__":
    run()