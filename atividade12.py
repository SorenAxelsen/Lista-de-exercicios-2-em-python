def ultimo_nome(nome_completo):
    partes = nome_completo.split()  
    if partes:  
        return partes[-1]  
    else:
        return None  

def main():
    nome = input("Digite o nome completo da pessoa: ")
    ultimo = ultimo_nome(nome)
    if ultimo:
        print("O último nome é:", ultimo)
    else:
        print("Nome inválido.")

if __name__ == "__main__":
    main()
