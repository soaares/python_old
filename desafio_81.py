# Desafio 81

idade = 3
valor1 = 0
valor2 = 5
valor3 = 10
frase = "O valor do seu ingresso é: R$ "
if idade < 4:
    print(frase + str(valor1))
elif idade < 18:
    print(frase + str(valor2))
else:
    print(frase + str(valor3))

# No exemplo acima, criei as variáveis: idade, valor1, valor2, valor3 e
# frase. O primeiro IF define, caso a idade seja menor que 4, o preço do
# ingresso é 0 reais. Já no ELIF, caso a idade seja menor que 18, o preço
# do ingresso é 5 reais e no caso do ELSE, se a idade for acima de 18 o
# preço do ingresso é 10 reais. No exemplo, utilizo a função str() para
# poder concatenar INTEIROS com STRINGS. 