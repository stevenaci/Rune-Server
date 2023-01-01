from flask import Blueprint, render_template

error_page = Blueprint('error_page', __name__,
                        template_folder='templates')

"""ERROR HANDLER"""
@error_page.errorhandler(403)
def page_not_found(e):
    # note that we set the 403 status explicitly
    return render_template('403.html'), 403
