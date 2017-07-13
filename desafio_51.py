# Desafio 51
print("Lista 'coisas':")
coisas = ["carro","chave","tesoura"]
print(coisas)
print("\nCopiando a lista...\n")
things = coisas[:]
print("Lista 'coisas':")
print(coisas)
print("\nLista 'things':")
print(things)
print("\nAdicionando uma palavra diferente para cada lista:")
coisas.append("cola")
things.append("papel")
print("\nLista 'coisas':")
print(coisas)
print("\nLista 'coisas_2':")
print(things)