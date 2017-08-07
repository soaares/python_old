# Desafio 119

numero = input("Digite um numero e direi se ele é par ou impar: ")
numero = int(numero)

if numero % 2 == 0:
    print("O numero " + str(numero) + " é par!")
else:
    print("O número " + str(numero) + " é impar!")
    
# Criando a variável 'numero' para guardar o valor digitado pelo usuário, em seguida
# transformando a valor em inteiro, feito isso, fazendo um teste condicional, caso
# o valor que restou da divisão do valor digitado por 2, for igual a '0', determina
# que o valor digitado é par, caso, retorne qualquer outro valor, o valor será con-
# siderado ímpar. 