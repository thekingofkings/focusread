from flask import Flask


fr = Flask(__name__)


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
