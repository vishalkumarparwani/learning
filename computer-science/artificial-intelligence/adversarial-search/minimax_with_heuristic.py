import math
GOAL = 6

def heuristic(agent_pos):
    return 10 - abs(GOAL - agent_pos)

# Terminal check
def is_terminal(agent_pos, opponent_pos):
    if agent_pos == GOAL:
        return 10
    if agent_pos == opponent_pos:
        return -10
    return None

# Minimax
def minimax(agent_pos, opponent_pos, depth, is_max):
    result = is_terminal(agent_pos, opponent_pos)

    if result is not None:
        return result

    if depth == 0:
        h = heuristic(agent_pos)
        print(f"Leaf node reached: Agent={agent_pos}, Heuristic={h}")
        return h

    if is_max:
        best = -math.inf
        for move in [-1, 1]:
            new_pos = agent_pos + move
            if 0 <= new_pos <= GOAL:
                val = minimax(new_pos, opponent_pos, depth-1, False)
                best = max(best, val)
        return best
    else:
        best = math.inf
        for move in [-1, 1]:
            new_pos = opponent_pos + move
            if 0 <= new_pos <= GOAL:
                val = minimax(agent_pos, new_pos, depth-1, True)
                best = min(best, val)
        return best

def best_move(agent_pos, opponent_pos, depth):
    best_val = -math.inf
    best_mv = None

    for move in [-1, 1]:
        new_pos = agent_pos + move
        if 0 <= new_pos <= GOAL:
            val = minimax(new_pos, opponent_pos, depth-1, False)
            print(f"Move {move} → Value {val}")
            if val > best_val:
                best_val = val
                best_mv = move

    return best_mv

def simulate(depth):
    agent = 0
    opponent = 3

    print(f"\nSimulation with depth={depth}")

    for step in range(3):
        print(f"\nStep {step+1}: Agent={agent}, Opponent={opponent}")

        move = best_move(agent, opponent, depth)
        print(f"Chosen Move: {move}")

        agent += move

        if opponent > agent:
            opponent -= 1
        else:
            opponent += 1

        result = is_terminal(agent, opponent)
        if result is not None:
            print(f"Game ended with value: {result}")
            break

simulate(2)
simulate(3)
