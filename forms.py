from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField, PasswordField
from wtforms.validators import DataRequired, Length, Email, ValidationError
from models import User


class RegisterForm(FlaskForm):
    email = StringField(
        'Email', validators=[DataRequired(), Email(), Length(min=6, max=40)]
    )
    password = PasswordField('Password')
    password_length = RadioField('Password length', choices=[(
        '8', '8'), ('16', '16')], validators=[DataRequired()])
    generate_password = SubmitField('Generate password')
    submit = SubmitField('Register')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError(
                "A user with this email already exists , Please choose a different one")
