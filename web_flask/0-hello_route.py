#!/usrbin/python3
""" This script starts a Flask web application.
    The app is listening on 0.0.0.0, port 5000

"""

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ This function displays the text Hello HBNB! """
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
