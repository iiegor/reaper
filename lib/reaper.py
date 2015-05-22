from network import NeuralNetwork
from emitter import Emitter
from conscience import Conscience
from interpreter import Interpreter
from vitals import Vitals
from util import get_time
from time import sleep

from ports.slack import Slack

class Reaper:
	def __init__(self, args):
		self.args = args

		self.emitter = Emitter()
		self.neural_network = NeuralNetwork((Vitals.FIRST_LAYER, Vitals.SECOND_LAYER, Vitals.OUTPUT_LAYER), learning_rate=Vitals.LEARNING_RATE, momentum=Vitals.MOMENTUM_RATE)
		self.conscience = Conscience()
		self.interpreter = Interpreter()

	def cl_start(self):
		print u'cl_start func'

	def slack_start(self):
		slack = Slack('xoxb-5033078835-U4Jcw2kkaebWWsuUUtyJNNaS', self.emitter)
		slack.start()

	def rpi_start(self):
		print u'rpi_start func'
