class GameNode:
    def __init__(self, name, children=None, value=None, is_max=True):
        self.name = name
        self.children = children if children else []
        self.value = value
        self.is_max = is_max


def minimax(node):
    if node.value is not None:
        return node.value

    if node.is_max:
        best = float("-inf")
        for child in node.children:
            best = max(best, minimax(child))
        node.value = best
    else:
        best = float("inf")
        for child in node.children:
            best = min(best, minimax(child))
        node.value = best

    return node.value


def build_tree():
    D = GameNode("D", [GameNode("3", value=3), GameNode("5", value=5)], True)
    E = GameNode("E", [GameNode("6", value=6), GameNode("9", value=9)], True)
    F = GameNode("F", [GameNode("1", value=1), GameNode("2", value=2)], True)
    G = GameNode("G", [GameNode("0", value=0), GameNode("-1", value=-1)], True)

    B = GameNode("B", [D, E], False)
    C = GameNode("C", [F, G], False)

    A = GameNode("A", [B, C], True)

    return A, B, C, D, E, F, G


A, B, C, D, E, F, G = build_tree()

minimax(A)

print("D =", D.value, "E =", E.value, "F =", F.value, "G =", G.value)
print("B =", B.value, "C =", C.value)
print("A =", A.value)
print("Best Move:", "B" if B.value >= C.value else "C")
