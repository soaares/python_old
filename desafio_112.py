# Desafio 112

users = {
    'rsoares':{
        'nome':'raphael',
        'sobrenome':'soares',
        'lugar':'recife'
    },
    'lsilva':{
        'nome':'lucas',
        'sobrenome':'silva',
        'lugar':'belo horizonte'
    }
}
for user, info_user in users.items():
    print("Nome do usuário: " + user)
    nome_completo = info_user['nome'] + " " + info_user['sobrenome']
    local = info_user['lugar']

    print("Nome completo: " + nome_completo.title())
    print("Local: " + local.title() + "\n")

# Crio o dicionário 'users' e dentro dele, duas chaves que terão dicionários como valores
# No loop FOR, a variável user vai guardar o valor das chaves, e a variável 'info_user'
# irá guardar os valores. Crio uma variável 'nome_completo' que irá fazer a concatenação
# de duas informações que estão dentro dos dicionários: 'nome' + 'sobrenome' e crio também
# uma segunda variável para guardar o 'local', por ultimo imprimo na tela as variáveis
# 'nome_completo' e 'local'. 