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

def closeConnection(connection):
	if isinstance(connection, mysql.connector.MySQLConnection):
		connection.close()
		print "Connection successfully closed."
	else:
		print "Error: Not a valid 'mysql.connector.MySQLConnection' object to close."

def closeCursor(cursor):
	cursor.close()

def executeQuery(cursor, query, errorDescription=''):
	try:
		cursor.execute(query)
	except mysql.connector.Error as e:
		print errorDescription+": "+str(e)


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
	executeQuery(cursor,query,'Error creating Cluster table in DB')

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
	executeQuery(cursor,query,'Error creating Song table in DB')


def addSongToDB(cursor, song, songIsTup = False, songIsDict = False):
	columns = (
		"INSERT INTO Songs "
		"(ClusterID, "
		"Title, "
		"Artist_Name, "
		"Artist_Familiarity, "
		"Artist_Hotness, "
		"Danceability, "
		"Duration, "
		"End_of_Fade_In, "
		"Energy, "
		"Loudness, "
		"Start_of_Fade_Out, "
		"Tempo) "
		)
	if songIsTup and not songIsDict:
		values = (
			"VALUES ("
			"{0}, "
			"'{1}', "
			"'{2}', "
			"{3:.8f}, "
			"{4:.8f}, "
			"{5:.8f}, "
			"{6:.8f}, "
			"{7:.8f}, "
			"{8:.8f}, "
			"{9:.8f}, "
			"{10:.8f}, "
			"{11:.8f}, "
			"{12:.8f} "
			" ) ;".format(
			songAttrTup[0],
			songAttrTup[1],
			songAttrTup[2],
			songAttrTup[3],
			songAttrTup[4],
			songAttrTup[5],
			songAttrTup[6],
			songAttrTup[7],
			songAttrTup[8],
			songAttrTup[9],
			songAttrTup[10],
			songAttrTup[11])
			)
	elif songIsDict and not songIsTup:
		values = (
			"VALUES ("
			"{0}, "
			"'{1}', "
			"'{2}', "
			"{3:.8f}, "
			"{4:.8f}, "
			"{5:.8f}, "
			"{6:.8f}, "
			"{7:.8f}, "
			"{8:.8f}, "
			"{9:.8f}, "
			"{10:.8f}, "
			"{11:.8f}, "
			"{12:.8f} "
			" ) ;".format(
			songAttrTup['ClusterID'],
			songAttrTup['Title'],
			songAttrTup['Artist_Name'],
			songAttrTup['Artist_Familiarity'],
			songAttrTup['Artist_Hotness'],
			songAttrTup['Danceability'],
			songAttrTup['Duration'],
			songAttrTup['End_of_Fade_In'],
			songAttrTup['Energy'],
			songAttrTup['Loudness'],
			songAttrTup['Start_of_Fade_Out'],
			songAttrTup['Tempo'])
			)
	if values:
		query = columns + values
		executeQuery(cursor,query,'Error adding Song to DB')
	else:
		print "Specify parameter to indicate song format."

def main():
	with SSHTunnelForwarder(
		(base64.b64decode(cred.getAddr()), int(base64.b64decode(cred.getAddr_port()))), 
		ssh_password=base64.b64decode(cred.getPassword_SSH()), 
		ssh_username=base64.b64decode(cred.getUsername_SSH()), 
		remote_bind_address=(base64.b64decode(cred.getRemoteAddr()), int(base64.b64decode(cred.getRemoteAddr_port())))
		) as server:
		
		try:
			conn = mysql.connector.connect(
				host='127.0.0.1', 
				port=server.local_bind_port, 
				database='Song_DB', 
				user=base64.b64decode(cred.getUsername_MySQL()), 
				passwd=base64.b64decode(cred.getPassword_MySQL()))
			cursor = conn.cursor()
		except mysql.connector.Error as e:
			print "Error making connection:", str(e)

		conn.commit()

		cursor.close()
		closeConnection(conn)

main()

# def addSongToDB(cursor, songAttrTup):
# 	# add_song_SQL = ("INSERT INTO Songs "
# 	# 	"(ClusterID, Title, Artist, Danceability, Energy, Loudness, Tempo) "
# 	# 	"VALUES (%d, %s, %s, %.4f, %.4f, %.4f, %.4f)")
# 	add_song_SQL = ("INSERT INTO Songs "
# 		"(ClusterID, Title, Artist, Danceability, Energy, Loudness, Tempo) "
# 		"VALUES ( {0}, '{1}', '{2}', {3:.4f}, {4:.4f}, {5:.4f}, {6:.4f} ) ;".format(songAttrTup[0],songAttrTup[1],songAttrTup[2],songAttrTup[3],songAttrTup[4],songAttrTup[5],songAttrTup[6]))
# 	if True:#isinstance(songAttrTup, (int,str,str,float,float,float,float)):
# 		cursor.execute(add_song_SQL)
# 		# cursor.execute(add_song_SQL, songAttrTup)
# 	else:
# 		print "Not a valid song tuple passed!"


