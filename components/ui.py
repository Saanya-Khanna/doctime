import streamlit as st

def load_css():

    st.markdown("""
    <style>

    /* =========================
       APP BACKGROUND (SOFT SaaS)
    ========================= */
    .stApp {
        background-color: #F8FAFC;
        font-family: Inter, sans-serif;
    }

    /* =========================
       SIDEBAR (DARK MODERN)
    ========================= */
    section[data-testid="stSidebar"] {
        background-color: #0B1220;
        color: #E2E8F0;
    }

    section[data-testid="stSidebar"] * {
        color: #E2E8F0;
    }

    /* =========================
       HEADINGS (CLEAN)
    ========================= */
    h1, h2, h3 {
        font-weight: 600;
        letter-spacing: -0.4px;
        color: #0F172A;
    }

    /* =========================
       CARD (Zocdoc STYLE)
    ========================= */
    .card {
        background: white;
        border: 1px solid #E2E8F0;
        border-radius: 14px;
        padding: 16px;
        margin-bottom: 12px;
        box-shadow: 0 1px 2px rgba(0,0,0,0.04);
        transition: all 0.2s ease;
    }

    .card:hover {
        border-color: #CBD5E1;
        transform: translateY(-1px);
    }

    /* =========================
       BUTTONS (SUBTLE PREMIUM)
    ========================= */
    .stButton > button {
        background-color: #0F172A;
        color: white;
        border-radius: 10px;
        padding: 8px 14px;
        border: none;
        font-weight: 500;
        font-size: 13px;
    }

    .stButton > button:hover {
        background-color: #1E293B;
    }

    /* =========================
       METRICS
    ========================= */
    [data-testid="stMetric"] {
        background: white;
        border: 1px solid #E2E8F0;
        border-radius: 12px;
        padding: 12px;
    }

    /* =========================
       REMOVE STREAMLIT CLUTTER
    ========================= */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    </style>
    """, unsafe_allow_html=True)
