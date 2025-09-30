# 🏏 Cricbuzz LiveStats: Real-Time Cricket Insights & SQL-Based Analytics
A **Python + Streamlit** project that delivers real-time cricket updates, live scorecards, and player insights using the Cricbuzz API. This project also integrates with a **MySQL** to store and manage cricket data, such as players, squads, and key statistics.

## 🚀 Features
* **📊 Live Cricket Updates** – Fetches real-time match details, including scores, status, and venues.
* **📝 Scorecards & Player Insights** – View batting, bowling, and player statistics at a glance.
* **🎯 Interactive Streamlit Dashboard** – A clean, responsive UI with filtering options.
* **🗄️ Database Support** – A MySQL backend for data persistence.
* **🔎 SQL Query Playground** – Write and execute custom SQL queries directly inside the app.
* **🛠 CRUD Operations** – Add, update, delete, and view cricket data in real time.

## ⚙️ Installation & Setup
### 1️⃣ Clone the Repository

```
git clone <repository-url>
cd cricbuzz_livestats
```

### 2️⃣ Install Dependencies

```
pip install -r requirements.txt
```

### 3️⃣ Configure Environment Variables
Create a `.env` file in the project's root directory and add your database and API credentials. This helps keep your sensitive information secure.

```
RAPIDAPI_KEY="759e4323e3msh8c6046223e5f544p1163e1jsneb8afe748d67"
DB_HOST="localhost"
DB_USER="root"
DB_PASSWORD="Pass123"
DB_NAME="cricket_db"
```

### 4️⃣ Run the App

```
streamlit run app.py
```

## 🎯 Key Features Walkthrough
### 1️⃣ Live Matches Dashboard
* **Auto-Refresh**: The dashboard updates every 30 seconds for live scores.
* **Filters**: You can filter matches by format, status, and venue.
* **Match Details**: Click on a match to view ball-by-ball information.
* **Visuals**: See real-time match statistics and data visualizations.

### 2️⃣ Top Stats & Analytics
* **Batting Leaders**: View leaderboards for runs, averages, strike rates, and boundaries.
* **Bowling Leaders**: See top bowlers by wickets, economy rates, and maidens.
* **Team Trends**: Compare teams across different cricket formats.
* **Data Management**: Quickly refresh, clear, or regenerate data.

### 3️⃣ SQL Query Playground
* **Pre-Built Queries**: Get quick insights from a list of pre-built queries for common stats.
* **Custom Query Builder**: Write and execute your own SQL queries.
* **Schema Explorer**: An interactive browser to view your database structure.

### 4️⃣ CRUD Operations
* **Player Management**: Add, update, and remove player information.
* **Match Management**: Manage match schedules and results.
* **Performance Data**: Insert or clean up batting and bowling statistics.

## 📦 requirements.txt

```
streamlit
pandas
requests
python-dotenv
mysql-connector-python
SQLAlchemy
PyMySQL
```

## 🙏 Acknowledgments
* **Cricbuzz API** – For rich, real-time cricket data.
* **Streamlit** – For the easy-to-use web app framework.
* **MySQL** – For reliable data storage and queries.

## ❤️Thumbs up 👍
✨ Built For: Cricket fans, analysts, and developers who thrive on live data and insights — crafted with passion by me.  
💼 If you value my project, drop a thumbs up 👍 or I’d be glad to explore part-time or full-time opportunities to bring my skills to your team.  
