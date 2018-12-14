from .configuraciones import *
import psycopg2
conn = psycopg2.connect("dbname=%s user=%s password=%s"%(database,user,passwd))
cur = conn.cursor()

sql ="""
insert into paises (pais,continente) values ('Inglaterra', 'Europa'),('Italia', 'Europa '),('Francia', 'Europa'),
('Estados Unidos', 'America'),('Australia', 'Oceania');
"""
cur.execute(sql)
sql ="""
insert into pilotos (numero,nombre,apellido,edad,pais,escuderia) values ('44 ','Lewis','Halmiton','33','1','0');
"""
cur.execute(sql)

sql ="""
insert into proveedores_marcas (nombre,pais_id) values ('Renault','1');
"""
cur.execute(sql)

sql ="""
insert into escuderias (nombre,jefe_motores,provedores_id,pais_id) values ('Mclaren','Pat Fry','1','1');
"""
cur.execute(sql)

sql ="""
insert into circuitos (nombre,pais_id,fecha) values ('MELBOURNE','1','1000');
"""
cur.execute(sql)

sql ="""
insert into resultados (circuito_id,piloto_id,accidente, puesto,puntuacion) values ('1','1','1','35','35');
"""
cur.execute(sql)
