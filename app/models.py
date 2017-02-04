from app import db

class Product(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(80), nullable=False)
	description = db.Column(db.String(140))
	rating = db.Column(db.Integer, nullable=False)
	price = db.Column(db.Float, nullable=False)

	def __init__(self, name, rating, price, description=None):
		self.name = name
		self.rating = rating
		self.price = price
		self.description = description

	def __repr__(self):
		return "<Product %r >" % self.name