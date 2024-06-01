def main():
    NUM_VENDEDORES = 10

    
    nomes = []
    vendas = []
    comissoes = []
    valores_a_receber = []

    
    for i in range(NUM_VENDEDORES):
        nome = input(f"Digite o nome do {i+1}º vendedor: ")
        nomes.append(nome)

        venda = float(input(f"Digite o total das vendas de {nome}: "))
        vendas.append(venda)

        comissao = float(input(f"Digite o percentual de comissão de {nome} (em %): "))
        comissoes.append(comissao)

        
        valor_a_receber = venda * (comissao / 100)
        valores_a_receber.append(valor_a_receber)

    
    total_vendas = sum(vendas)

    
    maior_valor = max(valores_a_receber)
    menor_valor = min(valores_a_receber)
    vendedor_maior_valor = nomes[valores_a_receber.index(maior_valor)]
    vendedor_menor_valor = nomes[valores_a_receber.index(menor_valor)]

    
    print("\nRelatório de Comissões:")
    for i in range(NUM_VENDEDORES):
        print(f"Vendedor: {nomes[i]}, Valor a receber: R$ {valores_a_receber[i]:.2f}")

    print(f"\nTotal das vendas de todos os vendedores: R$ {total_vendas:.2f}")
    print(f"Maior valor a receber: R$ {maior_valor:.2f} (Vendedor: {vendedor_maior_valor})")
    print(f"Menor valor a receber: R$ {menor_valor:.2f} (Vendedor: {vendedor_menor_valor})")


if __name__ == "__main__":
    main()
