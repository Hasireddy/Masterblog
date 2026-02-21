from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)


@app.route('/')
def index():
    """This route will display all blog posts"""
    try:
        with open("data.json", "r") as fileobj:
            blogs = json.load(fileobj)
            return render_template("index.html", blogs=blogs)

    except FileNotFoundError:
        print("File not found")




@app.route('/add', methods=['GET', 'POST'])
def add_blog():
    """This route allows user to add a
    new blog post"""

    #Read data from the file
    with open("data.json", "r") as fileobj:
        blogs = json.load(fileobj)
        length = len(blogs)
        last_index = len(blogs)

    if request.method == 'POST':
        blog = {
            "id": last_index + 1,
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
    """This route removes the specified blog post
    from the blogs"""

    with open("data.json", "r") as fileobj:
        blogs = json.load(fileobj)

        for blog in blogs:
            if int(blog['id']) == post_id:
                blogs.remove(blog)

    with open("data.json", "w") as fileobj:
        json.dump(blogs, fileobj, indent=4)

    return redirect(url_for('index'))


@app.route('/update/<int:post_id>', methods=['GET', 'POST'])
def update(post_id):
    """This route updates a specified blog post"""

    with open("data.json", "r") as fileobj:
        blogs = json.load(fileobj)

        post = None
        for blog in blogs:
            if int(blog['id']) == post_id:
                post = blog
                break

        if post is None:
            return redirect(url_for('index'))

    if request.method == 'POST':
        post['title'] = request.form.get('title')
        post['author'] = request.form.get('author')
        post['content'] = request.form.get('content')

        with open("data.json", "w") as file:
              json.dump(blogs, file, indent=4)

        return redirect(url_for('index'))

    # GET request → show update form with current values
    return render_template('update.html', post=post)




if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)