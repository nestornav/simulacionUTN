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
	reloj, procesos_activos, db_ocupada = 0., 0, False
	tiempo_consulta_total, tiempo_respuesta_total = None, None
	
	respuestas = []
	for iterations in xrange(numero_corridas):
		if reloj == 0:
			tiempo_consulta_rnd = siguiente_consulta()
			
			evento = "inicio"			
			tiempo_consulta_total = tiempo_consulta_rnd + reloj
			tiempo_consulta_rnd = 0
			tiempo_respuesta_total = 0
			procesos_activos = 0
		elif reloj == tiempo_consulta_total:
			evento = "Nueva Consulta"
			tiempo_consulta_rnd = siguiente_consulta()				
			tiempo_consulta_total = tiempo_consulta_rnd + reloj						
			
			procesos_activos = proceso_activos + (1 if proceso_activos < 20 else 0) 
		elif reloj == tiempo_respuesta_total:
			evento = "Fin Respuesta a Consulta"
			tiempo_respuesta_rnd = tiempo_respuesta()
			tiempo tiempo_respuesta_total = tiempo_respuesta_rnd + reloj
			
			
			procesos_activos = procesos_activos - (1 if procesos_activos > 0 else 0)
			tiempo_consulta_total =  if procesos_activos < 20 else tiempo_consulta_total
			


		db_ocupada = procesos_activos > 0
		respuesta = ResponseRow(
				iteration=iterations, reloj=reloj, evento=evento,
				tiempo_consulta_rnd=tiempo_consulta_rnd, tiempo_consulta_total=tiempo_consulta_total,
				tiempo_respuesta_rnd_db=tiempo_respuesta_rnd_db, tiempo_respuesta_total=tiempo_respuesta_total,
				procesos_activos=procesos_activos, db_ocupada=db_ocupada)
		respuestas.append(respuesta)
		
		reloj = tiempo_consulta_total if tiempo_consulta_total <= tiempo_respuesta_total else tiempo_respuesta_total

		























		for term_id, start_time in terminales_ordenadas:		
			tiempo_consulta_rnd = start_time
			tiempo_consulta_total = tiempo_consulta_rnd + reloj
					
			db_ocupada = procesos_activos > 0

			respuesta = ResponseRow(
				iteration=iterations, reloj=reloj, evento = eventos[0],
				tiempo_consulta_rnd=tiempo_consulta_rnd, tiempo_consulta_total=tiempo_consulta_total,
				tiempo_respuesta_rnd_db=tiempo_respuesta_rnd_db, tiempo_respuesta_total=tiempo_respuesta_total,
				procesos_activos=procesos_activos, db_ocupada=db_ocupada)
			respuestas.append(respuesta)

	
		#reloj += start_time
		procesos_activos += 1
		tiempo_respuesta_rnd_db = tiempo_respuesta()		
		tiempo_respuesta_total = tiempo_respuesta_rnd_db + reloj
		
		

	import ipdb;ipdb.set_trace()

	