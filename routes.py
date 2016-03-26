from flask import render_template, Flask, request
from models import db, User
from forms import SignupForm

app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {'DB': "learning-flask"}
db.init_app(app)

app.secret_key = "tom-petty"

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/about")
def about():
	return render_template("about.html")

@app.route("/signup", methods = ['GET', 'POST'])
def signup():
	form = SignupForm()

	if request.method == 'POST':
		if form.validate() == False:
			return render_template("signup.html", form=form)
		else:
			newuser = User(form.first_name.data, form.last_name.data, 
				form.email.data, form.password.data )
			newuser.save()
			return "Success!"
	elif request.method == 'GET':
		return render_template("signup.html", form=form)

if __name__ == "__main__":
	app.run(debug=True)