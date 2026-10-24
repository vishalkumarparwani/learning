class environment:
    def __init__(self, intensity='Dim'):
        self.intensity = intensity

    def getIntensity(self):
        return self.intensity

class Agent(environment):
    def __init__(self, motiondetected='true', intensity='Dim'):
        self.motiondetected = motiondetected
        super().__init__(intensity)

    def act(self):
        if self.intensity == 'Dim' and self.motiondetected == 'true':
            print("Light is ON")
        else:
            print("Light is OFF")

while True:
    intes = input("Enter intensity Bright/Dim : ")
    motion = input("Is motion detected (true/false): ")
    if intes in ['Bright', 'Dim'] and motion in ['true', 'false']:
        agent = Agent(motion,intes)
        agent.act()
    else:
        print("Invalid input")
