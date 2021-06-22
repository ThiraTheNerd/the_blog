from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,ValidationError,BooleanField
from wtforms.validators import Required,Email,EqualTo
from ..models import Blog

class BlogForm(FlaskForm):
  title = StringField('Enter title',validators = [Required()])
  subtitle= StringField('Enter subtitle',validators = [Required()])
  content = TextAreaField('make a blog', validators=[Required()])
  submit = SubmitField('Post Blog')

