from flask import Flask

application = Flask(__name__)

@application.route("/")
def hello():
    return "Welcome to UNIQUE88 Sample Python Flask App"


@application.route("/hello")
def hello_unique():
    return "Hello from second page to UNIQUE88 ! "

if __name__ == "__main__":
    application.run(port=8000, debug=True)
