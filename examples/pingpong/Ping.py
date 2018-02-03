# -*- encoding: utf-8 -*-
import time
from fatkernel import Actor

class Ping(Actor):
	def __init__(self, args):
		super(Ping, self).__init__(args)
		self.value = args['initvalue']
		print '[Ping] init', self.value

	def startup(self):
		super(Ping, self).startup()
		# self.createTimer(self.sendPing, 5)
		self.createRepeatTimer(self.sendPing, 1, 10)
		
	def sendPing(self, handle):
		print '[Ping] send ping', time.strftime('%H:%M:%S')
		pong = self.findActorByName('Pong')
		pong.mailbox().callMethod('recvPing', self.mailbox(), self.value)

	def recvPong(self, val):
		print '[Ping] recv pong', val
		self.value = val

	def voidArgCall(self):
		print '[Ping] voidArgCall'

