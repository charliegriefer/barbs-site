from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, TextAreaField
from wtforms.validators import DataRequired, Email


class VolunteerForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email Address", validators=[DataRequired(), Email()])
    phone = StringField("Phone")
    availability = SelectField(
        "Availability",
        choices=[
            ("", "Select your availability"),
            ("One-time Visit", "One-time Visit"),
            ("Weekly", "Weekly"),
            ("Monthly", "Monthly"),
            ("Flexible", "Flexible"),
        ],
    )
    comments = TextAreaField("About", validators=[DataRequired()])
