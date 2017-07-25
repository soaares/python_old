# Desafio 87

ingredientes = ["queijo", "tomate","presunto","oregano"]
for ingrediente in ingredientes:
    if ingrediente == "oregano":
        print("Desculpe, estamos sem " + ingrediente + ".")
    else:
        print(ingrediente.title() + " adicionado.")
print("Pizza pronta!")