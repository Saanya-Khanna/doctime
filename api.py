import requests

# -----------------------
# STATIC DATA (fallback)
# -----------------------
DOCTORS = [
    {"id": 1, "name": "Dr. Sarah Johnson", "specialty": "Cardiologist", "zip": "76013"},
    {"id": 2, "name": "Dr. Michael Lee", "specialty": "Dermatologist", "zip": "75001"},
    {"id": 3, "name": "Dr. Priya Patel", "specialty": "Pediatrician", "zip": "75201"},
]

# -----------------------
# AVAILABILITY
# -----------------------
def get_availability(doctor_id):

    base_times = ["9:00 AM", "10:30 AM", "12:00 PM", "2:00 PM", "4:00 PM"]

    schedule = []

    for day in ["Monday", "Tuesday", "Wednesday"]:

        for time in base_times:

            schedule.append({
                "doctor_id": doctor_id,
                "day": day,
                "time": time
            })

    return schedule
