import tornado.ioloop
import tornado.web
import os
import wsgi.routing

def make_app():
	return tornado.web.Application(
			wsgi.routing.paths
		)

if __name__ == '__main__':
	app = make_app()
	
	try:
		address = os.environ['OPENSHIFT_PYTHON_IP']
		port = os.environ['openshift_python_port']
	except KeyError:
		print('Error take ip or port use None or 8080')
		address = None
		port = 8080
	app.listen(port, address=address)
	tornado.ioloop.IOLoop.current().start()
