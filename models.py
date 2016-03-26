from flask.ext.mongoengine import MongoEngine
from werkzeug import generate_password_hash, check_password_hash

db = MongoEngine()

class User(db.Document):
	#user id is automatically created in MongoDB
	firstname = db.StringField()
	lastname = db.StringField()
	email = db.StringField(unique=True, required=True)
	pwdhash = db.StringField()

	def __init__(self, firstname, lastname, email, password):
		self.firstname = firstname.title()
		self.lastname = lastname.title()
		self.email = email.lower()
		self.set_password(password)

	def set_password(self, password):
		self.pwdhash = generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.pwdhash, password)

