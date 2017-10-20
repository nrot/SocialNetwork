class MainHandler(tornado.web.RequestHandler):
	def get(self):
		#self.write('<h1>Hello World!</h1>')
		self.render('index.html')