from collections import defaultdict
#topological sort
class DFS:
	def __init__(self):
		self.vertex={}
		self.visit=[]
		#self.vdfs=[]
		self.stack=[]
	def input(self):					# for getting input such as edges
		print " enter total number of edges"
		edgeno=input()
		print "enter edge pair separated by space"
		tempvertex=defaultdict(list)
		for i in range(0,edgeno):
			a,b=raw_input().split()
			tempvertex[a].append(b)
		self.vertex=dict(tempvertex)
		
	def printer(self):					#function to print the result
		print "Adjscency list", self.vertex
		self.stack.reverse()
		print "topological sorted list", self.stack

	def dfsRun(self,start):				#main code for topological sort

		self.visit.append(start)
		#self.vdfs.append(start)
		if start in self.vertex.keys():
			ver=self.vertex[start]
			for i in ver:
				if i not in self.visit:
					self.dfsRun(i)
					self.stack.append(i)

				
dfs=DFS()								#object initialization
dfs.input()								#calling input function

print "where to start?"
a=raw_input()

dfs.dfsRun(a)
dfs.stack.append(a)

dfs.printer()

