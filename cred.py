import base64
addr = base64.b64encode('10.76.136.154')
addr_port = base64.b64encode('22')
remoteAddr = base64.b64encode('127.0.0.1')
remoteAddr_port = base64.b64encode('3306')
username = base64.b64encode('lucasjakober')
password = base64.b64encode('FordF150$')


def getUsername():
	return username

def getPassword():
	return password

def getAddr():
	return addr

def getAddr_port():
	return addr_port

def getRemoteAddr():
	return remoteAddr

def getRemoteAddr_port():
	return remoteAddr_port