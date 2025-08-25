numerosPares = []
numerosImpares = []

while True:
  try:
    entrada = input("Digite um número: ")
    if entrada.lower() == "fim":
      break
    
    numero = int(entrada)
    if numero % 2 == 0:
      numerosPares.append(numero)
      print("O número é par.")
    elif numero % 2 != 0:
      numerosImpares.append(numero)
      print("O número é ímpar.")
    else:
      raise ValueError()
    print(f"Quantidade de números pares: {len(numerosPares)}")
    print(f"Quantidade de números ímpares: {len(numerosImpares)}")

  except ValueError:
    print("Este não é um número válido. Tente novamente, inserindo um número inteiro.")
    
print("Programa encerrado.")