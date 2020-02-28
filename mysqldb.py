import mysql.connector

def createConnection(user, password, host, database):
   con = mysql.connector.connect(user=user, password=password,
                              host=host,
                              database=database)
   return con
   pass

def selectAll(query, con):
   cursor = con.cursor(dictionary=True) # Transforma a resposta em um dicionário
   cursor.execute(query)
   return cursor.fetchall()
   pass

def create(data, con):
   cursor = con.cursor(dictionary=True)
   query = "INSERT INTO `dev`(`name`, `lang`, `position`) VALUES('{name}', '{lang}', '{position}')".format(name=data['name'], lang=data['lang'], position=data['position'])
   cursor.execute(query)
   con.commit()
   pass

def alter(data, con):
   cursor = con.cursor(dictionary=True)
   query = "UPDATE `dev` SET `name` = '{name}', `lang` = '{lang}', `position` = '{position}'  WHERE (`cod_dev` = {dev_id})".format(name=data['name'], lang=data['lang'], position=data['position'], dev_id=data['dev_id'])
   cursor.execute(query)
   con.commit()
   pass

def delete(data, con):
   cursor = con.cursor(dictionary=True)
   query = "DELETE FROM `dev` WHERE `cod_dev` = {dev_id}".format(dev_id=data['dev_id'])
   cursor.execute(query)
   con.commit()
   pass

