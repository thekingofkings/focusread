from flask import Flask, render_template, request, url_for, flash, redirect
from flask_login import LoginManager, login_user
from user import User
from google.appengine.ext import ndb


fr = Flask(__name__)
fr.secret_key = "super secret key"

login_manager = LoginManager()
login_manager.init_app(fr)


@fr.route("/login")
def login(message=""):
    return render_template("login.html", title="Login Page", message=message)


@fr.route("/register", methods=["POST"])
def user_register():
    user = request.form.get("name")
    password = request.form.get("password")
    q = User.query(User.name == user).get()
    if q == None:
        u = User(name=user, pwd=password)
        u.put()
        msg = "User {} registered successfully".format(user)
        return login(msg)
    else:
        msg = "User {} exists. Try a new one".format(user)
        return login(msg)


@fr.route("/authenticate", methods=['POST'])    
def check_auth():
    """
    Authenticate the login credential.
    
    If valid, login user and get Oauth tokens for Moves, Rescuetime.
    Otherwise, redirect to login page and ask user to retry.
    """
    user = request.form.get("name")
    password = request.form.get("password")
    u = User.query(ndb.AND(User.name==user, User.pwd==password)).get()
    if u != None:
        login_user(u)
        flash("Logged in successfully.")
        return redirect(url_for("home"))
    else:
        return login("Wrong username or password. Please try again.")



@fr.route('/')
def home():
    """
    The index page
    """
    return "<h1>Welcome to the FocusRead project!</h1>"



@fr.errorhandler(404)
def page_not_fount(error):
    return "<h1>Page not fount!</h1>"




if __name__ == '__main__':
    fr.run(debug=True)
