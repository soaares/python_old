# Desafio 54

frutas = ["banana","maçã","melão"]
print("Lista de frutas:")
print(frutas)
fruits = frutas[:]
print("\nLista 'frutas':")
print(frutas)
print("\nLista 'fruits':")
print(fruits)
frutas.append("uva")
fruits.append("melancia")
print("\nLista 'frutas':")
print(frutas)
print("\nLista 'fruits':")
print(fruits)
for fruta in frutas:
    print("Eu gosto de: "+ fruta)
for fruit in fruits:
    print("Meus amigos gostam de: " + fruit)
