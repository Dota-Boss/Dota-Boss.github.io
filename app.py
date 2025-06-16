from flask import Flask, render_template, request
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scout', methods=['POST'])
def scout():
    player_name = request.form.get('player_name')
    
    # Dummy data just to test form pipeline
    report = {
        "Player": player_name,
        "MMR": "4,250",
        "Favorite Hero": "Earth Spirit",
        "Win Rate": "56%",
        "Role": "Roaming Support"
    }

    return render_template('index.html', report=report)


if __name__ == '__main__':
    app.run(debug=True)