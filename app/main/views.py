from flask import render_template,request,redirect,url_for
from ..requests import get_quotes
from . import main



#Views
@main.route('/')
def index():
  
  quotes = get_quotes()
  title = "The Blog hompage"
  return render_template('index.html', quotes = quotes, title = title)


