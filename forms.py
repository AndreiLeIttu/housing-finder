from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, IntegerField
from wtforms.validators import DataRequired, AnyOf, NumberRange

city_list = ['Delft', 'Amsterdam', 'Rotterdam', 'Den Haag', 'Haarlem', 'Eindhoven', 'Groningen', 'Maastricht',
             'Leiden', 'Utrecht', 'Breda', 'Amstelveen', 'Arnhem', 'Almere', 'Den Bosch']

class FilterForm(FlaskForm):
    city = StringField('City', validators=[AnyOf(city_list)])
    rooms = IntegerField('No. of rooms', validators=[NumberRange(min=1)])
    min_price = IntegerField('Minimum price', validators=[NumberRange(min=0)])
    max_price = IntegerField('Maximum price', validators=[NumberRange(min=1)])
    interiorType = SelectField('Interior/Furniture', choices=['Furnished', 'Unfurnished'])
    size = IntegerField('Minimum size', validators=[NumberRange(min=0)])
    submit = SubmitField('Search for apartments')
