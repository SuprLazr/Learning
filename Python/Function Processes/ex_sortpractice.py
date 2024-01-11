def ascendSort(list):
    smallest = None
    ascended = []
    verifyPos = []
    while len(ascended) < len(list):
        indexCounter = -1
        for i in list:
            indexCounter+=1
            if indexCounter not in verifyPos:
                if smallest is None:
                    smallest=i
                    smallestIndex=indexCounter
                elif i <= smallest:  
                    smallest=i
                    smallestIndex=indexCounter
        verifyPos.append(smallestIndex)
        ascended.append(smallest)
        smallest = None
    return ascended

preSort = [-999,32,-42,-50,47,-2,-2]
print(ascendSort(preSort))