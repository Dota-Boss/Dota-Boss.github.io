# report_utils.py
import requests
import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("OPENDOTA_API_KEY")

def generate_report(team_a, team_b):
    response = requests.get("https://api.opendota.com/api/teams")
    if response.status_code == 200:
        teams = response.json()
        # Just return the first team name for now
        return {
            "Team A": team_a,
            "Team B": team_b,
            "Matchup Rating": "8.2/10",
            "Suggested Ban": teams[0]['name']
        }
    else:
        return {
            "Team A": team_a,
            "Team B": team_b,
            "Matchup Rating": "N/A",
            "Suggested Ban": "API Error"
        }
