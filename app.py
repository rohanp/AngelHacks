from flask import Flask, render_template, request, flash,\
					 session, redirect, url_for
from secret_key import secret_key 
from functools import wraps

app = Flask(__name__)

user_db = {'pandit.rohan@gmail.com': {
										'name': 'Rohan',
										'password': 'helo',
										'latitude': 30,
										'longitude': 50
										'grocery_list': []
									 },
			'ayylmao@gmail.com': {
									'name': 'John',
									'password': 'helo',
									'latitude': 31,
									'longitude':51
								 },

			'helo@gmail.com': {
								'name': 'Dat boi',
								'password': 'helo',
								'latitude': 32.5,
								'longitude':52.5

							  }

		  }

app.secret_key = secret_key

def login_required(test):
	@wraps(test)
	def wrap(*args, **kwargs):
		if 'name' in session:
			return test(*args, **kwargs)
		else:
			flash(u'You must login to access this page.')
			return redirect(url_for('login'))
	return wrap

@app.route("/")
def index():
	return render_template("pages/index.html") 

@app.route('/login', methods=['GET', 'POST'])
def login():

	if request.method == 'GET':
		return render_template('pages/login.html',)

	if request.method == 'POST':

		email = request.form['email']
		password = request.form['password']

		if user_db[email]['password'] != password:
			flash("Wrong password :o(")
			return render_template('pages/login.html')
		else:
			name = user_db[email]['name']
			session['name'] = name
			session['email'] = email
			flash(u'Hi {0}!'.format(name))

			return redirect(url_for('home'))

@app.route('/register', methods=['GET', 'POST'])
def register():

	if request.method == 'GET':
		return render_template('pages/register.html')

	elif request.method == 'POST':

		email = request.form['email']
		name = request.form['name']
		password = request.form['password']
          
		user_db[email] = {'name': name, 'password': password}

		session['name'] = name
		session['email'] = email
		flash(u'Hi {0}!'.format(session['name']))

		print(user_db)
		return redirect(url_for('home'))


@app.route('/logout')
@login_required
def logout():
    session.pop('name', None)
    return redirect(url_for('index'))


@app.route("/home")
@login_required
def home():
	return render_template("pages/home.html", email=session['email'])


@app.route("/requestFood", methods=['POST'])
@login_required
def request_food():

	x1 = float(request.form['latitude'])
	y1 = float(request.form['longitude'])

	def find_dist(user):
		x2 = user_db[user]['longitude']
		y2 = user_db[user]['longitude']

		return (x2 - x1)**2 - (y2 - y1)**2

	closest_user = min(user_db.keys(), key=find_dist)

	print("closest user is ", closest_user)

	flash("Worry not, food is on the way!")

	redirect(url_for('home'))

	return render_template("layouts/main.html")

@app.route("/updateLocation", methods=['POST'])
@login_required
def update_location():

	email = request.form['email']
	
	user_db[email]['latitude'] = float(request.form['latitude'])
	user_db[email]['longitude'] = float(request.form['longitude'])

	print("updated location for {email}".format(**locals()))
	print("new location is ", user_db[email]['latitude'], user_db[email]['longitude'])

	redirect(url_for('home'))

	return render_template("layouts/main.html")


if __name__ == "__main__":
	app.run(debug=True)

