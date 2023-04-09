import os
import uuid
import json

from flask import Flask, render_template
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()

def create_app():


    app = Flask(__name__)
    
    app.config['BOOTSTRAP_SERVE_LOCAL'] = True
    
    bootstrap.init_app(app)

    app.template_folder = 'templates'

    app.config.from_file('config.json', load=json.load)


    @app.route('/')
    def index():


        return render_template('index.html'), 200

    return app