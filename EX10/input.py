
from flask_wtf import FlaskForm
from wtforms import (StringField,IntegerField,FloatField)
from wtforms.validators import InputRequired, ValidationError, URL


def positive_check(form, field):
    if field.data < 0:
        raise ValidationError('Field must be positive')


def number_between_0_and_1(form, field):
    if field.data < 0.0 or field.data > 1.0:
        raise ValidationError('Field must be a number between [0,1]')


class RandomGraphForm(FlaskForm):
    nodes = IntegerField('nodes', validators=[InputRequired(), positive_check])
    p = FloatField('p', validators=[InputRequired(), number_between_0_and_1])


class GoogleSheetsForm(FlaskForm):
    url = StringField('url', validators=[InputRequired(), URL()])

