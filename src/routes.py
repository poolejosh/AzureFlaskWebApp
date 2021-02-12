from flask import Blueprint, render_template, redirect, url_for, session, request, flash
from models import User
from datastore import db_session, login_manager
from flask_login import current_user, login_user, logout_user, login_required
from common import logger

main_bp = Blueprint('main_bp', __name__)

@main_bp.route("/")
def home():
    return render_template("index.html", current_user=current_user)

@main_bp.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("main_bp.user_details"))
    
    if request.method == "POST":
        existing_user = User.query(db_session, 'query', username=request.form["username"]).first()
        if existing_user is None:
            user = User(
                username=request.form["username"],
                f_name=request.form["f_name"],
                l_name=request.form["l_name"],
                email=request.form["email"]
            )
            user.set_password(request.form["password"])
            db_session.add(user)
            db_session.commit()
            login_user(user)
            return redirect(url_for("main_bp.user_details"))
        logger.error("A user already exists with that username")
        flash("A user already exists with that username")
    else:
        return render_template("register.html")


@main_bp.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("main_bp.user_details"))

    if request.method == "POST":
        user = User.query(db_session, 'query', username=request.form['username']).first()
        if user and user.check_password(password=request.form['password']):
            login_user(user)
            return redirect(url_for("main_bp.user_details"))
        logger.error("Invalid username/password combination")
        flash("Invalid username/password combination")
        return redirect(url_for("main_bp.login"))
    else:
        return render_template("login.html")

@main_bp.route("/user_details")
@login_required
def user_details():
    return render_template("user_details.html", current_user=current_user)

@main_bp.route("/logout")
def logout():
  logout_user()
  return redirect(url_for("main_bp.home"))

@login_manager.user_loader
def load_user(user_id):
    if user_id is not None:
        return User.query(db_session, "query", user_id=user_id).first()
    return None

@login_manager.unauthorized_handler
def unauthorized():
    logger.error("You must be logged in to view that page.")
    flash("You must be logged in to view that page.")
    return redirect(url_for("main_bp.login"))