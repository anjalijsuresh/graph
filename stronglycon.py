def big(num):
	s1=0
	for key in keys:
		if num[key]>s1:
			s=key
                        s1=num[key]
	return s
def dfs2(v):
	global lis
	visited[v]=1
        keys.remove(v)
        lis.append(v)
	for w in adj2[v]:
		if visited[w]!=1:
                        dfs2(w)
		
def dfs(v):
	global count
	visited[v]=1
	keys.remove(v)
        for w in adj[v]:
		if visited[w]!=1:
			dfs(w)
                        count=count+1
                        num[w]=count
                        
	num[v]=count+1
adj=dict()
adj2=dict()
keys=[]
lis=[]
visited=dict()
num=dict()
print" Enter the no: of vertices"
v=input()
print" Enter the no: of edges"
e=input()
count=0
for i in range(1,v+1):
	keys.append(i)
adj={key:[] for key in keys}
adj2={key:[] for key in keys}
visited={key:0 for key in keys}
num={key:0 for key in keys}
for i in range(1,e+1):
	print "Enter the edges"
	v1=input()
	v2=input()
	adj[v1].append(v2)
	adj2[v2].append(v1)
print "Enter the starting node"
s=input()
print "DFS ",
dfs(s)
if len(keys)!=0:
        count=count+1
        dfs(keys[0])
for i in range(1,v+1):
	keys.append(i)
#num[s]=count
visited={key:0 for key in keys}
s=big(num)
while len(keys)!=0:
	s=big(num)
        dfs2(s)	
        print lis
        lis=[]
