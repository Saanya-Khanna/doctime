import streamlit as st
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
