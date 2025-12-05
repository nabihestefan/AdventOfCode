with open('input.txt', 'r') as f:
    lines = [x.strip() for x in f.readlines()]
    
rolls = set()
for i,line in enumerate(lines):
    for j,roll in enumerate(line):
        if roll == "@": rolls.add((i,j))

def accessible(roll,rolls):
    i,j = roll
    diffs = [(1,0), (0,1), (-1,0), (0,-1), (1,1), (1,-1), (-1,1), (-1,-1)]
    count = 0
    for dx,dy in diffs:
        if count >= 4: return False
        if (i+dx,j+dy) in rolls: count+=1

    if count < 4: return True
    return False

def p1(rolls):
    total = 0
    for roll in rolls:
        total += 1 if accessible(roll, rolls) else 0
    return total

def p2(rolls):
    keepGoing = True
    removed = set()
    while keepGoing:
        keepGoing = False
        for roll in rolls:
            if accessible(roll,rolls):
                removed.add(roll)
                keepGoing = True
        rolls = rolls - removed
    return len(removed)

    
print("Part 1: ", p1(rolls))
print("Part 2: ", p2(rolls))