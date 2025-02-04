from flask import Blueprint, render_template

bp = Blueprint('alterar_cadastro', __name__)

@bp.route('/alterar_cadastro')
def index():
    return render_template('index.html')