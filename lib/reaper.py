from network import Network, NeuralNetwork
from conscience import Conscience
from vitals import Vitals
from util import get_time

class Reaper:
	def __init__(self, args):
		self.args = args

		self.network = Network()
		self.neural_network = NeuralNetwork((Vitals.FIRST_LAYER, Vitals.SECOND_LAYER, Vitals.OUTPUT_LAYER), learning_rate=Vitals.LEARNING_RATE, momentum=Vitals.MOMENTUM_RATE)
		self.conscience = Conscience()

	def cl_start(self):
		print 'cl_start func'

	def slack_start(self):
		print 'slack_start func'
