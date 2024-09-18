from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired, ValidationError
from app.models import Product


class CreateReviewForm(FlaskForm):
    item_rating = StringField('name', validators=[DataRequired()])
    shipping_rating = StringField('price', validators=[DataRequired()])
    description = StringField('description', validators=[DataRequired()])
