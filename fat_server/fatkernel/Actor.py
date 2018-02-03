# -*- encoding: utf-8 -*-

class Actor(object):
	actorIdGlobal = 1	

	def __init__(self):
		self.actorId = self.actorIdGlobal
		self.actorIdGlobal += 1

