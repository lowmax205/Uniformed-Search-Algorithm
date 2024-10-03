from source import COLOR_VISITING, COLOR_GOAL, COLOR_VISITED
from source import BaseSearchLogic

class GBFSLogic(BaseSearchLogic):
    def __init__(self, canvas, update_node_color, show_goal_message):
        super().__init__(canvas, update_node_color, show_goal_message)
        self.heuristics = {}

    def set_heuristics(self, heuristics):
        self.heuristics = heuristics

    def greedy_bfs(self, start_node, goal_node=None):
        open_list = [start_node]
        visited = set()

        while open_list:
            open_list.sort(key=lambda node: self.heuristics.get(node, float('inf')))
            current_node = open_list.pop(0)

            if current_node not in visited:
                print(f"Visiting: {current_node}")
                self.update_node_color(current_node, COLOR_VISITING)

            if current_node == goal_node:
                print(f"Goal: {current_node}")
                self.update_node_color(current_node, COLOR_GOAL)
                self.show_goal_message(goal_node)
                return

            visited.add(current_node)
            print(f"Visited: {current_node}")
            self.update_node_color(current_node, COLOR_VISITED)

            for neighbor in self.get_neighbors(current_node):
                if neighbor not in visited and neighbor not in open_list:
                    open_list.append(neighbor)
                    print(f"Visiting neighbor: {neighbor}")
                    self.update_node_color(neighbor, COLOR_VISITING)
