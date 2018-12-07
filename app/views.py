from app import app
from flask import render_template,request,redirect
from configuraciones import *

import psycopg2
conn = psycopg2.connect("dbname=%s user=%s password=%s"%(database,user,passwd))
cur = conn.cursor()


@app.route('/')
@app.route('/index')
def index():
	sql ="""
	select circuitos.fecha, circuitos.nombre, pilotos.nombre, puesto, puntuacion
	from resultados, circuitos, pilotos
	where circuitos.id = resultados.circuito_id and resultados.piloto_id=pilotos.numero
	group by fecha
	order by fecha
	"""
	print sql 
	cur.execute(sql)
	resultados  = cur.fetchall()

	return render_template("index.html", resultados = resultados)

@app.route('/pilotos')
def pilotos():
	sql ="""
	select numero,nombre, apellido, pais, edad, escuderia
	from pilotos
	order by pilotos.nombre
	"""
	print sql 
	cur.execute(sql)
	pilotos  = cur.fetchall()

	return render_template("pilotos.html")


@app.route('/circuitos')
def circuitos():
	sql ="""
	select fecha, nombre, pais
	from circuitos
	order by fecha
	"""
	print sql 
	cur.execute(sql)
	circuitos  = cur.fetchall()

	return render_template("circuitos.html")

@app.route('/escuderias')
def escuderias():
	sql ="""
	select id, nombre, pais, proveedores_id, jefe_motores
	from circuitos
	order by escuderias.nombre
	"""
	print sql 
	cur.execute(sql)
	escuderias  = cur.fetchall()

	return render_template("escuderia.html")

@app.route('/proveedores')
def proveedores():
	sql ="""
	select id, nombre, pais
	from proveedores_marcas
	order by nombre
	"""
	print sql 
	cur.execute(sql)
	Proveedores_motores  = cur.fetchall()

	return render_template("proveedores.html")


@app.route('/insertarp', methods=['GET', 'POST']) 
def insertarp(pais):
	if request.method == 'POST':
		nombre =  request.form['nombre']
	        pais =  request.form['pais']
		
		pais1 = sql=""" select paises.id from paises where nombre='%s'"""%(pais)
		cur.execute(sql)

		sql = """ insert into Proveedores_motores  
		(nombre,pais1) 
		values ('%s','%s', ) returning rut_proveedor; """%(nombre,pais1)
		cur.execute(sql)
		conn.commit()
	return render_template('insertarp.html')

@app.route('/eliminarPais', methods=['GET', 'POST'])
def eliminar(id):

	sql ="""
		delete from paises where id = %s
	"""%(id)
	print sql
	cur.execute(sql)
	conn.commit()
	return  redirect(request.referrer)


