def fatorial(n):
    if n == 0:
        return 1
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

def main():
    numero = int(input("Digite um número inteiro positivo: "))
    if numero < 0:
        print("O número deve ser positivo.")
    else:
        resultado = fatorial(numero)
        print(f"O fatorial de {numero} é:", resultado)

if __name__ == "__main__":
    main()
