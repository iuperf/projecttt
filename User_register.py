from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DateField
from wtforms import SubmitField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import EmailField


class User_register(FlaskForm):
    name = StringField('Имя', validators=[DataRequired()])
    surname = StringField('Фамилия', validators=[DataRequired()])
    age = IntegerField('Возраст', validators=[DataRequired()])
    email = EmailField('Почта', validators=[DataRequired()])
    password = StringField('Пароль', validators=[DataRequired()])
    birth_date = StringField('Дата рождения', validators=[DataRequired()])
    submit = SubmitField('Зарегистрироватся')