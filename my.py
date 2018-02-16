#!/usr/bin/env python3
class sadnn(object):
	def __init__(self, name, age):
		self.__name = name
		self.__age = age
	def getData(self, main):
		if main == "name":
			return __name
		elif main == "age":
			return __age
		else:
			raise ValueError("the main is by zero")
	def setData(self, newname, newage):
		newname = self.__name
		newage = self.__age
k = sadnn("", 0)
f = str(input("Plase enter you name:"))
fk = int(input("Plase enter you age:"))
k.setData(f, fk)
file = open("~/tmp.txt")
file.read()
file.write(k.getData("name")k.getData("age"))
file.close()
