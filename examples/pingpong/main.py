# -*- encoding: utf-8 -*-
from fatkernel import ActorContainer

def main():
	ac = ActorContainer()
	ac.createActor('GlobalStarter')
	ac.run()

if __name__ == '__main__':
	main()

