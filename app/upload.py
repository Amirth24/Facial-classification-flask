from flask import current_app


@current_app.route('/upload', methods=['POST'])
def upload_response():
    return 'File uploaded sucessfully'