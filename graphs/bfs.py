def bfs(graph, source):
    from collections import deque
    queue = deque(source) 
    while len(queue) > 0:
        current = queue.popleft()
        print(current)
        for key in graph[current]:
            queue.append(key)

def bfs(graph, source):
    from collections import deque
    queue = deque(source) 
    current = queue.popleft()
    print(current)
    for key in graph[current]:
        bfs(graph,key)
    
            
 
bfs(graph,'a')
