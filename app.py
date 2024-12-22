from flask import Flask, render_template, request

app = Flask(__name__)

# Home Page
@app.route("/")
def home():
    return render_template("home.html")

# About Page
@app.route("/about")
def about():
    return render_template("about.html")

# Services Page
@app.route("/services")
def services():
    return render_template("services.html")

# Blog Page
@app.route("/blog")
def blog():
    posts = [
        {"title": "Post 1", "content": "Content for Post 1"},
        {"title": "Post 2", "content": "Content for Post 2"},
        {"title": "Post 3", "content": "Content for Post 3"}
    ]
    return render_template("blog.html", posts=posts)

# Contact Page
@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]
        return f"Thank you {name}, we have received your message!"
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
