import tornado.ioloop
import tornado.web
import os


class MainHandler(tornado.web.RequestHandler):
	def get(self):
		self.write('<h1>Hello World!</h1>')

def make_app():
	return tornado.web.Application([
		(r'/', MainHandler),
	])

if __name__ == '__main__':
	app = make_app()
	app.listen(os.environ['OPENSHIFT_PYTHON_PORT'], address=os.environ['OPENSHIFT_PYTHON_IP'])
	tornado.ioloop.IOLoop.current().start()
