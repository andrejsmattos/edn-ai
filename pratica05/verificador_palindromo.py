def verificar_palindromo(palavra):
    palavra = palavra.lower().replace(" ", "")
    palavra_invertida = "".join(reversed(palavra))
    if palavra == palavra_invertida:
        print(f"Sim. A palavra {palavra} é um palíndromo.")
        return True
    else:
        print(f"Não. A palavra {palavra} não é um palíndromo.")
        return False

while True:
    palavra = input("Digite uma palavra (ou digite 'sair' para encerrar): ")
    if palavra.lower() == 'sair':
        break
    verificar_palindromo(palavra)