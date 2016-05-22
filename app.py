from flask import Flask, render_template, request, flash,\
					 session, redirect, url_for
from secret_key import secret_key
from functools import wraps
#from flask_sslify import SSLify

app = Flask(__name__)


user_db = {'pandit.rohan@gmail.com': {
										'name': 'Rohan',
										'password': 'helo',
										'latitude': 30,
										'longitude': 50,
										'request_list': [('Get me a burger', '$10'),
														 ('Get me grapes', '$2')]
									 },
			'ayylmao@gmail.com': {
									'name': 'John',
									'password': 'helo',
									'latitude': 31,
									'longitude':51,
									'request_list': [('Solve the Riemann Hypothesis', '$1,000,000')]
								 },

			'helo@gmail.com': {
								'name': 'Dat boi',
								'password': 'helo',
								'latitude': 32.5,
								'longitude':52.5,
								'request_list': []
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

		user_db[email] = {'name': name,
						  'password': password,
						  'request_list': []
						  }

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

	email = session['email']
	request_list = user_db[email]['request_list']


	return render_template("pages/home.html", email=email,
											  request_list=request_list)


@app.route("/requestFood", methods=['POST'])
@login_required
def request_food():

	current_user = session['email']
	print(current_user)

	x1 = float(request.form['latitude'])
	y1 = float(request.form['longitude'])

	def find_dist(user):
		x2 = user_db[user]['latitude']
		y2 = user_db[user]['longitude']

		return (x2 - x1)**2 - (y2 - y1)**2

	closest_user = min(user_db.keys() - [current_user], key=find_dist)

	print("closest user is ", closest_user)

	flash("Worry not, food is on the way!")

	redirect(url_for('home'))

	return render_template("layouts/main.html")

@app.route("/updateLocation", methods=['POST'])
@login_required
def update_location():

	email = session['email']

	user_db[email]['latitude'] = float(request.form['latitude'])
	user_db[email]['longitude'] = float(request.form['longitude'])

	print("updated location for {email}".format(**locals()))
	print("new location is ", user_db[email]['latitude'], user_db[email]['longitude'])

	redirect(url_for('home'))

	return render_template("layouts/main.html")

@app.route('/openRequests')
@login_required
def open_requests():

	open_requests_list = []

	for user, data in user_db.items():
		for request in data['request_list']:
			open_requests_list.append((request[0], request[1], user))

	return render_template("pages/openRequests.html",
						    open_requests_list=open_requests_list)

"""
@app.route('/fulfillRequest')
@login_required
def fullfill_request():
	return render_template("layout/main")
"""

if __name__ == "__main__":
	app.run(debug=True)
