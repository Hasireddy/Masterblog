from flask import Flask,render_template
import json

app = Flask(__name__)


@app.route('/')
def index():
    with open("data.json", "r") as fileobj:
        blogs = json.loads(fileobj.read())
        return render_template("index.html", blogs=blogs)




if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)