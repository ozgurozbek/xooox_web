from flask import Flask, render_template, request
#pip install flask

app = Flask(__name__)

# Pages
@app.route("/")
def root():
    return render_template('index.html', button_val = "Yeniden Başlat")

# Page modules
@app.route('/get', methods=['GET'])
def get_dpf():
    board = request.args.get('board', default=['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'], type=list)
    return (type(board), board)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
