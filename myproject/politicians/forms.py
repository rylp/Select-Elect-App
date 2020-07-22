from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SubmitField

class AddForm(FlaskForm):

    state_id = IntegerField('Enter State Id')
    name=StringField('Enter Politician name')
    submit=SubmitField('Submit')
