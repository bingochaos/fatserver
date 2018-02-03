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

	# ----- override method -----
	def startup(self):
		print self.__class__.__name__, 'startup'

	def shutdown(self):
		print self.__class__.__name__, 'shutdown'
		self.__dict__.clear()

	# ----- public method -----
	def createActor(self, name, args = None):
		self.container.createActor(name, args)

	def createTimer(self, callback, timeout):
		return self.container.createTimer(callback, timeout)

	def createRepeatTimer(self, callback, timeout, repeat):
		return self.container.createRepeatTimer(callback, timeout, repeat)

