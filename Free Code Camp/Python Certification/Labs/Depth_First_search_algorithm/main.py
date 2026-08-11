def dfs(matrix, starting_node):
    number_of_nodes = len(matrix)
    visited = [False] * number_of_nodes
    reachable_nodes = []

    def sfs_visit(current_node):
        if not visited[current_node]:
            visited[current_node] = True
            reachable_nodes.append(current_node)
        
        for neighbor, conection in enumerate(matrix[current_node]):

            if conection == 1 and not visited[neighbor]:
                sfs_visit(neighbor)

            else:
                continue
        
    sfs_visit(starting_node)
    return reachable_nodes