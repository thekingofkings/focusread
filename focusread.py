from flask import Flask, render_template, request, url_for, flash, redirect
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
from user import User
from google.appengine.ext import ndb
from flask_socketio import SocketIO, send


fr = Flask(__name__)
fr.secret_key = "super secret key"
socketio = SocketIO(fr)

login_manager = LoginManager()
login_manager.init_app(fr)
login_manager.login_view = 'login'


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
@login_required
def home():
    """
    The index page
    """
    return render_template("home.html")


@fr.route("/logout")
@login_required
def logout():
    logout_user()
    return login("Logged out successfully.")


@fr.errorhandler(404)
def page_not_fount(error):
    return "<h1>Page not fount!</h1>"


@login_manager.user_loader
def load_user(user_id):
    return User.query(User.name==user_id).get()


"""
=========================
   SocketIO function
=========================
"""
@socketio.on('connect')
def handle_connect():
    msg = 'User {} connected'.format(current_user.name)
    send(msg, broadcast=True)
    
    
@socketio.on('message')
def handle_message(message):
    msg = "{0}: {1}".format(current_user.name, message)
    send(msg, broadcast=True)


if __name__ == '__main__':
#    fr.run(debug=True)
    socketio.run(fr)
