with open('input.txt', 'r') as f:
    lines = [x.strip().split(": ") for x in f.readlines()]
    
nodes = dict()
for input,outs in lines:
    nodes[input] = outs.split(" ")

paths = set()
memory = dict()
def run(nodes,start="you",end="out",avoid=[]):
    if start == end: return 1
    key = start+"T"+end
    if key in memory: return memory[key]
    total = 0
    for out in nodes[start]:
        if out in avoid: continue
        total += run(nodes,out,end,avoid+[start])
        
    memory[key] = total    
    return total

def p2(nodes):
    #      dac
    #    /  |  \
    # svr   |   out
    #    \  |  /
    #      fft
    # one set of paths is svr-dac-fft-out
    # the other is svr-fft-dac-out
    run(nodes,"svr","dac",["fft","out"])
    run(nodes,"svr","fft",["dac","out"])
    run(nodes,"dac","fft",["svr","out"])
    run(nodes,"fft","dac",["svr","out"])
    run(nodes,"dac","out",["svr","fft"])
    run(nodes,"fft","out",["svr","dac"])

    # Since im already storing all the paths for faster iteration, just use that
    sdfo = memory["svrTdac"]*memory["dacTfft"]*memory["fftTout"]
    sfdo = memory["svrTfft"]*memory["fftTdac"]*memory["dacTout"]
    return sdfo+sfdo

print("Part 1: ", run(nodes))
print("Part 2: ", p2(nodes))