import os
import uuid

from flask import Flask, render_template, redirect, request, flash, session, url_for
from flask_bootstrap import Bootstrap


from app.utils import handle_file

bootstrap = Bootstrap()

UPLOAD_FOLDER = os.path.abspath('upload')


def create_app():


    app = Flask(__name__)
    
    app.config['BOOTSTRAP_SERVE_LOCAL'] = True
    app.config['SECRET_KEY'] = 'this is a secreate'
    app.config['SESSION_PERMANENT'] = False
    
    bootstrap.init_app(app)



    app.template_folder = 'templates'
    app.config['UPLOAD_FOLDER'] = os.path.abspath('upload')

    if not os.path.exists(app.config['UPLOAD_FOLDER'])  :
        app.logger.info('Upload Folder Created')
        os.mkdir(os.path.abspath('upload'))

    # app.config.from_file('config.json', load=json.load)
    
    from . import dashboard
    app.register_blueprint(dashboard.dasb_board_bp,url_prefix='/dashboard')


    @app.route('/')
    def index():
        userid = session.get('userid')
        if not userid:
            userid = uuid.uuid1()
            app.logger.info('Creating user', userid)
            session['userid'] = userid


        
        if not os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'], str(userid))):
            
            
            os.mkdir(os.path.join(app.config['UPLOAD_FOLDER'], str(userid)))
            os.mkdir(os.path.join(app.config['UPLOAD_FOLDER'], str(userid)+'/imgs'))    
            app.logger.info('Folder for '+str(userid)+' created.')





        return render_template('index.html'), 200
    
    
    from app.core import Classifier
    

    @app.route('/upload', methods=['GET','POST'])
    def upload():

        if request.method == 'GET':
            
            if session.get('userid'):
                return redirect('/')
            
            return redirect('/')


        if 'files' not in request.files :
            flash('No file part')
            return redirect('/')
        
        
        files = request.files.getlist('files')
        
        

        if files[0].filename == '':
            flash('No file selected')
            return redirect('/')
        
        # if files and allowed_file(files.filename):
        for file_ in files:
            st  = handle_file(file_)
            if not st :
                return redirect('/')
            
        Classifier('models', os.path.join(app.config['UPLOAD_FOLDER'], str(session['userid']))).process()

       
        return redirect(url_for('dashboard.dashboard'))
    


    return app




# App exit handlers
import atexit
import shutil
def cleanup_upload_folder():
    if os.path.exists(UPLOAD_FOLDER):
        shutil.rmtree(UPLOAD_FOLDER)

# atexit.register(cleanup_upload_folder)