valor_1 = input('Digite um valor: ')
valor_2 = input('Digite outro valor:')

if valor_1 > valor_2:
    print(f'{valor_1=} é maior que o valor do que {valor_2=}')
elif valor_2 > valor_1:
    print(f'{valor_2=} é maior que do que o {valor_1=}')
else:
    print(f'O {valor_1=} e o {valor_2=} são iguais.')