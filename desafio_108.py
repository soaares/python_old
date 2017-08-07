# Desafio 108

inimigos = []
for novo_alien in range(30):
    novo_alien = {'cor':'verde','velocidade':'rapido','pontos':5}
    inimigos.append(novo_alien)
for alien in inimigos[:5]:
    print(alien)
print("\nNós criamos " + str(len(inimigos)) + " novos aliens.")

# Crio uma lista vazia 'inimigos', faço um loop for com a função 'range()' e 30
# como parâmetro, para que o loop seja executado 30 vezes, dentro do loop
# defino que a variável 'novo_alien' como um dicionário, com os pares de 
# chaves-valores, cor, velocidade e pontos, depois insiro dentro da lista vazia
# o dicionário com o método '.append()', depois é feito mais um loop for para
# que seja mostrado os 5 primeiros dicionários na lista 'inimigos', para isso
# uso o método de fatiamento '[:5]', por último, imprimo a msg dizendo quantos
# novos aliens foram criados, para isso utilizo a função 'len()'.