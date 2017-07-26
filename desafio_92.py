# Desafio 92

print("campeonato de tiros\n".upper())
# Definindo os participantes
participantes = ["raphael","lucas","carlos"]
# Loop for para mostrar quem se inscreveu no campeonato
for participante in participantes:
    print(participante.title() + " acabou de se inscrever!" )
print("\nInscrições encerradas!")
print("\nO campeonato começou!\n")
# Definição dos valores de cada alvo usando dicionário
alvos = {"azul":1,"vermelho":2,"preto":3,"cinza":4}
# Loop for para tiros realizados pelos participantes
for participante in participantes:
    if participante == "raphael":
        print("O participante " + participante.title() + " acertou o "
            + "alvo azul e o alvo preto, e ganhou " 
            + str(alvos["azul"] + alvos["preto"]) + " ponto(s)." + "\n")
        pontos_raphael = [alvos["azul"],alvos["preto"]]
    elif participante == "lucas":
        print("O participante " + participante.title() + " acertou o "
            + "alvo cinza e p alvo preto, e ganhou " 
            + str(alvos["cinza"] + alvos["preto"]) + " ponto(s)." + "\n")
        pontos_lucas = [alvos["cinza"] + alvos["preto"]]
    elif participante == "carlos":
        print("O participante " + participante.title() + " acertou o "
            + "alvo azul, vermelho e preto, e ganhou " 
            + str(alvos["azul"] + alvos["vermelho"] + alvos["preto"]) 
            + " ponto(s)" + "\n")
        pontos_carlos = [alvos["azul"],alvos["vermelho"],alvos["preto"]]
# Loop for para pontos alcançados pelos participantes
for participante in participantes:
    if participante == "raphael":
        print(participante.title() + " fez " + str(sum(pontos_raphael))
            + " pontos no campeonato!")
    elif participante == "lucas":
        print(participante.title() + " fez " + str(sum(pontos_lucas)) 
            + " pontos no campeonato!")
    elif participante == "carlos":
        print(participante.title() + " fez " + str(sum(pontos_carlos)) 
            + " pontos no campeonato!")
# Loop for para ranking
print("\nranking final".upper())
for participante in participantes:
    if participante == "raphael":
        print(participante.upper() + " = " + str(sum(pontos_raphael)) + " pontos!")
    elif participante == "lucas":
        print(participante.upper() + " = " + str(sum(pontos_lucas)) + " pontos!")
    elif participante == "carlos":
        print(participante.upper() + " = " + str(sum(pontos_carlos)) + " pontos!")
# Testes condicionais para saber quem foi o campeão
if sum(pontos_raphael) > sum(pontos_carlos) and sum(pontos_raphael) > sum(pontos_lucas):
    print("\nRaphael campeão!")
if sum(pontos_lucas) > sum(pontos_raphael) and sum(pontos_lucas) > sum(pontos_carlos):
    print("\nLucas campeão!")
if sum(pontos_carlos) > sum(pontos_raphael) and sum(pontos_carlos) > sum(pontos_lucas):
    print("\nCarlos campeão!")