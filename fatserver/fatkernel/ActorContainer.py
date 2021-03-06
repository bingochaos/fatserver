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

		self.mails      = []
		self.mailHandle = None

	def onSignal(self, handle, signum):
		print 'quit...'
		# [actor.shutdown() for actor in self.id2actor.itervalues()]
		# handle.close()
		self.loop.stop()

	def createActor(self, name, args = None):
		mod = __import__(name)
		clazz = getattr(mod, name, None)
		actor = clazz(args)
		actor.setContainer(self)

		self.id2actor[actor.getActorId()] = actor
		self.name2actor[name] = actor

		if isinstance(actor, IStartup):
			self.startupActors.append(actor)

		actor.startup()

	def findActorByName(self, name):
		return self.name2actor.get(name, None)

	def findActor(self, actorId):
		return self.id2actor.get(actorId, None)

	def createTimer(self, callback, timeout):
		return self.createRepeatTimer(callback, timeout, 0)

	def createRepeatTimer(self, callback, timeout, repeat):
		handle = pyuv.Timer(self.loop)
		handle.start(callback, timeout, repeat)
		return handle

	def callMethod(self, actorId, func, args):
		#print '[ActorContainer] callMethod', actorId, func
		#print '[ActorContainer] callMethod.mailTimer', self.mailHandle
		self.mails.append((actorId, func, args))
		if self.mailHandle is None:
			self.mailHandle = pyuv.Idle(self.loop)
			self.mailHandle.start(self.callMethodInternal)

	def callMethodInternal(self, handle):
		self.mailHandle.stop()
		self.mailHandle = None
		for mail in self.mails:
			actorId, func, args = mail
			actor = self.findActor(actorId)
			if actor and getattr(actor, func, None):
				fn = getattr(actor, func, None)
				try:
					fn(*args)
				except:
					print '[ActorContainer] callMethodInternal error', fn, args
		self.mails = []

	def run(self):
		for actor in self.startupActors:
			actor.applicationStartup()

		# event loop
		print 'container running'
		self.loop.run()

		for actor in self.startupActors:
			actor.applicationShutdown()


