from fastapi import FastAPI, HTTPException
import requests
import pandas as pd
from datetime import datetime

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/api/bitcoin/price")
def get_bitcoin_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Levanta um erro para códigos de status ruins (4xx ou 5xx)
        data = response.json()
        price = data['bitcoin']['usd']
        return {"bitcoin_price_usd": price}
    except requests.exceptions.RequestException as e:
        # Retorna um erro HTTP se a requisição falhar
        raise HTTPException(status_code=500, detail=f"Erro ao buscar preço na CoinGecko: {e}")

@app.get("/api/bitcoin/history")
def get_bitcoin_history():
    # Buscamos dados dos últimos 7 dias com granularidade diária
    url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=7&interval=daily"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        # Usar Pandas para processar os dados históricos (preços)
        prices = data['prices']
        df = pd.DataFrame(prices, columns=['timestamp', 'price_usd'])
        # Converter timestamp para formato de data legível
        df['date'] = pd.to_datetime(df['timestamp'], unit='ms')

        # Retornamos os dados em formato de dicionário/JSON para o front-end
        # Convertemos o DataFrame para uma lista de dicionários para fácil consumo pelo front-end
        return df[['date', 'price_usd']].to_dict(orient='records')

    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Erro ao buscar histórico na CoinGecko: {e}")

@app.get("/api/bitcoin/data")
async def get_bitcoin_data():
    try:
        # Busca o preço em tempo real (usando o endpoint da CoinGecko)
        response_price = requests.get("api.coingecko.com")
        response_price.raise_for_status()
        price_data = response_price.json()
        current_price = price_data['bitcoin']['usd']

        # Busca os dados históricos (dos últimos 7 dias)
        response_history = requests.get("api.coingecko.com")
        response_history.raise_for_status()
        history_data = response_history.json()

        # Processa os dados históricos com pandas
        prices_history = history_data['prices']
        df = pd.DataFrame(prices_history, columns=['timestamp', 'price_usd'])
        # Converter timestamp para formato ISO
        df['date'] = pd.to_datetime(df['timestamp'], unit='ms').dt.strftime('%Y-%m-%dT%H:%M:%SZ')

        # Converte o DataFrame para uma lista de dicionários para retornar como JSON
        historical_records = df[['date', 'price_usd']].to_dict(orient='records')

        # Retorna a resposta consolidada
        return {
            "last_updated": datetime.utcnow().isoformat() + "Z",
            "current_price": current_price,
            "history": historical_records
        }
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Erro ao buscar dados na CoinGecko: {e}")


