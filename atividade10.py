def eh_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def main():
    numero = int(input("Digite um número inteiro positivo: "))
    if numero <= 0:
        print("O número deve ser positivo.")
    else:
        if eh_primo(numero):
            print(numero, "é primo.")
        else:
            print(numero, "não é primo.")

if __name__ == "__main__":
    main()
