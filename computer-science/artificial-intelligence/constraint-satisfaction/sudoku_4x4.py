import ortools.sat.python.cp_model as cp_model

def solve_4x4_sudoku():
    model = cp_model.CpModel()

    grid = [[model.NewIntVar(1, 4, f'cell_{i}_{j}') for j in range(4)] for i in range(4)]

    for i in range(4):
        model.AddAllDifferent(grid[i])

    for j in range(4):
        model.AddAllDifferent([grid[i][j] for i in range(4)])


    for i in [0, 2]:
        for j in [0, 2]:
            model.AddAllDifferent([
                grid[i][j], grid[i][j + 1],
                grid[i + 1][j], grid[i + 1][j + 1]
            ])

    initial_grid = [
        [0, 0, 2, 0],
        [0, 0, 0, 3],
        [0, 3, 0, 0],
        [1, 0, 0, 0]
    ]

    for i in range(4):
        for j in range(4):
            if initial_grid[i][j] != 0:
                model.Add(grid[i][j] == initial_grid[i][j])

    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    if status == cp_model.FEASIBLE or status == cp_model.OPTIMAL:
        print("Completed 4x4 Sudoku Grid:")
        for i in range(4):
            row_values = [solver.Value(grid[i][j]) for j in range(4)]
            print(row_values)
    else:
        print("No solution found.")

solve_4x4_sudoku()
