# Desafio 100

nomes = {
    "raphael":"soares",
    "lucas":"lira",
    "diego":"souza"
    }
for nome, sobrenome in nomes.items():
    print("Olá, meu nome é " + nome.title() + " " + sobrenome.title())

# Defino o dicionário 'nomes', defino os pares de chave-valor e o loop for com duas
# variáveis, 'nome' e 'sobrenome', a variável 'nome' para guardar o valor da chave
# e a variável 'sobrenome' para guardar o valor da chave, e uso novamente o metodo
# '.items()' no loop for, em seguida imprimo a msg mostrando nome e sobrenome 
# concatenados.