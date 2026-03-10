from pydantic import BaseModel

class Booking(BaseModel):
    booking_id: str
    guest_name: str
    room_type:str
    check_in: str
    check_out: str
    status: str