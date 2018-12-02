
freq_freqs = {}

freq = 0

print("Reading Input")
with open("day1-input.txt",'r') as f:
    duplicate_found = False
    while not duplicate_found:
        for line in f:
            modifier = 1
            if line[0] == "-":
                modifier = -1
            
            addend = int(line[1:])

            freq += (modifier * addend)

            if freq in freq_freqs:
                freq_freqs[freq] += 1
            else:
                freq_freqs[freq] = 1

            print("%s%d  -> %d"%(line[0],addend,freq))
            if freq_freqs[freq] > 1:
                duplicate_found = True
                break
        if duplicate_found:
            break
        f.seek(0)
    
print("First Repeated Frequency: %d"%freq)