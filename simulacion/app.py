#!/usr/bin/env python
# -*- coding: utf-8 -*-

# =============================================================================
# IMPORTS
# =============================================================================

from flask import Flask, render_template, request
from flask.ext.script import Manager, Server
from flask_bootstrap import Bootstrap

from . import sim

# =============================================================================
# CONF
# =============================================================================

app = Flask(__name__)
cli_manager = Manager(app)
cli_manager.add_command("runserver", Server(use_reloader=True))

Bootstrap(app)

dmedia_respuesta = 10
ddesv_respuesta = 5
dmedia_consulta = 200
dnumero_corridas = 100


# =============================================================================
# ROUTES
# =============================================================================

@app.route("/")
def index():
    return render_template(
        'index.html', media_respuesta=dmedia_respuesta,
        desv_respuesta=ddesv_respuesta, media_consulta=dmedia_consulta,
        numero_corridas=dnumero_corridas)


@app.route("/run_simulation",methods=["POST"])
def run_simulation():
    media_respuesta = float(request.form["media_respuesta"])
    desv_respuesta = float(request.form["desv_respuesta"])
    media_consulta = float(request.form["media_consulta"])
    numero_corridas = int(request.form["numero_corridas"])

    resultados = sim.simulate(numero_corridas, media_respuesta, desv_respuesta, media_consulta)

    return render_template('index.html', resultados=resultados, media_respuesta=media_respuesta,
        desv_respuesta=desv_respuesta, media_consulta=media_consulta,
        numero_corridas=numero_corridas)





