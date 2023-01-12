from . import db # Imports DB object from current package
from sqlalchemy.sql import func

# "Whenever you want to make a new database model and in order to store a different type of object, you're going to define
# the name of the object ... and inherit from db.Model."

class Post(db.Model):
    # Database columns; schema
    id = db.Column(db.Integer, primary_key=True) # Primary key
    name = db.Column(db.String)
    email = db.Column(db.String)
    content = db.Column(db.String)
    date = db.Column(db.DateTime(timezone=True), default=func.now()) # Date is automatically calculated with func.now()