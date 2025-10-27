from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Email


class ContactForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email Address", validators=[DataRequired(), Email()])
    phone = StringField("Phone")
    comments = TextAreaField("Comments", validators=[DataRequired()])
