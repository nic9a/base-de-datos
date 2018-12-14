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
	select circuitos.nombre, pilotos.nombre, puesto, puntuacion
	from resultados, circuitos, pilotos
	where circuitos.id = resultados.circuito_id and resultados.piloto_id=pilotos.numero
	and fecha='13/05'
	"""
	print sql
	cur.execute(sql)
	resultados  = cur.fetchall()

	sql ="""
	select pilotos.nombre,sum(resultados.puntuacion) as totales
	from pilotos, resultados
	where pilotos.numero = resultados.piloto_id
	group by pilotos.nombre
	order by totales desc
	"""
	print sql
	cur.execute(sql)
	resultados  = cur.fetchall()

	sql ="""
	select circuitos.nombre, paises.nombre 
	from circuitos, paises
	where continente='asia'
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

	return render_template("pilotos.html", pilotos = pilotos)


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

	return render_template("circuitos.html", circuitos = circuitos)

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

	return render_template("escuderia.html", escuderias = escuderias)

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

	return render_template("proveedores.html", proveedores = proveedores)


@app.route('/insertarp', methods=['GET', 'POST'])
def insertarp(prov):
	if request.method == 'POST':
		nombre =  request.form['nombre']
		pais =  request.form['pais']

		pais1 = sql=""" select paises.id from paises where nombre='%s'"""%(pais)
		cur.execute(sql)

		sql = """ insert into Proveedores_motores
		(nombre,pais_id)
		values ('%s','%s'); """%(nombre,pais1)
		insert = cur.execute(sql)
		conn.commit()
	return render_template('insertarp.html' )

@app.route('/insertarescuderia', methods=['GET', 'POST'])
def insertarp(escuderia):
	if request.method == 'POST':
		nombre =  request.form['nombre']
		jefe =  request.form['jefe_motores']
		proveedor =  request.form['proveedor']
		pais =  request.form['pais']

		pais1 = sql=""" select paises.id from paises where nombre='%s'"""%(pais)
		cur.execute(sql)
		prov = sql=""" select id from proveedores_marcas where nombre='%s'"""%(proveedor)
		cur.execute(sql)

		sql = """ insert into escuderias
		(nombre,jefe_motores,proveedores_id,pais_id)
		values ('%s','%s','%s','%s' ); """%(nombre, jefe, prov,pais1)
		insert = cur.execute(sql)
		conn.commit()
	return render_template('insertarescuderia.html' )

@app.route('/insertarpais', methods=['GET', 'POST'])
def insertarp(pais):
	if request.method == 'POST':
		pais =  request.form['pais']
		continente =  request.form['continente']

		sql = """ insert into paises
		(pais,continente)
		values ('%s','%s'); """%(pais, continente)
		insert = cur.execute(sql)
		conn.commit()
	return render_template('insertarpais.html' )

@app.route('/insertarpilotos', methods=['GET', 'POST'])
def insertarp(piloto):
	if request.method == 'POST':
		numero = request.form['numero']
		nombre =  request.form['nombre']
		apellido =  request.form['apellido']
		edad =  request.form['edad']
		pais =  request.form['pais']
		escuderia =  request.form['escuderia']

		esc = sql=""" select escuderias.id from escuderias where nombre='%s'"""%(escuderia)
		cur.execute(sql)
		pais1 = sql=""" select paises.id from paises where nombre='%s'"""%(pais)
		cur.execute(sql)

		sql = """ insert into pilotos
		(numero, nombre, apellido, edad, pais, escuderia)
		values ('%s','%s','%s','%s','%s','%s' ) returning rut_proveedor;
		"""%(numero,nombre,apellido,edad,pais1, ecs)
		insert = cur.execute(sql)
		conn.commit()
	return render_template('insertarpilotos.html' )

app.route('/insertarcircuito', methods=['GET', 'POST'])
def insertarp(circuito):
	if request.method == 'POST':
		nombre =  request.form['nombre']
		pais =  request.form['pais']
		fecha =  request.form['fecha']

		pais1 = sql=""" select paises.id from paises where nombre='%s'"""%(pais)
		cur.execute(sql)

		sql = """ insert into circuitos
		(nombre,pais_id, fecha)
		values ('%s','%s', '%s'); """%(nombre, pais1, fecha)
		insert = cur.execute(sql)
		conn.commit()
	return render_template('insertarcircuito.html' )

@app.route('/eliminarPais', methods=['GET', 'POST'])
def eliminar(id):

	sql ="""
		delete from paises where id = %s
	"""%(id)
	print sql
	cur.execute(sql)
	conn.commit()
	return  redirect(request.referrer)
