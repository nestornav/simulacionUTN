#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import OrderedDict, namedtuple

import numpy as np


ResponseRow = namedtuple(
    "ResponseRow",
    ["iteration", "reloj","evento","tiempo_consulta_rnd","tiempo_consulta_total",
     "tiempo_respuesta_rnd_db", "tiempo_respuesta_total",
     "procesos_activos","db_ocupada","tiempo_ocioso"])


def tiempo_respuesta(mean, std):
    return np.random.normal(mean, std) + 0.1


def siguiente_consulta(mean):
    beta = 1/mean
    return np.random.exponential(beta) + 15


def simulate(numero_corridas, media_respuesta, desv_respuesta, media_consulta):
    reloj, db_ocupada, procesos_activos = 0., False, 0
    tiempo_consulta_total, tiempo_respuesta_total = None, None

    respuestas = []
    #import ipdb;ipdb.set_trace()
    for iterations in xrange(numero_corridas):
        if reloj == 0:
            tiempo_consulta_rnd = siguiente_consulta(media_consulta)

            evento = "inicio"
            tiempo_consulta_total = tiempo_consulta_rnd + reloj
            tiempo_respuesta_rnd_db = 0
            tiempo_respuesta_total = 0

        elif reloj == tiempo_consulta_total:
            evento = "Nueva Consulta"
            tiempo_consulta_rnd = siguiente_consulta(media_consulta)
            tiempo_consulta_total = tiempo_consulta_rnd + reloj

            tiempo_respuesta_rnd_db = tiempo_respuesta(media_respuesta, desv_respuesta)
            tiempo_respuesta_total = tiempo_respuesta_rnd_db + reloj
            procesos_activos += 1

        elif reloj == tiempo_respuesta_total:
            evento = "Fin Respuesta"
            procesos_activos -= 1

            if procesos_activos > 0:
                tiempo_respuesta_rnd_db = tiempo_respuesta(media_respuesta, desv_respuesta)
                tiempo_respuesta_total = tiempo_respuesta_rnd_db + reloj
            else:
                tiempo_respuesta_rnd_db = 0
                tiempo_respuesta_total = 0


        db_ocupada = procesos_activos > 0

        respuesta = ResponseRow(
                iteration=iterations, reloj=reloj, evento=evento,
                tiempo_consulta_rnd=tiempo_consulta_rnd, tiempo_consulta_total=tiempo_consulta_total,
                tiempo_respuesta_rnd_db=tiempo_respuesta_rnd_db, tiempo_respuesta_total=tiempo_respuesta_total,
                procesos_activos=procesos_activos, db_ocupada=db_ocupada, tiempo_ocioso=0)
        respuestas.append(respuesta)

        if tiempo_respuesta_total >0:
            if tiempo_consulta_total <= tiempo_respuesta_total:
                reloj = tiempo_consulta_total
            else :
                reloj = tiempo_respuesta_total
        else:
            reloj = tiempo_consulta_total

    return respuestas


def to_ndarray(respuestas, key):
    return  np.array([getattr(r, key) for r in respuestas])

