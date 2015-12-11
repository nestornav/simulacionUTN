#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import OrderedDict, namedtuple

import numpy as np
import scipy

import pygal

ResponseRow = namedtuple(
	"ResponseRow",
	["reloj","evento","tiempo_consulta_rnd","tiempo_consulta_total",
	 "tiempo_respuesta_rnd_db", "tiempo_respuesta_total",
	 "procesos_activos","db_ocupada","tiempo_ocioso",])


def tiempo_respuesta(mean, std):
	return np.random.normal(mean, std) + 0.1


def tiempo_ejecucion_terminal(mean, n):
	return np.random.exponential(mean, n) + 15


def simulate(media_respuesta, desv_respuesta, media_consulta):
	reloj, procesos_activos, db_ocupada = 0, 0, False
	eventos = ["Inicio","Fin Ejecucion Consulta","Fin Ejecucion Procesamiento"]
	terminales = ["ocupada"] * 20

	start_simulation = tiempo_ejecucion_terminal(media_consulta, 20)

	terminales_desordenadas = [(k, v) for k, v in enumerate(start_simulation)]
	terminales_ordenadas = sorted(terminales_desordenadas, key=lambda e: e[-1]))
	""" reloj = terminales_ordenadas[0][-1] """

	respuesta = []

	for term_id, start_time terminales_ordenadas:
		reloj += start_time
		
		tiempo_consulta_rnd = start_time
		tiempo_consulta_total = tiempo_consulta_rnd + reloj
		tiempo_respuesta_rnd_db = tiempo_respuesta()		
		tiempo_respuesta_total = tiempo_respuesta_rnd_db + reloj
		
		procesos_activos += 1
		db_ocupada = procesos_activos > 0

		ResponseRow(reloj = reloj, tiempo_consulta_rnd = tiempo_consulta_rnd, tiempo_consulta_total = tiempo_consulta_total,
					 tiempo_respuesta_rnd_db = tiempo_respuesta_rnd_db, tiempo_respuesta_total = tiempo_respuesta_total,
					 procesos_activos = procesos_activos, db_ocupada = db_ocupada )




	import ipdb;ipdb.set_trace()