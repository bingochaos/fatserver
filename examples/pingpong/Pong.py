# -*- encoding: utf-8 -*-
from fatkernel import Actor

class Pong(Actor):
	def __init__(self, args):
		super(Pong, self).__init__(args)

	def recvPing(self, sender, val):
		print '[Pong] recv ping', sender.actorId, val
		sender.callMethod('recvPong', val+1)
		sender.callMethod('voidArgCall')

