def main():
    NUM_PRODUTOS = 5

    
    nomes_produtos = []
    precos_produtos = []

    
    for i in range(NUM_PRODUTOS):
        nome = input(f"Digite o nome do {i+1}º produto: ")
        nomes_produtos.append(nome)

        preco = float(input(f"Digite o preço de {nome} (em R$): "))
        precos_produtos.append(preco)

    
    quantidade_inferior_50 = sum(1 for preco in precos_produtos if preco < 50.00)

    
    produtos_entre_50_100 = [nomes_produtos[i] for i in range(NUM_PRODUTOS) if 50.00 <= precos_produtos[i] <= 100.00]

    
    precos_superior_100 = [preco for preco in precos_produtos if preco > 100.00]
    if precos_superior_100:
        media_superior_100 = sum(precos_superior_100) / len(precos_superior_100)
    else:
        media_superior_100 = 0

    
    print(f"\nQuantidade de produtos com preço inferior a R$ 50,00: {quantidade_inferior_50}")
    
    print("\nProdutos com preço entre R$ 50,00 e R$ 100,00:")
    for produto in produtos_entre_50_100:
        print(produto)

    if precos_superior_100:
        print(f"\nMédia dos preços dos produtos com preço superior a R$ 100,00: R$ {media_superior_100:.2f}")
    else:
        print("\nNão há produtos com preço superior a R$ 100,00.")


if __name__ == "__main__":
    main()
