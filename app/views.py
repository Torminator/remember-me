# This Python file uses the following encoding: utf-8

from app import app
from flask import render_template, g, request, json, redirect, session
from sqlite3 import dbapi2 as sqlite3
import requests
from bs4 import BeautifulSoup


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

def load_users():
	db = get_db()
	cur = db.execute("SELECT * FROM login")
	users = cur.fetchall()
	close_db()
	return users

@app.route('/')
def login():
	return render_template("login.html")

@app.route('/index')
def index():
	if "username" in session: 
		db = get_db()
		cur = db.execute('SELECT name, description, rating, price, img_url FROM product')
		entries = cur.fetchall()
		close_db()
		return render_template("index.html", entries=entries)
	else:
		return redirect("/")

@app.route('/addProduct', methods=['POST'])
def addProduct():
	# input from the AddProduct form
	input = request.form
	# get the fírst image from Google Search
	search_words = input["name"].replace(" ", "+")
	r = requests.get("https://www.google.de/search?q=" + search_words + "&tbm=isch")
	soup = BeautifulSoup(r.content, "html5lib")
	images = soup.find_all("img")
	url = images[0]["src"]
	# insert a new product
	db = get_db()
	cur = db.execute("INSERT INTO product (name, description, rating, price, img_url) VALUES (?,?,?,?,?)", 
		(input["name"], input["description"], input["optradio"], input["price"], url))
	db.commit()
	close_db()
	return json.dumps({"status": "OK", "url": url})

@app.route('/deleteProduct', methods=['POST'])
def deleteProduct():
	input = request.form
	db = get_db()
	cur = db.execute("DELETE FROM product WHERE name=?", [input["value"]])
	db.commit()
	close_db()
	return json.dumps({"status": "OK"})

@app.route('/checkLogin', methods=['POST'])
def checkLogin():
	input = request.form
	users = load_users()
	user = next(filter(lambda x: x[0] == input["username"], users), None)
	if user != None:
		if input["password"] == user[1]:
			session["username"] = input["username"]
			return json.dumps({"status": "OK"})

	return json.dumps({"status": "BAD"})