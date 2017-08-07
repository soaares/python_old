# Desafio 110

pizzas = {
    'sabor':'queijo',
    'coberturas':['muzzarela','queijo','presunto']
}
print("A pizza pedida foi de " + pizzas['sabor'] + ".")
print("E as coberturas são:")
for cobertura in pizzas['coberturas']:
    print("\t" + cobertura)

# Crio um dicionário com o nome 'pizzas', nesse dicionário temos dois pares
# de chaves-valores, na primeira chave temos qual a pizza foi escolhida, na
# segunda, as coberturas que essa pizza tem dentro de uma lista, imprimimos
# qual pizza foi escolhida e em seguida fazemos um loop FOR, a variável co-
# bertura vai pegar cada valor da lista na chave 'coberturas' para que seja
# imprimida, mostrando quais coberturas a pizza tem. 