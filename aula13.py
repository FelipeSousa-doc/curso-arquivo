nome = 'Luiz Otávio'
altura = 1.80
peso = 95
imc = peso / (altura ** 2)

#f-strings (formatação de strings)
linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'pesa {peso} quilos e seu IMC é '
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)

# '...' é chamado de Ellipsis e não gera erro ao ser executado
