from source import COLOR_VISITING, COLOR_GOAL, COLOR_VISITED
from source import BaseSearchLogic

class BFSLogic(BaseSearchLogic):
    def bfs(self, start_node, goal_node=None):
        queue = [start_node]  
        visited = set()
        
        while queue:
            current_node = queue.pop(0)  # Dequeue the front node

            if current_node not in visited:
                print(f"Visiting: {current_node}")
                self.update_node_color(current_node, COLOR_VISITING)  # Mark the node as being visited

            if current_node == goal_node:
                
                # When the goal is reached, print the path and total cost
                path = self.reconstruct_path(visited, goal_node,)
                print("Path:", " -> ".join(path))
                
                print(f"Goal: {current_node}")
                self.update_node_color(current_node, COLOR_GOAL)  # Goal node found
                self.show_goal_message(goal_node)  # Notify goal achievement
                return

            visited.add(current_node)  # Mark current node as visited
            print(f"Visited: {current_node}")
            self.update_node_color(current_node, COLOR_VISITED)  # Mark the node as fully explored

            for neighbor in self.get_neighbors(current_node):
                if neighbor not in visited and neighbor not in queue:
                    # Add unvisited neighbors to the queue
                    queue.append(neighbor)  
                    print(f"Visiting neighbor: {neighbor}")
                    self.update_node_color(neighbor, COLOR_VISITING)  # Mark neighbor as being visited
                    
    #Reconstruct the path from start_node to goal_node and return it with the path costs.
    def reconstruct_path(self, visited, goal_node):
        
        path = []
        current_node = goal_node
        
        while current_node in visited:
            path.append(current_node)

        path.reverse()
        return path