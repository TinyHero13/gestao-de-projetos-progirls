from flask import Blueprint, render_template

bp = Blueprint('cadastro', __name__)

@bp.route('/cadastro')
def index():
    return render_template('cadastro.html')