import requests

def cotar_moeda(moeda):
    url = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"

    try:
        response = requests.get(url)
        response.raise_for_status()
        dados = response.json()
        cotacao = dados[f"{moeda}BRL"]
        return f"""
          Moeda: {moeda} para BRL
          Valor atual: R${float(cotacao["bid"]):.2f}
          Máximo: R${float(cotacao["high"]):.2f}
          Mínimo: R${float(cotacao["low"]):.2f}
          Data/Hora: {cotacao["create_date"]}
        """
    
    except requests.exceptions.RequestException as e:
      return f"Erro {e} ao obter cotação"
    except KeyError:
      return f"Moeda {moeda} não encontrada"
  
def main():
  moeda = input("Digite o código da moeda para cotação (Ex.: USD, EUR, BTC): ").upper().strip()
  resultado = cotar_moeda(moeda)
  print(resultado)

if __name__ == "__main__":
  main()
    
    