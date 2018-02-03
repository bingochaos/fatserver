# -*- encoding: utf-8 -*-
from fatkernel import Actor

class Ping(Actor):
	def __init__(self, args):
		super(Ping, self).__init__(args)
		self.value = args['initvalue']
		print 'Ping.__init__', self.value

		# self.createTimer(self.sendPing, 5)
		# self.createRepeatTimer(self.sendPing, 5, 10)
		
	def sendPing(self):
		pong = self.findActorByName('Pong')
		pong.callMethod('recvPing', (self.getMailbox(), self.value,))

	def recvPong(self, val):
		print 'recvPong', val

