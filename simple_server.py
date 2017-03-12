import socket

HOST, PORT = "", 8888

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen(1)

print "Serving HTTP on %s ..." % PORT

while True:
	conn, client = server.accept()
	request = conn.recv(1024)
	print request

	http_response = """\
	HTTP/1.1 200 OK

	Hello, World !
	"""

	conn.sendall(http_response)
	conn.close()