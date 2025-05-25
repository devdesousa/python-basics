"""Vamos criar um programa, na qual o usuário digita vários valores reais positivos.
Todos estes números devem ser somados e, quando for digitado algum número negativo, o laço de repetição deverá encerrar e, na sequência, exibir a média dos valores digitados."""

media = 0
qtd = 0
soma = 0
valor = int(input('Digite um valor:'))
print(valor)

while (valor > 0):
  soma = soma + valor
  qtd = qtd + 1
  valor = int(input('Digite um valor:'))
  print(valor)

media = soma / qtd

print(f'Total da soma: {soma}')
print(f'Quantidade de entradas: {qtd}')
print(f'Media dos valores: {media}')