from flask import Blueprint, render_template,current_app, session, redirect, flash

from app.utils import handle_file

import os


dasb_board_bp = Blueprint('dashboard',__name__)

@dasb_board_bp.route('/', methods=['GET'])
def dashboard():


    
    if not session.get('userid') or os.listdir(os.path.join(current_app.config['UPLOAD_FOLDER'],str(session['userid']))) == []:
        flash("Upload the files first")

        return redirect('/')




    
    return render_template('dashboard.html')


