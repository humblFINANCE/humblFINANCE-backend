from fastapi import APIRouter
from humbldata.portfolio.analytics.user_table.helpers import aggregate_user_table_data
from src.core.config import Config

config = Config()

router = APIRouter(prefix=config.API_V1_STR)

@router.get("/user-table")
async def user_table_route():
    user_table_data = (await aggregate_user_table_data(symbols=["XLU", "XLE", "AAPL"])).collect().to_dict(as_series=False)

    return user_table_data

# Add more routes as needed