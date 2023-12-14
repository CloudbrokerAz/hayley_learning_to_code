from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play():
    player_choice = request.form['choice']
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])
    # Your game logic here
    result = "It's a tie!"  # Placeholder
    return jsonify({'result': result, 'computer_choice': computer_choice})

if __name__ == '__main__':
    app.run(debug=True)
