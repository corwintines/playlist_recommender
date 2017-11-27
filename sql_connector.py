import mysql.connector
from mysql.connector import errorcode
import time
import base64
from sshtunnel import SSHTunnelForwarder
import cred

config = {
	'user': '',
	'password': '',
	'database': 'Song_DB',
	'host' : 'localhost',
	'raise_on_warnings': True,
}


def login(config):
	username = raw_input("username: ")
	password = raw_input("password: ")
	config['user'] = str(username)
	config['password'] = str(password)

def openConnection(config):
	try:
		cnx = mysql.connector.connect(**config)
		print "connected :)"
		
	except mysql.connector.Error as err:
		if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
			print("Something is wrong with your user name or password")
		elif err.errno == errorcode.ER_BAD_DB_ERROR:
			print("Database does not exist")
		else:
			print(err)
	else:
		return cnx

def closeConnection(connection):
	if isinstance(connection, mysql.connector.MySQLConnection):
		connection.close()
		print "Connection successfully closed."
	else:
		print "Error: Not a valid 'mysql.connector.MySQLConnection' object to close."

def openCursor(connection):
	if isinstance(connection, mysql.connector.MySQLConnection):
		cursor = connection.cursor()
		return cursor
	else:
		print "Error: Not a valid 'mysql.connector.MySQLConnection' object to close."

def closeCursor(cursor):
	cursor.close()

def createClusterTable(cursor):
	query = (
		"CREATE TABLE Cluster "
		"("
		"ClusterID int(11) NOT NULL, "
		"Danceability decimal(12,8) NOT NULL, "
		"Energy decimal(12,8) NOT NULL, "
		"Loudness decimal(12,8) NOT NULL, "
		"Tempo decimal(12,8) NOT NULL, "
		"PRIMARY KEY (ClusterID) "
		") "
		"ENGINE=InnoDB DEFAULT CHARSET=utf8; "
		)
	cursor.execute(query)

def createSongTable(cursor):
	query = (
		"CREATE TABLE Song "
		"("
		"song_DB_ID int(11) NOT NULL AUTO_INCREMENT, "
		"ClusterID int(11) NOT NULL, "
		"Title varchar(255) NOT NULL, "
		"Artist_Name varchar(255) NOT NULL, "
		"Artist_Familiarity decimal(12,8) NOT NULL, "
		"Artist_Hotness decimal(12,8) NOT NULL, "
		"Danceability decimal(12,8) NOT NULL, "
		"Duration decimal(12,8) NOT NULL, "
		"End_of_Fade_In decimal(12,8) NOT NULL, "
		"Energy decimal(12,8) NOT NULL, "
		"Loudness decimal(12,8) NOT NULL, "
		"Start_of_Fade_Out decimal(12,8) NOT NULL, "
		"Tempo decimal(12,8) NOT NULL, "
		"PRIMARY KEY (song_DB_ID), "
		"KEY Songs_ClusterID_INDEX (ClusterID)"
		") "
		"ENGINE=InnoDB AUTO_INCREMENT=86137 DEFAULT CHARSET=utf8; "
		)
	cursor.execute(query)

def addSongToDB(cursor, songTuple):
	query = (
		"INSERT INTO Songs "
		"(ClusterID, "
		"Title, "
		"Artist_Name, "
		"Artist_Familiarity, "
		"Danceability, Energy, Loudness, Tempo) "
		""
		)


def addSongToDB(cursor, songAttrTup):
	# add_song_SQL = ("INSERT INTO Songs "
	# 	"(ClusterID, Title, Artist, Danceability, Energy, Loudness, Tempo) "
	# 	"VALUES (%d, %s, %s, %.4f, %.4f, %.4f, %.4f)")
	add_song_SQL = ("INSERT INTO Songs "
		"(ClusterID, Title, Artist, Danceability, Energy, Loudness, Tempo) "
		"VALUES ( {0}, '{1}', '{2}', {3:.4f}, {4:.4f}, {5:.4f}, {6:.4f} ) ;".format(songAttrTup[0],songAttrTup[1],songAttrTup[2],songAttrTup[3],songAttrTup[4],songAttrTup[5],songAttrTup[6]))
	if True:#isinstance(songAttrTup, (int,str,str,float,float,float,float)):
		cursor.execute(add_song_SQL)
		# cursor.execute(add_song_SQL, songAttrTup)
	else:
		print "Not a valid song tuple passed!"

def main():
	with SSHTunnelForwarder((base64.b64decode(cred.getAddr()), int(base64.b64decode(cred.getAddr_port()))), 
		ssh_password=base64.b64decode(cred.getPassword()), 
		ssh_username=base64.b64decode(cred.getUsername()), 
		remote_bind_address=(base64.b64decode(cred.getRemoteAddr()), int(base64.b64decode(cred.getRemoteAddr_port())))) as server:
		
		# conn = MySQLdb.connect(host='127.0.0.1', port=server.local_bind_port, user='yashpatel', passwd='yashpatel')
		conn = mysql.connector.connect(host='127.0.0.1', port=server.local_bind_port, database='Song_DB', user='yashpatel', passwd='yashpatel')
		cursor = conn.cursor()
		
		createSongTable(cursor)
		# login(config)
		# cnx = openConnection(config)
		# cursor = openCursor(cnx)
		# counter = 0
		# while counter < 100:
		# 	song1 = (1,'Doctor Jones','Aqua',4.782,1000.004444,-999.99,188)
		# 	# song1_Clean = "VALUES {0}, {1}, {2}, {3:.4f}, {4:.4f}, {5:.4f}, {6:.4f}".format(song1[0],song1[1],song1[2],song1[3],song1[4],song1[5],song1[6])
		# 	song2 = (2,'My Heart Will Go On','Celine Dion',4.782,1000.004444,-999.99,188)
		# 	# song2_Clean = "{0}, {1}, {2}, {4}8.4f, {8.4f}, {8.4f}, {8.4f}".format(song2,)
		# 	addSongToDB(cursor, song1)
		# 	conn.commit()
		# 	addSongToDB(cursor, song2)
		# 	conn.commit()
		# 	counter +=1
		# print song1
		# print song2
		# print song1_Clean
		# print song2_Clean

		# print "INSERT INTO Songs (ClusterID, Title, Artist, Danceability, Energy, Loudness, Tempo) VALUES (%d, %s, %s, %.4f, %.4f, %.4f, %.4f)" %song1
		closeCursor(cursor)
		closeConnection(conn)

main()




