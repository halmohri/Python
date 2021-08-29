from math import floor
class Heap:
	def __init__(self):
		self.A = [] 

	def heapify(self,L):
		for x in L: 
			self.insert(x) 

	def insert(self,data):
		self.A.append(data)
		i = len(self.A)-1
		pi = floor((i-1)/2)
		while pi >= 0: 
			if self.A[pi] > self.A[i]: 
				break 
			self.A[pi],self.A[i]=self.A[i],self.A[pi]
			i = pi 
			pi = floor((i-1)/2)

	def pop(self): 
		deleted = self.A[0]
		self.A[0] = self.A[-1]
		del self.A[-1]
		self.max_heapify()
		return deleted

	def max_heapify(self):
		deleted = self.A[0]
		self.A[0] = self.A[-1]
		del self.A[-1]
		i = 0 
		l = 2*i+1 
		r = 2*i+2
		if len(self.A)==2: 
			if self.A[i] < self.A[l]: 
				self.A[l],self.A[i]=self.A[i],self.A[l]
				return deleted
		while r < len(self.A):
			if self.A[i] > self.A[l] and self.A[i] > self.A[r]: 
				break 
			c = r
			if self.A[l]>=self.A[r]: 
				c = l 
			self.A[c],self.A[i]=self.A[i],self.A[c]
			i = c
			l = 2*i+1 
			r = 2*i+2
		return deleted 
