# Desafio 111

idiomas = {
    'lucas':['frances','espanhol'],
    'carlos':['italiano','espanhol'],
    'raphael':['ingles','alemao'],
    'marcia':['arabe']
}
for nome, idioma in idiomas.items():
    print(nome.title() + " gosta do(s) seguinte(s) idioma(s):")
    for idi in idioma:
        print("\t" + idi)

# Criando o dicionário 'idiomas', com nomes nas chaves e nos valores, listas com idio-
# mas de preferência das pessoas. O primeiro loop FOR, utilizo a variável 'nome' para
# guardar o valor das chaves, e a variável idioma para guardar as listas e os valores
# nela contidos, no segundo loop FOR, utilizo a variável 'idi' para guardar cada valor
# contido na variável 'idioma' que já havia guardado os valores dentro das listas e de-
# pois imprindo cada idioma de preferencia das pessoas.