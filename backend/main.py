from fastapi import FastAPI
from humbldata.portfolio.analytics.user_table.helpers import aggregate_user_table_data

from .src.core.config import Config

# Setup API Configuration
config = Config()
app = FastAPI(title=config.PROJECT_NAME)

# # Add API Routes
# app.include_router(user_table_router)


@app.get("/")
async def root():
    return {"message": "Welcome to humblFINANCE API"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.get("/user-table")
async def user_table_route():
    user_table_data = (await aggregate_user_table_data(symbols=["XLU", "XLE", "AAPL"])).collect().to_dict(as_series=False)

    return user_table_data


# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8080)