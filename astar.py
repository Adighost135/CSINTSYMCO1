from queue import PriorityQueue
import time

def astar(graph, start, goal, heuristic):
    queue = PriorityQueue()
    queue.put((0, start))
    distances = {start: 0}
    previous_nodes = {start: None}

    while not queue.empty():
        (dist, current) = queue.get()
        if current == goal:
            path = []
            cost = distances[current]  
            while current is not None:
                path.append(current)
                current = previous_nodes[current]
            path.reverse()
            return path, cost  
        for neighbour, distance in graph[current].items():
            old_distance = distances.get(neighbour, float('inf'))
            new_distance = distances[current] + distance
            if new_distance < old_distance:
                distances[neighbour] = new_distance
                priority = new_distance + heuristic(neighbour, goal)
                queue.put((priority, neighbour))
                previous_nodes[neighbour] = current
    return [], None  

def get_user_heuristics(cities):
    heuristics = {}
    for city in cities:
        heuristic = float(input(f"Enter heuristic for {city}: "))
        heuristics[city] = heuristic
    return heuristics

def heuristic(city1, city2):
    return min(user_heuristics.get(city1), user_heuristics.get(city2))

graph = {
    'Chicago': {'New York': 800, 'San Francisco': 2200},
    'Miami': {'New York': 1000, 'Dallas':1200},
    'New York': {'Chicago': 800, 'Miami': 1000, 'Boston': 250, 'Los Angeles': 3000, 'Dallas': 1500},
    'Boston': {'New York': 250},
    'Dallas': {'New York': 1500, 'Miami': 1200, 'Los Angeles': 1700},
    'San Francisco': {'Los Angeles': 500, 'Chicago': 2200},
    'Los Angeles': {'Dallas': 1700, 'New York': 3000, 'San Francisco': 500}
}
cities = graph.keys()
user_heuristics = get_user_heuristics(cities)

start = input("Enter the starting city: ")
while start not in graph:
    print("Invalid city. Please enter a city from the graph.")
    start = input("Enter the starting city: ")

goal = input("Enter the goal city: ")
while goal not in graph:
    print("Invalid city. Please enter a city from the graph.")
    goal = input("Enter the goal city: ")

path, cost = astar(graph, start, goal, heuristic)

def printPath(path, cost):
    if cost is not None:
        print("Cost:", cost)
        print("Path:", ' -> '.join(path))
    else:
        print("No path found.")

start_time = time.time()
printPath(path, cost)
end_time = time.time()
execution_time = end_time - start_time
print("Time:", execution_time)
