import pandas as pd

def processar_logs_treinamento(nome_arquivo):
  try:
    df = pd.read_csv(nome_arquivo)
    media_tempo = df['tempo_execucao'].mean()
    desvio_padrao_tempo = df['tempo_execucao'].std()
    print(f'Média do tempo de execução: {media_tempo:.2f} segundos')
    print(f'Desvio padrão do tempo de execução: {desvio_padrao_tempo:.2f} segundos')
  except FileNotFoundError:
    print('Arquivo de logs de treinamento não encontrado.')
  except Exception as e:
    print(f'Erro ao processar logs de treinamento: {e}')

nome_arquivo = 'logs_treinamento.csv'
processar_logs_treinamento(nome_arquivo)