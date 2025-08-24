nome_produto = "Camiseta"
preco_original = 50.00
porcentagem_desconto = 0.20
preco_desconto = preco_original * (1 - porcentagem_desconto)

print(f"O produto {nome_produto} custa R${preco_original:.2f}, mas com desconto de {porcentagem_desconto * 100:.0f}%, ele sai por R${preco_desconto:.2f}.")
print(f"O desconto foi de R${preco_original - preco_desconto:.2f}.")