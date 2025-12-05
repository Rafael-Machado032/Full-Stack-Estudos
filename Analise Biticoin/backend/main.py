from fastapi import FastAPI, HTTPException
import pandas as pd
import httpx
from datetime import datetime

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "API de Análise de Bitcoin está funcionando!"}


@app.get("/api/bitcoin/data")
async def get_bitcoin_data():
    try:
        async with httpx.AsyncClient(timeout=5) as client:
            # Busca preço em tempo real
            resp_price = await client.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd")
            resp_price.raise_for_status()
            current_price = resp_price.json()['bitcoin']['usd']
            
            # Busca histórico de 7 dias
            resp_history = await client.get("https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=7&interval=daily")
            resp_history.raise_for_status()
            history_data = resp_history.json()
        
        # Processa com pandas
        prices_history = history_data['prices']
        df = pd.DataFrame(prices_history, columns=['timestamp', 'price_usd'])
        df['date'] = pd.to_datetime(df['timestamp'], unit='ms').dt.strftime('%d-%m-%Y %H:%M')
        historical_records = df[['date', 'price_usd']].to_dict(orient='records')
        
        return {
            "last_updated": datetime.utcnow().isoformat() + "Z",
            "current_price": current_price,
            "history": historical_records
        }
    except (httpx.RequestError, KeyError, ValueError) as e:
        raise HTTPException(status_code=502, detail=f"Erro ao buscar dados da CoinGecko: {e}")


