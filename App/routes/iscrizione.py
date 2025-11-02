from flask import Blueprint, render_template, request, redirect, url_for
import json
import os

iscrizione_bp = Blueprint('iscrizione', __name__)

@iscrizione_bp.route('/iscrizione', methods=['GET', 'POST'])
def iscrizione():
    if request.method == 'POST':
        nome = request.form.get('nome')
        cognome = request.form.get('cognome')

        nuovo_utente = {"nome": nome, "cognome": cognome}

        # Percorso del file JSON
        file_path = os.path.join('App', 'data', 'iscritti.json')

        # Crea la cartella se non esiste
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        # Leggi e aggiorna il file JSON
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                dati = json.load(f)
        else:
            dati = []

        dati.append(nuovo_utente)

        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(dati, f, indent=2, ensure_ascii=False)

        return redirect(url_for('iscrizione.iscrizione'))

    return render_template('iscrizione.html')