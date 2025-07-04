# Nesse segundo exercicio de area da circunferencia, vamos começar a tornar ele mais completo
from math import pi

def circulo(raio):
    return pi * float(raio) ** 2

raio = input("Digite o raio para descobrimos a área da circunferência: ")
area = circulo(raio)

print (area)


