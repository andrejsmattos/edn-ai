temperatura = float(input("Digite a temperatura: "))
unidade_origem = input("Digite a unidade de origem (C, F ou K): ").upper()
unidade_destino = input("Digite a unidade de destino (C, F ou K): ").upper()

if unidade_origem == unidade_destino:
  temperatura = unidade_origem
  print(f"A temperatura não foi alterada: {temperatura:.2f}.")

if unidade_origem == "C" and unidade_destino == "F":
  temp_fahrenheit = (temperatura * 9/5) + 32
  print(f"{temperatura} graus Celsius equivalem a {temp_fahrenheit:.2f} graus Fahrenheit.")

if unidade_origem == "C" and unidade_destino == "K":
  temp_kelvin = temperatura + 273.15
  print(f"{temperatura} graus Celsius equivalem a {temp_kelvin:.2f} graus Kelvin.")

if unidade_origem == "F" and unidade_destino == "C":
  temp_celsius = (temperatura - 32) * 5/9
  print(f"{temperatura} graus Fahrenheit equivalem a {temp_celsius:.2f} graus Celsius.")

if unidade_origem == "F" and unidade_destino == "K":
  temp_kelvin = (temperatura - 32) * 5/9 + 273.15
  print(f"{temperatura} graus Fahrenheit equivalem a {temp_kelvin:.2f} graus Kelvin.")

if unidade_origem == "K" and unidade_destino == "C":
  temp_celsius = temperatura - 273.15
  print(f"{temperatura} graus Kelvin equivalem a {temp_celsius:.2f} graus Celsius.")

if unidade_origem == "K" and unidade_destino == "F":
  temp_fahrenheit = (temperatura - 273.15) * 9/5 + 32
  print(f"{temperatura} graus Kelvin equivalem a {temp_fahrenheit:.2f} graus Fahrenheit.")