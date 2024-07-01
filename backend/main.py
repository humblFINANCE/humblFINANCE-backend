from fastapi import FastAPI

from .src.api.v1.user_table import router as user_table_router
from .src.core.config import Config

config = Config()
app = FastAPI(title=config.PROJECT_NAME)

app.include_router(user_table_router, prefix=config.API_V1_STR)

@app.get("/")
async def root():
    return {"message": "Welcome to humblFINANCE API"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)