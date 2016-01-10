import os

def run(**args):
	print "[*] in dirlister moduled."
	files = os.listerdir(".")

	return str(files)
