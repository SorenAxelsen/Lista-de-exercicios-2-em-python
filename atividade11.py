def calcular_serie(N):
    S = 0
    fatorial = 1
    for i in range(1, N + 1):
        fatorial *= i
        S += 1 / fatorial
    return S

def main():
    N = int(input("Digite um número inteiro positivo: "))
    if N <= 0:
        print("O número deve ser positivo.")
    else:
        resultado = calcular_serie(N)
        print("O valor de S é:", resultado)

if __name__ == "__main__":
    main()
