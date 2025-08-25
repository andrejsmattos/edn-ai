while True:
  senha = input("Digite a senha com 8 caracteres ou mais e pelo menos um número: ")
  if len(senha) >= 8 and any(char.isdigit() for char in senha):
    print("Senha forte!")
    break
  elif senha.lower() == "sair":
    print("Saindo do programa...")
    break
  else:
    print("Senha fraca! Tente novamente.")