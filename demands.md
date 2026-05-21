# Project Name: Quant Algo-Trading Dashboard

## 1. Project Overview

This project is a web-based dashboard that allows users to backtest and visualize momentum-based algorithmic trading strategies on historical stock data. It will pull market data, calculate specific technical indicators, and simulate buy/sell signals.

## 2. Tech Stack & Architecture Preferences

* **Backend:** Python with FastAPI (for high-performance API routing).
* **Frontend:** React (using TailwindCSS for styling and Recharts for data visualization).
* **Database:** SQLite (for simple, file-based local storage of backtest results).
* **Data Fetching:** `yfinance` library for historical market data.

## 3. Core Features & Business Logic

* **Market Data Ingestion:** The user can input a ticker symbol (e.g., AAPL) and a date range. The backend fetches daily OHLCV (Open, High, Low, Close, Volume) data.
* **Indicator Calculation:** The backend must calculate three technical indicators on the fetched data:
  * Simple Moving Average (SMA) - user-configurable periods (e.g., 20-day, 50-day).
  * Moving Average Convergence Divergence (MACD).
  * Average True Range (ATR) for volatility measurement.
* **Signal Generation:** Implement a basic momentum strategy: generate a 'BUY' signal when the fast SMA crosses above the slow SMA and MACD is positive. Generate a 'SELL' signal on the inverse.
* **Backtesting Engine:** Calculate the hypothetical portfolio return if the user started with $10,000 and executed trades based exclusively on the generated signals. 

## 4. Data Models / Database Schema

* **BacktestRecord:**
  * `id` (Integer, Primary Key)
  * `ticker` (String)
  * `start_date` (Date)
  * `end_date` (Date)
  * `final_portfolio_value` (Float)
  * `total_trades_executed` (Integer)

## 5. UI/UX Requirements

* **Control Panel (Sidebar):** Input fields for Ticker, Start Date, End Date, and sliders to adjust the SMA periods. A "Run Backtest" button.
* **Main Chart Area:** A large candlestick chart displaying the price data. The SMA lines should be overlaid on the price chart. MACD and ATR should be displayed in smaller sub-charts below the main price chart.
* **Metrics Cards:** Display the Final Portfolio Value, Total Return %, and Number of Trades at the top of the dashboard.

## 6. Constraints & Coding Standards

* All Python code must use strict type hinting (`typing` module) and PEP 8 standards.
* The API endpoints must be fully documented using FastAPI's auto-generated Swagger UI.
* Use asynchronous programming (`async/await`) for all FastAPI route handlers and database calls.
* Do not write monolithic files; separate concerns into `routers/`, `services/` (for pandas calculations), and `models/`.
