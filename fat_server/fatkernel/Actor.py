# -*- encoding: utf-8 -*-

class Actor(object):
	actorIdGlobal = 1	

	def __init__(self, args):
		self.actorId = self.actorIdGlobal
		self.actorIdGlobal += 1

		self.container = None

	# ----- internal method -----
	def getActorId(self):
		return self.actorId

	def setContainer(self, container):
		self.container = container

	def shutdown(self):
		print self.__class__.__name__, 'shutdown'
		self.__dict__.clear()

	# ----- public method -----
	def createActor(self, name, args = None):
		self.container.createActor(name, args)

