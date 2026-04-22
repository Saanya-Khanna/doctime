import requests

# -----------------------
# STATIC DATA (fallback)
# -----------------------
DOCTORS = [
    {"id": 1, "name": "Sarah Johnson", "specialty": "Cardiologist", "zip": "76013", "rating": 4.8},
    {"id": 2, "name": "Michael Lee", "specialty": "Dermatologist", "zip": "75001", "rating": 4.6},
    {"id": 3, "name": "Priya Patel", "specialty": "Pediatrician", "zip": "75201", "rating": 4.9},
    {"id": 4, "name": "James Wilson", "specialty": "Orthopedic", "zip": "76010", "rating": 4.4},
    {"id": 5, "name": "Emily Chen", "specialty": "Neurologist", "zip": "75080", "rating": 4.7},
    {"id": 6, "name": "David Kim", "specialty": "Cardiologist", "zip": "75204", "rating": 4.5},
    {"id": 7, "name": "Lisa Wong", "specialty": "Dermatologist", "zip": "76015", "rating": 4.6},
    {"id": 8, "name": "Ahmed Khan", "specialty": "Pediatrician", "zip": "75013", "rating": 4.8},
    {"id": 9, "name": "Robert Brown", "specialty": "General Physician", "zip": "75019", "rating": 4.3},
    {"id": 10, "name": "Anna Garcia", "specialty": "Cardiologist", "zip": "76011", "rating": 4.9},
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
