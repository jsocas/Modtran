#!/usr/bin/env python

import sys
import modtran_io

if __name__ == '__main__':

	# Check correct usage
	if (len(sys.argv) != 2):
		print("Usage: " + sys.argv[0] + " filename")
		sys.exit(-1)

	filename = sys.argv[1]
	
	(wls, radiances_wl) = modtran_io.ReadRadiances(filename)
	
	print(wls)
	print(type(wls))
	print(radiances_wl)
	print(type(radiances_wl))
	modtran_io.SaveRadiances(wls,radiances_wl)
	print('Proceso FINALIZADO. Fichero de salida:MODTRAN.txt')