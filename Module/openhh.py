import zipfile
import shutil
import os
from PML import openfile



class OpenHH:
	def __init__(self, file_name, path):
		self.zip_ref = zipfile.ZipFile(file_name)
		self.zip_ref.extractall(path)
		self.path = path
	def installation(self):
		os.mkdir(self.path + "/Main/Image")
		os.mkdir(self.path + "/Main/Module")

		for x, xx, files in os.walk(self.path + "Image/"):
			for y in files:
				shutil.move(self.path + "Image/" + str(y), self.path + "/Main/Image/" + str(y))
		for x, xx, files in os.walk(self.path + "Module/"):
			for y in files:
				shutil.move(self.path + "Module/" + str(y), self.path + "/Main/Module/" + str(y))

		try:
			os.rmdir(self.path + "Module")
		except:
			shutil.rmtree(self.path + "Module")
		try:
			os.rmdir(self.path + "Image")
		except:
			shutil.rmtree(self.path + "Image")


class run:
	def __init__(self, path):
		files = openfile(path + "/run.pyl")
		text = files.read()

		if text["hh-v"] == "2.0":
			a = text["main"].split(".")
			file = open("run_file.py", "r+")
			file.write("from tkinter import *\nfrom sys import path\npath.append('Path/Main')\nfrom " + a[0] + " import main\n\n\nclass a:\n    def __init__(self, window):        main(window)")
			file.close()

	def run_file(self):
		import run_file

OpenHH("Path/Open.hh", "Path/").installation()
run("Path/").run_file()