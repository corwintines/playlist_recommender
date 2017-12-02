# Some hand pickle methods I made for our project

import os
import pickle

def writeToPickle(object_to_write, out_pickle_filepath):
	try:
		with open(out_pickle_filepath, 'wb') as f:
			pickle.dump(object_to_write, f)
			print "...pickle dump successful."
	except OSError:
		print "Error saving as pickle. Check filepath."



def returnObjectFromPickle(in_pickle_filepath):
	if os.path.isfile(in_pickle_filepath):
		try:
			with open(in_pickle_filepath,'rb') as f:
				pickle_as_object = pickle.load(f)
				print "...pickle read successful."
				return pickle_as_object
		except OSError:
			print "Error reading object from pickle."
	else:
		print "Not a valid file at the path you specified: %s"%in_pickle_filepath