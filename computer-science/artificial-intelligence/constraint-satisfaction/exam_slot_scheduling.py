import ortools.sat.python.cp_model as cp_model

def solve_exam_optimization():
    model = cp_model.CpModel()

    e1 = model.NewIntVar(1, 3, 'E1')
    e2 = model.NewIntVar(1, 3, 'E2')
    e3 = model.NewIntVar(1, 3, 'E3')
    e4 = model.NewIntVar(1, 3, 'E4')
    e5 = model.NewIntVar(1, 3, 'E5')

    exams = [e1, e2, e3, e4, e5]

    model.Add(e1 != e2)
    model.Add(e2 != e3)
    model.Add(e4 != e5)

    is_late = []
    for i in range(5):
        v = model.NewBoolVar(f'is_late_{i}')
        model.Add(exams[i] == 3).OnlyEnforceIf(v)
        model.Add(exams[i] != 3).OnlyEnforceIf(v.Not())
        is_late.append(v)

    model.Minimize(sum(is_late))

    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    if status == cp_model.FEASIBLE or status == cp_model.OPTIMAL:
        print(f"Exam 1: Slot {solver.Value(e1)}")
        print(f"Exam 2: Slot {solver.Value(e2)}")
        print(f"Exam 3: Slot {solver.Value(e3)}")
        print(f"Exam 4: Slot {solver.Value(e4)}")
        print(f"Exam 5: Slot {solver.Value(e5)}")
        print(f"Total late exams: {solver.ObjectiveValue()}")

solve_exam_optimization()
