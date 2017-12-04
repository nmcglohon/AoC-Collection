import numpy as np


inputString = ''
with open('input.txt') as f:
    inputString = f.readline()
inputString = inputString.strip()

inputArray = np.zeros(len(inputString)+1)
for i,char in enumerate(inputString):
    if(char != '\n'):
        inputArray[i] = int(char)
inputArray[-1] = inputArray[0]

totalSum = 0
lastItem = -1
for item in inputArray:
    if item == lastItem:
        totalSum += item
    lastItem = item

print(totalSum)