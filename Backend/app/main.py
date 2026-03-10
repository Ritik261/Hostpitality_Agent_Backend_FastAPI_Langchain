from fastapi import FastAPI
from app.database import check_conn
from app.routes.chat_route import router

app = FastAPI()

app.include_router(router)

@app.get("/health")
async def db_health():
    connected = await check_conn()
    if connected:
        return {"database":"connected"}
    else:
        return {"database":"not connected"}