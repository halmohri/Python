from list import List
from node import Node 

class HashTable:
	def __init__(self,M=1999):
		self.M = M
		self.table = []
		for i in range(M):
			self.table.append(Node('$'))
	def hash(self,k):
		return k%self.M
	def insert(self,k):
		h = self.hash(k)
		if self.table[h] == '$': 
			self.table[h].key = k 
		else: 
			finder = self.table[h] 
			while finder.next: 
				finder = finder.next
			finder.next = Node(k)
		return h 
	def delete(self,k):
		h = self.hash(k)
		finder = self.table[h] 
		prev   = finder 
		while finder:
			if finder.key == k: 
				if finder == prev: 
					self.table[h] = Node('$') 
				elif not finder.next: 
					prev.next = None 
					del finder
					break 
				else:
					prev.next = finder.next 
					del finder 
					break 
			prev = finder 
			finder = finder.next


	def search(self,k):
		h = self.hash(k)
		finder = self.table[h] 
		while finder: 
			if finder.key == k: 
				return True 
			finder = finder.next 
		return False  
	def __str__(self):
		s = ''
		for i in range(self.M):
			node = self.table[i] 
			if node != '$':
				s += str(i)+' '+str(node)+'->'
				while node.next: 
					s+= str(node.next)+'->'
					node = node.next
				s+='\n'
		return s