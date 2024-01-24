def randomList():
    import random
    listLength = random.randrange(3,15)
    preSort = []
    while len(preSort) < listLength:
        preSort.append(random.randrange(-99999,99999))
    return preSort

def swapSort():
    currentIndex=0
    list = randomList()
    print(sorted(list))
    while currentIndex<len(list):
        smallest = list[-1]
        smallestIndex=len(list)-1
        for i in range(currentIndex, len(list)):
            if list[i] < smallest:
                smallest=list[i]
                smallestIndex=i
        list[smallestIndex],list[currentIndex]=list[currentIndex],list[smallestIndex]
        currentIndex+=1
    return(list)
print(swapSort())

