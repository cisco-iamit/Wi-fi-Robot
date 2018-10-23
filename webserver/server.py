from flask import Flask, render_template
app = Flask(__name__, template_folder='.')

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/move_forward', methods=['GET'])
def move_forward():
    pass

@app.route('/turn_left', methods=['GET'])
def turn_left():
    pass

@app.route('/turn_right', methods=['GET'])
def turn_right():
    pass

@app.route('/move_back', methods=['GET'])
def move_back():
    pass
