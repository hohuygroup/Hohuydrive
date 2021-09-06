import zipfile
import shutil
import os
from PML import openfile
from sys import path


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
	def __init__(self, path, intermediate_file):
		self.intermediate_file = intermediate_file

		files = openfile(path + "/run.pyl")
		text = files.read()

		if text["hh-v"] == "2.0":
			a = text["main"].split(".")
			file = open(intermediate_file + "run file.py", "w")
			file.write("from tkinter import *\nfrom sys import path\npath.append('"+ path + "Main')\nfrom " + a[0] + " import main\n\n\nclass a:\n    def __init__(self, window):")
			file.write("main(window)")
			file.close()

	def run_file(self, window=None):
		path.append(self.filess)
		import run_file
		run_file.main(window)

# OpenHH("Path/Open.hh", "Path/").installation()
# run("Path/").run_file()