import os

class openfile:
	def __init__(self, name_file):
		self.name_file = name_file
		try:
			self.file = open(name_file, "r+")
		except:
			print("Error")

		
	def read(self):
		self.pml = {}
		
		ah = self.file.read().split("\n")

		for y in ah:
			try:
				if y[0] == "#":
					ah.remove(y)
			except:
				pass

		for x in ah:
			a = x.split("=")
			self.pml[a[0]] = a[-1]
		return self.pml

	def write(self, value, text):
		text_file = str(self.file.read())
		file = open(self.name_file, "w")
		file.write(text_file)
		txt = value + "=" + text + "\n"
		file.write(txt)

	def delete(self):
		os.remove(self.name_file)
	
	def close(self):
		self.file.close()

class search:
	def __init__(self, read, *search):
		self.read = read
		self.search = search
		self.run = []

		self.a()

	def a(self):
		for x in self.read:
			for y in self.search:
				if x == y:
					self.run.append(x)

	def return_search(self):
		return self.run
def name(name_file):
	name_1 = str(name_file).split("/")
	name = name_1[-1].split(".")
	return name[0]