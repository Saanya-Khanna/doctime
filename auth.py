import streamlit as st

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

def login():

    # Centered layout
    col1, col2, col3 = st.columns([1,2,1])

    with col2:

        st.markdown("""
        <div style="text-align:center; padding:20px 0;">
            <h1 style="margin-bottom:5px;">🏥 DocTime</h1>
            <p style="color:#64748B; margin-top:0;">
                Book doctors instantly. Simple, fast, reliable.
            </p>
        </div>
        """, unsafe_allow_html=True)

        # -----------------------
        # DEMO CREDENTIALS BOX
        # -----------------------
        st.markdown("""
        <div style="
            background:#F1F5F9;
            padding:14px;
            border-radius:12px;
            font-size:13px;
            color:#334155;
            margin-bottom:15px;
            border:1px solid #E2E8F0;
        ">
        <b>Demo Credentials</b><br><br>
        👤 Patient → patient@test.com / 1234<br>
        👨‍⚕️ Doctor → doctor@test.com / 1234
        </div>
        """, unsafe_allow_html=True)

        # LOGIN FIELDS
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")

        if st.button("Sign In"):

            user = USERS.get(email)

            if user and user["password"] == password:

                st.session_state.logged_in = True
                st.session_state.role = user["role"]
                st.session_state.user = user

                st.rerun()

            else:
                st.error("Invalid credentials")


def logout():
    st.session_state.logged_in = False
    st.session_state.role = None
    st.session_state.user = None
    st.rerun()
