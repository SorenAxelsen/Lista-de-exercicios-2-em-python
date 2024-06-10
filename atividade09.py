import math

def calcular_volume_esfera(raio):
    volume = (4/3) * math.pi * (raio ** 3)
    return volume

def main():
    raio = float(input("Digite o raio da esfera: "))
    volume = calcular_volume_esfera(raio)
    print("O volume da esfera é:", volume)

if __name__ == "__main__":
    main()
