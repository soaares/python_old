# Desafio 82

idade = 45
valor1 = 0
valor2 = 5
valor3 = 10 
frase = "O valor de entrada é: R$ "
if idade < 4:
    print(frase + str(valor1))
elif idade < 18:
    print(frase + str(valor2))
elif idade < 65:
    print(frase + str(valor3))
else: 
    print(frase + str(valor2))