from pydantic import BaseModel
from datetime import date
from typing import Optional


class BacktestRequest(BaseModel):
	ticker: str
	start_date: date
	end_date: date
	fast_sma: int = 20
	slow_sma: int = 50


class BacktestResult(BaseModel):
	ticker: str
	start_date: date
	end_date: date
	final_portfolio_value: float
	total_trades_executed: int
