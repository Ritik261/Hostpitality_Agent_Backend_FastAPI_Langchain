from fastapi import APIRouter
from pydantic import BaseModel
from app.agents.booking_agent import run_agent

class chatRequest(BaseModel):
    message: str

router = APIRouter()

@router.post("/chat")
async def chat(req:chatRequest):
    print("#######request is ###########", req.message)
    result = await run_agent(req.message)

    return{
        "response":result
    }