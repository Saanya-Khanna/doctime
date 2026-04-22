import streamlit as st

# -----------------------------
# INITIAL SETUP
# -----------------------------
st.set_page_config(page_title="DocTime", layout="wide")

# Dummy users
users = {
    "patient@test.com": {"password": "1234", "role": "patient", "name": "John Doe"},
    "doctor@test.com": {"password": "1234", "role": "doctor", "name": "Dr. Smith"}
}

# Dummy doctors
doctors = [
    {"id": 1, "name": "Dr. Sarah Johnson", "specialty": "Cardiologist", "zip": "76013"},
    {"id": 2, "name": "Dr. Michael Lee", "specialty": "Dermatologist", "zip": "75001"},
    {"id": 3, "name": "Dr. Priya Patel", "specialty": "Pediatrician", "zip": "75201"},
]

# Availability (doctor → slots)
availability = [
    {"doctor_id": 1, "time": "9:00 AM"},
    {"doctor_id": 1, "time": "10:00 AM"},
    {"doctor_id": 2, "time": "11:00 AM"},
]

# Session state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.role = None
    st.session_state.user = None
    st.session_state.appointments = []

# -----------------------------
# LOGIN PAGE
# -----------------------------
def login():
    st.title("🏥 DocTime - Login")

    st.info("Demo Credentials:\nPatient: patient@test.com / 1234\nDoctor: doctor@test.com / 1234")

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if email in users and users[email]["password"] == password:
            st.session_state.logged_in = True
            st.session_state.role = users[email]["role"]
            st.session_state.user = users[email]
            st.success("Logged in successfully!")
        else:
            st.error("Invalid credentials")

# -----------------------------
# PATIENT DASHBOARD
# -----------------------------
def patient_dashboard():
    st.title(f"Welcome, {st.session_state.user['name']} 👋")

    menu = st.sidebar.selectbox(
        "Menu",
        ["Dashboard", "Search Doctors", "My Appointments", "Profile", "Logout"]
    )

    if menu == "Dashboard":
        st.subheader("Upcoming Appointments")
        if st.session_state.appointments:
            for appt in st.session_state.appointments:
                st.write(f"{appt['doctor']} at {appt['time']}")
        else:
            st.write("No appointments yet.")

    elif menu == "Search Doctors":
        search = st.text_input("Search by name")
        specialty = st.selectbox("Specialty", ["All", "Cardiologist", "Dermatologist", "Pediatrician"])
        zip_code = st.text_input("Zip Code")

        st.subheader("Doctors")

        for doc in doctors:
            if (specialty == "All" or doc["specialty"] == specialty) and (zip_code == "" or doc["zip"] == zip_code):
                st.write(f"### {doc['name']} ({doc['specialty']}) - {doc['zip']}")

                # Show availability
                for slot in availability:
                    if slot["doctor_id"] == doc["id"]:
                        if st.button(f"Book {slot['time']} with {doc['name']}", key=f"{doc['id']}{slot['time']}"):
                            st.session_state.appointments.append({
                                "doctor": doc["name"],
                                "time": slot["time"]
                            })
                            st.success("Appointment booked!")

    elif menu == "My Appointments":
        st.subheader("Your Appointments")
        for appt in st.session_state.appointments:
            st.write(f"{appt['doctor']} at {appt['time']}")

    elif menu == "Profile":
        st.write("Name:", st.session_state.user["name"])
        st.write("Email:", "patient@test.com")

    elif menu == "Logout":
        st.session_state.logged_in = False

# -----------------------------
# DOCTOR DASHBOARD
# -----------------------------
def doctor_dashboard():
    st.title(f"Welcome, {st.session_state.user['name']} 👨‍⚕️")

    menu = st.sidebar.selectbox(
        "Menu",
        ["Dashboard", "Appointments", "Availability", "Profile", "Logout"]
    )

    if menu == "Dashboard":
        st.subheader("Today's Appointments")
        if st.session_state.appointments:
            for appt in st.session_state.appointments:
                st.write(f"{appt['doctor']} - {appt['time']}")
        else:
            st.write("No appointments yet.")

    elif menu == "Appointments":
        st.subheader("All Appointments")
        for appt in st.session_state.appointments:
            st.write(f"{appt['doctor']} - {appt['time']}")

    elif menu == "Availability":
        st.subheader("Set Availability")
        new_time = st.text_input("Add Time Slot")
        if st.button("Add Slot"):
            availability.append({"doctor_id": 1, "time": new_time})
            st.success("Added!")

    elif menu == "Profile":
        st.write("Doctor Profile")

    elif menu == "Logout":
        st.session_state.logged_in = False

# -----------------------------
# MAIN APP FLOW
# -----------------------------
if not st.session_state.logged_in:
    login()
else:
    if st.session_state.role == "patient":
        patient_dashboard()
    else:
        doctor_dashboard()
