from flask import Flask, render_template, request, flash,\
					 session, redirect, url_for
from secret_key import secret_key 
from functools import wraps

app = Flask(__name__)

user_db = {}
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
	return render_template("pages/index.html")


@app.route("/sendData", methods=['POST'])
def send_data():

	print(request.form['latitude'])
	redirect(url_for('index'))

	return render_template("layouts/main.html")


if __name__ == "__main__":
	app.run(debug=True)