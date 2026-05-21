import asyncio
from typing import Optional
import pandas as pd
import yfinance as yf

from app.models import schemas
from app.services.indicators import sma, macd


async def run_backtest(request: schemas.BacktestRequest) -> schemas.BacktestResult:
	"""Fetch historical data and run a simple momentum backtest.

	This is a lightweight, deterministic placeholder implementation that:
	- fetches OHLCV with `yfinance`
	- computes SMA and MACD
	- counts signal crossovers as trades
	- returns a mock final portfolio value
	"""

	def _sync_work() -> Optional[schemas.BacktestResult]:
		df = yf.download(request.ticker, start=request.start_date.isoformat(), end=request.end_date.isoformat(), progress=False)
		if df is None or df.empty:
			return None

		close = df["Close"]
		fast = sma(close, request.fast_sma)
		slow = sma(close, request.slow_sma)
		macd_line, _, _ = macd(close)

		# simple momentum signal: when fast > slow and macd > 0
		signal = (fast > slow) & (macd_line > 0)
		trades = int(signal.astype(int).diff().abs().sum())

		# Placeholder P&L: keep capital unchanged (to be implemented)
		final_value = 10000.0

		return schemas.BacktestResult(
			ticker=request.ticker,
			start_date=request.start_date,
			end_date=request.end_date,
			final_portfolio_value=float(final_value),
			total_trades_executed=trades,
		)

	result = await asyncio.to_thread(_sync_work)
	if result is None:
		raise ValueError("no data for ticker / date range")
	return result
