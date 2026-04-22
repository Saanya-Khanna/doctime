import streamlit as st

# -----------------------
# PAGE CONFIG
# -----------------------
st.set_page_config(page_title="DocTime", layout="wide")

# -----------------------
# CUSTOM STYLING (FIGMA FEEL)
# -----------------------
st.markdown("""
<style>
.main {
    background-color: #F5F9FF;
}
.card {
    background: white;
    padding: 18px;
    border-radius: 14px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.08);
    margin-bottom: 15px;
}
.header {
    display:flex;
    justify-content:space-between;
    align-items:center;
    margin-bottom:20px;
}
.stButton>button {
    background-color: #2F80ED;
    color: white;
    border-radius: 8px;
    padding: 8px 14px;
    border: none;
}
.stButton>button:hover {
    background-color: #1c60c7;
}
</style>
""", unsafe_allow_html=True)

# -----------------------
# DATA
# -----------------------
users = {
    "patient@test.com": {"password": "1234", "role": "patient", "name": "John Doe"},
    "doctor@test.com": {"password": "1234", "role": "doctor", "name": "Dr. Smith"}
}

doctors = [
    {"id": 1, "name": "Dr. Sarah Johnson", "specialty": "Cardiologist", "zip": "76013"},
    {"id": 2, "name": "Dr. Michael Lee", "specialty": "Dermatologist", "zip": "75001"},
    {"id": 3, "name": "Dr. Priya Patel", "specialty": "Pediatrician", "zip": "75201"},
    {"id": 4, "name": "Dr. James Wilson", "specialty": "Orthopedic", "zip": "76010"},
    {"id": 5, "name": "Dr. Emily Chen", "specialty": "Neurologist", "zip": "75080"},
    {"id": 6, "name": "Dr. David Kim", "specialty": "Cardiologist", "zip": "75204"},
    {"id": 7, "name": "Dr. Lisa Wong", "specialty": "Dermatologist", "zip": "76015"},
    {"id": 8, "name": "Dr. Ahmed Khan", "specialty": "Pediatrician", "zip": "75013"},
]

availability = [
    {"doctor_id": 1, "time": "9:00 AM"},
    {"doctor_id": 1, "time": "10:00 AM"},
    {"doctor_id": 2, "time": "11:00 AM"},
]

# -----------------------
# SESSION STATE
# -----------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.role = None
    st.session_state.user = None
    st.session_state.appointments = []

# -----------------------
# LOGIN PAGE
# -----------------------
def login():
    col1, col2, col3 = st.columns([1,2,1])

    with col2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.title("🏥 DocTime Login")

        st.info("Demo:\nPatient → patient@test.com / 1234\nDoctor → doctor@test.com / 1234")

        email = st.text_input("Email")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            if email in users and users[email]["password"] == password:
                st.session_state.logged_in = True
                st.session_state.role = users[email]["role"]
                st.session_state.user = users[email]
                st.rerun()
            else:
                st.error("Invalid credentials")

        st.markdown('</div>', unsafe_allow_html=True)

# -----------------------
# HEADER
# -----------------------
def header(title):
    st.markdown(f"""
    <div class="header">
        <h2>{title}</h2>
        <div>🔔 👤</div>
    </div>
    """, unsafe_allow_html=True)

# -----------------------
# PATIENT DASHBOARD
# -----------------------
def patient_dashboard():
    header(f"Welcome, {st.session_state.user['name']} 👋")

    menu = st.sidebar.radio("Navigation", [
        "Dashboard", "Search Doctors", "My Appointments", "Profile", "Logout"
    ])

    if menu == "Dashboard":
        if "page" not in st.session_state:
            st.session_state.page = "dashboard"

menu = st.session_state.page

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
    ["🏠 Dashboard", "🔍 Search Doctors", "📅 My Appointments", "👤 Profile", "🚪 Logout"]
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
# MAIN
# -----------------------
if not st.session_state.logged_in:
    login()
else:
    if st.session_state.role == "patient":
        patient_dashboard()
    else:
        doctor_dashboard()
