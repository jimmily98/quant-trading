import asyncio
import math
from typing import Optional
import pandas as pd
import yfinance as yf

from app.models import schemas
from app.services.indicators import sma, macd
from app.models.db import engine
from sqlmodel import Session
from app.models.orm_models import BacktestRecord


async def run_backtest(request: schemas.BacktestRequest) -> schemas.BacktestResult:
	"""Fetch historical data and run a simple momentum backtest.

	Execution rules (deterministic simple model):
	- Signals computed per close price: BUY when fast_sma > slow_sma and MACD > 0.
	- Trades are executed at the next trading day's `Open` price when available.
	- On BUY: allocate as much cash as possible (integer shares).
	- On SELL: liquidate all shares.
	- Starting capital: $10,000.
	"""

	def _sync_work() -> Optional[schemas.BacktestResult]:
		df = yf.download(request.ticker, start=request.start_date.isoformat(), end=request.end_date.isoformat(), progress=False)
		if df is None or df.empty:
			return None

		# Ensure required columns
		required = {"Open", "High", "Low", "Close", "Volume"}
		if not required.issubset(set(df.columns)):
			return None

		close = df["Close"]
		fast = sma(close, request.fast_sma)
		slow = sma(close, request.slow_sma)
		macd_line, _, _ = macd(close)

		signal = (fast > slow) & (macd_line > 0)

		cash = 10000.0
		position = 0  # number of shares held
		trades = 0

		# Use next day's open for execution
		next_open = df["Open"].shift(-1)

		for idx in range(len(df)):
			try:
				cur_signal = bool(signal.iloc[idx])
			except Exception:
				continue

			exec_price = None
			if idx < len(df) - 1:
				exec_price = next_open.iloc[idx]

			# BUY
			if cur_signal and position == 0 and exec_price and not pd.isna(exec_price):
				shares = math.floor(cash / float(exec_price))
				if shares > 0:
					position = shares
					cash -= shares * float(exec_price)
					trades += 1

			# SELL
			if (not cur_signal) and position > 0 and exec_price and not pd.isna(exec_price):
				cash += position * float(exec_price)
				position = 0
				trades += 1

		last_close = float(df["Close"].iloc[-1])
		final_value = cash + position * last_close

		# persist result
		record = BacktestRecord(
			ticker=request.ticker,
			start_date=request.start_date,
			end_date=request.end_date,
			final_portfolio_value=float(final_value),
			total_trades_executed=int(trades),
		)

		with Session(engine) as session:
			session.add(record)
			session.commit()

		return schemas.BacktestResult(
			ticker=request.ticker,
			start_date=request.start_date,
			end_date=request.end_date,
			final_portfolio_value=float(final_value),
			total_trades_executed=int(trades),
		)

	result = await asyncio.to_thread(_sync_work)
	if result is None:
		raise ValueError("no data for ticker / date range")
	return result
