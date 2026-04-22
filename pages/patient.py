import streamlit as st
from auth import logout
from components.ui import load_css, doctor_card

def patient_dashboard():

    load_css()

    # SIDEBAR
    with st.sidebar:
        st.title("Patient Portal")

        if st.button("Logout"):
            logout()

    st.title("Find Doctors")

    # SEARCH BAR STYLE FILTERS
    col1, col2 = st.columns(2)

    specialty = col1.selectbox(
        "Specialty",
        ["All", "Cardiologist", "Dermatologist", "Pediatrician", "Neurologist"]
    )

    zipcode = col2.text_input("Zip Code")

    st.markdown("---")

    # DOCTOR DATABASE
    doctors = [
        {"name": "Dr. Sarah Johnson", "specialty": "Cardiologist", "zip": "76013"},
        {"name": "Dr. Michael Lee", "specialty": "Dermatologist", "zip": "75001"},
        {"name": "Dr. Priya Patel", "specialty": "Pediatrician", "zip": "75201"},
        {"name": "Dr. Emily Chen", "specialty": "Neurologist", "zip": "75080"},
    ]

    # FILTER LOGIC
    results = []

    for doc in doctors:
        if (specialty == "All" or doc["specialty"] == specialty) and (zipcode == "" or doc["zip"] == zipcode):
            results.append(doc)

    st.subheader(f"Available Doctors ({len(results)})")

    # DISPLAY DOCTORS
    for doc in results:

        doctor_card(doc["name"], doc["specialty"], doc["zip"])

        if st.button(f"Book Appointment with {doc['name']}", key=doc["name"]):

            if "appointments" not in st.session_state:
                st.session_state.appointments = []

            st.session_state.appointments.append(doc["name"])
            st.success("Appointment booked ✔")

    # APPOINTMENTS
    st.markdown("---")
    st.subheader("Your Appointments")

    if "appointments" in st.session_state and st.session_state.appointments:

        for a in st.session_state.appointments:
            st.markdown(f"""
            <div class="card">
                <b>{a}</b><br>
                10:00 AM (confirmed)
            </div>
            """, unsafe_allow_html=True)

    else:
        st.info("No appointments yet")
