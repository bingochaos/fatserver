# -*- encoding: utf-8 -*-
from fatkernel import Actor
from fatkernel.interface import IStartup

class GlobalStarter(Actor, IStartup):
	def __init__(self):
		super(GlobalStarter, self).__init__()

	def applicationStartup(self):
		print 'startup'
		#self.createActor('Ping')
		#self.createActor('Pong')

	def applicationShutdown(self):
		print 'shutdown'

