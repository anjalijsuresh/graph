def min(a,b):
	if a>b:
		return b
	else:
		return a
def dfs(v):
	global counter
	dfsnum[v] = counter
	visited[v]=1
	color[v]="GREY"
	low[v]=dfsnum[v]
	counter=counter+1
	for w in adj[v]:
		if visited[w] !=1:
			print "Tree edge "+str(v)+" "+str(w)
			parent[w]=v
			dfs(w)
			color[w]="BLACK"
			#if (low[w]>=dfsnum[v]): 
			#	print str(v)+" articulation point"
			low[v]=min(low[v],low[w])	#if child has low number give it to the parent
		elif parent[v]!=w:
			if dfsnum[v]<dfsnum[w]:
				print "Forward edge "+str(v)+" "+str(w)
			else:
				if color[w]=="BLACK":
					print "Cross edge "+str(v)+" "+str(w)
				else:
					print "Back edge "+str(v)+" "+str(w)
			low[v]=min(low[v],dfsnum[w])

adj=dict()
keys=[]
counter=1
visited=dict()
dfsnum=dict()
low=dict()
color=dict()
parent=dict()
print "Enter the no:of vertices"
v=input()
print "Enter the no: of edges"
e=input()
for i in range(1,v+1):
	keys.append(i)
adj={key:[] for key in keys}
visited={key:0 for key in keys}
dfsnum={key:0 for key in keys}
parent={key:0 for key in keys}
low={key:0 for key in keys}
low={key:"WHITE" for key in keys}
for i in range(1,e+1):
	print "Enter the edge"
	v1=input()
	v2=input()
	adj[v1].append(v2)
	
print "Enter the starting node"
s=input()
dfs(s)

