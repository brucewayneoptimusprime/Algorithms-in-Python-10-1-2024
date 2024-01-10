import random

def min_cut(graph):
    while len(graph) > 2:
        u, v = random_edge(graph)
        graph = contract(graph, u, v)
    
    return len(graph[0][1])

def random_edge(graph):
    u = random.choice(graph)
    v_label = random.choice(u[1])
    v = next(node for node in graph if node[0] == v_label)
    return u, v

def contract(graph, u, v):
    # Merge vertices u and v into a single vertex
    new_vertex = [u[0], u[1] + v[1]]
    
    # Create a copy of the graph before removing elements
    graph_copy = list(graph)
    
    graph_copy.remove(u)
    graph_copy.remove(v)
    
    for node in graph_copy:
        node[1] = [new_vertex[0] if x == u[0] or x == v[0] else x for x in node[1]]
    
    graph_copy.append(new_vertex)
    return graph_copy

def read_graph(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    graph = []
    for line in lines:
        parts = [int(x) for x in line.split() if x]
        graph.append([parts[0], parts[1:]])

    return graph

def main():
    graph = read_graph('E:/kmincut.txt')
    num_trials = 100  # You can adjust the number of trials based on the problem requirements

    min_cut_value = float('inf')
    for _ in range(num_trials):
        graph_copy = list(graph)
        cut = min_cut(graph_copy)
        min_cut_value = min(min_cut_value, cut)

    print(f"Minimum Cut: {min_cut_value}")

if __name__ == "__main__":
    main()
