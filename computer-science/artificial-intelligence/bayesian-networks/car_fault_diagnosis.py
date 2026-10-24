from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

model = DiscreteBayesianNetwork([
    ('Fault', 'CarWontStart'),
    ('Fault', 'DimLights'),
    ('Fault', 'StrangeNoise')
])

cpd_F = TabularCPD('Fault', 2, [[0.4], [0.6]])

cpd_S = TabularCPD('CarWontStart', 2,
                   [[0.85, 0.7],
                    [0.15, 0.3]],
                   evidence=['Fault'],
                   evidence_card=[2])

cpd_D = TabularCPD('DimLights', 2,
                   [[0.3, 0.8],
                    [0.7, 0.2]],
                   evidence=['Fault'],
                   evidence_card=[2])

cpd_N = TabularCPD('StrangeNoise', 2,
                   [[0.75, 0.2],
                    [0.25, 0.8]],
                   evidence=['Fault'],
                   evidence_card=[2])

model.add_cpds(cpd_F, cpd_S, cpd_D, cpd_N)

model.check_model()

inference = VariableElimination(model)

result1 = inference.query(variables=['Fault'])
print(result1)

result2 = inference.query(variables=['Fault'],
                          evidence={'CarWontStart': 0,
                                    'DimLights': 0,
                                    'StrangeNoise': 0})
print(result2)
