from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "UQ2Yik3ehsLPHsxxAWCH1w==eisXGbJaZOjddRb5"
API_URL = "https://api.api-ninjas.com/v1/exercises"

# List of valid muscle groups (you can expand this or fetch dynamically)
MUSCLE_GROUPS = [
    "Abdominals", "Abductors", "Adductors", "Biceps", "Calves", "Chest",
    "Forearms", "Glutes", "Hamstrings", "Lats", "Lower Back", "Middle Back",
    "Neck", "Quadriceps", "Traps", "Triceps"
]

def get_exercises_by_muscle(muscle):
    """Fetches exercises for the selected muscle group."""
    headers = {'X-Api-Key': API_KEY}
    response = requests.get(f"{API_URL}?muscle={muscle}", headers=headers)
    if response.status_code == 200:
        return response.json()
    return []

@app.route("/", methods=["GET", "POST"])
def index():
    exercises = []
    selected_muscle = None

    if request.method == "POST":
        selected_muscle = request.form.get("muscle")
        if selected_muscle:
            exercises = get_exercises_by_muscle(selected_muscle)

    return render_template("index.html", muscle_groups=MUSCLE_GROUPS, exercises=exercises)

if __name__ == "__main__":
    app.run(debug=True)

