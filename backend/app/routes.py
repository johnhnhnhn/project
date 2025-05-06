from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from .models import User, db, Article
from .services.scraper import scrape_bbc
from .services.sentiment import analyze_sentiment
from .trend_analysis import analyze_trends

# Blueprints
auth = Blueprint('auth', __name__)
main = Blueprint('main', __name__)
admin = Blueprint('admin', __name__)

# Login Manager setup
login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('main.dashboard'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html')

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.dashboard'))

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        role = request.form.get('role')
        new_user = User(username=username, email=email, role=role)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        flash(f'Account created for {username}!', 'success')
        return redirect(url_for('auth.login'))
    return render_template('signup.html')

@main.route('/dashboard')
@login_required
def dashboard():
    articles = scrape_bbc()
    sentiments = [analyze_sentiment(article['title']) for article in articles]
    trends = analyze_trends(articles)
    return render_template('dashboard.html', articles=articles, sentiments=sentiments, trends=trends)

@main.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    articles = Article.query.filter(Article.title.contains(query)).all()
    return render_template('search_results.html', articles=articles)

@admin.route('/admin')
@login_required
def admin_panel():
    if current_user.role != 'Admin':
        return redirect(url_for('main.dashboard'))
    users = User.query.all()
    return render_template('admin_panel.html', users=users)
