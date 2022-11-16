from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return "<h1>L'app flask fonctionne dans le container docker</h2>"


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)