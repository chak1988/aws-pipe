from flask import Flask

application = Flask(__name__)

@application.route("/")
def hello():
    return "Welcome to UNIQUE88 Sample Python Flask App"

if __name__ == "__main__":
    application.run(host='127.0.0.1', port=5000, debug=True)
