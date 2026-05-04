from flask import Flask,render_template
import requests
from post import Post

posts = requests.get("https://api.npoint.io/674f5423f73deab1e9a7").json()
post_objects = [] # Creating an array to check further in show_post
for post in posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"] , post["image_url"]) # Creating an onject of the Post class
    post_objects.append(post_obj)

app = Flask(__name__)

@app.route('/')
def get_all_posts():
    return render_template("index.html" , all_posts =post_objects)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

# @app.route('/post')
# def post():
#     return render_template("post.html")

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in post_objects:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

if __name__ == "__main__":
    app.run(debug=True)