from ortools.sat.python import cp_model
def solve_timetable():
    model = cp_model.CpModel()
    c1 = model.NewIntVar(1, 4, 'C1')
    c2 = model.NewIntVar(1, 4, 'C2')
    c3 = model.NewIntVar(1, 4, 'C3')
    c4 = model.NewIntVar(1, 4, 'C4')

    courses = [c1, c2, c3, c4]

    model.AddAllDifferent(courses)

    model.Add(c1 != 2)

    model.Add(c3 != 4)

    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    if status == cp_model.FEASIBLE or status == cp_model.OPTIMAL:
        print(f"Course C1: Slot {solver.Value(c1)}")
        print(f"Course C2: Slot {solver.Value(c2)}")
        print(f"Course C3: Slot {solver.Value(c3)}")
        print(f"Course C4: Slot {solver.Value(c4)}")
    else:
        print("No feasible solution found.")

solve_timetable()
