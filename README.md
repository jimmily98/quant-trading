
# Quant Algo-Trading Dashboard

Lightweight web dashboard to backtest and visualize momentum-based algorithmic trading strategies.

## Features
- Fetch historical OHLCV via `yfinance` (backend)
- Compute SMA, MACD, ATR indicators
- Generate momentum BUY/SELL signals (SMA cross + MACD)
- Backtest engine simulating trades from an initial capital
- Interactive React + TypeScript frontend with candlestick charts and indicator subcharts

## Quickstart (backend)
1. Create and activate a Python virtualenv:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Run the FastAPI server:

```powershell
uvicorn backend.app.main:app --reload --host 127.0.0.1 --port 8000
```

Open Swagger UI at `http://127.0.0.1:8000/docs` to test the backtest API.

## Quickstart (frontend)
From `frontend/`:

```bash
npm install
npm run dev
```

## Repository
Remote: https://github.com/jimmily98/quant-trading

## Contributing
- Follow PEP 8 and type-hinting for Python code.
- Routes in `backend/app/api/routers/`; core calculations in `backend/app/services/`.

---
Created from project scaffold. See `demands.md` for requirements and feature list.
