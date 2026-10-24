class AgentBasedDls:
    def __init__(self, goal, depth_limit):
        self.goal = goal
        self.depth_limit = depth_limit

    def formulate_goal(self, percept):
        if percept == self.goal:
            return "Goal reached"
        return "Searching"

    def act(self, percept, environment):
        goal_status = self.formulate_goal(percept)
        if goal_status == "Goal reached":
            return f"Goal {self.goal} already found at start!"
        else:
            return environment.dls(percept, self.goal, self.depth_limit)

class Environment:
    def __init__(self, graph):
        self.graph = graph

    def get_percept(self, node):
        return node

    def dls(self, start, goal, depth_limit):
        visited_path = []

        def dfs(node, depth):
            if depth > depth_limit:
                return None

            visited_path.append(node)

            if node == goal:
                return list(visited_path)

            for neighbor in self.graph.get(node, {}):
                result = dfs(neighbor, depth + 1)
                if result:
                    return result

            visited_path.pop()
            return None

        result_path = dfs(start, 0)
        if result_path:
            return f"Goal found! Path: {' -> '.join(result_path)}"
        return "Goal not found within depth limit."

def run_agent(agent, environment, start_node):
    percept = environment.get_percept(start_node)
    action = agent.act(percept, environment)
    print(action)

graph = {
    "A": {"B": 2, "C": 1},
    "B": {"D": 4, "E": 3},
    "C": {"F": 1, "G": 5},
    "D": {"H": 2},
    "E": {},
    "F": {"I": 6},
    "G": {},
    "H": {},
    "I": {},
}

start_node = "A"
goal_node = "I"
limit = 3

agent = AgentBasedDls(goal_node, limit)
environment = Environment(graph)

run_agent(agent, environment, start_node)
