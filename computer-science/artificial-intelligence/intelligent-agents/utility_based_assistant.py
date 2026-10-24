class UtilityBasedAssistant:
    def __init__(self, time_weight=0.6, cost_weight=0.4):
        self.w_time = time_weight
        self.w_cost = cost_weight

    def calculate_utility(self, time, cost):
        return -(self.w_time * time + self.w_cost * cost)

    def recommend(self, option_a, option_b):
        util_a = self.calculate_utility(option_a['time'], option_a['cost'])
        util_b = self.calculate_utility(option_b['time'], option_b['cost'])

        print(f"Utility for Option A (Fast/Expensive): {util_a:.2f}")
        print(f"Utility for Option B (Slow/Cheap): {util_b:.2f}")

        if util_a > util_b:
            return "Recommendation: Option A (The speed justifies the cost for this user)."
        else:
            return "Recommendation: Option B (The savings justify the wait for this user)."


option_a = {'name': 'Express', 'time': 2, 'cost': 25}
option_b = {'name': 'Standard', 'time': 7, 'cost': 5}

print("Customer 1")
assistant1 = UtilityBasedAssistant(time_weight=0.6, cost_weight=0.4)
print(assistant1.recommend(option_a, option_b))

print("\nCustomer-")
assistant2 = UtilityBasedAssistant(time_weight=0.2, cost_weight=0.8)
print(assistant2.recommend(option_a, option_b))
