import sys

def debugprint(*a):
    # print(*a)
    pass


class Keret():
    def __init__(self, input):
        self.name = input
        self.frozen = 0
        self.sc = False
        self.page = None

    def __repr__(self):
        return self.name + str(self.frozen)


line = sys.stdin.readline().strip()
keresek = [abs(int(n)) for n in line.split(',')]
res = ""

A = Keret("A")
B = Keret("B")
C = Keret("C")

fifo = [A, B, C]
faults = 0
for k in keresek:
    for f in fifo:
        debugprint(f)
    for f in fifo:
        if(f.frozen > 0):
            f.frozen -= 1
    pagehit = False 
    for f in fifo:
        if (f.page == k):
            res += "-"
            f.frozen = 0
            f.sc = True
            pagehit = True
    if (pagehit):
        continue
    faults += 1
    index = 0
    success = False
    while (index < 3 and not success):
        temp = fifo[index]
        if (temp.sc):
            debugprint("in sc")
            fifo.remove(temp)
            temp.sc = False
            fifo.append(temp)
        elif (temp.frozen > 0):
           index += 1
           debugprint("in frozen")
        else:
            success = True
            fifo.remove(temp)
            temp.page = k
            temp.frozen = 4
            fifo.append(temp)
            debugprint("in empty")
            res += temp.name
    
    if (index == 3):
        res += "*"
        
print(res)
print(faults)
