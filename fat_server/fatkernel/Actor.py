# -*- encoding: utf-8 -*-

from .Mailbox import Mailbox

# TODO
actorIdGlobal = 1

class Actor(object):

	def __init__(self, args):
		global actorIdGlobal

		self.actorId = actorIdGlobal
		actorIdGlobal += 1

		self.container = None

	# ----- internal method -----
	def getActorId(self):
		return self.actorId

	def setContainer(self, container):
		self.container = container

	# ----- override method -----
	def startup(self):
		print self.__class__.__name__, 'startup actorId =', self.getActorId()

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

	def findActorByName(self, name):
		return self.container.findActorByName(name)

	def mailbox(self):
		return Mailbox(self.container, self.actorId)

