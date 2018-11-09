from configuraciones import *
import psycopg2
conn = psycopg2.connect("dbname=%s user=%s password=%s"%(database,user,passwd))


cur = conn.cursor()
sql ="""DROP SCHEMA public CASCADE;
CREATE SCHEMA public;"""

cur.execute(sql)

sql ="""
CREATE TABLE paises 
           (id serial PRIMARY KEY, pais varchar(40), continente varchar(40));
"""

cur.execute(sql)


sql ="""
CREATE TABLE pilotos
           (numero integer , nombre varchar(40), apellido varchar(40), edad interger , pais varchar(40), escuderia integer);
"""

cur.execute(sql)

sql ="""
CREATE TABLE provedores_marcas 
           (id serial PRIMARY KEY, nombre varchar(40), pais_id integer);
"""

cur.execute(sql)

sql ="""
CREATE TABLE escuderias
           (id serial PRIMARY KEY, nombre varchar(40),jefe_motores varchar(40),provedores_id integer, pais_id integer );
"""

cur.execute(sql)

sql ="""
CREATE TABLE resultados
           (id serial PRIMARY KEY, circuito_id integer, piloto_id integer, accidente varchar, puesto integer, puntuacion integer);
"""

cur.execute(sql)

sql ="""
CREATE TABLE circuitos
           (id serial PRIMARY KEY, nombre varchar(40), pais_id integer, fecha timestap);
"""

cur.execute(sql)




conn.commit()
cur.close()
conn.close()
