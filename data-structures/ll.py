from node import Node 

class List:
	def __init__(self):
		self.head = None 
		self.tail = None 
	#Insert at the beginning of the list
	def insertf(self,node):
		if not isinstance(node,Node):
			raise Exception('Cannot add a non-Node object')
		if self.head == None: 
			self.head = node 
			self.tail = self.head
		else: 
			node.next = self.head 
			self.head = node 
	#Insert at the end of the list
	def insertl(self,node):
		if not isinstance(node,Node):
			raise Exception('Cannot add a non-Node object')
		if self.head == None: 
			self.head = node 
			self.tail = self.head
		else: 
			self.tail.next = node 
			self.tail = node 

	#Delete the first occurrence of data
	def delete(self,data):
		#Find the node first
		finder = self.head
		prev = finder 
		while finder: 
			if finder.key ==  data: 
				if finder == prev: 
					self.head = finder.next 
					del finder  
				else: 
					prev.next = finder.next 
					if finder == self.tail: 
						self.tail = prev 
					del finder 
				return True 
			prev = finder
			finder = finder.next 
		return False   


	def search(self,data):
		finder = self.head
		while finder: 
			if finder.key ==  data: 
				return finder
			finder = finder.next  
		return None 

	def length(self):
		l = 0 
		finder = self.head
		while finder:
			finder = finder.next
			l+=1 
		return l 

	def __str__(self):
		finder = self.head 
		m = ''
		while finder: 
			m+= str(finder.key)+'->'
			finder = finder.next 
		m+= 'X'
		return m 