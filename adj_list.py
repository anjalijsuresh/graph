adj=dict()
keys=[]
print" Enter the no: of vertices"
v=input()
print" Enter the no: of edges"
e=input()
for i in range(1,v+1):
	keys.append(i)
adj={str(key):[] for key in keys}
for i in range(1,e+1):
	print "Enter the edges"
	v1=raw_input()
	v2=raw_input()
	adj[v1].append(v2)
	adj[v2].append(v1)
print adj
#for i in range(1,v+1):
#	print adj[str(i)]

	
