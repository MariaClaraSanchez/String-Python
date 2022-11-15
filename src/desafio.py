from extrator_url import ExtratorURL

def conversor():

    url = "bytebank.com/cambio?quantidade=100&moedaOrigem=dolar&moedaDestino=real"
    extrator_url = ExtratorURL(url)

    VALOR_DOLAR = 5.33  # 1 dólar = 5,33 reais
    moeda_origem = extrator_url.get_valor_parametro("moedaOrigem")
    moeda_destino = extrator_url.get_valor_parametro("moedaDestino")
    quantidade = extrator_url.get_valor_parametro("quantidade")

    if moeda_origem == "real" and moeda_destino == "dolar":
        print(f"R${quantidade}reais = ${int(quantidade) / VALOR_DOLAR} dólares!!")
    elif moeda_origem == "dolar" and moeda_destino == "real":
        print(f" ${quantidade} dólares = R${(int(quantidade) * VALOR_DOLAR)} reais!!")
    else:
        print(f"A conversão de {moeda_origem} para {moeda_destino} não está disponível!")


conversor()
