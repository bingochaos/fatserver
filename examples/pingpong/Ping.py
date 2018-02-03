# -*- encoding: utf-8 -*-
import time
from fatkernel import Actor

class Ping(Actor):
	def __init__(self, args):
		super(Ping, self).__init__(args)
		self.value = args['initvalue']
		print 'Ping.__init__', self.value

	def startup(self):
		super(Ping, self).startup()
		# self.createTimer(self.sendPing, 5)
		self.createRepeatTimer(self.sendPing, 5, 10)
		
	def sendPing(self, handle):
		print time.strftime('%H:%M:%S'), 'sendPing'
		# pong = self.findActorByName('Pong')
		# pong.callMethod('recvPing', (self.getMailbox(), self.value,))

	def recvPong(self, val):
		print 'recvPong', val

