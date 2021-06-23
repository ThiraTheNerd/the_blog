from flask import render_template,request,redirect,url_for
from ..requests import get_quotes
from . import main
from flask_login import login_required, current_user
from .forms import BlogForm
from ..models import Blog
from .. import db

#Views
@main.route('/')
def index():
  page = request.args.get('page', 1, type=int)
  quotes = get_quotes()
  blogs = Blog.query.order_by(Blog.date.desc()).paginate(page=page, per_page=10)
  title = "The Blog hompage"
  return render_template('index.html', quotes = quotes, title = title, blogs=blogs)

@main.route('/blog/new', methods =['GET','POST'])
@login_required
def new_blog():
  form = BlogForm()
  if form.validate_on_submit():
      title = form.title.data
      subtitle = form.subtitle.data
      content = form.content.data

      new_post = Blog(title=title, subtitle=subtitle, content=content, user=current_user)
      db.session.add(new_post)
      db.session.commit()
      return redirect(url_for('main.index'))
  return render_template('blogs/new_blog.html', form=form)

@main.route('/blogs/new/<int:blog_id>', methods = ['GET','POST'])
def blog(blog_id):
    '''
    View root page function that returns the posts page and its data
    '''
    blog = Blog.query.filter_by(id=blog_id).one()
    # post_comments = Comment.get_comments(post_id)
    title = f'blog_id' 
    return render_template('post.html', title = title, blog=blog )



