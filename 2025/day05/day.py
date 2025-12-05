with open('input.txt', 'r') as f:
    lines = [x.strip() for x in f.readlines()]

fresh = []
available = []
for line in lines:
    if line == "": continue
    if "-" in line:
        fresh.append(tuple(map(int, line.split("-"))))
    else:
        available.append(int(line))

fresh.sort(key=lambda x:x[0])
available.sort()

def cleanRanges(fresh):
    cleanFresh = [fresh[0]]
    for i in range(1,len(fresh)):
        # if prev max is more than or equal to new min: merge
        if cleanFresh[-1][1] >= fresh[i][0]:
            lower,upper = cleanFresh.pop()
            cleanFresh.append((lower,max(upper,fresh[i][1])))
        else: cleanFresh.append(fresh[i])
    return cleanFresh

fresh = cleanRanges(fresh)


def p1(fresh,available):
    total = 0
    for i in available:
        for lower,upper in fresh:
            if lower <= i and i <= upper:
                    total += 1
                    break        
    return total

def p2(fresh):
    total = 0
    for lower,upper in fresh: total += upper-lower+1
    return total

               
print("Part 1: ", p1(fresh,available))
print("Part 2: ", p2(fresh))