from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "This is the server for FYP Project, Send request on /data endpoint to get result"

@app.route('/data', methods=['POST', 'GET'])
def data():
    return "This is the server for FYP Project, Send request on /data endpoint to get result"


if __name__ == '__main__':
    app.run(debug=True)
