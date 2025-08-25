soma = 0
quantidade = 0

while True:
  try:
    entrada = input("Digite uma nota entre 0 e 10: ")
    if entrada.lower() == "fim":
      break
    nota = float(entrada)
    if nota < 0 or nota > 10:
      raise ValueError()
    else:
      soma += nota
      quantidade += 1
      media = soma / quantidade
  except ValueError:
    print("Nota inválida. Digite um valor entre 0 e 10.")
    continue
  print(f"Média geral: {media:.2f}")