import streamlit as st

# ---------------- Page Config ----------------
st.set_page_config(
    page_title="ℹ️ About Project",
    page_icon="🏆",
    layout="wide"
)

# ---------------- Gradient & Styling ----------------
st.markdown("""
<style>
/* Background Gradient */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #e0f2fe, #f0fdf4);
    color: #1f2937;
    font-family: 'Segoe UI', sans-serif;
    padding: 15px;
}

/* Header Ribbon */
.header-ribbon {
    text-align:center; padding:16px;
    background:linear-gradient(90deg, #2563eb, #10b981);
    color:white; border-radius:12px; margin-bottom:25px;
}

/* Tabs Font Size */
.css-1d391kg .css-10trblm { 
    font-size: 24px !important;  /* 2x bigger than default */
    font-weight: bold !important;
}

/* Footer */
.footer-box {
    margin-top:30px;
    padding:15px;
    background:linear-gradient(90deg, #2563eb, #10b981);
    color:white;
    border-radius:10px;
    text-align:center;
}
</style>
""", unsafe_allow_html=True)

# ---------------- Header ----------------
st.markdown("""
<div class="header-ribbon">
    <h1>🏆 About This Project</h1>
    <p>Cricbuzz Livestats + Rapid API + SQL</p>
</div>
""", unsafe_allow_html=True)

# ---------------- Content ----------------
st.markdown("## 🛠 Tools Learned")
st.markdown("""
- Python 3.13  
- Streamlit  
- MySQL, PyMySQL, PostgreSQL  
- Pandas for DataFrames  
- Rapid API for data fetch  
- VS Code & PyCharm
""")
st.markdown("## 🛠 Tools Used")
st.markdown("""
- Python 3.13  
- Streamlit  
- MySQL  
- Pandas for DataFrames  
- Rapid API  
- VS Code
""")

# Tabs for Sections
tabs = st.tabs([
    "🧑‍🤝‍🧑 Team & Player Endpoints", 
    "📊 Stats & Rankings", 
    "🌍 Series & Matches", 
    "🏟 Venue Info", 
    "📝 Match Scorecards", 
    "🧠 Suggested Variables"
])

with tabs[0]:
    st.markdown("""
    - **https://api.cricbuzz.com/teams/v1/{team_id}/players** → Team Players List  
    - **https://api.cricbuzz.com/stats/v1/player/{player_id}** → Player Overview  
    - **https://api.cricbuzz.com/stats/v1/player/{player_id}/batting** → Batting Stats  
    - **https://api.cricbuzz.com/stats/v1/player/{player_id}/bowling** → Bowling Stats  
    """)

with tabs[1]:
    st.markdown("""
    - **https://api.cricbuzz.com/stats/v1/topstats/0** → Global Top Stats  
    """)

with tabs[2]:
    st.markdown("""
    - **https://api.cricbuzz.com/series/v1/international** → International Series List  
    - **https://api.cricbuzz.com/series/v1/{series_id}** → Series Details  
    """)

with tabs[3]:
    st.markdown("""
    - **https://api.cricbuzz.com/venues/v1/{venue_id}** → Venue Details  
    """)

with tabs[4]:
    st.markdown("""
    - **https://api.cricbuzz.com/mcenter/v1/{match_id}** → Match Summary  
    - **https://api.cricbuzz.com/mcenter/v1/{match_id}/scard** → Full Scorecard  
    - **https://api.cricbuzz.com/mcenter/v1/{match_id}/hscard** → Highlight Scorecard  
    - **https://api.cricbuzz.com/mcenter/v1/{match_id}/leanback** → Leanback View  
    """)

with tabs[5]:
    st.code("""
venue_ids = [41, 34, 27, 31, 81, 19, 10, 153, 50, 40, 80, 485, 87, 11]
match_ids = [100283, 100290, 130019, ...]
""", language="python")

# ---------------- Footer ----------------
st.markdown("""
<div class="footer-box">
    ❤️ Thumbs up 👍<br>
    ✨ Built For: Cricket fans, analysts, and developers who thrive on live data and insights — crafted with passion by me.<br>
    💼 If you value my project, drop a thumbs up 👍 or I’d be glad to explore part-time or full-time opportunities to bring my skills to your team.
</div>
""", unsafe_allow_html=True)
