from app import app
from flask import render_template, g, request, json
from sqlite3 import dbapi2 as sqlite3

def connect_db():
	db = sqlite3.connect(app.config['DATABASE'])
	db.row_factory = sqlite3.Row
	return db

def get_db():
	if not hasattr(g, 'sqlite_db'):
		g.sqlite_db = connect_db()
	return g.sqlite_db

def close_db():
	if hasattr(g, 'sqlite_db'):
		g.sqlite_db.close()


@app.route('/')
def index():
	db = get_db()
	cur = db.execute('SELECT * FROM product')
	entries = cur.fetchall()
	close_db()
	return render_template("index.html", entries=entries)

@app.route('/addProduct', methods=['POST'])
def addProduct():
	input = request.form
	db = get_db()
	cur = db.execute("INSERT INTO product (name, description, rating, price) VALUES (?,?,?,?)", 
		(input["name"], input["description"], input["optradio"], input["price"]))
	db.commit()
	close_db()
	return json.dumps({"status": "OK"})

@app.route('/deleteProduct', methods=['POST'])
def deleteProduct():
	input = request.form
	db = get_db()
	cur = db.execute("DELETE FROM product WHERE id=?", input["value"])
	db.commit()
	close_db()
	return json.dumps({"status": "OK"})