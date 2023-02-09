from queue import Queue

# The DFS Algorithm

def dfs(MAZE, position, visited, adj_list):

    visited.append(position)

    children = [] # used to collect all child nodes
    routes = ['U','D','L','R'] # up down left right
    
    for route in routes:
        intersection = False # check if a potential move can happen

        # check for all possible locations
        if route == 'U': 
            for next in MAZE:
                x_coord = next[0]
                y_coord = next[1]
                next_position = (position[0], position[1] - 50)
                if next_position[0] > x_coord[0] and next_position[0] < y_coord[0] and next_position[1] == x_coord[1] and next_position[1] == y_coord[1]:
                    intersection = True

            if intersection == False:    
                new_position = (position[0], position[1] - 100)
                children.append(new_position)
                if new_position not in visited:
                    dfs(MAZE, new_position, visited, adj_list)

        elif route == 'D':
            for next in MAZE:
                x_coord = next[0]
                y_coord = next[1]
                next_position = (position[0], position[1] + 50)
                if next_position[0] > x_coord[0] and next_position[0] < y_coord[0] and next_position[1] == x_coord[1] and next_position[1] == y_coord[1]:
                    intersection = True
                
            if intersection == False:
                new_position = (position[0], position[1] + 100)
                children.append(new_position)
                if new_position not in visited:
                    dfs(MAZE, new_position, visited, adj_list)

        elif route == 'L':
            for next in MAZE:
                x_coord = next[0]
                y_coord = next[1]
                next_position = (position[0] - 50, position[1])
                if next_position[1] > x_coord[1] and next_position[1] < y_coord[1] and next_position[0] == x_coord[0] and next_position[0] == y_coord[0]:
                    intersection = True
                
            if intersection == False:
                new_position = (position[0] - 100, position[1])
                children.append(new_position)
                if new_position not in visited:
                    dfs(MAZE, new_position, visited, adj_list)
        
        elif route == 'R':
            for next in MAZE:
                x_coord = next[0]
                y_coord = next[1]
                next_position = (position[0] + 50, position[1])
                if next_position[1] > x_coord[1] and next_position[1] < y_coord[1] and next_position[0] == x_coord[0] and next_position[0] == y_coord[0]:
                    intersection = True
                
            if intersection == False:
                new_position = (position[0] + 100, position[1])
                children.append(new_position)
                if new_position not in visited:
                    dfs(MAZE, new_position, visited, adj_list)
    
    if len(children) > 0:
        adj_list[position] = children

# The BFS Algorithm

def bfs(graph, start, end):
    visited = {}
    parent = {}

    queue = Queue()

    for node in graph.keys():
        visited[node] = False
        parent[node] = None

    visited[start] = True
    queue.put(start)

    while not queue.empty():
        u = queue.get()

        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                queue.put(v)

    path = []
    while end is not None:
        path.append(end)
        end = parent[end]

    path.reverse()

    return path


if __name__ == '__main__':
    MAZE = [
        ((100,100), (600,100)), ((100,100), (100,600)), 
        ((100,600), (600,600)), ((100,200), (300,200)), 
        ((300,200), (300,300)), ((300,300), (500,300)), 
        ((400,100), (400,200)), ((400,200), (500,200)), 
        ((100,400), (200,400)), ((200,300), (200,400)), 
        ((300,400), (300,500)), ((300,400), (400,400)), 
        ((200,500), (500,500)), ((500,400), (500,500)),
        ((400,500), (400,600)), ((600,100), (600,600))
        ]

    visited = [] # all locations visited
    position = (350, 550) # start position
    destination = (350,150) # end goal
    adj_list = {} # used to generate the node graph

    dfs(MAZE, position, visited, adj_list) # search all possible locations
    print('visited:', visited, len(visited),'\n') # all locations generated
    print('Graph:')
    for item in adj_list.items():
        print(item)
    print('')
    shortest_path = bfs(adj_list, position, destination) # find the shortest path
    print('Shortest Path:',shortest_path, len(shortest_path))