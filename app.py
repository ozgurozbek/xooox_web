from flask import Flask, render_template, request
#pip install flask
import ai

app = Flask(__name__)

# Pages
@app.route("/")
def root():
    return render_template('index.html', button_val = "Yeniden Başlat")

# Page modules
@app.route('/get', methods=['GET'])
def get():
    input_button_val = request.args.get('board', default=-1, type=int)
    return str(ai.processBoard(input_button_val))

if __name__ == "__main__":
    app.run(host='0.0.0.0')
