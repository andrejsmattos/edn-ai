nome = input("Digite seu nome: ")

salario_fixo = float(input("Digite seu salário fixo: "))
total_vendas = float(input("Digite o total em vendas: "))

percentual_comissao = 0.15

comissao = total_vendas * percentual_comissao

salario_total = salario_fixo + comissao

print(f"Nome do vendedor: {nome}")
print(f"Salário fixo: R${salario_fixo:.2f}")
print(f"Total de vendas: R${total_vendas:.2f}")
print(f"Comissão: R${comissao:.2f}")
print(f"Salário total: R${salario_total:.2f}")