#!/usr/bin/python3
""" This script sets up a flask web application """
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def close(self):
    """This closes the current SQLAlchemy session"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """This displays an HTML page with a list of all States"""
    states = storage.all('State')
    sort_states = sorted(states.values(), key=lambda st: st.name)
    return render_template('7-states_list.html', states=sort_states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
