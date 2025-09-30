import streamlit as st

# ✅ Page config
st.set_page_config(page_title="Cricbuzz Analytics", page_icon="🏏", layout="wide")

# ✅ CSS for full-page background and glowing banner
st.markdown("""
    <style>
        [data-testid="stAppViewContainer"] {
            background-image: url('https://i.ibb.co/LXhN4wJq/bg.jpg');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }

        .banner {
            background-image: url('https://media.licdn.com/dms/image/v2/C5616AQEa1TojQkeZIQ/profile-displaybackgroundimage-shrink_350_1400/profile-displaybackgroundimage-shrink_350_1400/0/1584768131661?e=1761782400&v=beta&t=455BkCYjAgCJTTBVRTSf-0qlMlEAz1w-JHfQkZVFugM');
            background-size: cover;
            background-position: center;
            padding: 60px 30px;
            border-radius: 12px;
            margin-bottom: 30px;
            text-align: center;
            box-shadow: 0 4px 12px rgba(0,0,0,0.2);
        }
        .banner h1 {
            font-size: 48px;
            color: white;
            text-shadow: 2px 2px 6px rgba(0,0,0,0.8);
        }
        .banner p {
            font-size: 20px;
            color: white;
            text-shadow: 1px 1px 4px rgba(0,0,0,0.7);
        }
        .card {
            padding: 20px;
            border-radius: 15px;
            text-align: center;
            font-weight: bold;
            font-size: 16px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            margin-bottom: 10px;
        }
        .live { background-color: #4B9EFF; color: white; }
        .top  { background-color: #FFD84B; color: black; }
        .sql  { background-color: #4BFFB3; color: black; }
        .crud { background-color: #FF4B4B; color: white; }
        .footer-box {
            background: rgba(0,0,0,0.6);
            border-radius: 12px;
            padding: 20px;
            margin-top: 50px;
            text-align: center;
            color: #eeeeee;
        }
    </style>
""", unsafe_allow_html=True)

# ✅ Banner section
st.markdown("""
    <div class="banner">
        <h1>🏏 Cricbuzz SQL Analytics</h1>
        <p>Welcome, Sholingan! Choose a module below to explore your cricket data.</p>
    </div>
""", unsafe_allow_html=True)

# ✅ Navigation cards
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="card live">📺 Live Matches<br><span style="font-size:14px;">View current match status and scores</span></div>', unsafe_allow_html=True)
    if st.button("Go to Live Matches"):
        st.switch_page("pages/1_live_matches.py")

    st.markdown('<div class="card sql">🧠 SQL Queries<br><span style="font-size:14px;">Run custom SQL queries on your database</span></div>', unsafe_allow_html=True)
    if st.button("Go to SQL Queries"):
        st.switch_page("pages/3_sql_queries.py")

with col2:
    st.markdown('<div class="card top">📊 Top Stats<br><span style="font-size:14px;">See top performers across formats</span></div>', unsafe_allow_html=True)
    if st.button("Go to Top Stats"):
        st.switch_page("pages/2_top_stats.py")

    st.markdown('<div class="card crud">🔄 CRUD Operations<br><span style="font-size:14px;">Add, edit, or delete player and match data</span></div>', unsafe_allow_html=True)
    if st.button("Go to CRUD Operations"):
        st.switch_page("pages/4_crud_operations.py")

# ✅ Footer (only passion/message)
st.markdown("""
<div class="footer-box">
    <p>❤️ Thumbs up 👍</p>
    <p>✨ <b>Built For:</b> Cricket fans, analysts, and developers who thrive on live data and insights — crafted with passion by me.</p>
    <p>💼 If you value my project, drop a thumbs up 👍 or I’d be glad to explore part-time or full-time opportunities to bring my skills to your team.</p>
</div>
""", unsafe_allow_html=True)
