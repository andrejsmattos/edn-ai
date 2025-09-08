import csv

def escrever_csv(nome_arquivo, dados):
    if not nome_arquivo.endswith('.csv'):
        nome_arquivo += '.csv'

    try:
      with open(nome_arquivo, 'w', encoding='utf-8') as arquivo_csv:
          escritor = csv.writer(arquivo_csv)
          escritor.writerow(['Nome', 'Idade', 'Cidade'])
          for linha in dados:
              escritor.writerow(linha)
      print(f"Dados salvos em {nome_arquivo} com sucesso.")

    except Exception as e:
        print(f"Erro ao escrever no arquivo CSV: {e}")

dados = [
    ['João', 25, 'São Paulo'],
    ['Maria', 30, 'Rio de Janeiro'],
    ['Carlos', 22, 'Belo Horizonte']
]

if __name__ == "__main__":
    nome_arquivo = input("Digite o nome do arquivo CSV: ").strip()
    escrever_csv(nome_arquivo, dados)