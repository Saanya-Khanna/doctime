import streamlit as st

st.set_page_config(page_title="DocTime", layout="wide")

# -----------------------
# STYLING (BRIGHT UI)
# -----------------------
st.markdown("""
<style>
body {
    background-color: #f8fbff;
}
.card {
    background-color: white;
    padding: 18px;
    border-radius: 12px;
    margin-bottom: 15px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.05);
}
.title {
    font-size: 26px;
    font-weight: 600;
}
.small {
    color: gray;
    font-size: 14px;
}
</style>
""", unsafe_allow_html=True)

# -----------------------
# DATA (MORE REALISTIC)
# -----------------------
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

availability = {
    1: ["10:00 AM", "2:00 PM"],
    2: ["9:00 AM", "3:00 PM"],
    3: ["11:00 AM"],
    4: ["1:00 PM"],
    5: ["12:00 PM"],
    6: ["4:00 PM"],
    7: ["10:30 AM"],
    8: ["2:30 PM"],
}

# -----------------------
# SESSION STATE
# -----------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "user_type" not in st.session_state:
    st.session_state.user_type = None
if "appointments" not in st.session_state:
    st.session_state.appointments = []
if "page" not in st.session_state:
    st.session_state.page = "Dashboard"

# -----------------------
# LOGIN
# -----------------------
def login():
    st.title("🏥 DocTime")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Patient Login")
        if st.button("Login as Patient"):
            st.session_state.logged_in = True
            st.session_state.user_type = "patient"
            st.session_state.page = "Dashboard"
            st.rerun()

    with col2:
        st.subheader("Doctor Login")
        if st.button("Login as Doctor"):
            st.session_state.logged_in = True
            st.session_state.user_type = "doctor"
            st.session_state.page = "Dashboard"
            st.rerun()

# -----------------------
# NAVBAR
# -----------------------
def navbar():
    cols = st.columns([1,1,1,1,1])

    if cols[0].button("Dashboard"):
        st.session_state.page = "Dashboard"
    if cols[1].button("Search"):
        st.session_state.page = "Search"
    if cols[2].button("Appointments"):
        st.session_state.page = "Appointments"
    if cols[3].button("Profile"):
        st.session_state.page = "Profile"
    if cols[4].button("Logout"):
        st.session_state.logged_in = False
        st.rerun()

# -----------------------
# DASHBOARD
# -----------------------
def dashboard():
    st.markdown('<div class="title">Welcome 👋</div>', unsafe_allow_html=True)

    if st.session_state.appointments:
        latest = st.session_state.appointments[-1]

        st.markdown(f"""
        <div class="card">
        <h4>📅 Upcoming Appointment</h4>
        <p>{latest['doctor']} at {latest['time']}</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.info("No upcoming appointments")

# -----------------------
# SEARCH DOCTORS
# -----------------------
def search():
    st.subheader("🔍 Search Doctors")

    specialty = st.selectbox("Specialty", ["All"] + list(set(d["specialty"] for d in doctors)))
    zip_code = st.text_input("Zip Code")

    for doc in doctors:
        if (specialty == "All" or doc["specialty"] == specialty) and (zip_code == "" or doc["zip"] == zip_code):

            st.markdown(f"""
            <div class="card">
                <b>{doc['name']}</b><br>
                {doc['specialty']} • {doc['zip']}
            </div>
            """, unsafe_allow_html=True)

            for time in availability[doc["id"]]:
                if st.button(f"Book {time}", key=f"{doc['id']}{time}"):
                    st.session_state.appointments.append({
                        "doctor": doc["name"],
                        "time": time
                    })
                    st.success("Appointment Booked!")
                    st.rerun()

# -----------------------
# APPOINTMENTS
# -----------------------
def appointments():
    st.subheader("📅 My Appointments")

    if st.session_state.appointments:
        for appt in st.session_state.appointments:
            st.markdown(f"""
            <div class="card">
            {appt['doctor']} at {appt['time']}
            </div>
            """, unsafe_allow_html=True)
    else:
        st.info("No appointments yet")

# -----------------------
# PROFILE
# -----------------------
def profile():
    st.subheader("👤 Profile")

    st.markdown("""
    <div class="card">
    Name: John Doe <br>
    Email: demo@doctime.com
    </div>
    """, unsafe_allow_html=True)

# -----------------------
# MAIN
# -----------------------
if not st.session_state.logged_in:
    login()
else:
    navbar()

    if st.session_state.page == "Dashboard":
        dashboard()
    elif st.session_state.page == "Search":
        search()
    elif st.session_state.page == "Appointments":
        appointments()
    elif st.session_state.page == "Profile":
        profile()
