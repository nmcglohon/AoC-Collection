
freq = 0

print("Reading Input")
with open("day1-input.txt",'r') as f:
    for line in f:
        modifier = 1
        if line[0] == "-":
            modifier = -1
        
        addend = int(line[1:])

        freq += (modifier * addend)
        print("%s%d  -> %d"%(line[0],addend,freq))
    
print("Final Frequency: %d"%freq)