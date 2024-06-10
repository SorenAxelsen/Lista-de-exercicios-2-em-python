def main():
    
    vendas = []
    comissoes = []
    nomes = []

    
    for i in range(10):
        nome = input(f"Nome do vendedor {i+1}: ")
        vendas.append(float(input("Total de vendas do vendedor: ")))
        comissoes.append(float(input("Percentual de comissão (%): ")))
        nomes.append(nome)

    
    valores_receber = []
    for venda, comissao in zip(vendas, comissoes):
        valor_receber = venda * (comissao / 100)
        valores_receber.append(valor_receber)

    
    print("\nRelatório:")
    for nome, valor in zip(nomes, valores_receber):
        print(f"{nome}: R${valor:.2f}")

    
    total_vendas = sum(vendas)
    print("\nTotal das vendas de todos os vendedores:", total_vendas)

    
    maior_valor = max(valores_receber)
    menor_valor = min(valores_receber)
    maior_valor_nome = nomes[valores_receber.index(maior_valor)]
    menor_valor_nome = nomes[valores_receber.index(menor_valor)]
    print("Maior valor a receber:", maior_valor, "- Receberá:", maior_valor_nome)
    print("Menor valor a receber:", menor_valor, "- Receberá:", menor_valor_nome)


if __name__ == "__main__":
    main()
