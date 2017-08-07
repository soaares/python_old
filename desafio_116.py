# Desafio 116

# MOSTRANDO O ERRO

# >>> papel = input("Quantos cm tem esse papel ? ")
# Quantos cm tem esse papel ? 20
# >>> papel >= 15
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: '>=' not supported between instances of 'str' and 'int'

# FUNCIONANDO

# >>> papel = input("Quanto cm tem esse papel ? ")
# Quanto cm tem esse papel ? 20
# >>> papel = int(papel)
# >>> papel >= 29
# False
# >>> papel <= 29
# True
# >>>

# No primeiro caso, o erro ocorre porque está tentando ser feita uma comparação
# de um string com um inteiro, para que seja sanado o problema, é feita a conversão
# da variável 'papel' para inteiro.