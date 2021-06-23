graph = {"A":["D","C","B"],
"B":["E"],
"C":["G","F"],
"D":["H"],
"E":["I"],
"F":["J"]}

#non recursive method

def dfs_nonrecursive(graph,source):
    if source is None or source not in graph:
        return "Invalid Input"
    path = []
    stack = [source]
    while (len(stack)!=0):
        s = stack.pop()
        if s not in path:
            path.append(s)
        if s not in graph:
            #leaf node
            continue
        for neighbor in graph[s]:
            stack.append(neighbor)
    return " ".join(path)

DFS_path = dfs_nonrecursive(graph,"A")
print(DFS_path)

def recursive_dfs(graph, source,path = []):
    if source not in path:
        path.append(source)

        if source not in graph:
            # leaf node, backtrack
            return path

        for neighbour in graph[source]:
            path = recursive_dfs(graph, neighbour, path)
    return path

path = recursive_dfs(graph,"A")
print(" ".join(path))
