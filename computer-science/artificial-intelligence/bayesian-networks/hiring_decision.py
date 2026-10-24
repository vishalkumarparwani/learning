from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

model = DiscreteBayesianNetwork([
    ('Education', 'Interview'),
    ('Experience', 'Interview'),
    ('Interview', 'HiringDecision')
])

cpd_E = TabularCPD('Education', 2, [[0.65], [0.35]])
cpd_X = TabularCPD('Experience', 2, [[0.5], [0.5]])

cpd_I = TabularCPD('Interview', 2,
                   [[0.9, 0.7, 0.6, 0.3],
                    [0.1, 0.3, 0.4, 0.7]],
                   evidence=['Education', 'Experience'],
                   evidence_card=[2, 2])

cpd_H = TabularCPD('HiringDecision', 2,
                   [[0.85, 0.2],
                    [0.15, 0.8]],
                   evidence=['Interview'],
                   evidence_card=[2])

model.add_cpds(cpd_E, cpd_X, cpd_I, cpd_H)

model.check_model()

inference = VariableElimination(model)

result1 = inference.query(variables=['HiringDecision'])
print(result1)

result2 = inference.query(variables=['HiringDecision'],
                          evidence={'Interview': 0})
print(result2)
