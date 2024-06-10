def main():
    
    vetor = []
    for i in range(6):
        num = int(input(f"Digite o {i+1}º número: "))
        vetor.append(num)

    
    pares = [num for num in vetor if num % 2 == 0]
    impares = [num for num in vetor if num % 2 != 0]

    
    print("Quantidade de números pares:", len(pares))
    print("Números pares:", pares)
    print("Quantidade de números ímpares:", len(impares))
    print("Números ímpares:", impares)


if __name__ == "__main__":
    main()
