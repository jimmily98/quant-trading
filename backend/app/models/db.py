from sqlmodel import SQLModel, create_engine
import os

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./backtests.db")
engine = create_engine(DATABASE_URL, echo=False)


def init_db() -> None:
	SQLModel.metadata.create_all(engine)
