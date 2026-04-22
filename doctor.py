import streamlit as st

# -----------------------
# DUMMY USERS DATABASE
# -----------------------
USERS = {
    "patient@test.com": {
        "password": "1234",
        "role": "patient",
        "name": "John Doe"
    },
    "doctor@test.com": {
        "password": "1234",
        "role": "doctor",
        "name": "Dr. Smith"
    }
}


# -----------------------
# LOGIN FUNCTION
# -----------------------
def login():

    st.markdown("## 🏥 DocTime Login")

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):

        if email in USERS and USERS[email]["password"] == password:

            st.session_state.logged_in = True
            st.session_state.role = USERS[email]["role"]
            st.session_state.user = USERS[email]

            st.success("Login successful ✔")
            st.rerun()

        else:
            st.error("Invalid email or password")


# -----------------------
# LOGOUT
# -----------------------
def logout():
    st.session_state.logged_in = False
    st.session_state.role = None
    st.session_state.user = None
    st.rerun()
