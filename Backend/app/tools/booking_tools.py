from langchain_core.tools import tool
from app.services.booking_service import (
    check_booking,
    check_room_availability,
    update_booking,
    cancel_booking,
    create_booking
)
@tool
async def create_booking_tool(
    booking_id: str,
    guest_name: str,
    room_type: str,
    check_in: str,
    check_out: str
):
    """Create a new hotel booking"""

    return await create_booking(
        booking_id,
        guest_name,
        room_type,
        check_in,
        check_out
    )

@tool
async def check_booking_tool(booking_id: str):
    """check booking details by booking id"""
    return await check_booking(booking_id)
@tool
async def cancel_booking_tool(booking_id: str):
    """check booking details by booking id"""
    return await cancel_booking(booking_id)
@tool
async def update_booking_tool(booking_id: str, field: str, value: str):
    """check booking details by booking id"""
    return await update_booking(booking_id, field, value)

@tool
async def check_room_availability_tool(room_type: str):
    """Check available rooms by type"""
    return await check_room_availability(room_type)

