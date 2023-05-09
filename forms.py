from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, AnyOf, NumberRange

city_list = ['Delft', 'Amsterdam']

class FilterForm(FlaskForm):
    city = StringField('City', validators=[DataRequired(), AnyOf(city_list)])
    rooms = StringField('No. of rooms', validators=[NumberRange(min=1)])
    min_price = StringField('Minimum price', validators=[NumberRange(min=0)])
    max_price = StringField('Maximum price', validators=[NumberRange(min=1)])
    interiorType = SelectField('Interior/Furniture', choices=['Furnished', 'Unfurnished'])
    size = StringField('Minimum size', validators=[DataRequired()])
    submit = SubmitField('Search for apartments')
