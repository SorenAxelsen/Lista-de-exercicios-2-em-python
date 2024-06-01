def ultimo_nome(nome_completo):
    
    partes = nome_completo.split()  
    if len(partes) == 0:
        return "Nome inválido"
    else:
        return partes[-1]  


nome = input("Digite o nome completo da pessoa: ")
ultimo = ultimo_nome(nome)
print(f"O último nome é: {ultimo}")
