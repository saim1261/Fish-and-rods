from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class AddRod(FlaskForm):
    description = StringField('Rod Description', validators=[DataRequired()])
    submit = SubmitField('Add a Rod')

class AddFish(FlaskForm):
    description = StringField('Fish Description', validators=[DataRequired()])
    submit = SubmitField('Add a Fish')