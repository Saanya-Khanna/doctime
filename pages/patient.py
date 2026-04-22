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

        # -----------------------
        # BRAND
        # -----------------------
        st.markdown("""
        <div style="padding:12px 0 18px 0;">
            <div style="font-size:18px; font-weight:600; color:#0F172A;">
                DocTime
            </div>
            <div style="font-size:12px; color:#64748B;">
                Healthcare platform
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<hr style='border:0.5px solid #E2E8F0;'>", unsafe_allow_html=True)

        # -----------------------
        # NAV SECTION
        # -----------------------
        st.markdown("### Navigation")

        def nav(label, value):
            if st.button(label, use_container_width=True):
                st.session_state.patient_tab = value

        nav("Dashboard", "Dashboard")
        nav("Find Doctors", "Find")
        nav("Appointments", "Appointments")

        st.markdown("---")

        st.markdown("### Account")

        nav("Profile", "Profile")
        nav("Settings", "Settings")

        st.markdown("---")

        # -----------------------
        # LOGOUT (SUBTLE)
        # -----------------------
        if st.button("Logout", use_container_width=True):
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
                
def doctor_profile_view():

    doc = st.session_state.selected_doctor

    if not doc:
        st.session_state.patient_tab = "Find"
        return

    if st.button("← Back"):
        st.session_state.patient_tab = "Find"
        return

    st.markdown(f"""
    <div class="card">
        <h2>Dr. {doc['name']}</h2>
        <p>{doc['specialty']} • 📍 {doc['zip']}</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### Available Times")

    schedule = get_availability(doc["id"])

    for slot in schedule:

        st.markdown(f"""
        <div class="card">
            {slot['day']} — {slot['time']}
        </div>
        """, unsafe_allow_html=True)

        if st.button(f"Book {slot['time']}", key=f"{doc['id']}-{slot['day']}-{slot['time']}"):

            st.session_state.appointments.append({
                "doctor": doc["name"],
                "time": f"{slot['day']} {slot['time']}"
            })

            st.success("Booked ✔")
            st.session_state.patient_tab = "Appointments"

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

    user = st.session_state.user

    if "profile_name" not in st.session_state:
        st.session_state.profile_name = user["name"]

    st.markdown("""
    <div class="card">
        <h4>Personal Information</h4>
    </div>
    """, unsafe_allow_html=True)

    name = st.text_input("Name", st.session_state.profile_name)
    email = st.text_input("Email", "patient@test.com")

    if st.button("Save Changes"):

        st.session_state.profile_name = name

        st.success("Profile updated ✔")

    st.markdown("---")

    st.markdown("""
    <div class="card">
        <h4>Account Info</h4>
        <p>Role: Patient</p>
        <p>Status: Active</p>
    </div>
    """, unsafe_allow_html=True)


# -----------------------
# SETTINGS VIEW
# -----------------------
def settings_view():

    st.title("Settings")

    st.markdown("""
    <div class="card">
        <h4>Preferences</h4>
    </div>
    """, unsafe_allow_html=True)

    notifications = st.toggle("Enable Notifications", value=True)
    dark_mode = st.toggle("Dark Mode (demo)", value=False)

    st.markdown("---")

    st.markdown("""
    <div class="card">
        <h4>Privacy</h4>
        <p>Manage how your data is used in the app.</p>
    </div>
    """, unsafe_allow_html=True)

    st.selectbox(
        "Data Sharing",
        ["Minimal", "Standard", "Full (for better recommendations)"]
    )

    st.success("Settings are saved automatically (demo behavior)")


# -----------------------
# MAIN ROUTER
# -----------------------
def patient_dashboard():

    # INIT STATE
    if "patient_tab" not in st.session_state:
        st.session_state.patient_tab = "Dashboard"

    tab = st.session_state.patient_tab

    # -----------------------
    # SIDEBAR MUST BE CALLED HERE
    # -----------------------
    sidebar()

    # -----------------------
    # ROUTER (MUST BE INSIDE FUNCTION)
    # -----------------------
    if tab == "Dashboard":
        dashboard_view()

    elif tab == "Find":
        find_doctors_view()

    elif tab == "DoctorView":
        doctor_profile_view()

    elif tab == "Appointments":
        appointments_view()

    elif tab == "Profile":
        profile_view()

    elif tab == "Settings":
        settings_view()

