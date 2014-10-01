#!/usr/bin/python
class node:
	children=[]
	value=""
	def __init__(self,value):
		self.value=value

	def add(self,child):
		self.children.append(child)

	def output(self):
		print self.value
		print len(self.children)
		for i in range(len(self.children)):
			self.children[i].output()

test=node("heading 1")
new=node("child1")
test.add(new)
new=node("child2")
test.add(new)
new=node("child3")
test.add(new)

test.output()
