import streamlit as st

# -----------------------
# PAGE CONFIG
# -----------------------
st.set_page_config(page_title="DocTime", layout="wide")

# -----------------------
# SESSION STATE INIT
# -----------------------
if "user_type" not in st.session_state:
    st.session_state.user_type = "patient"  # default

if "appointments" not in st.session_state:
    st.session_state.appointments = []

# -----------------------
# STYLING
# -----------------------
st.markdown("""
<style>
.card {
    background: white;
    padding: 18px;
    border-radius: 12px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.05);
    margin-bottom: 15px;
}
body {
    background-color: #f6f9fc;
}
</style>
""", unsafe_allow_html=True)

# -----------------------
# LAYOUT (SIDEBAR + HEADER)
# -----------------------
def layout(title):
    with st.sidebar:
        st.markdown("## 🏥 DocTime")

        # Toggle user type (for demo)
        st.session_state.user_type = st.selectbox(
            "Switch Role",
            ["patient", "doctor"],
            index=0 if st.session_state.user_type == "patient" else 1
        )

        if st.session_state.user_type == "patient":
            menu = st.radio("", [
                "🏠 Dashboard",
                "🔍 Search Doctors",
                "📅 My Appointments",
                "👤 Profile",
                "🚪 Logout"
            ])
        else:
            menu = st.radio("", [
                "🏠 Dashboard",
                "📅 Schedule",
                "⏰ Availability",
                "👤 Profile",
                "🚪 Logout"
            ])

    # Header
    col1, col2 = st.columns([8, 2])
    with col1:
        st.markdown(f"### {title}")
    with col2:
        st.markdown("🔔 👤")

    return menu

# -----------------------
# PATIENT DASHBOARD
# -----------------------
def patient_dashboard():
    menu = layout("Patient Dashboard")

    if menu == "🏠 Dashboard":
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.markdown("""
            <div class="card">
            <h4>📅 Book Appointment</h4>
            <p>Schedule a new visit</p>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown(f"""
            <div class="card">
            <h2>{len(st.session_state.appointments)}</h2>
            <p>Upcoming Appointments</p>
            </div>
            """, unsafe_allow_html=True)

        with col3:
            st.markdown("""
            <div class="card">
            <h2>3</h2>
            <p>Completed Visits</p>
            </div>
            """, unsafe_allow_html=True)

        with col4:
            st.markdown("""
            <div class="card">
            <h2>5</h2>
            <p>Saved Doctors</p>
            </div>
            """, unsafe_allow_html=True)

        st.subheader("Upcoming Appointments")

        if st.session_state.appointments:
            for appt in st.session_state.appointments:
                st.markdown(f"""
                <div class="card">
                <b>{appt['doctor']}</b><br>
                {appt['time']} • Confirmed
                </div>
                """, unsafe_allow_html=True)
        else:
            st.info("No appointments yet.")

    elif menu == "🔍 Search Doctors":
        st.subheader("Find a Doctor")

        doctors = ["Dr. Sarah Johnson", "Dr. Michael Lee", "Dr. Priya Patel"]

        for doc in doctors:
            if st.button(f"Book Appointment with {doc}"):
                st.session_state.appointments.append({
                    "doctor": doc,
                    "time": "10:00 AM"
                })
                st.success("Appointment booked!")

    elif menu == "📅 My Appointments":
        st.subheader("Your Appointments")

        if st.session_state.appointments:
            for appt in st.session_state.appointments:
                st.markdown(f"""
                <div class="card">
                {appt['doctor']} at {appt['time']}
                </div>
                """, unsafe_allow_html=True)
        else:
            st.info("No appointments.")

    elif menu == "👤 Profile":
        st.markdown("""
        <div class="card">
        <h4>Profile</h4>
        <p>Name: John Doe</p>
        </div>
        """, unsafe_allow_html=True)

    elif menu == "🚪 Logout":
        st.session_state.user_type = "patient"
        st.session_state.appointments = []
        st.rerun()

# -----------------------
# DOCTOR DASHBOARD
# -----------------------
def doctor_dashboard():
    menu = layout("Doctor Dashboard")

    if menu == "🏠 Dashboard":
        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown("""
            <div class="card">
            <h2>5</h2>
            <p>Today's Appointments</p>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown("""
            <div class="card">
            <h2>12</h2>
            <p>Total Patients</p>
            </div>
            """, unsafe_allow_html=True)

        with col3:
            st.markdown("""
            <div class="card">
            <h2>4.8 ⭐</h2>
            <p>Rating</p>
            </div>
            """, unsafe_allow_html=True)

        st.subheader("Today's Schedule")

        if st.session_state.appointments:
            for appt in st.session_state.appointments:
                st.markdown(f"""
                <div class="card">
                <b>Patient</b><br>
                Appointment at {appt['time']}
                </div>
                """, unsafe_allow_html=True)
        else:
            st.info("No appointments today")

    elif menu == "📅 Schedule":
        st.write("Schedule page")

    elif menu == "⏰ Availability":
        new_time = st.text_input("Add time slot")

        if st.button("Add"):
            st.success(f"Added {new_time}")

    elif menu == "👤 Profile":
        st.write("Doctor profile")

    elif menu == "🚪 Logout":
        st.session_state.user_type = "patient"
        st.rerun()

# -----------------------
# MAIN ENTRY
# -----------------------
if st.session_state.user_type == "patient":
    patient_dashboard()
else:
    doctor_dashboard()
