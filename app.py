from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)


@app.route('/')
def index():
    with open("data.json", "r") as fileobj:
        blogs = json.loads(fileobj.read())
        return render_template("index.html", blogs=blogs)




@app.route('/add', methods=['GET', 'POST'])
def add_blog():
    #Read data rom the file
    with open("data.json", "r") as fileobj:
        blogs = json.loads(fileobj.read())

    if request.method == 'POST':
        blog = {
            "id": request.form.get("id"),
            "title": request.form.get("title"),
            "author": request.form.get("author"),
            "content": request.form.get("content")
        }

        blogs.append(blog)

        #Write data to the file
        with open("data.json", "w") as fileobj:
            json.dump(blogs, fileobj, indent=4)

        return redirect(url_for('index'))
    return render_template("add.html")



@app.route('/delete/<int:post_id>')
def delete(post_id):
    with open("data.json", "r") as fileobj:
        blogs = json.loads(fileobj.read())

        for blog in blogs:
            if int(blog['id']) == post_id:
                blogs.remove(blog)

    with open("data.json", "w") as fileobj:
        json.dump(blogs, fileobj, indent=4)

    return redirect(url_for('index'))



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)