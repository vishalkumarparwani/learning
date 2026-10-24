import random

teachers = ['T1','T2','T3','T4','T5']
courses = ['C1','C2','C3','C4','C5']
days = 5
slots = 5
population_size = 20
generations = 200
mutation_rate = 0.1

def create_chromosome():
    return [[(random.choice(courses), random.choice(teachers)) for _ in range(slots)] for _ in range(days)]

def fitness(chrom):
    penalty = 0
    course_count = {c:0 for c in courses}
    for day in chrom:
        for i, (course, teacher) in enumerate(day):
            course_count[course] += 1
            for j, (c2, t2) in enumerate(day):
                if i!=j and teacher==t2:
                    penalty += 1
        for t in teachers:
            max_consec = 0
            consec = 0
            for course, teacher in day:
                if teacher==t:
                    consec += 1
                    max_consec = max(max_consec, consec)
                else:
                    consec = 0
            if max_consec > 3:
                penalty += (max_consec - 3)
    for c in courses:
        if course_count[c]!=3:
            penalty += abs(course_count[c]-3)
    return -penalty

def selection(pop):
    pop.sort(key=fitness, reverse=True)
    return pop[:population_size//2]

def crossover(p1, p2):
    point = random.randint(1,days-1)
    return p1[:point]+p2[point:]

def mutate(chrom):
    for day in chrom:
        if random.random() < mutation_rate:
            idx = random.randint(0, slots-1)
            day[idx] = (random.choice(courses), random.choice(teachers))

population = [create_chromosome() for _ in range(population_size)]

for gen in range(generations):
    selected = selection(population)
    children = []
    while len(children)<population_size:
        p1, p2 = random.sample(selected,2)
        child = crossover(p1,p2)
        mutate(child)
        children.append(child)
    population = children

best = max(population, key=fitness)
for d in best:
    print(d)
