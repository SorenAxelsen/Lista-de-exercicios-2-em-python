def analisar_vetor(vetor):
    pares = [num for num in vetor if num % 2 == 0]
    impares = [num for num in vetor if num % 2 != 0]
    
    quantidade_pares = len(pares)
    quantidade_impares = len(impares)
    
    return quantidade_pares, pares, quantidade_impares, impares

vetor = []
for i in range(6):
    num = int(input(f"Digite o {i+1}º número: "))
    vetor.append(num)

quantidade_pares, pares, quantidade_impares, impares = analisar_vetor(vetor)

print(f"\nQuantidade de números pares: {quantidade_pares}")
print(f"Números pares: {pares}")
print(f"Quantidade de números ímpares: {quantidade_impares}")
print(f"Números ímpares: {impares}")
