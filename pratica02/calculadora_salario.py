numero_funcionario = int(input("Digite o número do funcionário: "))
horas_trabalhadas = int(input("Digite o número de horas trabalhadas: "))
valor_hora = float(input("Digite o valor da hora trabalhada: "))

salario = horas_trabalhadas * valor_hora

print(f"Número do funcionário: {numero_funcionario}")
print(f"Salário: R${salario:.2f}")
print(f"Horas trabalhadas: {horas_trabalhadas}")
print(f"Valor da hora trabalhada: R${valor_hora:.2f}")
print(f"Salário: R$ {salario:.2f}")