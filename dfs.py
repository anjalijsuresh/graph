def dfs(v):
	visited[v]=1
	print str(v) +" ",
	for ele in adj[v]:
		if visited[ele]!=1:
			dfs(ele)

adj=dict()
keys=[]
visited=dict()
print" Enter the no: of vertices"
v=input()
print" Enter the no: of edges"
e=input()

for i in range(1,v+1):
	keys.append(i)
adj={key:[] for key in keys}
visited={key:0 for key in keys}
print visited
for i in range(1,e+1):
	print "Enter the edges"
	v1=input()
	v2=input()
	adj[v1].append(v2)
	adj[v2].append(v1)
#print adj
print "Enter the starting node"
s=input()
print "DFS ",
dfs(s)


