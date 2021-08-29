import math,random
from heap import Heap 

class SortAlgs:
	def __init__(self):
		pass

	#Worst case O(len(M)**2)
	def insertionsort(self,M):
		for j in range(1,len(M)):
			key = M[j] 
			i=j-1 
			while i>-1 and M[i] > key: 
				M[i+1] = M[i] 
				i-=1 
			M[i+1] = key 
		return M 

	#Worst case O(len(M)**2)
	def selectionsort(self,M):
		for i in range(len(M)):
			maxv=M[0]
			maxi=0
			for j in range(len(M)):
				if M[j]>maxv:
					maxv=M[j]
					maxi=j
			M[i],M[maxi]=M[maxi],M[i]
		return M
		
	def mergesort(self,M):
		def merge(L,R):
			n=len(L)
			m=len(R)
			if m==1 and n==1:
				if L[0]<R[0]:
					return R+L
				else:
					return L+R			
			i,j = 0,0 
			S = []
			while i < len(L) and j < len(R):
				if L[i] > R[j]: 
					S.append(L[i])
					i+=1 
				else: 
					S.append(R[j])
					j+=1 
			while i < len(L):
				S.append(L[i])
				i+=1 
			while j < len(R):
				S.append(R[j])
				j+=1 
			return S 
		
		def split(M):
			N=len(M)
			if N==1:
				return M
			else:
				end=math.ceil(N/2)
				L=split(M[:end])
				R=split(M[end:])
				return merge(L,R)
			
		return split(M)

	def quicksort(self,M): 
		def parition(M,i):
			pivot = M[i]  
			S=[pivot]
			k=0
			for j in range(len(M)):
				if j==i:
					continue   
				if M[j] >= pivot: 
					S.insert(0,M[j])
					k+=1 
				else:
					S.append(M[j]) 
			return S,k		
		if len(M)<=1:
			return M 
		i = random.randint(0,len(M)-1)
		pivot = M[i]
		S,i = parition(M,i)
		L = self.quicksort(S[:i])
		R = self.quicksort(S[i:])
		return L+R 

	def heapsort(self,M):
		HP = Heap()
		HP.heapify(M) 
		size = len(M)
		S = []
		for i in range(size):
			S.append(HP.max_heapify())
		return S
		
	def sort(self,L=[],keyindex=None,alg='merge'):
		if not isinstance(L,list):
			raise Exception('I can only expect a list here.')
		if len(L) <=1:
			return L
		M=L
		if keyindex:
			#assume an indirect list of numbers.
			M=[x[keyindex] for x in L]
		if alg=='selection':
			M= self.selectionsort(M)
		elif alg=='merge':
			M= self.mergesort(M)
		elif alg=='insertion':
			M=self.insertionsort(M)	
		elif alg=='quick':
			M=self.quicksort(M)
		elif alg=='heap':
			M=self.heapsort(M)	
		return M