from flask import render_template, request
from app import app
from app.report_utils import generate_report  # Adjust path if moved

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scout', methods=['POST'])
def scout():
    team_a = request.form.get('teamA')
    team_b = request.form.get('teamB')
    report = generate_report(team_a, team_b)
    return render_template('index.html', report=report)
