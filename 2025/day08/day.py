with open('input.txt', 'r') as f:
    boxes = [tuple(map(int,x.strip().split(","))) for x in f.readlines()]
    
def dist(b1,b2):
    return ((b1[0]-b2[0])**2 + (b1[1]-b2[1])**2 + (b1[2]-b2[2])**2)**0.5

def getDistances(boxes):
    distances = dict()
    checked = set()
    for b1 in boxes:
        for b2 in boxes:
            if b1 == b2: continue
            if (b2,b1) in checked or (b1,b2) in checked: continue
            distances[dist(b1,b2)] = distances.get(dist(b1,b2),[]) + [(b1,b2)]
            checked.add((b1,b2))
    return distances

distances = getDistances(boxes)

def run():
    partTwo=False
    keys = sorted(distances.keys())
    circuits = []
    connected = set()
    connections = 0
    while True:
        if connections >= 1000 and not partTwo:
            sizes = [len(x) for x in circuits]
            sizes.sort()
            print("Part 1: ", sizes[-1] * sizes[-2] * sizes[-3])
            partTwo = True

        for b1,b2 in distances[keys.pop(0)]:
            connections += 1
            if b1 not in connected and b2 not in connected:
                circuits.append(set([b1,b2]))
            elif b1 not in connected:
                for j in circuits:
                    if b2 in j: 
                        circuits.remove(j)
                        circuits.append(j.union(set([b1,b2])))
                        break
            elif b2 not in connected:
                for j in circuits:
                    if b1 in j: 
                        circuits.remove(j)
                        circuits.append(j.union(set([b1,b2])))
                        break
            else:
                s1, s2 = 0,0
                for j in circuits:
                    if b1 in j: s1 = j
                    if b2 in j: s2 = j
                    if s1 != 0 and s2 != 0: break
                circuits.remove(s1)
                if s1 != s2: circuits.remove(s2)
                circuits.append(s1.union(s2))
            connected.add(b1)
            connected.add(b2)

        if len(circuits[0]) == len(boxes):
            print("Part 2: ", b1[0]*b2[0])
            return

run()
