import os

def run(**args):
	print "[*] in env module."
	return str(os.environ)
