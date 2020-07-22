from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SubmitField

class AddForm(FlaskForm):

    name=StringField('Enter State name')
    submit=SubmitField('Submit')

class DelForm(FlaskForm):

    id = IntegerField('Enter id for deletion')
    submit=SubmitField('Submit')
