""" Form object declaration."""
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField,TextAreaField
from wtforms.validators import DataRequired,Length,Regexp
from dns.rdataclass import NONE


class RegistrationForm(FlaskForm):
    """Display registration form""" 
    username=StringField(label='Username',validators=[DataRequired(),Length(min=6,max=12)]) 
    regex ="^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[*.!@$%^&(){}[]:;<>,.?/~_+-=|\]).{6,16}"
    m = 'Password should contains Upper & lowercase letters,\
                    numbers,\
                \n\t length[6 -16]'
    #password = PasswordField(label='Password',validators=[DataRequired(),Length(min=6,max=16),Regexp(regex,flags=0,message=m)])
    password = PasswordField(label='Password',validators=[DataRequired(),Length(min=6,max=16)])
    
    submit = SubmitField(label = 'Register')
    
 

class LoginForm(FlaskForm): 
    """Display login form"""          
    username = StringField(label='Username', validators=[DataRequired(),Length(min=3,max=20)])
    regex ="^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[*.!@$%^&(){}[]:;<>,.?/~_+-=|\]).{6,16}"
    m = 'Password should contains Upper & lowercase letters,\
                    numbers,\
                \n\t length[6 -16]")'
    
    password = PasswordField(label='Password',
                           validators=[DataRequired(),Length(min=6,max=16)])
    
    submit = SubmitField(label = 'Login')
    
class updatePasswordForm(FlaskForm): 
    """Display login form"""          
    newpassword = PasswordField(label='Newpassword',
                           validators=[DataRequired(),Length(min=6,max=16)])
    
    
    submit = SubmitField(label = 'Submit')