def main():
    
    vetor = []
    for i in range(15):
        elemento = int(input(f"Digite o {i+1}º elemento: "))
        vetor.append(elemento)

    
    posicoes = [posicao for posicao, elemento in enumerate(vetor) if elemento == 30]

    
    if posicoes:
        print("Elemento 30 encontrado nas posições:", posicoes)
    else:
        print("Nenhum elemento igual a 30 encontrado.")


if __name__ == "__main__":
    main()
