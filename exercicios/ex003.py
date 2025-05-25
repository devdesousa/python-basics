# Desafio operadores lógicos
# Os trabalhos
terca = False
quinta = False

"""
Confirmando os 2 trabalhos = TV 50' + sorvete
Confirmando apenas 1 trabalho = TV 32' + sorvete
Nenhum dos dois = fica em casa
"""

tv_50 = terca and quinta
sorvete = terca or quinta
tv_32 = terca != quinta
ficar_em_casa = not sorvete

print(f'TV 50: {tv_50} TV 32: {tv_32} Sorvete: {sorvete} Saudável: {ficar_em_casa}')
