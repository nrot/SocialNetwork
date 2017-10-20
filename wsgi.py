import tornado.ioloop
import tornado.web
import os


class MainHandler(tornado.web.RequestHandler):
	def get(self):
		self.write('<h1>Hello World!</h1>')
		#self.render('index.html')

def make_app():
	return tornado.web.Application([
		(r'/', MainHandler),
	])

if __name__ == '__main__':
	app = make_app()
	port = os.environ['OPENSHIFT_PYTHON_PORT']
	try:
		address = os.environ['OPENSHIFT_PYTHON_IP']
	except KeyError:
		print('Error take ip use None')
		address = None
	app.listen(port, address=address)
	tornado.ioloop.IOLoop.current().start()
