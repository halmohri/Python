class Node:
	def __init__(self,d,nnode=None):
		self.next = nnode 
		self.prev = None 
		self.key = d   
	def __str__(self):
		return str(self.key)
	def __gt__(self, key):
		return self.key > key
	def __lt__(self, key):
		return self.key < key
	def __eq__(self, key):
		return self.key == key