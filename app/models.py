from app import db
from datetime import date

class Product(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(80), nullable=False)
	description = db.Column(db.String(140))
	rating = db.Column(db.Integer, nullable=False)
	price = db.Column(db.Float, nullable=False)
	date_stamp = db.Column(db.Date)
	img_url = db.Column(db.String(1024), nullable=False)

	def __init__(self, name, rating, price, img_url, description=None):
		self.name = name
		self.rating = rating
		self.price = price
		self.img_url = img_url
		self.date_stamp = date.today()
		self.description = description

	def __repr__(self):
		return "<Product %r >" % self.name

class Login(db.Model):
	username = db.Column(db.String(80), primary_key=True)
	password = db.Column(db.String(80), nullable=False)

	def __init__(self, username, password):
		self.username = username
		self.password = password

	def __repr__(self):
		return "<User %r >" % self.username