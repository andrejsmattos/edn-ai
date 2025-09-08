import csv 

def ler_csv(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            leitor = csv.reader(arquivo)
            dados = list(leitor)
            for linha in dados:
              if linha:
                  print(", ".join(linha))
            return dados

    except Exception as e:
        print(f"Erro ao ler o arquivo CSV: {e}")

if __name__ == "__main__":
    nome_arquivo = input("Digite o nome do arquivo CSV: ")
    dados = ler_csv(nome_arquivo)
