from flask import (Flask, request, session, redirect, url_for, abort, render_template, flash)

from blueprints.fileserver import fs_page

app = Flask(__name__)  # create app instance
app.config.from_object(__name__)  # load config from this file ()

# load default config and override config from an environment variable
app.config.update(
   # DATABASE=os.path.join(app.root_path, 'common.db'),
    SECRET_KEY=b'_5#y2L"F4Q8z\n\xec]/',
    USERNAME='ino',
    PASSWORD='fin'
)

app.register_blueprint(fs_page)
