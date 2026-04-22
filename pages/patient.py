import streamlit as st
from auth import logout
from api import DOCTORS, get_availability

# -----------------------
# NAV STATE INIT
# -----------------------
if "patient_tab" not in st.session_state:
    st.session_state.patient_tab = "Dashboard"

# -----------------------
# SIDEBAR NAVIGATION
# -----------------------
def sidebar():

    with st.sidebar:
        st.title("🏥 DocTime")

        if st.button("📊 Dashboard"):
            st.session_state.patient_tab = "Dashboard"

        if st.button("🔍 Find Doctors"):
            st.session_state.patient_tab = "Find"

        if st.button("📅 Appointments"):
            st.session_state.patient_tab = "Appointments"

        if st.button("👤 Profile"):
            st.session_state.patient_tab = "Profile"

        if st.button("⚙️ Settings"):
            st.session_state.patient_tab = "Settings"

        st.markdown("---")

        if st.button("🚪 Logout"):
            logout()

# -----------------------
# DASHBOARD
# -----------------------
def dashboard_view():

    st.title("Welcome 👋")

    col1, col2, col3 = st.columns(3)

    col1.metric("Appointments", len(st.session_state.get("appointments", [])))
    col2.metric("Doctors", len(DOCTORS))
    col3.metric("Status", "Active")

    st.markdown("---")

    st.subheader("Quick Activity")

    st.info("Use sidebar to find doctors or manage appointments")

# -----------------------
# FIND DOCTORS
# -----------------------
def find_doctors_view():

    st.title("Find Doctors")

    col1, col2 = st.columns(2)

    specialty = col1.selectbox(
        "Specialty",
        ["All", "Cardiologist", "Dermatologist", "Pediatrician"]
    )

    zipcode = col2.text_input("Zip Code")

    st.markdown("---")

    for doc in DOCTORS:

        if (specialty == "All" or doc["specialty"] == specialty) and (zipcode == "" or zipcode in doc["zip"]):

            st.markdown(f"""
            <div style="
                background:white;
                padding:16px;
                border-radius:14px;
                margin-bottom:10px;
                box-shadow:0 8px 20px rgba(0,0,0,0.06);
            ">
                <h3>🧑‍⚕️ {doc['name']}</h3>
                <p>{doc['specialty']} • 📍 {doc['zip']}</p>
            </div>
            """, unsafe_allow_html=True)

            if st.button(f"View Availability - {doc['id']}", key=f"view-{doc['id']}"):

                st.session_state.selected_doctor = doc
                st.session_state.patient_tab = "DoctorView"

# -----------------------
# DOCTOR AVAILABILITY VIEW
# -----------------------
def doctor_view():

    doc = st.session_state.selected_doctor

    st.title(f"{doc['name']}")

    st.subheader("Available Slots")

    schedule = get_availability(doc["id"])

    if "appointments" not in st.session_state:
        st.session_state.appointments = []

    for slot in schedule:

        st.markdown(f"""
        <div style="
            background:white;
            padding:14px;
            border-radius:12px;
            margin-bottom:8px;
        ">
            📅 {slot['day']} — ⏰ {slot['time']}
        </div>
        """, unsafe_allow_html=True)

        if st.button(f"Book {slot['time']}", key=f"{slot['day']}-{slot['time']}"):

            st.session_state.appointments.append({
                "doctor": doc["name"],
                "time": f"{slot['day']} {slot['time']}"
            })

            st.success("Booked ✔")

# -----------------------
# APPOINTMENTS VIEW
# -----------------------
def appointments_view():

    st.title("My Appointments")

    appts = st.session_state.get("appointments", [])

    if not appts:
        st.info("No appointments yet")
        return

    for a in appts:

        st.markdown(f"""
        <div style="
            background:white;
            padding:16px;
            border-radius:14px;
            margin-bottom:10px;
        ">
            🧑‍⚕️ {a['doctor']}<br>
            📅 {a['time']}
        </div>
        """, unsafe_allow_html=True)

# -----------------------
# PROFILE VIEW
# -----------------------
def profile_view():

    st.title("Profile")

    st.markdown(f"""
    <div style="background:white;padding:16px;border-radius:14px;">
        Name: John Doe<br>
        Role: Patient<br>
        Email: patient@test.com
    </div>
    """, unsafe_allow_html=True)

# -----------------------
# SETTINGS VIEW
# -----------------------
def settings_view():

    st.title("Settings")

    st.info("Settings page (expand later with notifications, privacy, etc.)")

# -----------------------
# MAIN ROUTER
# -----------------------
def patient_dashboard():

    sidebar()

    tab = st.session_state.patient_tab

    if tab == "Dashboard":
        dashboard_view()

    elif tab == "Find":
        find_doctors_view()

    elif tab == "DoctorView":
        doctor_view()

    elif tab == "Appointments":
        appointments_view()

    elif tab == "Profile":
        profile_view()

    elif tab == "Settings":
        settings_view()
