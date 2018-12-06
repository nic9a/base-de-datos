from configuraciones import *
import psycopg2
conn = psycopg2.connect("dbname=%s user=%s password=%s"%(database,user,passwd))
cur = conn.cursor()

sql ="""
insert into paises (pais,continente) values ('Inglaterra, Europa '),('Italia, Europa '),('Francia, Europa'),
('Estados Unidos, America'),('Australia, Oceania');
"""
cur.execute(sql)
sql =""",
insert into pilotos (numero,nombre,apellido,edad,pais,escuderia) values ('44 ','Lewis ','Halmiton ','33','Inglaterra ','0') returning id;
"""
cur.execute(sql)

sql ="""
insert into provedores_marcas (nombre,pais_id) values ('Renault ','0 ') returning id;
"""
cur.execute(sql)

sql ="""
insert into escuderias (nombre,jefe_motores,provedores_id,pais_id) values ('Mclaren','Pat Fry','0','0') returning id;
"""
cur.execute(sql)

sql ="""
insert into circuitos (nombre,pais_id) values ('MELBOURNE ','0 ',now()) returning id;
"""
cur.execute(sql)

sql ="""
insert into resultados (circuito_id,piloto_id,accidente, puesto,puntacion) values ('0 ','0 ','4','35') returning id;
"""
cur.execute(sql)




conn.commit()
cur.close()
conn.close()
