from math import pi

def circulo(raio):
    print(f'O valor da área da circunferência é:', pi * float(raio) ** 2)

raio = input("Digite o raio para descobrimos a área da circunferência: ")

print (circulo(raio))