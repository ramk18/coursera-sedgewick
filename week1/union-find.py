class quickFind(object):

	def __init__(self):
		self.data = []
		for x in range(10):
			self.data.append(x)
	
	def find(self,p,q):
		return  self.data[p] == self.data[q]
		
	def union(self,p,q):
		p = self.data[p]
		q = self.data[q]
		for x in range(len(self.data)):
			if self.data[x] == p:
				self.data[x] = q


class quickUnion(object):
	def __init__(self):
		self.data = []
		
		for x in range(10):
			self.data.append(x)


	def root(self,p):
		while p != self.data[p]:
			p = self.data[p]
		return p 

	def find(self,p,q):
		return self.root(p) == self.root(q)
		
		
	def union(self,p,q):
		p = self.root(p)
		q = self.root(q)
		self.data[p] = q




class weightedQuickUnion(object):
	def __init__(self):
		self.data = []
		self.sz = []
		for x in range(10):
			self.data.append(x)
			self.sz.append(0)

	def root(self,p):
		while p != self.data[p]:
			p = self.data[p]
		return p 

	def find(self,p,q):
		return self.root(p) == self.root(q)
		
		
	def union(self,p,q):
		p = self.root(p)
		q = self.root(q)
		if p == q:
			return
		if(self.sz[p] < self.sz[q]):
			self.data[p] = q
			self.sz[q] += self.sz[p]
		else:
			self.data[q] = p
			self.sz[p] += self.sz[q]


class weightedQuickUnionPathCompression(object):
	def __init__(self):
		self.data = []
		self.sz = []
		for x in range(10):
			self.data.append(x)
			self.sz.append(0)

	def root(self,p):
		while p != self.data[p]:
			self.data[p] = self.data[self.data[p]]
			p = self.data[p]
		return p 

	def find(self,p,q):
		return self.root(p) == self.root(q)
		
		
	def union(self,p,q):
		p = self.root(p)
		q = self.root(q)
		if p == q:
			return
		if(self.sz[p] < self.sz[q]):
			self.data[p] = q
			self.sz[q] += self.sz[p]
		else:
			self.data[q] = p
			self.sz[p] += self.sz[q]


c = quickFind()
c.union(0,1)
c.union(2,4)



d = quickUnion()
d.union(4,3)
d.union(3,8)


		

e = weightedQuickUnion()
e.union(4,3)
e.union(3,8)





	


		


		