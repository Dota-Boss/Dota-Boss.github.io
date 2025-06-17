from flask import Flask, render_template, request
import os
from dotenv import load_dotenv
from report_utils import generate_report


load_dotenv()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scout', methods=['POST'])
def scout():
    team_a = request.form.get('teamA')
    team_b = request.form.get('teamB')

    report = generate_report(team_a, team_b)
    return render_template('index.html', report=report)


if __name__ == '__main__':
    app.run(debug=True)