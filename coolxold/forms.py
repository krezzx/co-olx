from email.headerregistry import Address
from flask_wtf import Form
from wtforms import PasswordField,IntegerField,SubmitField,StringField,BooleanField,TextAreaField,SelectField
from wtforms.validators import DataRequired,Length,EqualTo,NumberRange


class RegistrationForm(Form):
    RollNo=IntegerField("Mobile Number",validators=[DataRequired(),NumberRange(min=6000000000,max=9999999999)])
    userName=StringField("Full Name",validators=[DataRequired(),Length(min=2,max=20)])
    emailId=StringField("Webmail")
    address=StringField("Hostel Address",validators=[DataRequired()])
    course=SelectField("Course",choices=[('B.Tech','B.Tech'),('B.Arch','B.Arch'),('MCA','MCA'),('MBA','MBA'),('MA','MA'),('M.Arch','M.Arch'),('M.Sc','M.Sc'),('M.Tech','M.Tech'),('PhD','PhD')],validators=[DataRequired()])
    password=PasswordField("Password",validators=[DataRequired(),Length(min=8)])
    confirm_password=PasswordField("Confirm_Password",validators=[DataRequired(),EqualTo('password')])
    submit=SubmitField('Sign Up')

class LoginForm(Form):
    emailId=StringField("Email",validators=[DataRequired()])
    password=PasswordField("Password",validators=[DataRequired()])
    remember=BooleanField("remember me")
    submit=SubmitField('Login')