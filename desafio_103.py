# Desafio 103

idiomas = {
    "lucas":"ingles",
    "raphael":"frances",
    "carlos":"espanhol",
    "sergio":"russo"
}
pessoas = ["raphael","lucas"]
for nome in idiomas.keys():
    if nome not in pessoas:
        print("Você não sabe nenhum idioma, " + nome.title() + " ?")

# Defino o dicionário 'idiomas', e insiro os pares de chaves-valores
# Faço uma lista com dois nomes para serem utilizados no teste condicional
# Utilizo o loop for para percorrer todo o dicionário e no teste condicional
# uso o 'not in', caso o nome que está sendo varrido no dicionário, não conste
# na lista 'pessoas', será impresso a msg. 
        
        

