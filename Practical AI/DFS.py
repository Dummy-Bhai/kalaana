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
stack=['A']

while(len(stack)!=0):
    s=stack.pop()
    if s not in visited:
        visited.append(s)
        for n in graph[s]:
            stack.append(n)
print(visited)
