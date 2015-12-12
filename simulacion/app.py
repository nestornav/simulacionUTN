#!/usr/bin/env python
# -*- coding: utf-8 -*-

# =============================================================================
# IMPORTS
# =============================================================================

from collections import Counter

from flask import Flask, render_template, request
from flask.ext.script import Manager, Server
from flask_bootstrap import Bootstrap

import pygal

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

    proc_active = sim.to_ndarray(resultados, "procesos_activos")
    stats = {
        "max_process": proc_active.max(),
        "demora_promedio":  sim.to_ndarray(resultados, "tiempo_respuesta_total").mean(),
        "tiempo_ocioso": sim.to_ndarray(resultados, "tiempo_ocioso").sum(),
        "demora_maxima": sim.to_ndarray(resultados, "tiempo_consulta_rnd").max(),
        "promedio_gt8": (proc_active >= 8).sum() / float(len(proc_active))
    }

    # process evolution
    proc_line_chart = pygal.Line(width=800, height=400, explicit_size=True)
    proc_line_chart.title = u'Evolución de procesos por tiempo'
    proc_line_chart.x_labels = map(str, sim.to_ndarray(resultados, "reloj"))
    proc_line_chart.add(u'Procesos', proc_active)

    cnt = Counter(proc_active)
    proc_histogram = pygal.Bar(width=800, height=400, explicit_size=True)
    proc_histogram.title = 'Frencuencia de procesos simultaneos'
    proc_histogram.x_labels = map(str, cnt.keys())
    proc_histogram.add(u'Procesos', cnt.values())

    cnt = Counter(sim.to_ndarray(resultados, "evento"))
    eventos_histogram = pygal.Bar(width=800, height=400, explicit_size=True)
    eventos_histogram.title = 'Frencuencia de eventos'
    eventos_histogram.x_labels = map(str, cnt.keys())
    eventos_histogram.add(u'Eventos', cnt.values())

    graphs = [proc_line_chart, proc_histogram, eventos_histogram]

    return render_template('index.html', resultados=resultados, media_respuesta=media_respuesta,
        desv_respuesta=desv_respuesta, media_consulta=media_consulta,
        numero_corridas=numero_corridas, stats=stats, graphs=graphs)
