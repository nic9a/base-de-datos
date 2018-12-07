from app import app
from flask import render_template,request,redirect
from configuraciones import *

import psycopg2
conn = psycopg2.connect("dbname=%s user=%s password=%s"%(database,user,passwd))
cur = conn.cursor()


@app.route('/insertarp', methods=['GET', 'POST']) 
def insertarp():
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


