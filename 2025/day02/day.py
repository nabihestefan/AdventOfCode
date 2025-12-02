with open('input.txt', 'r') as f:
    ranges = [map(lambda x:map(int,x.split("-")),x.strip().split(",")) for x in f.readlines()][0]

def mirrored(id,sections):
    if len(id)%sections!=0: return False
    l = len(id)//sections
    val = id[0:l]
    for i in range(1,sections):
        if val != id[i*l:(i+1)*l]: return False
    return True

def factors(id):
    fs = set([id])
    for i in range(2,id//2):
        if i in fs: return fs
        if id%i==0:
            fs.add(i)
            fs.add(id//i)
    return fs

def isValid(id):
    if len(id)==1: return False
    fs = factors(len(id))
    for i in fs:
        if mirrored(id,i): return True
    return False
    
    
def run():
    p1 = p2 = 0
    for l,u in ranges:
        for i in range(l,u+1):
            p1 += i if mirrored(str(i),2) else 0
            p2 += i if isValid(str(i)) else 0
    return p1,p2

    
print("Part 1&2: ", run())
