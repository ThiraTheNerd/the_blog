from flask import render_template,request,redirect,url_for
from ..requests import get_quotes
from . import main
from flask_login import login_required



#Views
@main.route('/')
def index():
  
  quotes = get_quotes()
  title = "The Blog hompage"
  return render_template('index.html', quotes = quotes, title = title)

@main.route('/blogs/new/<int:id>', methods = ['GET','POST'])
@login_required
def new_review(id):
  return render_template('new_blog.html')


