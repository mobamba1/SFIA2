from flask_wtf import FlaskForm 
from wtforms import StringField, SubmitField, IntegerField 
from wtforms.validators import DataRequired, Length  


class AddForm(FlaskForm): 
    coordinates = StringField('coordinates',
        validators = [
            DataRequired(),
            Length(min=1, max=30)


        ]
    )
     
    submit = SubmitField('Post!')
