import streamlit as st
import http.client
import json
import requests
import pandas as pd
import os
from urllib.parse import quote

# ---------------- Setup ----------------
st.set_page_config(page_title="🏏 Cricbuzz LiveStats", layout="wide")

# 🔑 API KEY (directly set here)
API_KEY = "759e4323e3msh8c6046223e5f544p1163e1jsneb8afe748d67"   # <-- replace with your actual RapidAPI key

if not API_KEY:
    st.error("❌ RAPIDAPI_KEY is missing. Please paste your key in the code.")
    st.stop()

HEADERS = {"x-rapidapi-key": API_KEY, "x-rapidapi-host": "cricbuzz-cricket.p.rapidapi.com"}
BASE_URL = "cricbuzz-cricket.p.rapidapi.com"

# ---------------- Global CSS ----------------
st.markdown("""
    <style>
    /* Background */
    html, body, [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #8082D6, #7ED8FA);
        font-family: 'Segoe UI', sans-serif;
        color: #f5f5f5;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background: linear-gradient(135deg, #50B6FE, #2297FA);
        color: white !important;
    }
    section[data-testid="stSidebar"] * {
        color: white !important;
    }

    /* Titles */
    h1, h2, h3, h4, h5 {
        font-weight: 700 !important;
        color: #fdfdfd !important;
        letter-spacing: 0.5px;
    }

    /* DataFrame Styling */
    div[data-testid="stDataFrame"] table {
        border-radius: 12px;
        overflow: hidden;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }

    /* Metric Cards */
    .metric-card {
        background: rgba(255, 255, 255, 0.08);
        padding: 12px;
        border-radius: 12px;
        text-align: center;
        margin: 8px;
        box-shadow: 0 3px 10px rgba(0,0,0,0.25);
        transition: transform 0.2s;
    }
    .metric-card:hover {
        transform: scale(1.05);
    }
    .metric-title {
        font-size: 14px;
        color: #ddd;
        margin-bottom: 4px;
    }
    .metric-value {
        font-size: 20px;
        font-weight: bold;
        color: #fff;
    }

    /* Warning / Info messages */
    .stWarning, .stInfo {
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------- Helper Functions ----------------
def search_players(query):
    """Search for players by name"""
    query_encoded = quote(query)
    conn = http.client.HTTPSConnection(BASE_URL)
    conn.request("GET", f"/stats/v1/player/search?plrN={query_encoded}", headers=HEADERS)
    res = conn.getresponse()
    data = res.read()
    conn.close()
    try:
        return json.loads(data.decode("utf-8"))
    except:
        return {}

def get_player_details(player_id):
    """Fetch player details"""
    conn = http.client.HTTPSConnection(BASE_URL)
    conn.request("GET", f"/stats/v1/player/{player_id}", headers=HEADERS)
    res = conn.getresponse()
    data = res.read()
    conn.close()
    try:
        return json.loads(data.decode("utf-8"))
    except:
        return {}

def get_player_stats(player_id, stat_type="batting"):
    """Fetch player stats (batting or bowling)"""
    url = f"https://cricbuzz-cricket.p.rapidapi.com/stats/v1/player/{player_id}/{stat_type}"
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        return response.json()
    return {}

def parse_stats_table(stats_json, drop_columns=None):
    """Convert stats JSON to dataframe"""
    if not stats_json or "headers" not in stats_json or "values" not in stats_json:
        return pd.DataFrame()
    headers = stats_json["headers"]
    rows = [row["values"] for row in stats_json["values"]]
    df = pd.DataFrame(rows, columns=headers)
    if drop_columns:
        df = df.drop(columns=drop_columns, errors="ignore")
    return df

# ---------------- Sidebar ----------------
st.sidebar.title("ℹ️ About")
st.sidebar.markdown("""
**Cricbuzz LiveStats Dashboard**  
Built with **Streamlit + Cricbuzz API** 🎯  

✅ Real-time Player Profiles  
✅ ICC Rankings (Premium UI)  
✅ Batting & Bowling Stats  
""")

# ---------------- Main Page ----------------
st.title("🏏 Cricbuzz Player Stats & ICC Rankings")
player_name = st.text_input("🔍 Enter player name (e.g. Virat Kohli, Joe Root):")

if player_name:
    results = search_players(player_name)

    if "player" in results and results["player"]:
        player_options = {p["name"]: p for p in results["player"]}
        selected_name = st.selectbox("Select a player:", list(player_options.keys()))
        selected_player = player_options[selected_name]

        tabs = st.tabs(["📌 Profile", "🏏 Batting Stats", "🎯 Bowling Stats"])

        # ---------------- Profile Tab ----------------
        with tabs[0]:
            st.subheader(f"{selected_player['name']} ({selected_player.get('teamName','N/A')})")
            details = get_player_details(selected_player["id"])
            st.markdown(f"📅 **DOB:** {selected_player.get('dob', 'N/A')}")
            st.markdown(f"🧢 **Role:** {details.get('role', 'N/A')}")
            st.markdown(f"🏏 **Batting Style:** {details.get('bat', 'N/A')}")
            st.markdown(f"⚾ **Bowling Style:** {details.get('bowl', 'N/A')}")
            st.markdown(f"🌍 **Birth Place:** {details.get('birthPlace', 'N/A')}")
            st.markdown(f"👥 **Teams:** {details.get('teams', 'N/A')}")

            # ---------------- ICC Rankings ----------------
            if "rankings" in details and details["rankings"]:
                st.subheader("🏆 ICC Rankings")
                rankings = details["rankings"]

                col1, col2, col3 = st.columns(3)

                def styled_metric(title, value):
                    """Styled ranking card"""
                    try:
                        rank_int = int(value)
                    except:
                        rank_int = None
                    color = "#3b6978"  # default card color
                    if rank_int is not None:
                        if rank_int <= 5:
                            color = "#16a085"
                        elif rank_int <= 10:
                            color = "#f39c12"
                        else:
                            color = "#7f8c8d"
                    return f"""
                    <div class='metric-card' style='background-color:{color};'>
                        <div class='metric-title'>{title}</div>
                        <div class='metric-value'>{value}</div>
                    </div>
                    """

                with col1:
                    st.markdown("### 🏏 Batting")
                    for k, v in rankings.get("bat", {}).items():
                        if "DiffRank" not in k:
                            label = k.replace("odi","ODI ").replace("test","Test ").replace("t20","T20 ").replace("Rank"," Rank").replace("Best"," Best")
                            st.markdown(styled_metric(label.strip(), v), unsafe_allow_html=True)

                with col2:
                    st.markdown("### ⚾ Bowling")
                    for k, v in rankings.get("bowl", {}).items():
                        if "DiffRank" not in k:
                            label = k.replace("odi","ODI ").replace("test","Test ").replace("t20","T20 ").replace("Rank"," Rank").replace("Best"," Best")
                            st.markdown(styled_metric(label.strip(), v), unsafe_allow_html=True)

                with col3:
                    st.markdown("### 🏏⚾ All-Rounder")
                    for k, v in rankings.get("all", {}).items():
                        if "DiffRank" not in k:
                            label = k.replace("odi","ODI ").replace("test","Test ").replace("t20","T20 ").replace("Rank"," Rank").replace("Best"," Best")
                            st.markdown(styled_metric(label.strip(), v), unsafe_allow_html=True)

        # ---------------- Batting Stats Tab ----------------
        with tabs[1]:
            st.subheader("🏏 Batting Stats")
            batting_stats = get_player_stats(selected_player["id"], "batting")
            df_bat = parse_stats_table(batting_stats, drop_columns=["400"])
            if not df_bat.empty:
                st.dataframe(df_bat, use_container_width=True)
            else:
                st.warning("No batting stats available.")

        # ---------------- Bowling Stats Tab ----------------
        with tabs[2]:
            st.subheader("☄️ Bowling Stats")
            bowling_stats = get_player_stats(selected_player["id"], "bowling")
            df_bowl = parse_stats_table(bowling_stats, drop_columns=["10w"])
            if not df_bowl.empty:
                st.dataframe(df_bowl, use_container_width=True)
            else:
                st.warning("No bowling stats available.")
    else:
        st.warning("⚠ No players found. Try another name.")
