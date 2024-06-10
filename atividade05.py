def is_primo(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def main():
    
    vetor = []
    for i in range(15):
        num = int(input(f"Digite o {i+1}º número inteiro: "))
        vetor.append(num)

    
    vetor_primos = [num for num in vetor if is_primo(num)]

    
    print("\nVetor resultante contendo apenas números primos:")
    print(vetor_primos)

if __name__ == "__main__":
    main()
