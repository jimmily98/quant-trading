import pandas as pd
from typing import Tuple


def sma(series: pd.Series, period: int) -> pd.Series:
	"""Simple Moving Average"""
	return series.rolling(window=period, min_periods=1).mean()


def macd(series: pd.Series, fast: int = 12, slow: int = 26, signal: int = 9) -> Tuple[pd.Series, pd.Series, pd.Series]:
	"""Return macd_line, signal_line, histogram"""
	fast_ema = series.ewm(span=fast, adjust=False).mean()
	slow_ema = series.ewm(span=slow, adjust=False).mean()
	macd_line = fast_ema - slow_ema
	signal_line = macd_line.ewm(span=signal, adjust=False).mean()
	hist = macd_line - signal_line
	return macd_line, signal_line, hist


def atr(df: pd.DataFrame, period: int = 14) -> pd.Series:
	"""Average True Range"""
	high_low = df["High"] - df["Low"]
	high_close = (df["High"] - df["Close"].shift()).abs()
	low_close = (df["Low"] - df["Close"].shift()).abs()
	tr = pd.concat([high_low, high_close, low_close], axis=1).max(axis=1)
	return tr.rolling(window=period, min_periods=1).mean()

