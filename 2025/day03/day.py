with open('input.txt', 'r') as f:
    lines = [map(int,x.strip()) for x in f.readlines()]


def getMaxNext(bank,l,digit):
    if digit == l: return str(max(bank))
    val = max(bank[:-(l-digit)])
    i = bank.index(val)
    return str(val)+getMaxNext(bank[i+1:],l,digit+1)

def run(partTwo=False):
    total = 0
    l = 12 if partTwo else 2
    for bank in lines:
        total += int(getMaxNext(bank,l,1))
    return total

    
print("Part 1: ", run())
print("Part 2: ", run(True))