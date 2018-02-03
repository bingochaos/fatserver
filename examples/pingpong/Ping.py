# -*- encoding: utf-8 -*-
from fatkernel import Actor

class Ping(Actor):
	def __init__(self):
		super(Ping, self).__init__()
		self.value = 1

		# self.createTimer(self.sendPing, 5)
		self.createRepeatTimer(self.sendPing, 5, 10)
		
	def sendPing(self):
		pong = self.findActor('Pong')
		pong.callMethod('recvPing', (self.getMailbox(), self.value,))

	def recvPong(self, val):
		print 'recvPong', val

