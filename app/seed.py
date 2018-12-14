from configuraciones import *
import psycopg2
conn = psycopg2.connect("dbname=%s user=%s password=%s"%(database,user,passwd))
cur = conn.cursor()

sql ="""
insert into paises (pais,continente) values ('Reino Unido', 'Europa '),('Italia', 'Europa '),('Francia', 'Europa'),
('Estados Unidos', 'America'),('Australia', 'Oceania'),('Finlandia','Europa'), ('Belgica','Europa'), ('Alemania','Europa'),
('Mexico','America'), ('Canada','America'), ('Rusia','Europa'), ('España','Europa'), ('Nueva Zelanda','Oceania'),
('Dinamarca','Europa'), ('Suecia','Europa'), ('Monaco','Europa'), ('Suiza','Europa'), ('India','Asia'),
('Austria','Europa'), ('Bahrein','Asia'), ('China','Asia'), ('Azerbaiyan','Asia'), ('Hungria','Europa'),
('Singapur','Asia'), ('Japon','Asia'), ('Brasil','America'), ('Emiratos Arabes','Asia')
returning id;
"""
cur.execute(sql)
sql =""",
insert into pilotos (numero,nombre,apellido,edad,pais,escuderia) values ('44 ','Lewis ','Halmiton ','33','1','6'),
('77','Valteri','Bottas','29','6','6'), ('5','Sebastian','Vettel','31','8','3'), ('7','Kimi','Raikkonen','39','6','3'),
('3','Daniel','Ricciardo','29','5','2'), ('33','Max','Verstappen','21','7','2'), ('11','Sergio','Perez','28','9','4'),
('31','Esteban','Ocon','22','3','4'), ('18','Lance','Stroll','30','10','5'), ('35','Sergey','Sirotkin','23','11','5'),
('27','Nico','Hulkenberg','31','8','9'), ('55','Carlos','Sainz','24','12','9'), ('10','Piere','Gasly','22','3','7'),
('28','Brendon','Hartley','29','13','7'), ('8','Romain','Grosjean','32','3','8'), ('20','Kevin','Magnussen','26','14','8'),
('14','Fernando','Alonso','37','12','1'), ('2','Stoffel','Vandoorne','26','7','1'), ('9','Marcus','Ericsson','28','15','10'),
('16', 'Charles', 'Leclerc', '21','16','10') returning id;
"""
cur.execute(sql)

sql ="""
insert into escuderias (nombre,jefe_motores,proveedores_id, pais_id) values ('Mclaren','Gil de Ferran','1','1'), 
('Red Bull','Christian Horner','1','19'),
('Ferrari','Maurizio Arrivabene','1','2'), ('Force India','Vijay Mallya','1','18'), ('Williams','Paddy Lowe','1','1'),
('Mercedes','James Allison','1','8'), ('Toro Rosso','Franz Tost','1','2'), ('Haas','Guenther Steiner','1','4'),
('Renault','Cyril Abiteboul','1','1'), ('Sauber','Frederic Vasseur','1','17') returning id;
"""
cur.execute(sql)

sql ="""
insert into circuitos (nombre,pais_id, fecha) values ('Melbourne ','5', '25/03'),('Sakhir ','20', '08/04'),('Shanghai ','21', '15/04'),
('Baku City Circuit ','22', '29/04'),('Cataluña ','12', '13/05'),('Montecarlo ','16', '27/05'), ('Gilles Villeneuve','10','10/06'),
('Le Castellet','3', '24/06'),('Spielberg ','19', '01/07'),('Silverstone ','1, 08/07'), ('Hockenheim','8','22/07'),
('Hungaroring','22', '29/07'),('SPA Francorchamps ','7', '26/08'),('Monza ','2', '02/09'), ('Marina Bay','24','16/09'),
('Sochi','11', '30/09'),('Suzuka ','25', '07/10'),('Las Americas ','4', '21/10'), ('Hermanos Rodrigues','9','28/10'),
('Jose Carlos Pace ','26', '11/11'),('Yas Marina Circuit ','27', '25/11') returning id;
"""
cur.execute(sql)

