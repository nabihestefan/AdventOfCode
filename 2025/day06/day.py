with open('input.txt', 'r') as f:
    rawData = [x.strip() for x in f.readlines()]

actions = []
for i in rawData.pop():
    if i != " ": actions.append(i)

def calculate(numbers,actions):
    total = 0
    for i,act in enumerate(actions):
        if act == "+": total += sum(numbers[i])
        else:
            temp = 1
            for v in numbers[i]: temp *= v
            total += temp
    return total

def p1():
    lines = [x.split() for x in rawData]
    numbers = []
    actions = []
    for i in range(len(lines[0])):
        actions.append(lines[-1][i])
        numbers.append([int(lines[x][i]) for x in range(len(lines)-1)])
    return calculate(numbers, actions)

def skipping(data,i):
    for line in data:
        if line[i] != " ": return False
    return True

def p2():
    numbers = []
    nums = []
    for i in range(len(rawData[0])):
        if skipping(rawData,i):
            numbers+=[nums]
            nums = []
        else:
            num = ""
            for j in range(len(rawData)): num += rawData[j][i]
            nums.append(int(num))
    numbers+=[nums]
    return calculate(numbers, actions)

print("Part 1: ", p1())
print("Part 2: ", p2())