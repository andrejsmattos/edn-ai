# Crie um script em Python que leia e escreva dados em um arquivo JSON. O arquivo JSON deve conter informações de uma pessoa, com campos nome, idade e cidade.

import csv
import json

def escrever_arquivo_json(nome_arquivo, dados):
  try:
    with open(nome_arquivo, 'w') as arquivo:
      json.dump(dados, arquivo)

  except Exception as e:
    print(f"Erro ao escrever o arquivo JSON: {e}")

def ler_arquivo_json(nome_arquivo):
  try:
    with open(nome_arquivo, 'r') as arquivo:
        dados = json.load(arquivo)
    return dados
  except FileNotFoundError:
    print(f"Arquivo '{nome_arquivo}' não encontrado.")
    return None

if __name__ == "__main__":
  nome_arquivo = input("Digite o nome do arquivo de escrita JSON: ")
  escrever_arquivo_json(nome_arquivo, dados)

  nome_arquivo = input("Digite o nome do arquivo de leitura JSON: ")
  dados = ler_arquivo_json(nome_arquivo)
  if dados:
    print("Dados lidos do arquivo JSON:")
    print(dados)


