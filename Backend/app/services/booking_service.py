from app.database import booking_collection
from datetime import datetime
from app.database import booking_collection


async def create_booking(
    booking_id: str,
    guest_name: str,
    room_type: str,
    check_in: str,
    check_out: str
):

    booking = {
        "booking_id": booking_id,
        "guest_name": guest_name,
        "room_type": room_type,
        "check_in": check_in,
        "check_out": check_out,
        "status": "confirmed",
        "created_at": datetime.utcnow()
    }

    await booking_collection.insert_one(booking)

    return {
        "message": "Booking created successfully",
        "booking_id": booking_id
    }
async def check_booking(booking_id:str):
    booking = await booking_collection.find_one(
        {"booking_id":booking_id},
        {"_id":0}
    )
    return booking

async def cancel_booking(booking_id:str):
    result = await booking_collection.update_one(
        {"booking_id":booking_id},
        {"$set":{"status":"cancelled"}}
    )
    return {"updated":result.modified_count}

async def update_booking(booking_id: str, field: str, value: str):

    result = await booking_collection.update_one(
        {"booking_id": booking_id},
        {"$set": {field: value}}
    )

    return {"updated": result.modified_count}


async def check_room_availability(room_type: str):

    cursor = booking_collection.find(
        {
            "room_type": room_type
            # "room_type": room_type,
            # "status": {"$ne": "cancelled"}
        },
        {"_id": 0}
    )

    results = []

    async for doc in cursor:
        results.append(doc)

    return results