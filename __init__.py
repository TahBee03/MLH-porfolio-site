from asyncio import constants # ?
import os # Import operating system tools
from sqlite3 import Time # ?
from urllib import response # ?
from flask import Flask, render_template, request, url_for, Response, jsonify  # Flask, render_template(), request.form, url_for(), Response, jsonify()
from dotenv import load_dotenv # load_dotenv()
from peewee import * # Used to connect to database
import datetime # datetime.datetime.now
from playhouse.shortcuts import model_to_dict # model_to_dict()

# NOTE: url_for is linked to the functions below and returns the corresponding index; preferred over hardcoding links
# NOTE: Database is closed after all uses with mydb.close() to prevent mysql container error
# NOTE: Added jsonify() to prevent "Access to fetch..." console error

load_dotenv() # Loads .env file; the data from MySQL is read
app = Flask(__name__)

# Connect to database depending on environment variable
if os.getenv("TESTING") == "true":
    # Establish copy of app in memory (?)
    print("Running in test mode")
    mydb = SqliteDatabase('file:memory?mode=memory&cache=shared', uri=True)
else: 
    mydb = MySQLDatabase(os.getenv("MYSQL_DATABASE"),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        host=os.getenv("MYSQL_HOST"),
        port=3306)

# Object-relational mapper (ORM) model (?)
class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = mydb

mydb.connect()
mydb.create_tables([TimelinePost])
if os.getenv("TESTING") != "true":
    mydb.close()

# WEBSITE PAGES
# Home page
@app.route("/")
def home():
    return render_template("home.html", url=os.getenv("URL"))

# Fellowship experience page
@app.route("/fellowship-experience/")
def fellowship():
    return render_template("fellowship.html", url=os.getenv("URL"))

# About me page
@app.route("/about-me/")
def about_me():
    return render_template("about_me.html", url=os.getenv("URL"))

# Contact page
@app.route("/contact/")
def contact():
    return render_template("contact.html", url=os.getenv("URL"))

# Posts page
@app.route("/timeline/")
def timeline():
    return render_template("timeline.html", url=os.getenv("URL"))
########################################

# HTTP requests + database interaction
# POST request: Adds timeline post to database
@app.route("/api/timeline-post/", methods=['POST'])
def post_timeline_post():
    # SOURCE: https://stackoverflow.com/questions/57664997/how-to-return-400-bad-request-on-flask
    if request.form.get('name') == None or request.form.get('name') == "":
        return Response(
            "Invalid name.",
            status=400
        )
    elif request.form.get('content') == "":
        return Response(
            "Invalid content.",
            status=400
        )
    elif not('@' in request.form.get('email')):
        return Response(
            "Invalid email.",
            status=400
        )
    name = request.form['name']
    email = request.form['email']
    content = request.form['content']
    timeline_post = TimelinePost.create(name=name, email=email, content=content)
    if os.getenv("TESTING") != "true":
        mydb.close()
    return model_to_dict(timeline_post)

# GET request: Puts posts in descending order
@app.route("/api/timeline-post/", methods=['GET'])
def get_timeline_post():
    api = {'timeline_posts':[model_to_dict(p) for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())]}
    response = jsonify(api)
    response.headers.add('Access-Control-Allow-Origin', '*')
    if os.getenv("TESTING") != "true":
        mydb.close()
    return response

# DELETE request: Deletes a specific post
@app.route("/api/timeline-post/<list_num>/", methods=['DELETE'])
def delete_timeline_post(list_num):
    # SOURCE: https://docs.peewee-orm.com/en/latest/peewee/querying.html
    data = TimelinePost.select().order_by(TimelinePost.created_at.desc())
    counter = 1
    for post in data:
        if counter == int(list_num):
            post.delete_instance()
            break
        else:
            counter += 1
    if os.getenv("TESTING") != "true":
        mydb.close()
    return 'ok'
########################################

if __name__ == "__main__":
    app.run(debug=True)