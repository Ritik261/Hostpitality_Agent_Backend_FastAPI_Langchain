from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI=os.getenv("MONGO_URI")

client = AsyncIOMotorClient(MONGO_URI)

db = client["hotel_db"]
booking_collection =  db["bookings"]

async def check_conn():
    try:
        await client.admin.command("ping")
        return True
    except Exception:
        return False