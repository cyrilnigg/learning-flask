from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class SignupForm(Form):
	first_name = StringField('First Name', validators=[DataRequired("Please enter first name")])
	last_name = StringField('Last Name', validators=[DataRequired()])
	email = StringField('Email address', 
		validators=[DataRequired("Please enter valid email address"), 
		Email("Please enter valid email")])
	password = PasswordField('Password', 
		validators=[DataRequired(),
		Length(min=6, message="Password must be at least 6 characters")])
	submit = SubmitField('Sign Up')