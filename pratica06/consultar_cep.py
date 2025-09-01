import requests

def consultar_cep(cep: str):
    url = f"https://viacep.com.br/ws/{cep}/json/"

    try:
        response = requests.get(url)
        response.raise_for_status()  # lança erro se status != 200
        dados = response.json()

        if "erro" in dados: 
            return "CEP não encontrado."

        print(f"""
                CEP: {dados.get('cep')}
                Logradouro: {dados.get('logradouro')}
                Bairro: {dados.get('bairro')}
                Cidade: {dados.get('localidade')}
                Estado: {dados.get('uf')}
              """)

    except requests.exceptions.RequestException as e:
        print(f"Erro ao consultar o CEP: {e}")

if __name__ == "__main__":
    cep = input("Digite o CEP (somente números): ")
    consultar_cep(cep)
