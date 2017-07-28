# Desafio 95

personagens = {"shrek":"verde","homer":"amarelo","avatar":"azul"}
print("Persongens de Desenho: \n")
for person, color in personagens.items():
    print("O " + person + " é " + color)
for person, color in personagens.items():
    if person == "shrek":
        color = "marrom"
        print("O " + person + " se pintou, e agora ele é " + color + "!")
    elif person == "homer":
        color = "preto"
        print("O " + person + " derramou piche nele mesmo, e agora ele é " + color + "!")
    elif person == "avatar":
        color = "cinza"
        print("O "  + person + " passou por muita fumaça, e agora é " + color + "!")
# O dicionário é definido na linha 3 com o nome 'personagens', dentro dele contém nomes
# de personagens e suas respectivas cores. Fazendo o primeiro loop FOR para mostrar
# qual a cor atual dos personagens, esse loop consiste em definir a primeira variável
# 'person' que vai guardar os nomes dos personagens, a variável 'color' guarda as cores
# de cada personagem, e a função 'personagens.items()' faz com o loop passe pela chave
# e pelo seu respectivo valor no dicionário, no segundo loop FOR fazemos um loop 
# semelhante ao anterior, a diferença é que temos um sequência de IF-ELIF-ELIF
# dentro do loop for, para que quando o loop FOR encontre determinado valor
# na variavel 'personagem', ele altere a cor do personagem e imprima a mensagem
# que os personagens mudaram de cor. 