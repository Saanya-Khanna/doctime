from datetime import datetime, timedelta

# -----------------------
# DOCTOR DATABASE
# -----------------------
DOCTORS = [
    {
        "id": 1,
        "name": "Dr. Sarah Johnson",
        "specialty": "Cardiologist",
        "zip": "76013"
    },
    {
        "id": 2,
        "name": "Dr. Michael Lee",
        "specialty": "Dermatologist",
        "zip": "75001"
    },
    {
        "id": 3,
        "name": "Dr. Priya Patel",
        "specialty": "Pediatrician",
        "zip": "75201"
    }
]

# -----------------------
# REALISTIC AVAILABILITY GENERATOR
# -----------------------
def get_availability(doctor_id):

    base_times = ["9:00 AM", "10:30 AM", "12:00 PM", "2:00 PM", "4:00 PM"]

    today = datetime.now()

    schedule = []

    for i in range(3):  # next 3 days

        day = (today + timedelta(days=i)).strftime("%A")

        for time in base_times:

            schedule.append({
                "doctor_id": doctor_id,
                "day": day,
                "time": time
            })

    return schedule
