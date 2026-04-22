import streamlit as st

def load_css():

    st.markdown("""
    <style>

    /* =====================
       GLOBAL BACKGROUND
    ===================== */
    .stApp {
        background-color: #F8FAFC;
        font-family: 'Inter', sans-serif;
        color: #0F172A;
    }

    /* =====================
       SIDEBAR (clean dark slate)
    ===================== */
    section[data-testid="stSidebar"] {
        background-color: #0B1220;
        color: #E2E8F0;
    }

    section[data-testid="stSidebar"] * {
        color: #E2E8F0;
    }

    /* =====================
       HEADINGS
    ===================== */
    h1, h2, h3 {
        font-weight: 600;
        letter-spacing: -0.3px;
    }

    /* =====================
       CARD (minimal + elegant)
    ===================== */
    .card {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 14px;
        padding: 16px 18px;
        margin-bottom: 12px;
        box-shadow: none;
        transition: all 0.2s ease;
    }

    .card:hover {
        border-color: #CBD5E1;
        transform: translateY(-1px);
    }

    /* =====================
       BUTTONS (subtle, not loud)
    ===================== */
    .stButton > button {
        background: #0F172A;
        color: white;
        border-radius: 10px;
        padding: 8px 14px;
        border: none;
        font-weight: 500;
        font-size: 13px;
    }

    .stButton > button:hover {
        background: #1E293B;
    }

    /* =====================
       METRICS (clean)
    ===================== */
    [data-testid="stMetric"] {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        padding: 12px;
        border-radius: 12px;
    }

    /* =====================
       TEXT MUTED
    ===================== */
    p {
        color: #475569;
    }

    /* =====================
       REMOVE STREAMLIT CLUTTER
    ===================== */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    </style>
    """, unsafe_allow_html=True)
