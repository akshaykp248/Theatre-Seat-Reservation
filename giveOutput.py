import os
def generateOutput(seats, path):
	outF = open(path, 'w')
	outF.writelines(["%s\n" % i for i in seats])
	print("Output generated at: ", path)
