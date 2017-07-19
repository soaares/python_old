# Desafio 76 

users_banidos = ["Carlos","Marcos","Isabella"]
users = ["Carlos", "Marcos", "Isabella","Laura","Maria","João"]
for user in users:
    if user not in users_banidos:
        print(user + ", você já pode enviar sua resposta agora!")
    else:
        print("Usuário " + user + ", você está bloqueado!")