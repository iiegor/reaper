from util import read_file

class Conscience:
	def __init__(self):
		print u'Loading the conscience...'

		self.cache = {}

		self.load()

	def load(self):
		try:
			cons_dat = read_file('conscience.dat')

			# Store in the cache for the session
			self.cache = marshal.loads(cons_dat)

			# Delete
			del cons_dat
		except (EOFError, IOError):
			self.cache = {}
			print 'The conscience is empty!'