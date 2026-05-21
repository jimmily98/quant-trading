from fastapi import FastAPI

from app.api.routers import backtest, health

app = FastAPI(title="Quant Algo-Trading Dashboard API")

app.include_router(health.router)
app.include_router(backtest.router, prefix="/backtest", tags=["backtest"])

@app.get("/", tags=["meta"])
async def root() -> dict:
	return {"service": "quant-trading-backend", "status": "ok"}
