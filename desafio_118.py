# Desafio 118

numero = input("Digite um numero: ")
print("O valor digitado foi: " + numero)
numero_2 = input("Digite um segundo numero: ")
print("O numero digitado foi: " + numero_2)
print("\nDivindo os dois numeros: " + numero + "/" + numero_2)
numero = int(numero)
numero_2 = int(numero_2)
resultado = numero % numero_2
print("O que resta dessa divisão é: " + str(resultado))


# O operador '%' serve para determinar o valor que resta de uma divisão. Qualquer
# numero par, se dividido por 2 terá um valor de 'resto' = 0. 