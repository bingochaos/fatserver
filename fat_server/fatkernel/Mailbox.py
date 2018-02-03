# -*- encoding: utf-8 -*-

class Mailbox(object):
	def __init__(self, container, actorId):
		self.container = container
		self.actorId   = actorId

	def callMethod(self, func, *args):
		self.container.callMethod(self.actorId, func, args)

