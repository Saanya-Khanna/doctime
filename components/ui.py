import streamlit as st

def load_css():
    st.markdown("""
    <style>

/* APP BACKGROUND */
.stApp {
    background: #F6F8FC;
    font-family: 'Inter', sans-serif;
}

/* SIDEBAR */
section[data-testid="stSidebar"] {
    background-color: #0F172A;
    color: white;
}

/* CARD */
.card {
    background: white;
    border-radius: 16px;
    padding: 18px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.06);
    border: 1px solid rgba(0,0,0,0.05);
    transition: 0.2s ease;
}

.card:hover {
    transform: translateY(-2px);
}

/* PRIMARY BUTTON */
.stButton > button {
    background: linear-gradient(135deg, #2563EB, #60A5FA);
    color: white;
    border-radius: 10px;
    padding: 10px 14px;
    border: none;
    font-weight: 500;
}

/* HEADINGS */
h1, h2, h3 {
    color: #0F172A;
}

/* TEXT */
p {
    color: #64748B;
}

    </style>
    """, unsafe_allow_html=True)
