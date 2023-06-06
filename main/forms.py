from wtforms.validators import email
from flask_wtf import FlaskForm
from wtforms.validators import (StringField, IntegerField, BooleanField,
                                RadioField, Length, DataRequired, SubmitField)

class createMenu(FlaskForm):
    category  = StringField('category', validators = [DataRequired(), Length(1,50)])
    code = StringField('code', validators = [DataRequired(), Length(1,10)])
    dish = StringField('dish', validators = [DataRequired(), Length(1,50)])
    price = IntegerField('price', validators = [DataRequired, Length(1,5)])
    submit1 = SubmitField('save')

class deleteItems(FlaskForm):
    item = StringField("{{ item['id'] }}", validators = [DataRequired(), RadioField()])