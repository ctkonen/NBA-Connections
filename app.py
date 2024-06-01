from flask import Flask, render_template, request, jsonify
from get_Players import ensure_unique_groups, urls

app = Flask(__name__)

# Get unique groups of players
unique_player_groups = ensure_unique_groups(urls)

@app.route('/')
def index():
    return render_template('index.html', player_groups=unique_player_groups)

@app.route('/check', methods=['POST'])
def check():
    selected_players = request.json.get('selectedPlayers', [])
    correct_groups = set(player for group in unique_player_groups for player in group)
    
    if len(selected_players) != 4:
        return jsonify({"message": "Please select exactly 4 players.", "success": False})
    
    correct_selection = all(player in correct_groups for player in selected_players)
    if correct_selection:
        return jsonify({"message": "Correct!", "success": True})
    else:
        return jsonify({"message": "Incorrect, try again.", "success": False})

if __name__ == '__main__':
    app.run(debug=True)

