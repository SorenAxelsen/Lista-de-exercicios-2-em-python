def soma_ate_n(N):
    soma = 0
    for i in range(1, N + 1):
        soma += i
    return soma

def main():
    numero = int(input("Digite um número inteiro e positivo: "))
    if numero <= 0:
        print("O número precisa ser inteiro e positivo.")
    else:
        resultado = soma_ate_n(numero)
        print("A soma dos números de 1 até", numero, "é:", resultado)

if __name__ == "__main__":
    main()
