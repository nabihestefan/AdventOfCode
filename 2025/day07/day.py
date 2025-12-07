with open('input.txt', 'r') as f:
    lines = [x.strip() for x in f.readlines()]

splitters = set()
end = len(lines)

for i, line in enumerate(lines):
    for j, val in enumerate(line):
        if val=="S": start = (i,j)
        if val=="^": splitters.add((i,j))

def p1(beams):
    total = 0
    while beams:
        beam = beams.pop(0)
        if beam[0] == end: continue
        if beam in splitters: 
            if (beam[0]+1,beam[1]-1) not in beams:
                beams.append((beam[0]+1,beam[1]-1))
            if (beam[0]+1,beam[1]+1) not in beams:
                beams.append((beam[0]+1,beam[1]+1))
            total += 1
        elif (beam[0]+1,beam[1]) not in beams:
            beams.append((beam[0]+1,beam[1]))
    return total

possiblePaths = dict()
hits = set()
def run(beam):
    if beam[0] == end: return 1
    if beam not in possiblePaths:
        if beam in splitters:
            hits.add(beam)
            possiblePaths[beam] = run((beam[0]+1,beam[1]-1)) + run((beam[0]+1,beam[1]+1))
        else:
            possiblePaths[beam] = run((beam[0]+1,beam[1]))
    return possiblePaths[beam]


print("Original Part 1: ", p1([start]))
print("Part 2: ", run(start))
print("Part 1: ", len(hits))