print("Indique si es binario o decimal")
conversor= input()

if conversor.lower()== "binario":
    print("Introduzca numero Binario:")
    numero= list(input())
    x= [128,64,32,16,8,4,2,1]
    sumador= []
    for i in range (0, len(x)):
        if numero[i]== "1":
            sumador.append(x[i])
            valor_t= sum(sumador)
    print("-"*39)
    print("Resultado en «Decimal» es:", valor_t)

elif conversor.lower()== "decimal":
    print("Ingresa valor decimal (0-255):")
    def decimal_a_binario(n):
        resto = ""
        while n > 0:
            resto= str(n%2) + resto
            n= n//2
        return resto or "0"
    try:
        dec = int(input())
        if 0 <= dec <= 255:
            resultado_bin = decimal_a_binario(dec)
            print("-"*39)
            print(f"Resultado en «Binario» es: {resultado_bin}")
        else:
            print("Por favor ingresa un numero entre 0 y 255.")
    except ValueError:
        print("Valor invalida. Por favor ingresa un numero valido.")
else:
    print("Opcion invalida. Ingresa «Binario» o «Decimal».")
