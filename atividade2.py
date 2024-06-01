def verificar_elementos(vetor, valor):
    posicoes = [i for i, num in enumerate(vetor) if num == valor]
    return posicoes

vetor = []
for i in range(15):
    num = int(input(f"Digite o {i+1}º número: "))
    vetor.append(num)

valor_procurado = 30
posicoes = verificar_elementos(vetor, valor_procurado)

if posicoes:
    print(f"\nO valor {valor_procurado} foi encontrado nas posições: {posicoes}")
else:
    print(f"\nO valor {valor_procurado} não foi encontrado no vetor.")
