def calcular_soma(N):
    
    if N <= 0:
        return "N deve ser um valor inteiro positivo."
    else:
        S = 0
        fatorial = 1
        for i in range(1, N + 1):
            fatorial *= i
            S += 1 / fatorial
        return S


N = int(input("Digite um valor inteiro positivo: "))
resultado = calcular_soma(N)
print(f"O valor de S para N = {N} é: {resultado:.6f}")
