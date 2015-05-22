import marshal
from util import read_file, write_file

class Conscience:
	def __init__(self):
		print u'Loading the conscience...'

		self.cache = {}
		self.saving = False

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

	def save(self):
		if self.saving == False:
			try:
				cons_dat = open('conscience.dat', 'w+b')

				# Write
				marshal.dump(self.cache, cons_dat)

				# Delete
				del cons_dat
			except (EOFError, IOError):
				print 'Can not save the conscience!'