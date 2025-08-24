valor_reais = 100.00
taxa_dolar = 5.60
taxa_euro = 6.60

conversao_dolar = valor_reais / taxa_dolar
conversao_euro = valor_reais / taxa_euro

print(f"O valor de R${valor_reais:.2f} em dólar é U${conversao_dolar:.2f}")
print(f"O valor de R${valor_reais:.2f} em euro é U${conversao_euro:.2f}")