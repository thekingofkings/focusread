from flask import Flask, render_template, request
from flask_login import LoginManager
from user import User


fr = Flask(__name__)
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
        return login("User {} registered successfully".format(user))
    else:
        return login("User {} exists. Try a new one".format(user))
        
        
    

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
