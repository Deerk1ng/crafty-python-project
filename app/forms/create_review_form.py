from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, ValidationError
from app.models import Product


class CreateReviewForm(FlaskForm):
    item_rating = IntegerField('name', validators=[DataRequired()])
    shipping_rating = IntegerField('price', validators=[DataRequired()])
    description = StringField('description', validators=[DataRequired()])
