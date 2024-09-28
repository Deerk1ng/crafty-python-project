from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Email, ValidationError
from app.models import User


def user_exists(form, field):
    # Checking if user exists
    email = field.data
    user = User.query.filter(User.email == email).first()
    if user:
        raise ValidationError('Email address is already in use.')


def username_exists(form, field):
    # Checking if username is already in use
    username = field.data
    user = User.query.filter(User.username == username).first()
    if user:
        raise ValidationError('Username is already in use.')

def shopname_exists(form, field):
    # checking if shopname is already in use
    shop_name = field.data

    user_shop = User.query.filter(User.shop_name == shop_name).first()

    if user_shop:
        raise ValidationError("Shop name is already in use")


class SignUpForm(FlaskForm):
    first_name = StringField('first_name', validators=[DataRequired()])
    last_name = StringField('last_name', validators=[DataRequired()])
    shop_name = StringField('shop_name', validators=[DataRequired(), shopname_exists])
    address = StringField('address', validators=[DataRequired()])
    username = StringField('username', validators=[DataRequired(), username_exists])
    email = StringField('email',  validators=[DataRequired(), user_exists])
    password = StringField('password', validators=[DataRequired()])
