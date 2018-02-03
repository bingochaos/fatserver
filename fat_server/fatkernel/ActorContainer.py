# -*- encoding: utf-8 -*-

class ActorContainer(object):
	def __init__(self):
		pass

	def createActor(self, name, args = None):
		mod = __import__(name)
		import sys
		print mod
		print sys.modules[name]

	def findSingletonActor(self, name):
		pass

	def findActor(self, actorId):
		pass

	def run(self):
		print 'run'

