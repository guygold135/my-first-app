from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>It's Alive!</h1><p>My first app running locally.</p>"

if __name__ == "__main__":
    app.run(debug=True)