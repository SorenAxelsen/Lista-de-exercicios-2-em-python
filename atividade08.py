def fatorial(numero):
    
    if numero < 0:
        return "O número deve ser positivo."
    elif numero == 0 or numero == 1:
        return 1
    else:
        resultado = 1
        for i in range(2, numero + 1):
            resultado *= i
        return resultado


num = int(input("Digite um número inteiro positivo: "))
resultado = fatorial(num)
print(f"O fatorial de {num} é: {resultado}")
