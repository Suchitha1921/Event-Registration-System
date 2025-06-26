from fastapi import FastAPI, HTTPException
from model import UserRegistration
import filehandler

app = FastAPI(title= "EVENT REGISTRATION APP! 🗓️✨",
    description="A FastAPI backend to view available events and register for them.",
    version="0.115.13"
)

@app.get("/events")
def get_events():
    return filehandler.load_events()

# FIXED version of register_user
@app.post("/register")
def register_user(user: UserRegistration):
    events = filehandler.load_events()

    matching_event = next((event for event in events if event["event_id"] == user.event), None)

    if not matching_event:
        raise HTTPException(status_code=404, detail="Event does not exist.")

    if matching_event["available_slots"] == 0:
        raise HTTPException(status_code=400, detail="Event is full.")

    filehandler.reduce_event_slot(user.event)
    filehandler.save_registration(user.name, user.email_id, user.age, user.event)

    return {"message": "Registration successful!"}


@app.get("/registrations")
def view_registrations():
    return filehandler.get_all_registrations()