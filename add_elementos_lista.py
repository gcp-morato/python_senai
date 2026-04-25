# Criando uma lista vazia
compras = []

# Adicionando itens um por um
compras.append("arroz")
compras.append("feijão")
compras.append("macarrão")
compras.append(input("Insira um produto na lista de compras: "))

print(compras)  # ['arroz', 'feijão', 'macarrão']

# Lista de Compras 

compras = [ ]
i = 0

print("Usando o metodo append com While")

while i < 10:
    item = input("Insira o item para salvar na lista de compras: ")
    compras.append(item) 
    i +=1

print("Segue o itens de compra: ", compras)    