nome_do_produto = input("Digite o nome do produto: ")
preco_do_produto = float(input("Digite o preço do produto: "))
quantidade = int(input("Digite a quantidade: "))

valor_total = preco_do_produto * quantidade

print(f"O valor total de {quantidade} unidade(s) de {nome_do_produto} é R${valor_total:.2f}")