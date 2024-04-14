
import numpy as np
import heapq
import itertools

class DeliveryDriverTSP:
    # constructor to use seed (if applied) to generate locations between [0 - 1). 
    # np.vstack creates new vertical array of [locations, distribution_center]
    # linalg calculates distance between each pair of points in the array. axis=-1 is calc should be done in the last dimension, result is 1D array of distances. 
    def __init__(self, num_locations, distribution_center, seed=None):
        np.random.seed(seed)
        self.locations = np.random.rand(num_locations, 2)
        self.distances = np.linalg.norm(
            np.vstack((self.locations, distribution_center))[:, np.newaxis, :] -
            np.vstack((self.locations, distribution_center))[np.newaxis, :, :], axis=-1)
        # debugging code
        #print(self.distances)

    # Astar search and report shortest path and total distance
    def a_star_tsp(self):
        start_node = 0
        num_locations = len(self.locations)
        visited = set()
        priority_queue = [(0, start_node, [start_node])]
        while priority_queue:
            #print("Priority Queue:", priority_queue)
            _, current_node, path = heapq.heappop(priority_queue)
            #print("Current Path:", path)
            if len(path) == num_locations + 1:
                return path, self.calculate_total_distance(path)
            if current_node not in visited:
                visited.add(current_node)
                for next_node in range(num_locations + 1):
                    if next_node not in visited:
                        new_path = path + [next_node]
                        new_cost = self.calculate_total_distance(new_path)
                        heuristic = self.minimum_spanning_tree_heuristic(new_path)
                        priority = new_cost + heuristic
                        #print("Exploring node:", next_node)
                        #print("New Path:", new_path)
                        #print("Priority:", priority)
                        heapq.heappush(priority_queue, (priority, next_node, new_path))
        return None, None
    
    def minimum_spanning_tree_heuristic(self, path):
        remaining_nodes = set(range(len(self.locations) + 1)) - set(path)
        remaining_distances = [(self.distances[i, j], i, j) for i in remaining_nodes for j in remaining_nodes if i != j]
        remaining_distances.sort()
        mst_cost = 0
        parent = {node: node for node in remaining_nodes}

        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]

        def union(node1, node2):
            parent[find(node1)] = find(node2)
            
        for distance, i, j in remaining_distances:
            if find(i) != find(j):
                mst_cost += distance
                union(i, j)    
        # Add the cost to return to the starting node (0) from the last node in the path
        mst_cost += self.distances[path[-1], 0]    
        return mst_cost
            
    def calculate_total_distance(self, path):
        total_distance = 0
        for i in range(len(path) - 1):
            #print("Calculating distance between nodes", path[i], "and", path[i + 1])
            total_distance += self.distances[path[i], path[i + 1]]
        return total_distance
    

# Get user inputs for number of places and starting position
num_locations = int(input("Enter the number of delivery locations: "))
distribution_center = np.array([float(x) for x in input("Enter the coordinates of the distribution center (x y): ").split()])

# Set seed for testing purposes
seed = 5
tsp_solver = DeliveryDriverTSP(num_locations, distribution_center, seed)
shortest_path, total_distance = tsp_solver.a_star_tsp()

print("Shortest Path:", shortest_path)
print("Total Distance Traveled:", total_distance)
