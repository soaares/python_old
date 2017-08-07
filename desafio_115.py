# Desafio 115

msg = "So, are you reading this text ? If yes, please let me know!"
msg += "\nBe kind, please, tell me what's your name ? "

mensagem = input(msg)
print("Welcome, " + mensagem + ". Nice to meet you!")

# A primeira variável 'msg' guarda a primeira frase, em seguida utilizo o 
# o operador '+=' para que a segunda frase seja guardada na mesma variável
# 'msg', em seguida, a variável 'mensagem' irá guardar o valor digitado pelo
# usuário, utilizando a função 'input()' e utilizando a variável 'msg' para
# seja mostrado as msgs guardadas nela antes da resposta do usuário. Por
# último, concateno as frases com a variável 'mensagem' onde foi guardado
# a resposta do usuário.