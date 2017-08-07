# Desafio 109

inimigos = []
for alien in range(30):
    alien = {'cor':'verde','velocidade':'rapido','pontos':5}
    inimigos.append(alien)
for alien in inimigos[:3]:
    if alien['cor'] == 'verde':
        alien['cor'] = 'azul'
        alien['velocidade'] = 'media'
        alien['pontos'] = 2
for aliens in inimigos:
    print(aliens)

# Criando a lista 'inimigos' vazia, utilizo o loop for com a função range()
# com o parametro 30 para que seja criado 30 novos aliens e os adiciono a 
# lista vazia, no loop seguinte, utilizo o fatiamento para que o loop funcione
# apenas nos 3 primeiros itens da lista 'inimigos', utilizando um IF dentro do
# loop, caso a cor do alien seja verde, a cor, a velocidade e os pontos serão
# alterados para o novo valor, definido dentro do loop, por ultimo, imprimir
# as informações sobre os aliens dentro da lista.