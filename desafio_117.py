# Desafio 117

altura = input("Olá, bem-vindo! Qual sua altura? ")
altura = int(altura)
if altura >= 45:
    print("Você pode andar neste brinquedo!")
else:
    print("Você não tem altura suficiente para andar neste brinquedo!"
    + "\nQual sua idade?")

# Crio a variável 'altura' para guardar a resposta do usuário, no caso, a altura
# Transformo a variável para um valor inteiro para que possa ser feito o teste
# condicional, caso tenha mais ou 45 polegadas é executado o bloco dentro de IF
# permitindo entrar no brinquedo, caso tenho menos de 45 polegadas, é executado
# o bloco ELSE, não permitindo a entrada e perguntando a idade.