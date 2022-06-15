#!/usr/bin/env python

import numpy as np

def _ReadRadiances(filename, version):
	
	# Set version-dependent variables
	if (version == 1):
		
		line_start = '    var all_models = '
		y_start_str = '"y": ['
		y_end_str = ']'
		x_start_str = '"x": ['
		x_end_str = ']'
		
	elif (version == 2):
		
		line_start = '                var docs_json = '
		y_start_str = '"y":['
		y_end_str = ']'
		x_start_str = '"x":['
		x_end_str = ']'
		
	else:
	
		raise ValueError("Unknown version")

	# Open input file
	with open(filename, "r") as f:
	
		# Try to find line of interest
		found = False
		for line in f:
			if (line[:len(line_start)] == line_start):
				found = True
				break
		
	# Check whether the line of interest has been found
	if (found == False):
		
		# Not found, so raise an exception
		raise ValueError('Not a Modtran-Bokeh script')
	
	# Find "y" and "x" lists
	y_start = line.index(y_start_str) + len(y_start_str)
	y_end = line.index(y_end_str, y_start)
	x_start = line.index(x_start_str) + len(x_start_str)
	x_end = line.index(x_end_str, x_start)
	
	# Convert the string list to a numpy array
	wls = np.fromstring(line[x_start:x_end], sep=', ') * 1e3
	radiances_wl = np.fromstring(line[y_start:y_end], sep=', ')
	
	return (wls, radiances_wl)

def ReadRadiances(filename):

	"""Read radiances from MODTRAN web.
    
	Imports the spectral radiance calculated by MODTRAN Web, available at:
	http://modtran.spectral.com/modtran_home
	
	Procedure:
	 1) Open the above-mentioned URL in Firefox.
	 2) Fill in the web form and click "Run MODTRAN".
	 3) Right click over the radiance plot -> "Inspect element".
	 4) Navigate to "html > body > div.container-fluid > div.row > div.col-sm-7 > div.row > div#plot.col-xs-4 > script".
	 5) Save the script contents to disk (e.g., right click on the "script" section -> Copy -> Inner HTML).
	 6) Call this Python function, passing the path to the file that was saved in the previous step.
	
	Other browsers may be capable of obtaining the script contents using an equivalent procedure.
	
	Returns the spectral radiance [W/(m^2·m·sr)] as a function of wavelength [m].
	"""

	try:
		(wls, radiances_wl) = _ReadRadiances(filename, 2)
	except ValueError:
		(wls, radiances_wl) = _ReadRadiances(filename, 1)

	return (wls, radiances_wl)


def SaveRadiances(wls,radiances_wl):

	wls_c =np.array([wls])
	wls_c=wls.T
	radiances_c=np.array([radiances_wl])
	radiances_c=radiances_wl.T
	suma = np.stack((wls_c,radiances_c),axis=1)
	np.savetxt('MODTRAN.dat',suma,fmt='%.8f')
	#print(tamaño)
	return (wls, radiances_wl)

