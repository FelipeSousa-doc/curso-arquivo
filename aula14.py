a = 'A'
b = 'B'
c = 1.1 
string = 'a={} b={nome2} c={nome3:.2f}'

# Nomeando os argumentos com parâmetros
formato = string.format(a, nome2=b, nome3=c)

print(formato)
