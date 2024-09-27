from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired, ValidationError
from app.models import Product




class CreateProductForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    price = StringField('price', validators=[DataRequired()])
    description = StringField('description', validators=[DataRequired()])
    category = SelectField(
        'Category',
        choices=[('mens', 'MENS'), ('womens', 'WOMENS'), ('melee', 'MELEE'), ('long-range', 'LONG-RANGE'), ('accessories', 'ACCESSORIES')],
        validators=[DataRequired()]
    )
