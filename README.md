# Ejercicio 26

Desde el momento en que se presenta una petición de información hasta el momento en que se entrega, una base
de datos demora un tiempo que responde a la siguiente función:

Tiempo respuesta = `0,1 seg + x seg` . (número de procesos ejecutándose en ese momento)

Donde x es un tiempo que responde a una distribución normal de media 10 segundos y desviación estándar 5
segundos.

Los procesos llegan a la base de datos de 20 terminales, cada una de las cuales ejecuta una consulta cada 200
segundos en promedio (distribución exponencial), más 15 segundos.

- ¿Determinar la cantidad máxima de procesos trabajando simultáneamente?
- ¿Cuál es la demora promedio de respuesta de la base de datos?
- ¿Cuánto es el tiempo ocioso de la base de datos?
- ¿Cuál es la demora máxima de un proceso?
- ¿Cuál es la probabilidad de que existan 8 o más procesos simultáneamente?
