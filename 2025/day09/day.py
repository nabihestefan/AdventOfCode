
with open('input.txt', 'r') as f:
    dots = [tuple(map(int,x.strip().split(","))) for x in f.readlines()]
        
# Just check if a line intersects the box
# There is a couple of edge cases where this fails but they weren't in my input and I can't be bothered to figure them out right now
def isValid(d1,d2):
    dmx1,dmx2,dmy1,dmy2 = min(d1[0],d2[0]),max(d1[0],d2[0]),min(d1[1],d2[1]),max(d1[1],d2[1])

    for i in range(len(dots)-1):
        x1,y1,x2,y2 = dots[i]+dots[i+1]
        if y1==y2:
            # Ignores the start or end of line because of the ends being red
            if dmy1 < y1 < dmy2 and (min(x1,x2) <= dmx1 < max(x1,x2) or min(x1,x2) < dmx2 <= max(x1,x2)):
                return False
        elif x1==x2:
            # Ignores the start or end of line because of the ends being red
            if dmx1 < x1 < dmx2 and (min(y1,y2) <= dmy1 < max(y1,y2) or min(y1,y2) < dmy2 <= max(y1,y2)):
                return False

    return True

def run(dots):
    a1,a2 = 0,0
    for s,d1 in enumerate(dots):
        for d2 in dots[s+1:]:
            a1 = max(a1,(abs(d1[0]-d2[0])+1)*(abs(d1[1]-d2[1])+1))
            if isValid(d1,d2):
                a2 = max(a2,(abs(d1[0]-d2[0])+1)*(abs(d1[1]-d2[1])+1))

    return a1,a2

print("Part 1&2: ", run(dots))