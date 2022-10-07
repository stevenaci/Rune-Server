from flask import Blueprint, request, session, redirect, url_for, abort, render_template, flash
from jinja2 import TemplateNotFound
from werkzeug.utils import secure_filename
from os import getcwd, path
from utilities import file_storage as fs
import Log as log

fs_page = Blueprint('fs_page', __name__,
                        template_folder='templates')

ALLOWED_UPLOAD_EXTS = set(['txt', 'pdf', 'png', 'jpg', 'gif']) 
CURRENT_DIR = getcwd()
UPLOAD_PATH = path.join(getcwd(),"static","uploads")

log.__log("UPLOAD DIR {}".format(UPLOAD_PATH), log.logging.DEBUG)
# GLOBALS 
uploadedfile = None
uploadtype = None

# validate file
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_UPLOAD_EXTS

"""ERROR HANDLER"""
@fs_page.errorhandler(403)
def page_not_found(e):
    # note that we set the 403 status explicitly
    return render_template('403.html'), 403

"""VIEW FUNCTIONS"""
@fs_page.route('/', methods=['GET', 'POST'])
def main_menu():

    # go to the functions for these pages
    if request.method == 'POST':

        if request.form['uo'] == "upload_menu":
            return redirect(url_for('fs_page.upload_menu'))

        if request.form['uo'] == "view_uploads":
            return redirect(url_for("fs_page.upload_viewer"))
    #
    return render_template('main_menu.html', user="Guest")

@fs_page.route('/upload', methods=['GET', 'POST'])
def upload():
    global uploadedfile
    error = ""
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file')
            return redirect(request.url)
        file = request.files['file']

        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filename = "/" + filename
            # get correct path for type of file
            # 
            if fs.isvalidfile(len(filename), filename, session['utype']):
                fs.validate_folder( UPLOAD_PATH)

                file.save(path.join( UPLOAD_PATH  + filename))

                uploadedfile = filename
                # thank you screen
                return redirect(url_for('fs_page.uploaded_file'))
            else:
                print(session['utype'])
                error = "invalid file type"
                # upload_menu()

    return render_template('upload.html', error=error)

@fs_page.route('/upload_menu', methods=['GET', 'POST'])
def upload_menu():
    if request.method == 'POST':

        session['utype'] = request.form['utype']

        return redirect(url_for('fs_page.upload'))

    return render_template('uploadmenu.html')

# thank you screen
@fs_page.route('/uploaded')
def uploaded_file():
    global uploadedfile
    print("Uploaded file: ", uploadedfile)
    fpath = fs.to_upload_path(uploadedfile)
    return render_template('uploaded.html', image=fpath)


@fs_page.route('/upload_viewer', methods=['GET', 'POST'])
def upload_viewer():
    if request.method == 'GET':
        files = fs.gather_images( UPLOAD_PATH)
        files.extend(fs.find_video_files(UPLOAD_PATH))
        return render_template('upload_viewer.html', user="Guest", files=files)

@fs_page.route('/display/<filename>')
def display_video(filename):
	print('display_video filename: ' + filename)
	return redirect(url_for('static', filename='uploads/' + filename), code=301)

@fs_page.route('/video_viewer', methods=['POST'])
def video_viewer():
    return render_template('video_viewer.html', filename=request.form['vid_fn'])

###################################### # log in form # #################################################################

# fs_page.route('/login', methods=['GET', 'POST'])
# def login():
#     error = None
#     if request.method == 'POST':
#         if request.form['username'] != app.config['USERNAME']:
#             error = 'Invalid username'
#         elif request.form['password'] != app.config['PASSWORD']:
#             error = 'Invalid password'
#         else:
#             session['logged_in'] = True
#             flash('You were logged in')
#             return redirect(url_for('main_menu'))
#     return render_template('login.html', error=error)


# @fs_page.route('/logout')
# def logout():
#     session.pop('logged_in', None)
#     flash('You were logged out')
#     return redirect(url_for('upload_viewer'))
