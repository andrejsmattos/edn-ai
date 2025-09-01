import requests

def obter_usuario_aleatorio():
    url = "https://randomuser.me/api/"

    try:
        response = requests.get(url)
        response.raise_for_status()
        dados = response.json()['results'][0]

        nome = dados['name']['first']
        email = dados['email']
        pais = dados['location']['country']

        return f"Nome: {nome}\nEmail: {email}\nPaís: {pais}"
    
    except requests.RequestException as e:
        return f"Erro ao obter usuário aleatório: {e}"

def main():   
  print("Gerando usuário aleatório...")
  usuario_aleatorio = obter_usuario_aleatorio()
  print(usuario_aleatorio)

if __name__ == "__main__":
    main()