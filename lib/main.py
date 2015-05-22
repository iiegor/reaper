__author__ = 'Iegor Azuaga, iegorazuaga@googlemail.com'

import reaper
import sys

if __name__ == '__main__':
	reaper = reaper.Reaper(sys.argv)

	if "--cl" in sys.argv:
		"""
		Command line start
		"""
		reaper.cl_start()
	elif "--raspberry" in sys.argv:
		"""
		Raspberry PI
		"""
		reaper.rpi_start()
	else:
		print u'The bootstrap argument is not supported.'
		sys.exit(0)

	del reaper