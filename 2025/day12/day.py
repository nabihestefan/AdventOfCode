with open('input.txt', 'r') as f:
    lines = [x.split("\n") for x in f.read().split("\n\n")]
print(lines[-1])
shapeAreas = []
areas = []
areaReqs = []
for section in lines[:-1]:
    shapeAreas.append(sum(i.count("#") for i in section[1:]))
for line in lines[-1]:
    area,reqs = line.split(":")
    area = map(int, area.strip().split("x"))
    areas.append(area[0]*area[1])
    areaReqs.append(list(map(int,reqs.strip().split(" "))))
    
    
def run(partTwo=False):
    total = 0
    print(shapeAreas)
    for i in range(len(areas)):
        areaNeeded = 0
        print(areas[i],areaReqs[i])
        for ind,req in enumerate(areaReqs[i]):
            areaNeeded += req*shapeAreas[ind]
        if areaNeeded <= areas[i]: total += 1
    return total

    
print("Part 1: ", run())