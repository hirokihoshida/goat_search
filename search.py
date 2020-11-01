from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DecimalField
from wtforms.validators import DataRequired


class SearchForm(FlaskForm):
    smallSize = DecimalField('Small Size')
    largeSize = DecimalField('Large Size')
    searchQuery = StringField('Search Query')
    search = SubmitField('Search')