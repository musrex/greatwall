from wtforms import StringField, IntegerField, BooleanField, RadioField, SubmitField
from wtforms.validators import Email, Length, DataRequired
from flask_wtf import FlaskForm

class createMenu(FlaskForm):
    category  = StringField('category', validators = [DataRequired(), Length(1,50)])
    code = StringField('code', validators = [DataRequired(), Length(1,10)])
    dish = StringField('dish', validators = [DataRequired(), Length(1,50)])
    price = IntegerField('price', validators = [DataRequired(), Length(1,5)])
    submit1 = SubmitField('save')

class deleteItems(FlaskForm):
    item = StringField("{{ item['id'] }}", validators = [DataRequired()])
    radio_field = RadioField('Choices')

# DataRequired is not a valid validator because it is a class, it should be an instance