# -*- encoding: utf-8 -*-

# ActorContainer will call actor's startup / shutdown according to app's life-cycle
class IStartup(object):
	def applicationStartup(self):
		raise NotImplementedError

	def applicationShutdown(self):
		raise NotImplementedError

