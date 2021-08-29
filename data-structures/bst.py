from node import Node 

class BST: 
	def __init__(self):
		self.root = None 
		self.size = 0 
	#Insert a node in the tree. Left < Root < Right
	#Nodes are unique.  
	def insert(self,node):
		if not self.root: 
			self.root = node 
		else: 
			finder = self.root
			while finder: 
				if finder == node: 
					return node 
				if finder > node: 
					if not finder.left: 
						#print(node,'inserted left of', finder.key)
						finder.left = node 
						node.parent = finder 
						break
					else: 
						finder = finder.left 
				if finder < node: 
					if not finder.right: 
						#print(node,'inserted right of', finder.key)
						finder.right = node 
						node.parent = finder 
						break 
					else: 
						finder = finder.right 
		self.size+=1 
		return node 

	def search(self,key,start=None):
		if start: 
			finder = start 
		else: 
			finder = self.root 
		parent = None 
		while finder: 
			if finder.key == key: 
				return finder,parent
			parent = finder
			if finder.key > key: 
				finder = finder.left 
			else:
				finder = finder.right 

	def resetpointer(self, parent,child,pointer):
		if parent.left == child:
			parent.left = pointer 
		else:
			parent.right = pointer 
	def smallestnode(self,node):
		finder = node 
		while finder: 
			if finder.left: 
				finder = finder.left
			else: 
				return finder 

	def delete(self,key,start=None):
		finder,parent = self.search(key,start)
		if not finder: 
			return False 

		if finder.isleaf():
			self.resetpointer(parent,finder,None)
			del finder 
			self.size-=1
			return True 
		elif not finder.left:
			self.resetpointer(parent,finder,finder.right)
			del finder 
			self.size-=1
			return True 
		elif not finder.right:
			self.resetpointer(parent,finder,finder.left)
			del finder 
			self.size-=1
			return True 
		else: 
			#Find the smallest in the left subtree
			smallest = self.smallestnode(finder.right) 
			
			finder.key = smallest.key 
			return self.delete(smallest,finder.right)

	def dft(self,node=None):
		if not node:
			return 
		self.dft(node.left)
		print(node) 
		self.dft(node.right)
		
	def bft(self,start=None):
		Q = [start]
		while Q: 
			node = Q.pop()
			print(node)
			if node.left:
				Q.insert(0,node.left)
			if node.right:
				Q.insert(0,node.right)


	def bfp(self,t,node=None):
		Q = []
		top = node 
		t.node(str(top),shape='doublecircle')
		i=0
		while top:
			if top.left:
				t.edge(str(top),str(top.left), color='blue')
				Q.append(top.left)
			if top.right:
				t.edge(str(top),str(top.right), color='red')
				Q.append(top.right)
			try:
				top = Q.pop(0)
			except Exception as e:
				break 		

	def __str__(self):
		if not self.root:
			return 'Empty'
		tree = '' 
		next_level = [self.root]
		#Find the next level below
		next_node = next_level.pop(0)
		while next_node: 
			tree += str(next_node)+'\n'
			if next_node.left:
				next_level.append(next_node.left)
			if next_node.right:
				next_level.append(next_node.right)
			try:
				next_node = next_level.pop(0)
			except Exception as ex: 
				break 
		return tree 