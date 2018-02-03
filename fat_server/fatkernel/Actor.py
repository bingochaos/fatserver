# -*- encoding: utf-8 -*-

class Actor(object):
	actorIdGlobal = 1	

	def __init__(self, args):
		self.actorId = self.actorIdGlobal
		self.actorIdGlobal += 1

	def getActorId(self):
		return self.actorId

