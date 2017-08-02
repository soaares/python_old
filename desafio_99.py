# Desafio 99

nomes = {"raphael":"soares","carlos":"almeida","lucas":"rodrigues"}
for nome, sobrenome in nomes.items():
    print("Olá, meu nome é " + nome.title() + " " + sobrenome.title() + ".")

# Defino o dicionario 'nomes' e defino as chaves-valores, em seguida utilizo o loop
# for com as variáveis 'nome' pra guardar a chave do dicionário, e a variável
# 'sobrenome' pra guardar o valor da chave, declaro tbm o dicionário 'nomes' com 
# o método '.items()' para que ele retorne cada chave e valor no loop. Depois
# só imprime a msg com o nome e sobrenome que está no dicionário.