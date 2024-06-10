def main():
    
    produtos = []
    precos = []

    
    for i in range(5):
        produto = input(f"Nome do produto {i+1}: ")
        preco = float(input("Preço do produto: R$"))
        produtos.append(produto)
        precos.append(preco)

    
    qtd_inferior_50 = sum(1 for preco in precos if preco < 50)

    
    produtos_50_100 = [produtos[i] for i in range(len(produtos)) if 50 <= precos[i] <= 100]

    
    precos_superior_100 = [preco for preco in precos if preco > 100]
    media_precos_superior_100 = sum(precos_superior_100) / len(precos_superior_100) if precos_superior_100 else 0

    
    print("\nQuantidade de produtos com preço inferior a R$ 50,00:", qtd_inferior_50)
    print("Nome dos produtos com preço entre R$ 50,00 e R$ 100,00:", produtos_50_100)
    print("Média dos preços dos produtos com preço superior a R$ 100,00: R${:.2f}".format(media_precos_superior_100))


if __name__ == "__main__":
    main()
