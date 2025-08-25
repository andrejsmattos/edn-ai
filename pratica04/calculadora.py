while True:
  try: 
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    operacao = input("Digite a operação (+, -, *, /): ")

    if operacao == "+":
        resultado = num1 + num2
    elif operacao == "-":
        resultado = num1 - num2
    elif operacao == "*":
        resultado = num1 * num2
    elif operacao == "/":
        if num2 != 0:
            resultado = num1 / num2
        else:
            print("Erro: Divisão por zero.")
            resultado = None
    else:
        raise ValueError("Operação inválida")

    print(f"Resultado: {resultado}")
    break

  except ZeroDivisionError as e:
    print(f"Erro: {e}")

  except ValueError as e:
    print(f"Erro: {e}: Por favor, tente novamente.")
