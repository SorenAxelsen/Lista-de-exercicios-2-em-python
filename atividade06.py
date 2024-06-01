def soma_numeros(n):
    
    if n <= 0:
        return "O número deve ser inteiro e positivo."
    return sum(range(1, n + 1))


N = int(input("Digite um número inteiro e positivo: "))
resultado = soma_numeros(N)
print(f"A soma dos números inteiros de 1 até {N} é: {resultado}")
