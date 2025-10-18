from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, SelectField

class RegistrationForm(FlaskForm):
    username = StringField('Tunnus')
    password1 = PasswordField('Salasana')
    password2 = PasswordField('Salasana uudestaan')
    submit = SubmitField('Luo tunnus')

class LoginForm(FlaskForm):
    username = StringField('Tunnus')
    password = PasswordField('Salasana')
    submit = SubmitField('Kirjaudu')

class NewBookForm(FlaskForm):
    book_name = StringField('Kirjan nimi')
    author = StringField('Kirjailija')
    description = TextAreaField('Kuvaus')
    book_classification = SelectField('Genre', choices=[
        ('', '(valitse)'),
        ('scifi', 'scifi'),
        ('fantasia', 'fantasia'),
        ('klassikko', 'klassikko'),
        ('lasten', 'lasten'),
        ('nykyromaani', 'nykyromaani'),
        ('sarjakuva', 'sarjakuva')
    ])
    submit = SubmitField('Luo kirja')

class EditBookForm(FlaskForm):
    book_name = StringField('Kirjan nimi')
    author = StringField('Kirjailija')
    description = TextAreaField('Kuvaus')
    book_classification = SelectField('Genre', choices=[
        ('', '(valitse)'),
        ('scifi', 'scifi'),
        ('fantasia', 'fantasia'),
        ('klassikko', 'klassikko'),
        ('lasten', 'lasten'),
        ('nykyromaani', 'nykyromaani'),
        ('sarjakuva', 'sarjakuva')
    ])
    submit = SubmitField('Tallenna muutokset')

class EmptyForm(FlaskForm):
    pass