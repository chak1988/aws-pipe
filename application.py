from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_function():
    return "Hello from Flask main page"

@app.route("/help")
def help_function():
    return "<b><font color=blue> Hello from HELP page</font></b>"

@app.route("/<username>")
def user(username):
    return f"Hello {username}"

@app.route("/path/<path:subpath>")
def subpath(subpath):
    return "Route is : " + subpath #получаем так любой под-путь

@app.route("/square/<int:x>")
def square(x):
    return f"square of x is : {x * x}"
@app.route("/index.html")
def php_func():
    my_file = open('index.html', mode = "r")
    content = my_file.read()
    my_file.close()
    return content


if __name__ == "__main__":
    #app.env = 'Work hard'
    app.run(debug = True)