import queue as Q
import time

def ucs(thing, start, goal):
    visited = {start: 0} 
    q = Q.PriorityQueue()
    q.put((0, start))
    path = {} 

    while not q.empty():
        cost, node = q.get()
        print("Exploring node:", node)
        print("Frontier nodes:", list(q.queue))
        print("Visited nodes:", list(visited.keys()))

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
        print("Path:", ' -> '.join(path))
        print("Cost:", cost)
    else:
        print("No path found.")

thing = {
    'Chicago': {'New York': 800, 'San Francisco': 2200},
    'Miami': {'New York': 1000, 'Dallas':1200},
    'New York': {'Chicago': 800, 'Miami': 1000, 'Boston': 250, 'Los Angeles': 3000, 'Dallas': 1500},
    'Boston': {'New York': 250},
    'Dallas': {'New York': 1500, 'Miami': 1200, 'Los Angeles': 1700},
    'San Francisco': {'Los Angeles': 500, 'Chicago': 2200},
    'Los Angeles': {'Dallas': 1700, 'New York': 3000, 'San Francisco': 500}
}


while True:
    start = input("Enter the start node (enter 0 to exit): ")
    if start == '0':
        break
    end = input("Enter the end node: ")

    if start not in thing or end not in thing:
        print("Invalid start or end node.")
        continue
    start_time = time.time()
    printPath(thing, start, end)
    end_time = time.time()
    execution_time = end_time - start_time
    print("Algorithm execution time:", execution_time)

