from flask import Blueprint, render_template, request, redirect, url_for
from .models import Post
from . import db # Imports DB object from current package

# The use of Blueprint turns this file into a "blueprint" i.e. it contains routes for the app
views = Blueprint('views', __name__)

# Home page
@views.route('/')
def home():
    return render_template('home.html')

# Fellowship experience page
@views.route('/fellowship-experience')
def fellowship():
    return render_template('fellowship.html')

# About me page
@views.route('/about-me')
def about_me():
    return render_template('about_me.html')

# Contact page
@views.route('/contact')
def contact():
    return render_template('contact.html')

# Posts page
@views.route('/timeline', methods=['GET', 'POST'])
def timeline():
    if request.method == 'GET':
        print(Post.query.all())
        for post in Post.query.all():
            print('[' + str(post.id) + ']: ' + str(post.content))

    if request.method == 'POST':
        # Grab data from the submitted form
        name = request.form.get('name')
        email = request.form.get('email')
        content = request.form.get('content')

        # Create new post in database
        new_post = Post(name=name, email=email, content=content)
        db.session.add(new_post)
        db.session.commit()

        return redirect(url_for('views.timeline'))
        
    return render_template('timeline.html', posts=Post.query.all())

# NOTE TO SELF: Since URLs default to a GET request in browsers, only use the DELETE request via cmd
@views.route('/timeline/<num>/delete', methods=['DELETE'])
def delete_post(num):
    posts = Post.query.all()
    if int(num) > 0 and int(num) <= len(posts):
        db.session.delete(posts[int(num) - 1])
        db.session.commit()
    return redirect(url_for('views.timeline'))