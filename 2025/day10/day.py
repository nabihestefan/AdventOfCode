from scipy.optimize import linprog
with open('input.txt', 'r') as f:
    lines = [x.strip().split(" ") for x in f.readlines()]

finals = []
buttons = []
joltage = []

for line in lines:
    finals.append([True if x=="#" else False for x in line[0][1:-1]])
    joltage.append(tuple(map(int,line[-1][1:-1].split(","))))
    butts = []
    for b in line[1:-1]:
        butts.append(tuple(map(int, b[1:-1].split(","))))
    buttons.append(butts)
   

def findFastestP1(f,buttons):
    queue = [([False for _ in range(len(f))],0)]
    visited = set()
    while queue:
        state,presses = queue.pop(0)
        if str(state) in visited: continue
        visited.add(str(state))
        for button in buttons:
            ns = state[:]
            for b in button:
                ns[b] = not ns[b]
            if ns == f: return presses+1
            queue.append((ns,presses+1))
    

print("Part 1: ", sum(findFastestP1(finals[i],buttons[i]) for i in range(len(finals))))

def linprogP2(buttons,joltage):
    costs = [1 for _ in buttons]
    # Basically a matrix of how does this button affect this joltage
    fullButtons = [[(i in b) for b in buttons] for i in range(len(joltage))]
    return int(linprog(costs, A_eq=fullButtons, b_eq=joltage, integrality=1).fun)
    
print("Part 2 (linprog): ", sum(linprogP2(buttons[i],joltage[i]) for i in range(len(buttons))))
