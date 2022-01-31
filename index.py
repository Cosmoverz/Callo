from flask import Flask, render_template
import json
import gunicorn

with open("data.json", "r") as file:
    posts = json.load(file)

app = Flask(__name__)


# DARK MODE

@app.route("/index.html")
@app.route("/index")
@app.route('/')
def get_all_posts():
    return render_template("index.html")


@app.route("/blog.html")
@app.route('/blog')
def blog():
    return render_template("blog.html", all_posts=posts)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.route("/about.html")
@app.route("/about")
def about():
    return render_template("about.html")


# ERROR

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404


# LIGHT MODE

prefix = "/light"


@app.route(f"{prefix}/blog.html")
@app.route(f'{prefix}/blog')
def blog_light():
    return render_template("blog-light.html", all_posts=posts)


@app.route(f"{prefix}/post/<int:index>")
def show_post_light(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post-light.html", post=requested_post)


@app.route(f"{prefix}/about.html")
@app.route(f"{prefix}/about")
def about_light():
    return render_template("about-light.html")


# @app.route("/contact", methods=["GET", "POST"])
# def contact():
#     if request.method == "POST":
#         data = request.form
#         data = request.form
#         send_email(data["name"], data["email"], data["phone"], data["message"])
#         return render_template("contact.html", msg_sent=True)
#     return render_template("contact.html", msg_sent=False)


# def send_email(name, email, phone, message):
#     email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
#     with smtplib.SMTP("smtp.gmail.com") as connection:
#         connection.starttls()
#         connection.login(OWN_EMAIL, OWN_PASSWORD)
#         connection.sendmail(OWN_EMAIL, email, email_message)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
