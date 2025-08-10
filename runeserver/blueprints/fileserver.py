from flask import Blueprint, request, session, redirect, url_for, render_template, flash
from werkzeug.utils import secure_filename
from os import getcwd, path
from runeserver.utilities.extensions import allowed_file, file_extensions
from utilities import file_storage as fs
import Log as log

fs_page = Blueprint('fs_page', __name__, template_folder='templates')

CURRENT_DIR = getcwd()
UPLOAD_PATH = path.join(CURRENT_DIR,"runeserver/static/uploads")

log.DEBUG("UPLOAD DIR {}".format(UPLOAD_PATH))

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
            if fs.is_valid_file(filename, session['utype']):
                fs.touch_folder( UPLOAD_PATH)
                file.save(path.join( UPLOAD_PATH  + filename))
                # thank you screen
                return redirect(url_for('fs_page.uploaded_file', uploaded_file = filename))
            else:
                print(session['utype'])
                error = "invalid file type"

    return render_template('upload.html', error=error)

@fs_page.route('/upload_menu', methods=['GET', 'POST'])
def upload_menu():
    if request.method == 'POST':
        session['utype'] = request.form['utype']
        return redirect(url_for('fs_page.upload'))

    return render_template('uploadmenu.html')

# thank you screen
@fs_page.route('/uploaded')
def uploaded_file(uploaded_file: str):
    print("Uploaded file: ", uploaded_file)
    fpath = fs.get_upload_path(uploaded_file)
    return render_template('uploaded.html')


@fs_page.route('/upload_viewer', methods=['GET', 'POST'])
def upload_viewer():
    if request.method == 'GET':
        files = fs.find_image_files( UPLOAD_PATH)
        files.extend(fs.find_video_files(UPLOAD_PATH))
        return render_template('upload_viewer.html', user="Guest", files=files)


@fs_page.route('/display/<filename>')
def display_video(filename):
	print('display_video filename: ' + filename)
	return redirect(url_for('static', filename='uploads/' + filename), code=301)


@fs_page.route('/video_viewer', methods=['POST'])
def video_viewer():
    return render_template(
        'video_viewer.html',
        filename=request.form['vid_fn'],
        enctype=file_extensions.video_html_encodings.get(fs.get_ext(request.form['vid_fn']))
    )
