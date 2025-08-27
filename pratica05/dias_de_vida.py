from datetime import datetime

try:
  ano_nascimento = int(input("Digite o ano de nascimento: "))
  ano_atual = datetime.now().year
  def calcular_idade(ano_nascimento, ano_atual):
      idade_em_dias = (ano_atual - ano_nascimento) * 365
      return print(f"Você já viveu {idade_em_dias} dias!")
except ValueError:
  print("Ano de nascimento inválido. Por favor, insira um número válido.")

calcular_idade(ano_nascimento, ano_atual)