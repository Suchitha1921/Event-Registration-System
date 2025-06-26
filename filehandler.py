import json
import csv
import os

EVENTS_FILE = "events.json"
REGISTRATIONS_FILE = "registrations.csv"

def load_events(filename=EVENTS_FILE):
    with open(filename, "r") as f:
        return json.load(f)

def is_event_available(event_id, filename=EVENTS_FILE):
    events = load_events(filename)
    for event in events:
        if event["event_id"] == event_id:
            return event["available_slots"] > 0
    return False

def reduce_event_slot(event_id, filename=EVENTS_FILE):
    events = load_events(filename)
    for event in events:
        if event["event_id"] == event_id and event["available_slots"] > 0:
            event["available_slots"] -= 1
            break
    with open(filename, "w") as f:
        json.dump(events, f, indent=4)

def save_registration(name, email, age, event_id, filename=REGISTRATIONS_FILE):
    file_exists = os.path.isfile(filename)
    with open(filename, mode='a', newline='') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["Name", "Email", "Age", "Event ID"])
        writer.writerow([name, email, age, event_id])


def get_all_registrations(filename="registrations.csv"):
    registrations = []
    try:
        with open(filename, mode='r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                registrations.append(row)
    except FileNotFoundError:
        pass  # Return empty list if no registrations yet
    return registrations