# Desafio 89

coberturas_disponiveis = ["queijo","tomate","catupiry"]
pedido_pizza = ["palmito","tomate","queijo"]
for cobertura in pedido_pizza:
    if cobertura in coberturas_disponiveis:
        print(cobertura.title() + " adicionado(a).")
    else:
        print("Não temos " + cobertura + " disponível, senhor!")
