# Problem_5++: Write an algorithm that computes the the number of edits it takes to 
# turn a string into another. Edits include adding, deleting or replacing a character.

def distance(first, second):

    pairs = []

    for firstIndex in range(len(first)):
        for secondIndex in range(len(second)):

            if first[firstIndex] == second[secondIndex]:

                pairs.append((firstIndex, secondIndex))

    pairsFirst = [pair for pair in pairs if pair[0] <= pair[1]]

    pairsFirst = sorted(pairsFirst, key = lambda pair : pair[1])

    newPairsFirst = []
    if len(pairsFirst) > 0:
        currentIndex = pairsFirst[0][0]
        for pair in pairsFirst:
            if pair[0] >= currentIndex:
                newPairsFirst.append(pair)
                currentIndex = pair[0]

    firstAnswer = max(len(first), len(second)) - len(newPairsFirst)

    pairsSecond = [pair for pair in pairs if pair[0] >= pair[1]]

    pairsSecond = sorted(pairsSecond, key = lambda pair : pair[0])

    newPairsSecond = []
    if len(pairsSecond) > 0:
        currentIndex = pairsSecond[0][1]
        for pair in pairsSecond:
            if pair[1] >= currentIndex:
                newPairsSecond.append(pair)
                currentIndex = pair[1]

    secondAnswer = max(len(first), len(second)) - len(newPairsSecond)

    return min(firstAnswer, secondAnswer)


print(distance("abcdef", "mammmcmmbmf"))
print(distance("mammmcmmbmf", "abcdef"))

print(distance("abce", "abcde"))




