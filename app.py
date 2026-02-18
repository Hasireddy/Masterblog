from flask import Flask,render_template,request
import json

app = Flask(__name__)


@app.route('/')
def index():
    with open("data.json", "r") as fileobj:
        blogs = json.loads(fileobj.read())
        return render_template("index.html", blogs=blogs)



@app.route('/add', methods=['GET', 'POST'])
def add_blog():
    if request.method == 'POST':
        pass
    return render_template("add.html")



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)