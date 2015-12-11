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


# =============================================================================
# ROUTES
# =============================================================================

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/run_simulation",methods=["POST"])
def run_simulation():
	media_respuesta = float(request.form["media_respuesta"])
	desv_respuesta = float(request.form["desv_respuesta"])
	media_consulta = float(request.form["media_consulta"])
	numero_corridas = int(request.form["numero_corridas"])
	
	resultado = sim.simulate(media_respuesta, desv_respuesta, media_consulta, numero_corridas)
	
	return "lala"
	



