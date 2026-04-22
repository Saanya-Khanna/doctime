import streamlit as st

# -----------------------
# PAGE CONFIG
# -----------------------
st.set_page_config(page_title="DocTime", layout="wide")

# -----------------------
# STYLING
# -----------------------
st.markdown("""
<style>
    .card {
        background-color: #f0f2f6;
        padding: 15px;
        border-radius: 8px;
        margin-bottom: 10px;
    }
</style>
""", unsafe_allow_html=True)

# -----------------------
# SAMPLE DATA
# -----------------------
doctors = [
    {"id": 1, "name": "Dr. Sarah Johnson", "specialty": "Cardiologist", "zip": "10001"},
    {"id": 2, "name": "Dr. James Smith", "specialty": "Dermatologist", "zip": "10002"},
    {"id": 3, "name": "Dr. Emily Brown", "specialty": "Pediatrician", "zip": "10001"},
    {"id": 4, "name": "Dr. Michael Lee", "specialty": "Cardiologist", "zip": "10003"},
]

availability = [
    {"doctor_id": 1, "time": "10:00 AM"},
    {"doctor_id": 1, "time": "2:00 PM"},
    {"doctor_id": 2, "time": "9:00 AM"},
    {"doctor_id": 2, "time": "3:00 PM"},
    {"doctor_id": 3, "time": "11:00 AM"},
    {"doctor_id": 4, "time": "1:00 PM"},
]

# -----------------------
# HELPER FUNCTION
# -----------------------
def header(title):
    st.title(title)

# -----------------------
# SESSION STATE INITIALIZATION
# -----------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "user_type" not in st.session_state:
    st.session_state.user_type = None
if "user" not in st.session_state:
    st.session_state.user = {}
if "appointments" not in st.session_state:
    st.session_state.appointments = []

# -----------------------
# LOGIN PAGE
# -----------------------
def login_page():
    st.title("🏥 DocTime - Healthcare Appointment System")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("👤 Patient Login")
        patient_email = st.text_input("Patient Email", key="patient_email")
        if st.button("Login as Patient"):
            if patient_email:
                st.session_state.logged_in = True
                st.session_state.user_type = "patient"
                st.session_state.user = {"name": patient_email.split("@")[0].title()}
                st.rerun()
            else:
                st.error("Please enter email")
    
    with col2:
        st.subheader("👨‍⚕️ Doctor Login")
        doctor_email = st.text_input("Doctor Email", key="doctor_email")
        if st.button("Login as Doctor"):
            if doctor_email:
                st.session_state.logged_in = True
                st.session_state.user_type = "doctor"
                st.session_state.user = {"name": doctor_email.split("@")[0].title()}
                st.rerun()
            else:
                st.error("Please enter email")

# -----------------------
# PATIENT DASHBOARD
# -----------------------
def patient_dashboard():
    header(f"Welcome, {st.session_state.user['name']} 👋")

    menu = st.sidebar.radio("Navigation", [
        "Dashboard", "Search Doctors", "My Appointments", "Profile", "Logout"
    ])

    if menu == "Dashboard":
        st.markdown('<div class="card"><h4>📊 Dashboard</h4></div>', unsafe_allow_html=True)

    elif menu == "Search Doctors":
        st.subheader("🔍 Find a Doctor")

        col1, col2 = st.columns(2)
        specialty = col1.selectbox("Specialty", ["All", "Cardiologist", "Dermatologist", "Pediatrician"])
        zip_code = col2.text_input("Zip Code")

        cols = st.columns(2)

        for i, doc in enumerate(doctors):
            if (specialty == "All" or doc["specialty"] == specialty) and (zip_code == "" or doc["zip"] == zip_code):

                with cols[i % 2]:
                    st.markdown(f"""
                    <div class="card">
                        <h4>{doc['name']}</h4>
                        <p>{doc['specialty']} • {doc['zip']}</p>
                    </div>
                    """, unsafe_allow_html=True)

                    for slot in availability:
                        if slot["doctor_id"] == doc["id"]:
                            if st.button(f"Book {slot['time']}", key=f"{doc['id']}{slot['time']}"):
                                st.session_state.appointments.append({
                                    "doctor": doc["name"],
                                    "time": slot["time"]
                                })
                                st.success("✅ Appointment booked!")

    elif menu == "My Appointments":
        st.subheader("📊 Your Appointments")

        if st.session_state.appointments:
            for appt in st.session_state.appointments:
                st.markdown(f"""
                <div class="card">
                <p><b>{appt['doctor']}</b> at {appt['time']}</p>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.info("No appointments yet.")

    elif menu == "Profile":
        st.markdown(f"""
        <div class="card">
        <h4>👤 Profile</h4>
        <p>Name: {st.session_state.user['name']}</p>
        <p>Email: patient@test.com</p>
        </div>
        """, unsafe_allow_html=True)

    elif menu == "Logout":
        st.session_state.logged_in = False
        st.rerun()


# -----------------------
# DOCTOR DASHBOARD
# -----------------------
def doctor_dashboard():
    header(f"{st.session_state.user['name']} Dashboard 👨‍⚕️")

    menu = st.sidebar.selectbox(
        "Navigation",
        ["Dashboard", "Appointments", "Availability", "Profile", "Logout"]
    )

    if menu == "Dashboard":
        st.markdown("""
        <div class="card">
        <h4>📅 Today's Appointments</h4>
        <p>10:00 AM - John Doe</p>
        </div>
        """, unsafe_allow_html=True)

    elif menu == "Appointments":
        st.subheader("📊 All Appointments")
        for appt in st.session_state.appointments:
            st.markdown(f"""
            <div class="card">
            <p>{appt['doctor']} - {appt['time']}</p>
            </div>
            """, unsafe_allow_html=True)

    elif menu == "Availability":
        st.subheader("⏰ Manage Availability")

        new_time = st.text_input("Add Time Slot")

        if st.button("Add Slot"):
            availability.append({"doctor_id": 1, "time": new_time})
            st.success("Added!")

    elif menu == "Profile":
        st.markdown("""
        <div class="card">
        <h4>👨‍⚕️ Doctor Profile</h4>
        <p>Specialty: Cardiology</p>
        </div>
        """, unsafe_allow_html=True)

    elif menu == "Logout":
        st.session_state.logged_in = False
        st.rerun()


# -----------------------
# MAIN APP
# -----------------------
if __name__ == "__main__":
    if not st.session_state.logged_in:
        login_page()
    else:
        if st.session_state.user_type == "patient":
            patient_dashboard()
        else:
            doctor_dashboard()
