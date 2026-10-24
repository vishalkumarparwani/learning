import random

N = 8

def conflicts(state):
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            if state[i]==state[j] or abs(state[i]-state[j])==j-i:
                count += 1
    return count

def random_state():
    return [random.randint(0,N-1) for _ in range(N)]

def hill_climb(state):
    while True:
        curr_conflict = conflicts(state)
        if curr_conflict == 0:
            return state
        neighbor_found = False
        for i in range(N):
            for j in range(N):
                if state[i] == j:
                    continue
                new_state = state[:]
                new_state[i] = j
                if conflicts(new_state) < curr_conflict:
                    state = new_state
                    neighbor_found = True
        if not neighbor_found:
            return None

for attempt in range(20):
    state = random_state()
    result = hill_climb(state)
    if result:
        print("Solution:", result)
        break
else:
    print("No solution found after 20 restarts")
