from flask import Blueprint, render_template

servizi_bp = Blueprint('servizi', __name__)

@servizi_bp.route('/')
def servizi():
    return render_template('servizi.html')