from flask import Flask, render_template, request, flash,\
					 session, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
	if request.method == 'GET':
		return render_template("index.html")

	elif request.method == "POST":
		print(request.form['latitude'])
		return render_template("index.html")

@app.route("/sendData", methods=['GET', 'POST'])
def send_data():

	if request.method == "POST":
		print(request.form['latitude'])
		redirect(url_for('index'))

	return render_template("main.html")


if __name__ == "__main__":
	app.run(debug=True)