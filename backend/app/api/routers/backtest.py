from fastapi import APIRouter, HTTPException
from app.models.schemas import BacktestRequest, BacktestResult
from app.services.backtester import run_backtest

router = APIRouter()

@router.post("/run", response_model=BacktestResult)
async def run_backtest_endpoint(request: BacktestRequest) -> BacktestResult:
	try:
		result = await run_backtest(request)
	except ValueError as exc:
		raise HTTPException(status_code=400, detail=str(exc))
	return result
