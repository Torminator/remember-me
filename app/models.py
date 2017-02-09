from app import db

class Product(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(80), nullable=False)
	description = db.Column(db.String(140))
	rating = db.Column(db.Integer, nullable=False)
	price = db.Column(db.Float, nullable=False)
	img_url = db.Column(db.String(1024), nullable=False)

	def __init__(self, name, rating, price, img_url, description=None):
		self.name = name
		self.rating = rating
		self.price = price
		self.img_url = img_url
		self.description = description

	def __repr__(self):
		return "<Product %r >" % self.name