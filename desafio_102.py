# Desafio 102

idiomas = {
    'lucas':'francês',
    'carlos':'espanhol',
    'raphael':'inglês',
    'jorge':'alemão'
}
pessoas = ["raphael","lucas"]
for nome in idiomas:
    if nome in pessoas:
        print("Olá " + nome.title() + ", fiquei sabendo que o seu idioma preferido é o "
        + idiomas[nome] + ".")

# Definindo o dicionário 'idiomas' e inserindo as chaves-valores, defino uma lista 
# 'pessoas' para utilizar no teste condicional, faço o loop for para que ele percorra
# todos os pares de chaves-valores e faço um teste condicional para que só seja impresso
# a msg de boas-vindas, caso o nome conste na lista pessoas que eu havia definido. 