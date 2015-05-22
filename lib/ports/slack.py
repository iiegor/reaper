from slackclient import SlackClient
from time import time, sleep

class Slack:
	def __init__(self, token):
		self._slack = SlackClient(token)
		self.last_ping = 0

	def connect(self):
		self._slack.rtm_connect()

	def start(self):
		self.connect()

		while True:
			for data in self._slack.rtm_read():
				self._input(data)
				self._ping()

			sleep(.1)

	def _ping(self):
		now = int(time())
		if now > self.last_ping + 3:
			self._slack.server.ping()
			self.last_ping = now

	def _input(self, data):
		if "type" in data:
			print data['type']

	def getInstance(self):
		return self._slack