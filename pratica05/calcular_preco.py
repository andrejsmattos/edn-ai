def calcular_desconto(preco_original, percentual_desconto):
  desconto = preco_original * (percentual_desconto / 100)
  preco_final = preco_original - desconto
  return print(f"Valor original do produto: R$ {preco_original:.2f}\nValor do desconto: R$ {desconto:.2f}\nValor final do produto: R$ {preco_final:.2f}")

try:
  preco_original = float(input("Digite o preço original do produto: "))
  percentual_desconto = float(input("Digite o percentual de desconto: "))
  calcular_desconto(preco_original, percentual_desconto)
except ValueError:
  print("Ocorreu um erro ao calcular o desconto. Verifique se digitou apenas números.")