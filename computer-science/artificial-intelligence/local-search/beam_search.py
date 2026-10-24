graph = {
    'A': [('B',2),('C',3),('D',6)],
    'B': [('E',5),('F',4)],
    'C': [('G',6),('H',2)],
    'D': [('I',1),('J',7)],
    'E': [('K',3)], 'F': [('L',2)], 'G':[('M',1)], 'H':[('N',5)], 'I':[('O',2)],
    'J':[], 'K':[], 'L':[], 'M':[], 'N':[], 'O':[]
}

def beam_search(start, goal):
    width = 2
    max_width = 5
    level = 0
    beam = [(start, [start], 0)]
    
    while beam:
        level += 1
        new_beam = []
        for node, path, cost in beam:
            if node == goal:
                print("Path:", path)
                print("Cost:", cost)
                return
            for n, c in graph[node]:
                if n not in path:
                    new_beam.append((n, path+[n], cost+c))
        new_beam.sort(key=lambda x:x[2])
        beam = new_beam[:width]
        print(f"Level {level}:", [n for n,_,_ in beam], "Width:", width)
        if level % 3 == 0 and width < max_width:
            width += 1

beam_search('A','M')
