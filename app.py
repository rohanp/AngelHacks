from flask import Flask, render_template, request, flash,\
					 session, redirect, url_for

app = Flask(__name__)

user_db = {}
salt = "helo"

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
def info():
	return render_template("pages/index.html") 

@app.route('/login', methods=['GET', 'POST'])
def login():

	form = LoginForm(request.form)

	if request.method == 'GET':
		return render_template('pages/login.html', form=form)

	if request.method == 'POST':
		if form.validate() == False:
			return render_template('pages/login.html', form=form)
		else:
			session['name'] = form.name.data.lower()
			flash(u'Hi {0}!')

			return redirect(url_for('home'))

@app.route('/register', methods=['GET', 'POST'])
def register():

	if request.method == 'GET':
		return render_template('forms/register.html', form=form)

	elif request.method == 'POST':
		if form.validate() == False:
			return render_template('pages/register.html', form=RegisterForm())
		else:            
			user_db[form.email.data] = form.password.data

			session['name'] = newuser.name
			flash(u'Successfully Registered')

			return redirect(url_for('home'))


@app.route("/home")
def index():
	return render_template("pages/index.html")


@app.route("/sendData", methods=['POST'])
def send_data():

	print(request.form['latitude'])
	redirect(url_for('index'))

	return render_template("layouts/main.html")


if __name__ == "__main__":
	app.run(debug=True)