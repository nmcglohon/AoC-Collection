import collections

def isAnagram(word1, word2):
    return collections.Counter(word1) == collections.Counter(word2)

def isValidPhrase(phrase, level):
    isValid = True
    phrase = phrase.strip()
    words = phrase.split(' ')

    if level is 1:
        usedWords = {}
        for word in words:
            if word not in usedWords:
                usedWords[word] = 1
            elif word in usedWords:
                isValid = False
                break

    if level is 2:
        usedWords = {}
        for word in words:
            if word not in usedWords:
                for usedWord in usedWords:
                    if isAnagram(word, usedWord):
                        isValid = False
                        return isValid
                usedWords[word] = 1
            elif word in usedWords:
                isValid = False
                return isValid
    return isValid

def getInputLines(filename):
    inputList = []
    with open(filename) as f:
        for line in f:
            inputList.append(line)
    return inputList

def solvePartOne(inputPhrases):
    validCount = 0
    for phrase in inputPhrases:
        if isValidPhrase(phrase,1):
            validCount += 1
    return validCount


def solvePartTwo(inputPhrases):
    validCount = 0
    for phrase in inputPhrases:
        if isValidPhrase(phrase,2):
            validCount += 1
    return validCount

def main():
    phrases = getInputLines('input.txt')
    print("Part 1: " + str(solvePartOne(phrases)))
    print("Part 2: " + str(solvePartTwo(phrases)))

if __name__ == '__main__':
    main()