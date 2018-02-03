# -*- encoding: utf-8 -*-
from fatkernel import Actor
from fatkernel.interface import IStartup

class GlobalStarter(Actor, IStartup):
	def __init__(self, args):
		super(GlobalStarter, self).__init__(args)

	def applicationStartup(self):
		print 'startup'
		self.createActor('Ping', {'initvalue': 10})
		self.createActor('Pong')

	def applicationShutdown(self):
		print 'shutdown'

