with open('input.txt', 'r') as f:
    lines = [(x[0], int(x.strip()[1:])) for x in f.readlines()]
    
def brute():
    pos = 50
    p1 = p2 = 0
    for d,m in lines:
        for _ in range(m):
            pos = (pos+{"R":1, "L":-1}[d])%100
            p2 += pos==0
        p1 += pos == 0
    return p1,p2

def smart():
    pos = 50
    total = passes = 0
    for d,m in lines:
        passes += abs(m) // 100
        if d == "R":
            npos = (pos + m)%100
            passes += npos < pos
        elif d == "L":
            npos = (pos - m)%100
            passes += (pos != 0 and (npos > pos or npos == 0))
        pos = npos
        total += pos == 0
    return total, passes

    
print("Brute Part 1&2: ", brute())
print("Smart Part 1&2: ", smart())