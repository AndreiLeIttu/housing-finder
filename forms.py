from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, AnyOf, NumberRange

city_list = ['Delft', 'Amsterdam']

class FilterForm(FlaskForm):
    city = StringField('City', validators=[DataRequired(), AnyOf(city_list)])
    bedrooms = StringField('No. of rooms', validators=[NumberRange(min=1)])

