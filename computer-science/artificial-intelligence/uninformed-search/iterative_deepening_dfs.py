def dls(graph, node, goal, depth, path, visited):
    path.append(node)
    if node == goal:
        return path
    if depth <= 0:
        path.pop()
        return None

    visited.add(node)
    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            result = dls(graph, neighbor, goal, depth - 1, path, visited)
            if result:
                return result

    path.pop()
    visited.remove(node)
    return None

def iddfs(graph, start, goal, max_depth):
    for limit in range(max_depth + 1):
        result = dls(graph, start, goal, limit, [], set())
        if result:
            return result
    return None

tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H'],
    'E': [],
    'F': ['I'],
    'G': [],
    'H': [],
    'I': []
}

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H', 'A'],
    'E': [],
    'F': ['I'],
    'G': [],
    'H': [],
    'I': []
}

print(f"Tree search result: {iddfs(tree, 'A', 'I', 3)}")
print(f"Graph search result: {iddfs(graph, 'A', 'I', 3)}")