sql ="""
insert into resultados (circuito_id,numero,accidente, puesto,puntacion) values 

('1','5','NO','1', '25'),
('1','44','NO','2', '18'),('1','7','NO','3', '15'),('1','3','NO','4', '12'),('1','14','NO','5', '10'),
('1','33','NO','6', '8'),('1','27','NO','7', '6'),('1','77','NO','8', '4'),('1','2','NO','9', '2'),
('1','55','SI','10', '1'),('1','11','NO','11', '0'),('1','31','NO','12', '0'),('1','16','SI','13', '0'), 
('1','18','SI','14', '0'),('1','28','NO','15', '0'),('1','8','SI','16', '0'),('1','20','SI','17', '0'),
('1','10','SI','18', '0'),('1','9','SI','19', '0'),('1','35','SI','20', '0'),

('2','5','NO','1', '25'),
('2','77','NO','2', '18'), ('2','44','NO','3', '15'), ('2','10','NO','4', '12'), ('2','20','NO','5','10'),
('2','27','NO','6', '8'), ('2','14','NO','7', '6'), ('2','2','NO','8', '4'), ('2','9','NO','9','2'), 
('2','31','NO','10', '1'), ('2','55','NO','11', '0'), ('2','16','NO','12', '0'), ('2','8','NO','13','0'),
('2','18','NO','14', '0'), ('2','35','NO','15', '0'), ('2','11','NO','16','0'), ('2','28','NO','17','0'),
('2','7','SI','18', '0'), ('2','33','SI','19', '0'), ('2','3','SI','2','0'), 

('3','3','NO','1', '25'),
('3','77','NO','2', '18'), ('3','7','NO','3', '15'), ('3','44','NO','4', '12'), ('3','33','NO','5','10'),
('3','27','NO','6', '8'), ('3','14','NO','7', '6'), ('3','5','SI','8', '4'), ('3','55','NO','9','2'), 
('3','20','NO','10', '1'), ('3','31','NO','11', '0'), ('3','11','NO','12', '0'), ('3','2','NO','13','0'),
('3','18','NO','14', '0'), ('3','35','NO','15', '0'), ('3','9','NO','16','0'), ('3','8','NO','17','0'),
('3','10','NO','18', '0'), ('3','16','NO','19', '0'), ('3','28','SI','2','0'),

('4','44','NO','1', '25'),
('4','7','NO','2', '18'), ('4','11','NO','3', '15'), ('4','5','NO','4', '12'), ('4','55','NO','5','10'),
('4','16','NO','6', '8'), ('4','14','NO','7', '6'), ('4','18','NO','8', '4'), ('4','2','NO','9','2'), 
('4','28','NO','10', '1'), ('4','9','NO','11', '0'), ('4','10','NO','12', '0'), ('4','20','NO','13','0'),
('4','77','SI','14', '0'), ('4','8','SI','15', '0'), ('4','33','SI','16','0'), ('4','3','NO','17','0'),
('4','27','SI','18', '0'), ('4','31','NO','19', '0'), ('4','35','SI','2','0'),

('5','44','NO','1', '25'),
('5','77','NO','2', '18'), ('5','33','NO','3', '15'), ('5','5','NO','4', '12'), ('5','3','NO','5','10'),
('5','20','NO','6', '8'), ('5','55','NO','7', '6'), ('5','14','NO','8', '4'), ('5','11','NO','9','2'), 
('5','16','NO','10', '1'), ('5','18','NO','11', '0'), ('5','28','NO','12', '0'), ('5','9','NO','13','0'),
('5','35','SI','14', '0'), ('5','2','NO','15', '0'), ('5','31','SI','16','0'), ('5','7','SI','17','0'),
('5','8','SI','18', '0'), ('5','10','NO','19', '0'), ('5','27','SI','2','0')

 returning id;
"""
cur.execute(sql)

sql ="""
insert into proveedores_marcas (nombre,pais_id) values ('BMW ','8') returning id;
"""
cur.execute(sql)


conn.commit()
cur.close()
conn.close()
