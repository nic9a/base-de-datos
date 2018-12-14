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
insert into pilotos (numero,nombre,apellido,edad,pais,escuderia) values ('44 ','Lewis ','Halmiton ','33','0','5'),
('77','Valteri','Bottas','29','5','5'), ('5','Sebastian','Vettel','31','7','2'), ('7','Kimi','Raikkonen','39','5','2'),
('3','Daniel','Ricciardo','29','4','1'), ('33','Max','Verstappen','21','6','1'), ('11','Sergio','Perez','28','8','3'),
('31','Esteban','Ocon','22','2','3'), ('18','Lance','Stroll','30','9','4'), ('35','Sergey','Sirotkin','23','10','4'),
('27','Nico','Hulkenberg','31','7','8'), ('55','Carlos','Sainz','24','11','8'), ('10','Piere','Gasly','22','2','6'),
('28','Brendon','Hartley','29','12','6'), ('8','Romain','Grosjean','32','2','7'), ('20','Kevin','Magnussen','26','13','7'),
('14','Fernando','Alonso','37','11','0'), ('2','Stoffel','Vandoorne','26','6','0'), ('9','Marcus','Ericsson','28','14','9'),
('16', 'Charles', 'Leclerc', '21','15','9') returning id;
"""
cur.execute(sql)

sql ="""
insert into escuderias (nombre,jefe_motores,pais_id) values ('Mclaren','Gil de Ferran','0'), ('Red Bull','Christian Horner','18'),
('Ferrari','Maurizio Arrivabene','1'), ('Force India','Vijay Mallya','17'), ('Williams','Paddy Lowe','0'),
('Mercedes','James Allison','7'), ('Toro Rosso','Franz Tost','1'), ('Haas','Guenther Steiner','3'),
('Renault','Cyril Abiteboul','0'), ('Sauber','Frederic Vasseur','16') returning id;
"""
cur.execute(sql)

sql ="""
insert into circuitos (nombre,pais_id) values ('Melbourne ','4', '25/03'),('Sakhir ','19', '08/04'),('Shanghai ','20', '15/04'),
('Baku City Circuit ','21', '29/04'),('Cataluña ','11', '13/05'),('Montecarlo ','9', '27/05'), ('Gilles Villeneuve','9','10/06'),
('Le Castellet','2', '24/06'),('Spielberg ','18', '01/07'),('Silverstone ','0', 08/07'), ('Hockenheim','7','22/07'),
('Hungaroring','21', '29/07'),('SPA Francorchamps ','6', '26/08'),('Monza ','1', '02/09'), ('Marina Bay','23','16/09'),
('Sochi','10', '30/09'),('Suzuka ','24', '07/10'),('Las Americas ','3', '21/10'), ('Hermanos Rodrigues','8','28/10'),
('Jose Carlos Pace ','25', '11/11'),('Yas Marina Circuit ','26', '25/11') returning id;
"""
cur.execute(sql)

sql ="""
insert into resultados (circuito_id,piloto_id,accidente, puesto,puntacion) values 

('0','5','NO','1', '25'),
('0','44','NO','2', '18'),('0','7','NO','3', '15'),('0','3','NO','4', '12'),('0','14','NO','5', '10'),
('0','33','NO','6', '8'),('0','27','NO','7', '6'),('0','77','NO','8', '4'),('0','2','NO','9', '2'),
('0','55','SI','10', '1'),('0','11','NO','11', '0'),('0','31','NO','12', '0'),('0','16','SI','13', '0'), 
('0','18','SI','14', '0'),('0','28','NO','15', '0'),('0','8','SI','16', '0'),('0','20','SI','17', '0'),
('0','10','SI','18', '0'),('0','9','SI','19', '0'),('0','35','SI','20', '0'),

('1','5','NO','1', '25'),
('1','77','NO','2', '18'), ('1','44','NO','3', '15'), ('1','10','NO','4', '12'), ('1','20','NO','5','10'),
('1','27','NO','6', '8'), ('1','14','NO','7', '6'), ('1','2','NO','8', '4'), ('1','9','NO','9','2'), 
('1','31','NO','10', '1'), ('1','55','NO','11', '0'), ('1','16','NO','12', '0'), ('1','8','NO','13','0'),
('1','18','NO','14', '0'), ('1','35','NO','15', '0'), ('1','11','NO','16','0'), ('1','28','NO','17','0'),
('1','7','SI','18', '0'), ('1','33','SI','19', '0'), ('1','3','SI','2','0'), 

('2','3','NO','1', '25'),
('2','77','NO','2', '18'), ('2','7','NO','3', '15'), ('2','44','NO','4', '12'), ('2','33','NO','5','10'),
('2','27','NO','6', '8'), ('2','14','NO','7', '6'), ('2','5','SI','8', '4'), ('2','55','NO','9','2'), 
('2','20','NO','10', '1'), ('2','31','NO','11', '0'), ('2','11','NO','12', '0'), ('2','2','NO','13','0'),
('2','18','NO','14', '0'), ('2','35','NO','15', '0'), ('2','9','NO','16','0'), ('2','8','NO','17','0'),
('2','10','NO','18', '0'), ('2','16','NO','19', '0'), ('2','28','SI','2','0'),

('3','44','NO','1', '25'),
('3','7','NO','2', '18'), ('3','11','NO','3', '15'), ('3','5','NO','4', '12'), ('3','55','NO','5','10'),
('3','16','NO','6', '8'), ('3','14','NO','7', '6'), ('3','18','NO','8', '4'), ('3','2','NO','9','2'), 
('3','28','NO','10', '1'), ('3','9','NO','11', '0'), ('3','10','NO','12', '0'), ('3','20','NO','13','0'),
('3','77','SI','14', '0'), ('3','8','SI','15', '0'), ('3','33','SI','16','0'), ('3','3','NO','17','0'),
('3','27','SI','18', '0'), ('3','31','NO','19', '0'), ('3','35','SI','2','0'),

('4','44','NO','1', '25'),
('4','77','NO','2', '18'), ('4','33','NO','3', '15'), ('4','5','NO','4', '12'), ('4','3','NO','5','10'),
('4','20','NO','6', '8'), ('4','55','NO','7', '6'), ('4','14','NO','8', '4'), ('4','11','NO','9','2'), 
('4','16','NO','10', '1'), ('4','18','NO','11', '0'), ('4','28','NO','12', '0'), ('4','9','NO','13','0'),
('4','35','SI','14', '0'), ('4','2','NO','15', '0'), ('4','31','SI','16','0'), ('4','7','SI','17','0'),
('4','8','SI','18', '0'), ('4','10','NO','19', '0'), ('4','27','SI','2','0')

 returning id;
"""
cur.execute(sql)




conn.commit()
cur.close()
conn.close()
