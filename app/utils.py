import os
import zipfile


from werkzeug.utils import secure_filename
from flask import current_app, session, flash


ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg','zip'}
def allowed_file(filenames):
    t = []
    for filename in filenames:
        t.append('.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS)

    return all(t)


def handle_file(file_):
    filename = secure_filename(file_.filename)

    # if zip file
    if filename.rsplit('.', 1)[1].lower() == 'zip':
        zip_like_obj = zipfile.ZipFile(file_)

        print(zip_like_obj.namelist())

        if allowed_file(zip_like_obj.namelist()):
            zip_like_obj.extractall(path=os.path.join(current_app.config['UPLOAD_FOLDER'], str(session['userid'])))
            return True

        else: 
            flash('Zip contains invalid format found we accept only .png, .jpeg, .jpg formats')
            return False


    file_.save(os.path.join(current_app.config['UPLOAD_FOLDER'], str(session['userid'])+'/'+ filename ))
    return True
