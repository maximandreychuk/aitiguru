from fastapi import FastAPI, HTTPException
import requests

from core import settings

app = FastAPI()
@app.get("/api/rates/")
async def get_currency_rate(
        from_currency: str,
        to_currency: str,
        value: int,
):
    """
    Получает курс валюты с внешнего сервиса и возвращает результат.
    """
    url = f"https://v6.exchangerate-api.com/v6/{settings.api.key}/latest/{from_currency}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {"result": data["conversion_rates"][to_currency]*value}
    else:
        raise HTTPException(status_code=400, detail="Ошибка получения курса валюты")
