from flask import Flask
from flask_login import LoginManager
from user import User


fr = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(fr)


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
