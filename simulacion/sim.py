#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import OrderedDict, namedtuple

import numpy as np
import scipy

import pygal

ResponseRow = namedtuple(
	"ResponseRow",
	["iteration", "reloj","evento","tiempo_consulta_rnd","tiempo_consulta_total",
	 "tiempo_respuesta_rnd_db", "tiempo_respuesta_total",
	 "procesos_activos","db_ocupada","tiempo_ocioso"])


def tiempo_respuesta(mean, std):
	return np.random.normal(mean, std) + 0.1


def siguiente_consulta(mean):
	return np.random.exponential(mean) + 15


def simulate(numero_corridas, media_respuesta, desv_respuesta, media_consulta):
	reloj, db_ocupada = 0., False
	tiempo_consulta_total = None
	
	respuestas = []
	tiempos_respuestas = []
	import ipdb;ipdb.set_trace()
	for iterations in xrange(numero_corridas):
		if reloj == 0:
			tiempo_consulta_rnd = siguiente_consulta(media_consulta)
			
			evento = "inicio"			
			tiempo_consulta_total = tiempo_consulta_rnd + reloj
			tiempo_consulta_rnd = 0	
			tiempo_respuesta_rnd_db = 0
			tiempo_respuesta_total = 0				
		elif reloj == tiempo_consulta_total:
			evento = "Nueva Consulta"
			tiempo_consulta_rnd = siguiente_consulta(media_consulta)				
			tiempo_consulta_total = tiempo_consulta_rnd + reloj						

			tiempo_respuesta_rnd_db = tiempo_respuesta(media_respuesta, desv_respuesta)
			tiempo_respuesta_total = tiempo_respuesta_rnd_db + reloj
			tiempos_respuestas.append(tiempo_respuesta_total)
			tiempos_respuestas.sort()
						
		elif tiempos_respuestas and reloj == tiempos_respuestas[0]:
			evento = "Fin Respuesta a Consulta"			
			tiempos_respuestas.pop(0)			


		procesos_activos = len(tiempos_respuestas)
		db_ocupada = procesos_activos > 0
		respuesta = ResponseRow(
				iteration=iterations, reloj=reloj, evento=evento,
				tiempo_consulta_rnd=tiempo_consulta_rnd, tiempo_consulta_total=tiempo_consulta_total,
				tiempo_respuesta_rnd_db=tiempo_respuesta_rnd_db, tiempo_respuesta_total=tiempo_respuesta_total,
				procesos_activos=procesos_activos, db_ocupada=db_ocupada, tiempo_ocioso=0)
		respuestas.append(respuesta)
		
		if tiempos_respuestas:
			if tiempo_consulta_total <= tiempos_respuestas[0]:
				reloj = tiempo_consulta_total
			else :
				reloj = tiempos_respuestas[0]
		else :
			reloj = tiempo_consulta_total

	return respuestas
	