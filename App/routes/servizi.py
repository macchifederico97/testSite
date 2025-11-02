from flask import Blueprint, render_template

servizi_bp = Blueprint('home', __name__)

@servizi_bp.route('/')
def home():
    return render_template('servizi.html')