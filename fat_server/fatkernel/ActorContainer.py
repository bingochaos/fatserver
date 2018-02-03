# -*- encoding: utf-8 -*-

import pyuv
import signal
from .interface import IStartup

class ActorContainer(object):
	def __init__(self):
		self.loop = pyuv.Loop.default_loop()
		handle = pyuv.Signal(self.loop)
		handle.start(self.onSignal, signal.SIGINT)
		
		self.id2actor   = {}
		self.name2actor = {}
		self.startupActors = []

	def onSignal(self, handle, signum):
		print 'quit...'
		[actor.shutdown() for actor in self.id2actor.itervalues()]
		handle.close()

	def createActor(self, name, args = None):
		mod = __import__(name)
		clazz = getattr(mod, name, None)
		actor = clazz(args)
		actor.setContainer(self)

		self.id2actor[actor.getActorId()] = actor
		self.name2actor[name] = actor

		if isinstance(actor, IStartup):
			self.startupActors.append(actor)

	def findActorByName(self, name):
		return self.name2actor.get(name, None)

	def findActor(self, actorId):
		return self.id2actor.get(actorId, None)

	def run(self):
		for actor in self.startupActors:
			actor.applicationStartup()

		# event loop
		print 'container running'
		self.loop.run()

		for actor in self.startupActors:
			actor.applicationShutdown()


