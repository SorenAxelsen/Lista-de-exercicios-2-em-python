def eh_primo(numero):
    
    if numero <= 1:
        return False
    elif numero <= 3:
        return True
    elif numero % 2 == 0 or numero % 3 == 0:
        return False
    else:
        
        for i in range(5, int(numero ** 0.5) + 1, 6):
            if numero % i == 0 or numero % (i + 2) == 0:
                return False
        return True


num = int(input("Digite um número inteiro positivo: "))
if eh_primo(num):
    print(f"O número {num} é primo.")
else:
    print(f"O número {num} não é primo.")
