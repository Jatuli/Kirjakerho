from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length

class RegistrationForm(FlaskForm):
    username = StringField('Tunnus', validators=[DataRequired(), Length(max=30)]) 
    password1 = PasswordField('Salasana', validators=[DataRequired(), Length(max=30)])  
    password2 = PasswordField('Salasana uudestaan', validators=[DataRequired(), Length(max=30)]) 
    submit = SubmitField('Luo tunnus')

class LoginForm(FlaskForm):
    username = StringField('Tunnus', validators=[DataRequired()])  
    password = PasswordField('Salasana', validators=[DataRequired()])  
    submit = SubmitField('Kirjaudu')

class NewBookForm(FlaskForm):
    book_name = StringField('Kirjan nimi', validators=[DataRequired()])  
    author = StringField('Kirjailija', validators=[DataRequired()])  
    description = TextAreaField('Kuvaus', validators=[DataRequired()])  
    book_classification = SelectField('Genre', choices=[
        ('', '(valitse)'),
        ('scifi', 'scifi'),
        ('fantasia', 'fantasia'),
        ('klassikko', 'klassikko'),
        ('lasten', 'lasten'),
        ('nykyromaani', 'nykyromaani'),
        ('sarjakuva', 'sarjakuva'),
        ('muu', 'muu')  
    ], validators=[DataRequired()])
    submit = SubmitField('Luo kirja')

class EditBookForm(FlaskForm):
    book_name = StringField('Kirjan nimi', validators=[DataRequired()]) 
    author = StringField('Kirjailija', validators=[DataRequired()])  
    description = TextAreaField('Kuvaus', validators=[DataRequired()])  
    book_classification = SelectField('Genre', choices=[
        ('', '(valitse)'),
        ('scifi', 'scifi'),
        ('fantasia', 'fantasia'),
        ('klassikko', 'klassikko'),
        ('lasten', 'lasten'),
        ('nykyromaani', 'nykyromaani'),
        ('sarjakuva', 'sarjakuva'),
        ('muu', 'muu')  
    ], validators=[DataRequired()])
    submit = SubmitField('Tallenna muutokset')

class ReviewForm(FlaskForm):
    review = TextAreaField('Arvostelu', validators=[DataRequired()])  # Pakollinen kenttä
    submit = SubmitField('Lisää arvio')

class EmptyForm(FlaskForm):
    pass