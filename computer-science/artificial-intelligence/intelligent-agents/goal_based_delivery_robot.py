class WarehouseEnvironment:
    def __init__(self, start_pos=0, goal_pos=15):
        self.current_position = start_pos
        self.goal_position = goal_pos
        self.steps_taken = 0
        self.path = [start_pos]

    def move(self, action):
        if action == "forward":
            self.current_position += 1
        elif action == "backward":
            self.current_position -= 1

        self.steps_taken += 1
        self.path.append(self.current_position)
        return self.current_position

    def is_goal_reached(self):
        return self.current_position == self.goal_position

class GoalBasedRobot:
    def __init__(self, goal_pos=15):
        self.goal_position = goal_pos

    def decide_action(self, current_pos):
        if current_pos < self.goal_position:
            return "forward"
        elif current_pos > self.goal_position:
            return "backward"
        else:
            return "stop"

def simulate_delivery():
    env = WarehouseEnvironment(start_pos=0, goal_pos=15)
    agent = GoalBasedRobot(goal_pos=15)

    print(f"Starting delivery from position {env.current_position} to {env.goal_position}...")

    while not env.is_goal_reached():
        current_pos = env.current_position

        action = agent.decide_action(current_pos)

        new_pos = env.move(action)

        print(f"Step {env.steps_taken}: Action = {action}, Current Position = {new_pos}")

    print("\nGoal Reached!")
    print(f"Sequence of positions visited: {env.path}")
    print(f"Total steps taken: {env.steps_taken}")

simulate_delivery()
