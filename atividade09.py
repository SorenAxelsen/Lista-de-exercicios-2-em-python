import math

def calcular_volume_esfera(raio):
    
    if raio < 0:
        return "O raio deve ser um valor não negativo."
    else:
        volume = (4/3) * math.pi * (raio ** 3)
        return volume


raio = float(input("Digite o raio da esfera: "))
volume = calcular_volume_esfera(raio)
print(f"O volume da esfera com raio {raio} é: {volume:.2f}")
