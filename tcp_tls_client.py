import socket
import ssl
import time
import sys

hostname = '%s.mysite.com' % sys.argv[1]
print(hostname)
context = ssl.create_default_context()
context.load_verify_locations('./.certs/*.mysite.com.pem')

with socket.create_connection((hostname, 443)) as sock:
	with context.wrap_socket(sock, server_hostname=hostname) as secure_sock:
		print(secure_sock.version())
		try:
			for i in range(30):
				#Send data
				message = "This is the message.  It will be repeated."
				print('sending "%s"' % message)
				secure_sock.sendall(str.encode(message))

				# Look for the response
				amount_received = 0
				amount_expected = len(message)
				string_received = ""
				while amount_received < amount_expected:
					data = secure_sock.recv(16)
					amount_received += len(data)
					string_received += data.decode()
				print('received "%s' % string_received)
				time.sleep(2)

		finally:
			print('closing socket')
			secure_sock.close()