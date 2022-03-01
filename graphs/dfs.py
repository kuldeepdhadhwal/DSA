graph = {
    'a' : ['c','b'],
    'b' : ['d'],
    'c' : ['e'],
    'd' : ['f'],
    'e' : [],
    'f' : []
}

def dfs(graph,source):
    stack = [source]
    while len(stack) > 0:
        current = stack.pop()
        print(current)
        for key in graph[current]:
            stack.append(key)

def dfs(graph,source):
    # recursion
    stack = [source]
    for key in graph[source]:
        print(key)
        dfs(graph,key)

y = dfs(graph,'a')
print(y)
