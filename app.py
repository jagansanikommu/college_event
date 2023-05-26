from flask import Flask, render_template,request,redirect,url_for,send_from_directory
from models import create_post,get_posts

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/about_us")
def about_us():
    return render_template('about-us.html')

@app.route("/gallery")
def gallery():
    return render_template('gallery.html')

@app.route("/pricing")
def pricing():
    return render_template('pricing.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/social")
def social():
    return render_template('social.html')

@app.route("/schedule")
def schedule():
    return render_template('schedule.html')

@app.route("/query")
def query():
    return render_template('query.html')

@app.route("/post_query", methods={"GET","POST"})
def post_query():
    if request.method == 'POST':
        query = request.form.get('query')
        mail = request.form.get('mail')
        create_post(mail,query)
    return render_template('mail-success.html')

@app.route("/admin", methods={"GET","POST"})
def admin():
    if request.method == 'POST':
        if request.form.get('password') == '725':
            posts = get_posts()
            return render_template('admin.html' , posts=posts)
    return render_template('admin.html')

@app.route("/mail_success")
def mail_success():
    return render_template('mail-success.html')

@app.route("/404")
def error_404():
    return render_template('404.html')

if __name__ == '__main__':
    app.run(debug=True)
