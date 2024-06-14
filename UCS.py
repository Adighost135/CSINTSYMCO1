import queue as Q

def ucs(thing, start, goal):
    visited = {start: 0} 
    q = Q.PriorityQueue()
    q.put((0, start))
    path = {} 

    while not q.empty():
        cost, node = q.get()
        print("Current Node:", node)
        print("Frontier:", list(q.queue))  # Print the queue

        if node == goal:
            break

        if cost > visited[node]:
            continue

        for i in thing[node]:
            total_cost = cost + thing[node][i]
            if i not in visited or total_cost < visited[i]:
                visited[i] = total_cost
                q.put((total_cost, i))
                path[i] = node

        print("Visited:", visited)  # Print the visited nodes

    if goal not in visited:
        return None, None, list(q.queue), visited
    
    shortest_path = []
    nodeRN = goal
    while nodeRN != start:
        shortest_path.append(nodeRN)
        nodeRN = path[nodeRN]
    shortest_path.append(start)
    shortest_path.reverse()

    return visited[goal], shortest_path, list(q.queue), visited

def printPath(thing, start, goal):
    cost, path, queue, visited = ucs(thing, start, goal)
    if cost is not None:
        print("Cost:", cost)
        print("Path:", ' -> '.join(path))
    else:
        print("No path found.")

thing = {
    'Chicago': {'New York': 800, 'San Francisco': 2200},
    'Miami': {'New York': 1000, 'Dallas':1200},
    'New York': {'Chicago': 800, 'Miami': 1000, 'Boston': 250, 'Los Angeles': 3000},
    'Boston': {'New York': 250},
    'Dallas': {'New York': 1500, 'Miami': 1200, 'Los Angeles': 1700},
    'San Francisco': {'Los Angeles': 500, 'Chicago': 2200},
    'Los Angeles': {'Dallas': 1700, 'New York': 3000, 'San Francisco': 500}
}

printPath(thing, 'Boston', 'Los Angeles')
