from typing import Optional
from sqlmodel import SQLModel, Field
from datetime import date


class BacktestRecord(SQLModel, table=True):
	id: Optional[int] = Field(default=None, primary_key=True)
	ticker: str
	start_date: date
	end_date: date
	final_portfolio_value: float
	total_trades_executed: int
