#!/usr/bin/python

import sys
import os
sys.path = ['../..'] + sys.path

from flask import Flask
import flask_autorouter


app = Flask(__name__)
app.config['ROOT_PATH'] = os.path.abspath(os.path.dirname(__file__))


flask_autorouter.generate_urls(app, 'www')
flask_autorouter.generate_urls(app, 'api', '/api')
print flask_autorouter.list_routes(app)



if __name__ == '__main__':
    app.run()
