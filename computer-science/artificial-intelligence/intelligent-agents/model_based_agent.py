class ModelBasedAgent:
    def __init__(self):

        self.model = {1: 'Unknown', 2: 'Unknown', 3: 'Unknown'}
        self.current_pos = 1

    def update_model(self, percept):
        self.model[self.current_pos] = percept
        print(f"Internal Model Update: {self.model}")

    def predict_action(self):
        if self.model[self.current_pos] == 'Dirty':
            return 'Clean'

        if self.current_pos < 3:
            return 'Move Right'

        if all(state == 'Clean' for state in self.model.values()):
            return 'Done'

        return 'No action'

    def act(self, percept):
        self.update_model(percept)
        action = self.predict_action()

        if action == 'Move Right':
            self.current_pos += 1

        return action

class Environment:
    def __init__(self):
        self.rooms = {1: 'Dirty', 2: 'Dirty', 3: 'Dirty'}
        self.robot_pos = 1

    def get_percept(self):
        return self.rooms[self.robot_pos]

    def apply_action(self, action):
        if action == 'Clean':
            self.rooms[self.robot_pos] = 'Clean'
        elif action == 'Move Right':
            self.robot_pos += 1

def run_agent(agent, environment):
    step = 1
    while True:
        percept = environment.get_percept()
        action = agent.act(percept)

        print(f"Step {step}: Position - Room {environment.robot_pos}, Percept - {percept}, Action - {action}")

        if action == 'Done':
            print("All rooms are clean. Task finished!")
            break

        environment.apply_action(action)
        step += 1
        if step > 10:
            break

agent = ModelBasedAgent()
environment = Environment()

run_agent(agent, environment)
