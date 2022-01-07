from flask import Flask, render_template, request, jsonify
#pip install flask
import ai

app = Flask(__name__)
empty_board = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# Pages
@app.route("/")
def root():
    return render_template('index.html')

# Page modules
@app.route('/get', methods=['GET']) # Maybe it can converted to a POST only, using a form to this.
def get():
    input_board = [int(i) for i in request.args.get('board', default=empty_board, type=str).split(",")]
    return jsonify(ai.runMinimax(input_board))

if __name__ == "__main__":
    app.run(host='0.0.0.0')
