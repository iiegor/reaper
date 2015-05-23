import aiml

class Interpreter:
	def __init__(self, emitter):
		print u'Initializing the interpreter...'

		self.emitter = emitter
		self.kernel = aiml.Kernel()

		# Kernel setup
		self.kernel.verbose(False)
		self.kernel.setPredicate('secure', "yes")
		self.kernel.learn('startup.xml')
		self.kernel.setPredicate('secure', "no")
		self.kernel.respond('bootstrap')

	def learn(self, data):
		# The machine will store the responses by the user and will learn how to reply better the next time...
		# print 'interpreter#learn func'

		# At the moment...
		res = self.kernel.respond(data['text'])

		self.emitter.emit('send_message', res)




