# Desafio 80

idade = 19
valor1 = "R$ 5,00" 
valor2 = "R$ 10,00"
if idade < 4:
    print("Você não paga entrada.")
elif idade < 18:
    print("O valor de ingresso para sua idade é: " + valor1)
else:
    print("O valor de ingresso para sua idade é: " + valor2)

# No exemplo acima, defino a idade de uma pessoa, em seguida 
# defino os valores dos ingressos, e então, no teste condicional
# IF, verifico se a idade é menor que 4 anos, caso seja, imprimo
# a mensagem que esta pessoa não pagará a entrada, no segundo teste
# ELIF, no caso, verifico se a idade da pessoa é menor que 18 anos
# caso seja, imprimo a mensagem que o valor da entrada para sua idade
# é 5 reais, no ELSE, se a pessoa tiver mais que 18 anos anos, o valor
# de ingresso é de 10 reais.