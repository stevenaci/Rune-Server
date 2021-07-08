import os
from utilities import f_storage as fs
from flask import (Flask, request, session, redirect, url_for, abort, render_template, flash)
from werkzeug.utils import secure_filename

app = Flask(__name__)  # create app instance
app.config.from_object(__name__)  # load config from this file (flaskr.py)

# load default config and override config from an environment variable
app.config.update(
   # DATABASE=os.path.join(app.root_path, 'flaskr.db'),
    SECRET_KEY=b'_5#y2L"F4Q8z\n\xec]/',
    USERNAME='ino',
    PASSWORD='fin'
)

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'gif'])

CURRENT_DIR = os.getcwd() 
UPLOAD_DIR = '/static/uploads'

app.config['UPLOAD_DIR'] = CURRENT_DIR + UPLOAD_DIR

#
# GLOBALS 
#
uploadedfile = None
uploadtype = None

# validate file
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

"""ERROR HANDLER"""

@app.errorhandler(403)
def page_not_found(e):
    # note that we set the 403 status explicitly
    return render_template('403.html'), 403

"""VIEW FUNCTIONS"""

@app.route('/', methods=['GET', 'POST'])
def main_menu():

    # go to the functions for these pages
    if request.method == 'POST':

        if request.form['uo'] == "upload_menu":
            return redirect(url_for('upload_menu'))

            # return render_template('upload.html', type="image")

        if request.form['uo'] == "view_uploads":
            return redirect(url_for("upload_viewer"))
    #
    return render_template('main_menu.html', user=app.config['USERNAME'])


@app.route('/upload', methods=['GET', 'POST'])
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
                fs.validate_folder(app.config['UPLOAD_DIR'])

                file.save(os.path.join(app.config['UPLOAD_DIR'] + filename))

                uploadedfile = filename
                # thank you screen
                return redirect(url_for('uploaded_file'))
            else:
                print(session['utype'])
                error = "invalid file type"
                # upload_menu()

    return render_template('upload.html', error=error)


@app.route('/upload_menu', methods=['GET', 'POST'])
def upload_menu():
    if request.method == 'POST':

        session['utype'] = request.form['utype']

        return redirect(url_for('upload'))

    return render_template('uploadmenu.html')


# thank you screen
@app.route('/uploaded')
def uploaded_file():
    global uploadedfile
    print("Uploaded file: ", uploadedfile)
    imgURL= UPLOAD_DIR + uploadedfile
    return render_template('uploaded.html', image=imgURL)


@app.route('/upload_viewer', methods=['GET', 'POST'])
def upload_viewer():
    if request.method == 'GET':
        files = fs.gather_images(UPLOAD_DIR)
        return render_template('upload_viewer.html', user=app.config['USERNAME'], files=files)


###################################### # unused # #################################################################


@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    db = get_db()

    chars = ['<', '>', '%', '$', '&', '#']

    if any((c in chars) for c in request.form['title']):
        abort(403)
    if any((c in chars) for c in request.form['text']):
        abort(403)

    db.execute('insert into entries (title, text) values (?,?)',
               [request.form['title'], request.form['text']])
    db.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))
    # return redirect("http://www.infowars.com")

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('main_menu'))
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('upload_viewer'))
