import os
import uuid
import json

from flask import Flask, render_template, redirect, request, flash, session
from flask_bootstrap import Bootstrap

from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg','zip'}
def allowed_file(filenames):
    t = []
    for filename in filenames:
        t.append('.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS)

    return all(t)

bootstrap = Bootstrap()

def create_app():


    app = Flask(__name__)
    
    app.config['BOOTSTRAP_SERVE_LOCAL'] = True
    app.config['SECRET_KEY'] = 'this is a secreate'
    
    bootstrap.init_app(app)



    app.template_folder = 'templates'
    app.config['UPLOAD_FOLDER'] = '/uploads'



    app.config.from_file('config.json', load=json.load)


    @app.route('/')
    def index():
        session['username'] = uuid.uuid1()

        return render_template('index.html'), 200
    

    @app.route('/upload', methods=['POST'])
    def upload():
        if 'files' not in request.files :
            flash('No file part')
            return redirect('/')
        
        
        files = request.files.getlist('files')
        print(files)

        if files== []:
            flash('No file selected')
            return redirect('/')
        
        # if files and allowed_file(files.filename):
        

       
        return render_template('upload.html')
    
    @app.route('/upload/' , methods=['GET'])
    def upload_get():

        return 'Files uploaded sucessfully'

    return app