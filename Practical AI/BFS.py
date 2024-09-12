graph={
    'A':['B','C'],
    'B':['D','E'],
    'C':['F','G'],
    'D':[],
    'E':[],
    'F':[],
    'G':[]
    }
visited=[]
queue=[]
node='A'

visited.append(node)
queue.append(node)

while queue:
    s=queue.pop(0)
    print(s,end=" ")
    for n in graph[s]:
        if n not in visited:
            visited.append(n)
            queue.append(n)
