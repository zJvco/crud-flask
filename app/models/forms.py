from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import Length, Email, DataRequired


class RegisterForm(FlaskForm):
    name = StringField(label="Name", validators=[Length(min=2, max=45), DataRequired()])
    email = StringField(label="Email", validators=[Email(), DataRequired()])
    phone = IntegerField(label="Phone")
    address_cep = IntegerField(label="CEP")
    address_street = StringField(label="Street")
    address_number = IntegerField(label="Number")
    address_complement = StringField(label="Complement")
    submit = SubmitField(label="Create")