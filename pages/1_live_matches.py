import streamlit as st
import requests
import pandas as pd
from datetime import datetime

# ================= 🎨 Custom Background & Sidebar Style =================
page_bg = """
<style>
/* Main App Background */
[data-testid="stAppViewContainer"] {
    background-color: #7ED8FA; /* Light aqua blue */
}

/* Sidebar Background */
[data-testid="stSidebar"] {
    background-color: #50B6FE; /* Corporate blue */
}

/* Sidebar Title */
[data-testid="stSidebar"] h1, 
[data-testid="stSidebar"] h2, 
[data-testid="stSidebar"] h3 {
    color: white;
}

/* General Text */
.stMarkdown, .stText, .css-1v3fvcr {
    color: #1c1c1c;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)
# ========================================================================

# 🔑 API Key (directly set here)
CRICBUZZ_API_KEY = "759e4323e3msh8c6046223e5f544p1163e1jsneb8afe748d67"

if not CRICBUZZ_API_KEY:
    st.error("❌ RAPIDAPI_KEY not found. Please set it inside the script.")
    st.stop()

# 🌍 API Configuration
CRICBUZZ_HOST = "cricbuzz-cricket.p.rapidapi.com"

class CricbuzzAPI:
    def __init__(self):
        self.headers = {
            "x-rapidapi-key": CRICBUZZ_API_KEY,
            "x-rapidapi-host": CRICBUZZ_HOST,
        }
        self.base_url = "https://cricbuzz-cricket.p.rapidapi.com"

    def get_live_matches(self):
        """Fetch all live matches"""
        try:
            url = f"{self.base_url}/matches/v1/live"
            response = requests.get(url, headers=self.headers, timeout=10)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            st.error(f"⚠ Error fetching live matches: {e}")
            return {}

    def get_scorecard(self, match_id: str):
        """Fetch detailed scorecard by matchId"""
        try:
            url = f"{self.base_url}/mcenter/v1/{match_id}/scard"
            response = requests.get(url, headers=self.headers, timeout=10)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            st.error(f"⚠ Error fetching scorecard: {e}")
            return {}

def format_time(epoch_ms):
    """Convert epoch ms to human-readable format"""
    try:
        if epoch_ms:
            return datetime.fromtimestamp(int(epoch_ms) / 1000).strftime(
                "%d %b %Y, %I:%M %p"
            )
        return "N/A"
    except:
        return "N/A"

def show_innings_scorecard(api: CricbuzzAPI, match_id: str):
    """Display batting & bowling scorecard for selected match"""
    data = api.get_scorecard(match_id)
    if not data or "scorecard" not in data:
        st.warning("⚠ No scorecard data available.")
        return

    for i, innings in enumerate(data.get("scorecard", []), start=1):
        st.subheader(f"📊 Inning {i} - {innings.get('batteamname', 'Unknown')}")

        # 🏏 Batting Table
        batsmen_list = [
            {
                "Batsman": b.get("name", ""),
                "Runs": b.get("runs", 0),
                "Balls": b.get("balls", 0),
                "4s": b.get("fours", 0),
                "6s": b.get("sixes", 0),
                "SR": b.get("strkrate", 0),
                "Out": b.get("outdec", ""),
            }
            for b in innings.get("batsman", [])
        ]
        batsmen_df = pd.DataFrame(batsmen_list)
        if not batsmen_df.empty:
            st.write("### 🏏 Batting")
            st.dataframe(batsmen_df, use_container_width=True)

        # 🎯 Bowling Table
        bowlers_list = [
            {
                "Bowler": bl.get("name", ""),
                "Overs": bl.get("overs", 0),
                "Maidens": bl.get("maidens", 0),
                "Runs": bl.get("runs", 0),
                "Wickets": bl.get("wickets", 0),
                "Economy": bl.get("economy", 0),
            }
            for bl in innings.get("bowler", [])
        ]
        bowlers_df = pd.DataFrame(bowlers_list)
        if not bowlers_df.empty:
            st.write("### ☄️ Bowling")
            st.dataframe(bowlers_df, use_container_width=True)

        st.markdown("---")

def show_live_matches():
    """Main function to display live matches"""
    # 🔥 Animated GIF in header (~3× size)
    st.markdown(
        """
        <div style="display:flex; align-items:center;">
            <img src="https://cdnl.iconscout.com/lottie/premium/thumb/cricket-bat-8547074-6737094.gif" 
                 width="180" height="180" style="margin-right:20px;">
            <h1 style="font-size:50px; color:#003366;">Cricbuzz LiveStats - Live Matches</h1>
        </div>
        <p style="font-size:18px;">📡 Real-time cricket updates with stats & scorecards</p>
        """,
        unsafe_allow_html=True
    )

    api = CricbuzzAPI()
    data = api.get_live_matches()

    if not data or "typeMatches" not in data:
        st.warning("⚠ No live matches available right now.")
        return

    series_options = {}
    for type_match in data.get("typeMatches", []):
        match_type = type_match.get("matchType", "Unknown")
        for series in type_match.get("seriesMatches", []):
            series_info = series.get("seriesAdWrapper", {})
            if "matches" in series_info:
                series_name = series_info.get("seriesName", "Unknown Series")
                key = f"{series_name} ({match_type})"
                series_options[key] = series_info["matches"]

    if not series_options:
        st.warning("⚠ No active series at the moment.")
        return

    selected_series = st.selectbox(
        "🛑 LIVE 🎞️🎥 Select a Live Series", list(series_options.keys())
    )
    matches = series_options[selected_series]

    for match in matches:
        match_info = match.get("matchInfo", {})
        match_score = match.get("matchScore", {})

        team1 = match_info.get("team1", {}).get("teamName", "Team 1")
        team2 = match_info.get("team2", {}).get("teamName", "Team 2")
        match_id = match_info.get("matchId", "")

        st.subheader(f"🆚 {team1} vs {team2}")
        st.write(
            f"**Match:** {match_info.get('matchDesc', '')} ({match_info.get('matchFormat', '')})"
        )
        st.write(f"**Status:** {match_info.get('status', '')}")
        st.write(f"**State:** {match_info.get('stateTitle', '')}")

        venue = match_info.get("venueInfo", {})
        st.write(f"**Venue:** {venue.get('ground', '')}, {venue.get('city', '')}")
        st.write(f"**Start Time:** {format_time(match_info.get('startDate'))}")
        st.write(f"**End Time:** {format_time(match_info.get('endDate'))}")

        # Show Team Scores
        if "team1Score" in match_score:
            t1 = match_info.get("team1", {}).get("teamSName", "Team 1")
            t1_inn = match_score.get("team1Score", {}).get("inngs1", {})
            st.success(
                f"{t1}: {t1_inn.get('runs', 0)}/{t1_inn.get('wickets', 0)} "
                f"in {t1_inn.get('overs', 0)} overs"
            )

        if "team2Score" in match_score:
            t2 = match_info.get("team2", {}).get("teamSName", "Team 2")
            t2_inn = match_score.get("team2Score", {}).get("inngs1", {})
            st.success(
                f"{t2}: {t2_inn.get('runs', 0)}/{t2_inn.get('wickets', 0)} "
                f"in {t2_inn.get('overs', 0)} overs"
            )

        # Button to show detailed scorecard
        if match_id and st.button(
            f"📑 View Scorecard - {team1} vs {team2}", key=f"btn_{match_id}"
        ):
            show_innings_scorecard(api, match_id)

        st.markdown("---")

# ================= Sidebar Info =================
st.sidebar.title("ℹ️ About")
st.sidebar.markdown(
    """
**Cricbuzz LiveStats Dashboard**  
Built with **Streamlit + Cricbuzz API**, this app lets you explore:
- ✅ Real-time Live Matches  
- ✅ Series & Match Info  
- ✅ Batting & Bowling Scorecards  
"""
)

# 🚀 Run App
show_live_matches()
