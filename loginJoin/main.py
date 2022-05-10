from flask import Flask
from acountAPI import account_api

app = Flask(__name__)

app.register_blueprint(account_api)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)